# Data Run — Next Steps / Implementation Plan

**Purpose:** Logical order to plan and execute after GDD. Focus: **shooting-feel feasibility first**, then logic and optional Rive assets.

---

## 0. Shooting feel / VFX testing environment (gate before full build)

The **primary USP** is how satisfying the shooting feels (lasers, electricity/shockers, hypnotic-style attacks). Before building the full game, validate feasibility in code via a dedicated **testing environment**.

| Item | Why |
|------|-----|
| **Sandbox app or screen** | Isolated place to prototype and iterate on: **lasers** (beams, tracers), **electricity emitters / shockers** (arcs, chains), **hypnotic-style attacks** (swirls, pulses). No run loop, rewards, or menus—just VFX and shooting feel. |
| **Code-first** | Implement in Flutter (e.g. CustomPainter, animations). If the feel is good enough, the full game is built on this; if not, consider Rive or other options for those effects. |
| **Outcome** | Decision: “code can deliver the dopamine-releasing feel” → proceed with full game on that basis; else add Rive or alternative for VFX. |

**Output:** A runnable sandbox (e.g. `lib/sandbox/` or a small test app) where each effect type can be toggled, tuned, and judged. Document which effects are code-viable and which (if any) need fallback.

---

## 1. Lock technical foundation (do this first)

Before heavy logic or asset work, lock:

| Item | Why |
|------|-----|
| **Engine / runtime** | **Flutter** (locked). Android + iOS; Rive via package:rive. See game-architecture.md. (e.g. Flutter + Rive, or JS/Canvas). Rive runs in many of these; choice affects how you “fix up logic” and where Rive sits. |
| **Run result contract** | What the game sends on run end: `{ tier, win: bool, livesLeft?, collectiblesEarned[], level? }`. Backend (or stub) consumes this to grant “random pack up to tier” + vouchers. |
| **Where Rive fits** | Rive for: characters/ships, bullets, bosses, UI, VFX? Export (e.g. `.riv`) and runtime (Rive runtime in your engine). Decide so asset work matches the pipeline. |

**Output:** One-pager or short doc: engine choice, run result schema, “Rive = [list of asset types] + how we load them.”

---

## 2. Logic workstream (“fix up logic”)

Order logic so the game is playable end-to-end with placeholders, then refine.

1. **Core loop (no rewards yet)**  
   - Tier select (UI or debug menu) → start run.  
   - Run: vertical scroll, 3 lives, dodge/shoot/collect (placeholders OK).  
   - Boss wave; win = defeat boss, fail = 3 deaths.  
   - End screen: win/fail + mock “reward” text.

2. **Difficulty and level**  
   - Tier → difficulty params (spawn rate, bullet speed, boss health/speed).  
   - Level → which power-ups are available in-run (e.g. shield, burst).  
   - Persist level (and optionally tier caps) between runs.

3. **Run result and rewards integration**  
   - On run end, build run result (tier, win, collectibles).  
   - Call backend (or stub) to get “actual data pack won” (random up to tier) + voucher list.  
   - End screen shows actual pack + vouchers; claim/play again.

4. **Polish and edge cases**  
   - 3-life flow, respawn, boss phase transitions.  
   - Anti-grind: e.g. daily caps per tier if backend supports.

**Output:** Playable loop (placeholders OK) → then hook to real or stub rewards.

---

## 3. Rive assets workstream

Plan assets so they drop into the pipeline you chose in step 1.

1. **Asset list (from GDD)**  
   - Player ship (idle, hit, destroy?).  
   - Enemies (1–2 types) + bullets.  
   - Boss (2–3 variants; state machines if needed).  
   - Voucher pickups, optional power-up VFX.  
   - UI: tier select, HUD (lives, level?), end screen (win/fail).

2. **Rive pipeline**  
   - Create in Rive → export `.riv` (and any atlases/sounds if you use them).  
   - In engine: load at runtime; drive state (e.g. “hit”, “destroy”) from game code.  
   - Agree naming and state/animation names so logic can “fix up” without re-exporting every time.

3. **Order of production**  
   - First: ship + one enemy + one bullet + one boss (so loop is visible).  
   - Then: more enemies/bosses, voucher/power-up art, UI.

**Output:** Rive files per asset type; integration guide (how game code triggers Rive state/animation).

---

## 4. Suggested order of work

| Phase | Focus | Outcome |
|-------|--------|--------|
| **0. Shooting sandbox** | Lasers, electricity, hypnotic VFX in code; iterate on feel | Decision: code-first viable or not; sandbox runnable, effects documented. **Gate:** Only build full game once this feels good. |
| **A. Foundation** | Engine + run result + Rive role | Short technical note; repo/runtime runs. |
| **B. Logic** | Core loop, 3 lives, tier/level, boss, run end | Playable run with placeholder art and mock rewards. |
| **C. Rive** | Asset list, pipeline, first assets (ship, enemy, boss) — only if sandbox showed need | Rive assets loading in-engine and driven by logic. |
| **D. Integration** | Run result → backend/stub; end screen real rewards; Rive for remaining assets + UI | MVP: play for “win up to” tier, get random pack + vouchers, levels = power-ups. |

Do **Phase 0** first. Once shooting feel is validated in the sandbox, do **A** then **B** (and **C** in parallel if Rive is needed).

---

## 5. If you use BMAD for execution

- **Game Architecture** (`/bmad-gds-game-architecture`): formal technical design (engine, systems, run result, backend).  
- **Sprint planning** (`/bmad-gds-sprint-planning`): break epics into stories.  
- **Create Story** then **Dev Story**: implement logic or integration in chunks.

If you prefer to stay lightweight, use this plan as your checklist and only add formal GDD epics/sprints when you need them.

---

## 6. Rive-specific notes

- **Rive** = vector animations + state machines; good for 2D ships, bullets, bosses, UI motion.  
- **Engine support:** Check official Rive runtimes for your engine (Unity, Flutter, web, etc.) so “fix up logic” and “drive Rive from code” are aligned.  
- **Logic owns:** Tier, level, lives, win/fail, run result. **Rive owns:** how it looks and animates. Keep a clear boundary (e.g. game sends “boss_hit” → Rive plays “hit” animation).

---

*Doc generated from GDD and game brief. Update this plan as you lock engine, backend, and Rive pipeline.*
