# Video Shooting Mechanics Analyzer

This is a small Python tool that takes a gameplay video file (e.g. from a competitor) and produces a **structured summary** of:

- Detected **shooting mechanics** (fire rate, reload timing, recoil pattern, hit feedback, etc.)
- Likely **asset types** you would need to build: weapons, animations, VFX, HUD elements.

The code is designed so you can later plug in your preferred **multimodal LLM** (OpenAI, Gemini, etc.) to get deeper, higher-level analysis from sampled frames.

---

## 1. Installation

From the `MobileGame` project root:

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

---

## 2. Usage

**Drop videos into `vids/`** and run:

```bash
cd /Users/udai.deori/Desktop/CursorAI/Projects/MobileGame
source .venv/bin/activate   # or: .venv\Scripts\activate on Windows
export GEMINI_API_KEY="your-key"   # optional, for AI analysis

python video_agent.py
```

With no arguments, it processes **all videos** in `vids/` (mp4, mov, avi, webm, mkv, m4v).

**Or** point at a specific file or folder:

```bash
python video_agent.py vids/competitor-gameplay.mp4
python video_agent.py /path/to/other/folder
```

What it does:

- Samples frames from each video at a fixed interval.
- Extracts a simple timeline of **brightness spikes** that often correlate with muzzle flashes.
- Groups those into **bursts** to approximate fire rate and burst patterns.
- Sends frames to Gemini (if `GEMINI_API_KEY` is set) for weapon/HUD/VFX/asset analysis.
- Prints a **JSON summary** you can paste into your GDD / asset list.

---

## 3. AI Analysis (Google Gemini – Free & Fast)

The tool uses **Google Gemini 1.5 Flash** for visual analysis: free tier, fast, and good at images.

1. Get an API key at [Google AI Studio](https://aistudio.google.com) (no credit card).
2. Set it in your environment:
   ```bash
   export GEMINI_API_KEY="your-key-here"
   ```
   (or `GOOGLE_API_KEY`)
3. Run the tool as usual. If the key is set, you'll get `llm_notes` in the JSON with weapon types, HUD, VFX, and an asset list.

If the key is missing, the tool still runs and returns the brightness-based fire detection.

