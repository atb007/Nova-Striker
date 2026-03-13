import argparse
import base64
import json
import math
import os
import sys
from dataclasses import dataclass
from typing import List, Optional, Tuple

import cv2
import numpy as np


@dataclass
class FireEvent:
    timestamp: float
    brightness: float


@dataclass
class FireBurst:
    start_time: float
    end_time: float
    shot_count: int
    average_interval: Optional[float]


@dataclass
class AnalysisResult:
    video_path: str
    duration_seconds: float
    frame_count: int
    fps: float
    fire_events: List[FireEvent]
    fire_bursts: List[FireBurst]
    inferred_mechanics: dict
    content_description: Optional[str] = None  # Short "what we saw" from LLM
    llm_notes: Optional[str] = None


def sample_frames(
    video_path: str,
    sample_every_seconds: float = 0.05,
) -> Tuple[List[np.ndarray], float, int, float, List[float]]:
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise RuntimeError(f"Could not open video: {video_path}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    duration = frame_count / fps if fps > 0 else 0.0

    frames: List[np.ndarray] = []
    timestamps: List[float] = []

    step_frames = max(1, int(fps * sample_every_seconds))

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if frame_idx % step_frames == 0:
            timestamp = frame_idx / fps if fps > 0 else 0.0
            frames.append(frame)
            timestamps.append(timestamp)

        frame_idx += 1

    cap.release()

    return frames, duration, frame_count, fps, timestamps


def detect_fire_events(
    frames: List[np.ndarray],
    timestamps: List[float],
    brightness_threshold_factor: float = 1.8,
) -> List[FireEvent]:
    if not frames:
        return []

    brightness_values = []
    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        brightness_values.append(float(np.mean(gray)))

    baseline = np.median(brightness_values)
    threshold = baseline * brightness_threshold_factor

    events: List[FireEvent] = []
    for ts, b in zip(timestamps, brightness_values):
        if b >= threshold:
            events.append(FireEvent(timestamp=ts, brightness=b))

    return events


def group_fire_bursts(
    events: List[FireEvent],
    max_interval_between_shots: float = 0.18,
) -> List[FireBurst]:
    if not events:
        return []

    bursts: List[FireBurst] = []
    current: List[FireEvent] = [events[0]]

    for prev, curr in zip(events, events[1:]):
        dt = curr.timestamp - prev.timestamp
        if dt <= max_interval_between_shots:
            current.append(curr)
        else:
            bursts.append(_make_burst(current))
            current = [curr]

    if current:
        bursts.append(_make_burst(current))

    return bursts


def _make_burst(events: List[FireEvent]) -> FireBurst:
    if len(events) <= 1:
        return FireBurst(
            start_time=events[0].timestamp,
            end_time=events[0].timestamp,
            shot_count=1,
            average_interval=None,
        )

    intervals = [
        b.timestamp - a.timestamp for a, b in zip(events, events[1:])
    ]
    avg_interval = sum(intervals) / len(intervals) if intervals else None

    return FireBurst(
        start_time=events[0].timestamp,
        end_time=events[-1].timestamp,
        shot_count=len(events),
        average_interval=avg_interval,
    )


def infer_mechanics(bursts: List[FireBurst]) -> dict:
    if not bursts:
        return {
            "has_detectable_shooting": False,
            "notes": "No clear muzzle-flash-like events detected from brightness spikes.",
        }

    total_shots = sum(b.shot_count for b in bursts)
    total_time = bursts[-1].end_time - bursts[0].start_time
    overall_rps = total_shots / total_time if total_time > 0 else None

    avg_intervals = [b.average_interval for b in bursts if b.average_interval]
    median_interval = (
        float(np.median(avg_intervals)) if avg_intervals else None
    )

    mechanics = {
        "has_detectable_shooting": True,
        "total_shots_estimate": total_shots,
        "burst_count": len(bursts),
        "overall_rps_estimate": overall_rps,
        "median_shot_interval_seconds": median_interval,
    }

    if overall_rps:
        rpm = overall_rps * 60
        mechanics["overall_rpm_estimate"] = rpm

        if rpm < 120:
            mechanics["fire_mode_guess"] = "single-shot / slow semi-auto"
        elif rpm < 450:
            mechanics["fire_mode_guess"] = "semi-auto / controlled bursts"
        else:
            mechanics["fire_mode_guess"] = "full-auto / very fast bursts"

    return mechanics


def _build_llm_parts(frames: List[np.ndarray], max_frames: int = 12) -> List[dict]:
    """Build list of parts for Gemini: prompt + image bytes (no base64)."""
    prompt = """You are analyzing video frames (gameplay or any other content).

First line only: one short sentence describing what this video shows (e.g. "Vertical shooter with a spaceship and power-ups" or "Social media clips with text overlays, no game content"). This is the counter-description of what we actually see.

Then, if it looks like a shooter/game, provide:

1. **Weapons & shooting** – weapon types, fire mode, recoil, reload if visible
2. **HUD / UI** – crosshair, ammo, health, hit markers, etc.
3. **Visual effects** – muzzle flash, tracers, impacts, screen effects
4. **Asset list** – bullet list of assets to recreate (models, animations, VFX, UI, sounds)

If it is NOT game/shooter content, say so briefly and describe what is on screen instead. Be concise; use headers and bullets. This is for game design reference."""
    parts: List[dict] = [{"text": prompt}]
    step = max(1, len(frames) // max_frames) if frames else 0
    for frame in frames[::step][:max_frames]:
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        _, buf = cv2.imencode(".jpg", rgb)
        parts.append({"inline_data": {"mime_type": "image/jpeg", "data": buf.tobytes()}})
    return parts


def analyze_with_llm(sample_frames_for_llm: List[np.ndarray]) -> Tuple[Optional[str], Optional[str]]:
    """
    Use Google Gemini to analyze frames. Returns (content_description, llm_notes).
    Tries new google-genai SDK first; falls back to google-generativeai and reports errors.
    """
    if not sample_frames_for_llm:
        return None, None

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Warning: GEMINI_API_KEY (or GOOGLE_API_KEY) not set; skipping LLM analysis.", file=sys.stderr)
        return None, None

    # Prefer new google-genai SDK (supported)
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        parts = _build_llm_parts(sample_frames_for_llm, max_frames=12)
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=[{"parts": parts}],
        )
        text = getattr(response, "text", None) or (response.candidates[0].content.parts[0].text if response.candidates else None)
        if text:
            text = text.strip()
            first_line, _, _ = text.partition("\n")
            description = first_line.strip() if first_line else None
            return description, text
    except ImportError:
        pass
    except Exception as e:
        print(f"Gemini (google-genai) error: {e}", file=sys.stderr)

    # Fallback: deprecated google-generativeai (with base64 parts)
    try:
        import google.generativeai as genai_legacy
        genai_legacy.configure(api_key=api_key)
        model = genai_legacy.GenerativeModel("gemini-2.5-flash-lite")
        prompt_parts = _build_llm_parts(sample_frames_for_llm, max_frames=12)
        # Legacy SDK expects prompt first, then list of inline_data (base64)
        content = [prompt_parts[0]["text"]]
        for p in prompt_parts[1:]:
            content.append({"inline_data": {"mime_type": p["inline_data"]["mime_type"], "data": base64.b64encode(p["inline_data"]["data"]).decode("utf-8")}})
        response = model.generate_content(content)
        if response and response.text:
            text = response.text.strip()
            first_line, _, _ = text.partition("\n")
            return (first_line.strip() if first_line else None), text
    except Exception as e:
        print(f"Gemini (legacy) error: {e}", file=sys.stderr)

    return None, None


def run_analysis(
    video_path: str,
    sample_every_seconds: float = 0.05,
    max_frames_for_llm: int = 32,
) -> AnalysisResult:
    (
        frames,
        duration,
        frame_count,
        fps,
        timestamps,
    ) = sample_frames(video_path, sample_every_seconds=sample_every_seconds)

    fire_events = detect_fire_events(frames, timestamps)
    fire_bursts = group_fire_bursts(fire_events)
    mechanics = infer_mechanics(fire_bursts)

    if frames:
        step = max(1, math.floor(len(frames) / max_frames_for_llm))
        sample_for_llm = frames[::step][:max_frames_for_llm]
    else:
        sample_for_llm = []

    content_description, llm_notes = analyze_with_llm(sample_for_llm)

    return AnalysisResult(
        video_path=video_path,
        duration_seconds=duration,
        frame_count=frame_count,
        fps=fps,
        fire_events=fire_events,
        fire_bursts=fire_bursts,
        inferred_mechanics=mechanics,
        content_description=content_description,
        llm_notes=llm_notes,
    )


def result_to_json(result: AnalysisResult) -> str:
    def fire_event_to_dict(ev: FireEvent):
        return {"timestamp": ev.timestamp, "brightness": ev.brightness}

    def burst_to_dict(b: FireBurst):
        return {
            "start_time": b.start_time,
            "end_time": b.end_time,
            "shot_count": b.shot_count,
            "average_interval": b.average_interval,
        }

    payload = {
        "video_path": result.video_path,
        "duration_seconds": result.duration_seconds,
        "frame_count": result.frame_count,
        "fps": result.fps,
        "fire_events": [fire_event_to_dict(ev) for ev in result.fire_events],
        "fire_bursts": [burst_to_dict(b) for b in result.fire_bursts],
        "inferred_mechanics": result.inferred_mechanics,
        "content_description": result.content_description,
        "llm_notes": result.llm_notes,
    }
    return json.dumps(payload, indent=2)


VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".webm", ".mkv", ".m4v"}
VIDS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vids")


