# Nova Striker — Preview Gameplay

**Build:** `preview/gameplay.html` (opened via **Battle** on home screen).  
**Status:** Phase 2 preview — fodder waves, formations, boss L1, ship weapons.

**Home:** `preview/index.html` matches Figma [node 2154-410](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2154-410); art lives in `preview/assets/images/home/` (ship, strike line, battle button texture, nav icons).

---

## Current Implementation

### Controls
- **Movement:** Drag (mouse) or touch to move the ship. **X and Y** movement; smooth lerp so the ship follows the pointer without snapping.
- **Shooting:** Automatic laser (single-file or three-way spread — **[T]** when Laser is active). Weapon switch: **F** (cycle), **2** / **3** / **E** (Electric), or tap top-right.

### Ship (Figma-aligned)
- **Size:** 80% scale; 96×112 px body reference + thruster glow below.
- **Main Body Hull:** Figma vector shape or image; orange outline with soft glow.
- **Cockpit / wings / thrusters:** As in Figma; blue thruster exhaust.
- **Position bounds:** X 10%–90% of width; Y 28%–86% of play area height.
- **Upgraded hull:** PNG `assets/images/Level 1/spaceship_upgrade_L1.png` when an upgrade is collected or **[U]** toggles preview.

### Weapons
- **Laser:** Single or triple spread **[T]**; fire interval 240 ms. Cyan tracers, muzzle flash.
- **Fire Blaster:** Continuous stream; damage over contact (fodder dies in one frame; **boss** loses HP per tick).
- **Electric Shock:** Up to 3 targets; fodder removed in one zap; **boss** loses 2 HP per zap while in range.

### Enemies — fodder (Level 1)
- **Art:** `Fodder Class=Type1.png` and `Fodder Class=Type2.png` under `assets/images/Level 1/`. Fallback: cyan diamond / orange circle if PNG missing.
- **Waves:** Declared in code as `LEVEL_FODDER_ASSETS` (array of paths). With **two** types: **Wave 1** = Type 1 only, **Wave 2** = Type 2 only, **Wave 3** = mix (alternating types). With **one** type: a single fodder wave repeats. **Total fodder waves** = `n` types → `n + 1` waves when `n ≥ 2`, else `1`.
- **Entry:** **Wave 1** always from **top** (`pickEntryPathVariant`: straight ~55%, arc-left, arc-right). **Later waves:** random **top** (~45%) or **all from one side** (left/right 50/50). Side paths: **circular** (quadratic arc), **figure‑8**, or **straight** angled file.
- **File / stagger:** Enemies release onto the path every **~200 ms** per slot in their entry group (continuous file).
- **Formations:** **Rectangle** grid (up to 5 columns) or **triangle** when count is a triangular number (3, 6, 10, …). **Split flank** (two files L/R into one grid) when wave ≥ 2, side entry, even count ≥ 6, rectangular layout, random roll.
- **After formation:** No passive “fall.” Enemies keep **formation offset** vs the ship, **track** horizontally, and **drift slowly** toward the player vertically, capped by a **closest approach** above the ship.
- **Shooting:** Enemies fire only after **`formed`**; interval scales with run time; **boss** fires somewhat slower.
- **Drops:** ~10% pickup on fodder kill; boss ~40% chance on destroy. Pickup: `assets/images/Level 1/upgrade-pickup.png`.

### Boss (Level 1)
- **Asset:** `assets/images/Level 1/Boss_L1.png`.
- **When:** After **all** fodder waves in a cycle complete, the next spawn is the **boss** (HUD shows **Boss**). **Win:** destroying the boss triggers a **victory sequence** (no immediate fodder respawn). **Retry Mission** on the results screen starts a fresh run from wave 1 (including wave-1 intro).
- **Stats:** Large hitbox (~108 px draw size), **~32 HP**, score bonus on kill (see `BOSS_SCORE_BONUS` in `gameplay.html`). Enters from **top** using the same path variants as fodder top entry; then same formation-follow + drift behaviour with a **higher** hold (larger `|formation Y|` cap).

### Boss win → mission complete (Figma 2273:84529)
- **FX:** Keeps the existing **VIBGYOR radial ripple** on hits; on boss death adds **extra ripples** and **additive VIBGYOR spark particles** (`victorySparks`, `drawVictorySparks`).
- **Fly-out:** Ship **auto-rises** off the top; center message **“Awesome”** (`VICTORY_FLYOUT_MS`).
- **Results overlay:** HTML/CSS **Mission Complete** screen aligned with [Figma Gratification screen](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2273-84529): subtitle *Sector 7 Alpha Secured*, unlocked reward strip, tactical stars (from laser accuracy sample), score + accuracy, **Retry Mission** / **Exit to Menu** (`preview/index.html`).

### Run / HUD
- **No run timer** in preview (removed). **Lose:** run ends on **0 lives** (**OUT OF LIVES** on canvas). **Win:** boss defeat → mission complete overlay (separate from loss).
- **Wave label:** `Wave N` during fodder, **`Boss`** during boss fight.
- **Lives:** 3 hearts; hit flash; chain score + ripples on kills.

### Docs
- `RUN.md` — how to run preview.
- `_bmad-output/phase-2-implementation-handoff.md` — Phase 2 scope vs preview.
- `_bmad-output/shooting-mechanics-reference.md` — weapons table + §6 implemented.

---

## Extending fodder / levels

Add PNG paths to **`LEVEL_FODDER_ASSETS`** in `gameplay.html`. Wave count becomes **`length + 1`** (mix wave) when `length ≥ 2`. For **Level 2+**, duplicate the pattern with another array or load from a level key when the host app provides it.

Boss per level: currently **L1** only in preview (`BOSS_L1_URL`). Later levels can switch image URL and stats the same way.

---

*Preview build for Data Run / Nova Striker. See GDD and game-brief for full product design.*