def _get_videos_from_folder(folder: str) -> List[str]:
    """Return sorted list of video file paths in folder."""
    paths = []
    for name in sorted(os.listdir(folder)):
        ext = os.path.splitext(name)[1].lower()
        if ext in VIDEO_EXTENSIONS:
            paths.append(os.path.join(folder, name))
    return paths


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Analyze gameplay video(s) for shooting mechanics. "
        "Pass a video file, a folder (e.g. vids), or nothing to use vids/."
    )
    parser.add_argument(
        "path",
        type=str,
        nargs="?",
        default=VIDS_FOLDER,
        help="Video file or folder containing videos (default: vids/).",
    )
    parser.add_argument(
        "--sample-every",
        type=float,
        default=0.05,
        help="Seconds between sampled frames (default: 0.05).",
    )

    args = parser.parse_args()
    path = os.path.abspath(args.path)

    if os.path.isfile(path):
        videos = [path]
    elif os.path.isdir(path):
        videos = _get_videos_from_folder(path)
        if not videos:
            print(json.dumps({"error": f"No video files found in {path}"}, indent=2))
            return
    else:
        print(json.dumps({"error": f"Not a file or folder: {path}"}, indent=2))
        return

    results = []
    for video_path in videos:
        result = run_analysis(
            video_path=video_path,
            sample_every_seconds=args.sample_every,
        )
        results.append(json.loads(result_to_json(result)))

    if len(results) == 1:
        print(json.dumps(results[0], indent=2))
    else:
        print(json.dumps({"videos_analyzed": len(results), "results": results}, indent=2))


if __name__ == "__main__":
    main()

