# Phase 2 Implementation — Dev Handoff

**Source:** `Phase 2 implementation.docx` (sifted and structured for handoff)  
**Purpose:** Single reference for Phase 2 scope, design links, and clarification points.  
**Related:** `implementation-plan.md` (§2 Logic workstream), `preview/PREVIEW-GAMEPLAY.md` (Phase 2 frameworks), `shooting-mechanics-reference.md` (§7).

---

## 1. Phase 2 scope (from doc)

| # | Area | Spec (from doc) | Clarify? |
|---|------|-----------------|----------|
| 1 | **Enemy flanking** | Groups enter from left/right as well as top. | — |
| 2 | **Flanking UX** | When enemies enter from sides, viewport has **red blur edges** at left/right as indicator. | **Q:** Exact blur style (gradient width, opacity, animation)? |
| 3 | **Entry motion** | Enemies can enter in **circular motion**, following a path, then **settle into formation**. | **Q:** Path defined per wave (data) or procedural? |
| 4 | **Enemy types** | **Fodder**, **mid**, **boss**. Designs for fodder and boss for **level 1** only so far. | **Q:** Mid-type design timeline; level 2+ asset plan. |
| 5 | **Enemy attacks** | Enemies attack (projectiles, beams) **after** they are in formation. Player can attack **before** they settle. | — |
| 6 | **Enemy positioning** | After entering: take positions — **static** or **move relative to player** (e.g. constant distance, orbit). | — |
| 7 | **Spaceship upgrades** | Upgrades change **ship visuals** and/or **bullet types** (unlock/enhance Fire Blaster, Electric Shock, spread). | — |
| 8 | **Drops on kill** | Enemies drop upgrades when destroyed; pickups drive **weapon unlocks and progression**. | — |
| 9 | **Blur in assets** | “Blur elements need to be taken into account to be rendered properly.” | **Q:** Which assets use blur (viewport edges, pickups, other)? Export as raster + blur or replicate in engine? |
| 10 | **Asset format** | Along with **SVG**, **PNG** files are provided in images folder with proper naming for reference. | — |

---

## 2. Design links (Figma — CaseStudies)

**File:** `CaseStudies` — [Figma design](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies)  
*(Use `node-id` in URL for direct component/screen.)*

### Enemies (Level 1)

| Asset | Node ID | URL |
|-------|---------|-----|
| Fodder Type 1 | 2191-4817 | [Fodder 1](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2191-4817) |
| Fodder Type 2 | 2191-4819 | [Fodder 2](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2191-4819) |
| Boss Level 1 | 2195-718 | [Boss L1](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2195-718) |

### Ship & upgrades

| Asset | Node ID | URL |
|-------|---------|-----|
| Upgraded spaceship (Level 1) | 2181-1169 | [Upgraded ship L1](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2181-1169) |
| Upgrade pickup asset | 2190-4732 | [Upgrade pickup](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2190-4732) |

### Full screens (reference)

| Screen | Node ID | URL |
|--------|---------|-----|
| **Home / menu** | **2154-410** | [**Body (home)**](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2154-410) — `preview/index.html`; assets in `preview/assets/images/home/` |
| L1 fight | 2181-1064 | [L1 fight](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2181-1064) |
| L1 Boss fight | 2195-749 | [L1 Boss fight](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2195-749) |
| **Mission complete (gratification)** | **2273-84529** | [**Gratification screen**](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2273-84529) |

---

## 3. Decisions (locked for dev)

| Topic | Decision |
|-------|----------|
| **Asset source of truth** | **Figma** — draw from Figma links; export SVG/PNG as needed. |
| **Level 2+** | **Keep** — Level 2+ assets and logic stay in scope; implement when ready. |
| **Points / logic** | **Open for now** — exact formulas (spawn rates, drop rates, etc.) can be tuned later. |
| **Mid enemy** | **When design is ready** — use placeholder until Figma/design available. |
| **Blurs** | **Code/engine** — blur effects (e.g. red flanking edges, UI blur) implemented in code, not baked in art. |

---

## 4. Phase 2 step-by-step feature list (iterate one at a time)

Implement in this order; complete and iterate on **one** feature before moving to the next.

| Step | Feature | Brief spec | Figma / asset |
|------|---------|------------|---------------|
| **1** | **Drops on kill** | Enemies drop upgrade pickups when destroyed; pickups fall or stay; player overlap = collect; drives weapon unlock/progression. | Upgrade pickup: [2190-4732](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2190-4732) |
| 2 | Enemy flanking (entry sides) | Groups enter from top/left/right based on weighted side selection (configurable in preview via `ENEMY_ENTRY_SIDE_WEIGHTS`). | — |
| 3 | Flanking UX (red blur edges) | Viewport shows red blur at left/right when enemies entering from sides (code-driven blur). | Blur in code/engine |
| 4 | Entry motion + formations | Enemies enter (e.g. circular path) then settle into formation (V, line, wedge). | — |
| 5 | Enemy types (L1) | Fodder 1 & 2 + Boss L1 in preview (`LEVEL_FODDER_ASSETS`, `Boss_L1.png`); mid = placeholder until design ready. | Fodder: 2191-4817, 2191-4819; Boss: 2195-718 |
| 6 | Enemy positioning / holding | After formation: static or move relative to player (orbit, constant distance). | — |
| 7 | Enemy attacks | Enemies fire (projectiles/beams) **after** in formation; player can attack before they settle. | — |
| 8 | Spaceship upgrades | Pickup grants upgrade: ship visual and/or weapon (Fire Blaster, Electric Shock, spread). | Upgraded ship L1: [2181-1169](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2181-1169) |

**Current focus:** Step 2 — **Enemy flanking (entry sides)**, now wired in preview via weighted side selection; next: flanking UX and entry motion.

### Step 2 — Enemy flanking: implementation notes (for dev)

- **Preview logic:** In `preview/gameplay.html`, `addEnemyWave()` now chooses an `entrySide` via `pickEnemyEntrySide()`, which uses `ENEMY_ENTRY_SIDE_WEIGHTS` to bias how often waves spawn from **top**, **left**, or **right**.
- **Config:** `ENEMY_ENTRY_SIDE_WEIGHTS` defaults to `top: 0.6, left: 0.2, right: 0.2`; adjust for testing or level tuning.
- **Motion:** While `entryPhase === 'entering'`, enemies lerp from `(startX, startY)` (off-screen for left/right) to their formation slots using a smoothstep easing; once `entryT >= 1`, they switch to `entryPhase: 'formed'` and fall under normal behaviour.

### Step 1 — Drops on kill: implementation notes (for dev)

- **Source of truth:** Figma — [Upgrade pickup node 2190-4732](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2190-4732). Export PNG; place in **level-wise** asset folder. **Path (Level 1):** `preview/assets/images/Level 1/upgrade-pickup.png`; in code: `assets/images/Level 1/upgrade-pickup.png`. Asset folder structure is level-only for now (Level 1, Level 2, …).
- **Trigger:** When an enemy is destroyed (removed from `enemies` array), spawn a pickup at that position `(enemy.x, enemy.y)`.
- **Pickup behaviour (MVP):** Pickup can fall slowly (e.g. same as scroll) or stay in place; player overlap (ship hitbox vs pickup hitbox) = collect. On collect: remove pickup; apply effect (e.g. unlock or temporary Fire Blaster / Electric — logic open for now; can start with a simple “collected” counter or weapon toggle).
- **Rates:** Drop chance or “which enemy types drop” left open; can start with “every kill drops one” or a fixed probability.
- **Preview:** In `preview/gameplay.html`, today enemies are removed on hit and `addExplosion()` is called; add a `pickups` array, spawn a pickup when filtering out a dead enemy, draw and update pickups, and detect overlap with ship for collection.
- **Flutter/Rive:** When moving to Flutter, drop (pickup) assets can be replaced with Rive files (`.riv`) for animated drop/collect; keep the same trigger and collection logic in code.

---

## 5. Clarification checklist (for product/design before or during dev)

- [x] **Blur rendering:** Implement in code/engine (not baked in art).
- [x] **Mid enemy:** When design is ready; placeholder until then.
- [x] **Level 2+:** Keep in scope; logic open for now.
- [ ] **Red blur edges (flanking):** Spec (width, opacity, animation) when implementing step 3.
- [ ] **Entry paths:** Authored per wave vs procedural — leave open until step 4.
- [ ] **SVG vs PNG:** Prefer SVG for runtime where possible; use Figma exports with proper naming.

---

## 6. Implementation alignment with existing docs

- **GDD / implementation-plan:** Phase 2 “Logic” (implementation-plan §2) covers core loop, tier/level, run result, polish. This handoff is the **gameplay/UX Phase 2** (flanking, formations, attacks, positioning, upgrades, drops).
- **Stack:** Flutter host; assets from Figma (SVG/PNG in `assets/images/`); code-first animation, Rive fallback per `game-architecture.md`.
- **Dev order:** Use the step-by-step list in §4 (drops first, then flanking, etc.).

---

## 7. Asset delivery note (from doc)

> Along with SVG, PNG files are provided in images folder with proper naming for reference.

**Asset folder structure (level-wise):** Assets are organized by level only for now. Use `preview/assets/images/Level 1/` for Level 1 (upgrade pickup, fodder, boss, ship, etc.); add `Level 2/`, `Level 3/`, … as needed. In code, paths are relative to the preview page, e.g. `assets/images/Level 1/upgrade-pickup.png`.

Ensure dev has: **images folder** per level with named PNG/SVG for fodder 1 & 2, boss L1, upgraded ship L1, upgrade pickup; and any viewport-edge/blur assets if separate.

---

## 8. New additions — high-level game rule framework (from doc)

These points extend the Phase 2 scope above; they should be treated as **constraints on how Phase 2 features behave**, not as a separate phase.

- **Enemy health scaling**
  - Every enemy has a health bar.
  - Early waves: fodder die in a **single hit**.
  - As waves/levels progress, health increases so that enemies **take multiple hits**, with tuning per wave.

- **Wave cadence (preview)**
  - **No global run timer** in `preview/gameplay.html` (timer removed). The next **fodder** wave spawns when **all enemies are cleared**, after a short cooldown (`SPAWN_INTERVAL_MS`).
  - **Wave count** is **data-driven** from `LEVEL_FODDER_ASSETS`: with **n** fodder PNGs, there are **n** single-type/mix waves (`n + 1` waves when `n ≥ 2`, else **1** fodder wave), then **Boss L1** (`Boss_L1.png`) **once per cycle**, then the cycle repeats from wave 1.

- **Player lives**
  - Player has **3 lives**, shown as **heart icons**.
  - When the player is hit (enemy bullet / collision), a life is lost; on 0 lives the run ends.

- **Upgrade taxonomy**
  - There are now **two upgrade categories**:
    - **Ship upgrades** (visual + general power; e.g. upgraded hull, faster base fire).
    - **Turret system/type upgrades** (weapon mode & pattern: laser, electric, psionic, etc.).
  - Drops for these two categories should be visually distinguishable (different pickup art).

- **Wave difficulty curve**
  - **Enemy density** (enemies per wave) increases with wave index.
  - **Enemy fire-back behaviour**:
    - Wave 1: enemies do **not** shoot.
    - After wave 1: enemies start to shoot back.
    - Fire rate / bullet density increases per wave, up to a **cap after a certain wave**.

- **Enemy positioning relative to player**
  - Enemies should be able to **maintain a relative distance** to the player, roughly **200px** away, when in “tracking” / “orbit” behaviours.

- **Entry styles (extended)**
  - Existing: **vanilla top entry** and basic side flanking.
  - New patterns to support over time:
    - Figure-eight weave from **both** sides simultaneously.
    - Figure-eight weave from **either** side alone.

- **Formations (preview implementation)**
  - “Formation” = slot layout before settle, then **offsets relative to the player** (ship tracking + slow vertical drift toward player, capped standoff).
  - Preview uses **rectangular grid** and **triangular** slot layouts (triangular numbers: 3, 6, 10, …). Legacy **V / line / wedge** names are superseded in code by `pickFormationSlots()` (rect vs triangle).

- **Hit FX and chain scoring**
  - Every enemy hit should produce a **rainbow, ripple-like blurry wave** across the screen (stacking when multiple hits occur quickly).
  - **Chain hits** (streaks) should:
    - Accumulate **bonus points**.
    - Show a **chain / streak indicator** at the top of the battle screen.
    - Fade/reset when the chain is broken.

- **Turret system details**
  - **Turret types**:
    - **Laser** (currently implemented).
    - **Electric shock** (currently implemented).
    - **Psionic**: concentric arc “wifi” waves that scramble enemies into colliding with each other; **one-shot special**, then reverts to previous turret type.
  - **Laser turret patterns**:
    - Single turret — single file (current).
    - Dual turret — dual straight pattern.
    - Dual turret — S-wave interweaving pattern.
    - Triple turret — triangle pattern (current).
  - Upgrade drops for turret types/patterns:
    - **One turret-upgrade drop per wave**, or until consumed.
    - Separate pickup asset for turret upgrades (distinct from ship-upgrade pickup).
    - Turret types/patterns can also advance via **round-robin progression** across waves.

- **Upgrade drop frequency (nerfed)**
  - Upgrades are **capped to one active drop per wave** (for both ship and turret category, unless explicitly overridden).
  - Once the player picks up / consumes that drop, a new one can appear in a later wave.

---

## 9. Updated dev action points (preview prototype)

Treat these as **Phase 2.1–2.3** milestones on the HTML5 preview before porting to Flutter.

1. **Lock in current Phase 2 gameplay basics (mostly done)**
   - **Already implemented in `preview/gameplay.html`:**
     - Drops on kill pickup system (ship-upgrade pickup art, collection, counter).
     - Fodder waves driven by **`LEVEL_FODDER_ASSETS`** (Type 1 / Type 2 PNGs); wave 1 = type 1, wave 2 = type 2, wave 3 = mix (when two types); **Boss L1** after each full fodder cycle (`Boss_L1.png`, multi-hit HP).
     - Entry: **wave 1 from top** only (`pickEntryPathVariant`: straight / arc-left / arc-right); later waves **random top vs all-left or all-right**; side paths **circular / fig8 / straight**; **staggered file** via `entryReleaseAt`.
     - Formations: **rectangle** and **triangle** slot grids; optional **split L/R** files into one grid.
     - Flanking UX via red blur edges tied to side entry.
     - Post-formation: **no passive fall** — `formRelX` / `formRelY` track ship + capped drift (`FORMATION_CLOSEST_REL_Y`, boss uses `BOSS_FORMATION_CLOSEST_REL_Y`).
     - Per-enemy health; **boss** takes multiple hits from laser / fire / electric.
     - **No run timer** — end of run = **0 lives** only (`OUT OF LIVES`).
     - 3-life system with heart icons and collision-based life loss.
     - Score tracking and basic chain mechanic (score multiplier + HUD chain label); boss kill bonus (`BOSS_SCORE_BONUS`).
   - **Still open (short-term):**
     - Reintroduce optional **time pressure** as a separate mode or tier if design wants it back.
     - **V-shaped** formation as an explicit layout variant (if still desired alongside rect/triangle).

2. **Core game rule framework (tuning + FX for scoring)**
   - Tune scoring values and chain timeout per wave / difficulty.
   - Layer in visual/audio polish for chains (e.g. subtle FX tied to chainCount, integrating with planned ripple FX in §5).

3. **Enemy behaviour polish**
   - **Figure-eight** from sides: **done** (`pathVariant: 'fig8'`).
   - **Hold relative to player:** **done** — formation offsets + drift (replaced older `track` / `orbit` / global fall).
   - **Enemy attacks** after `formed`: **done** (`enemyBullets`); boss fires with a slower interval multiplier.
   - **Wave HUD:** **done** — `Wave N` (and brief center titles); **`Boss`** during boss fight.
     - **Boss fight:** **done** — L1 boss image, spawns at end of each fodder cycle. **Win:** mission complete flow (§10); **Retry** restarts at wave 1 with intro.
   - **NOTE (open design item):** Very large simultaneous fodder counts were reverted earlier; current cap is **6** on wave 1 and **10** on later fodder waves (tuning pass still valid).

4. **Weapons and turret system**
   - Cleanly separate:
     - **Ship tier / visual upgrades** (hull + baseline stats).
     - **Turret type and firing pattern** (laser(implmeented) / fire(implemented) / electric(implemented) / psionic + single/dual/S-wave/triangle)-toggleable through F,s currently implemented.
   - Introduce a **turret-upgrade pickup** asset and logic, distinct from the ship-upgrade pickup.
   - Implement **round-robin turret progression** across waves plus one-shot **psionic** special that reverts to prior weapon.

5. **FX and UX**
   - Implement **ripple/rainbow hit-wave FX** on enemy kills that stacks visually for chains.
   - HUD shows: **Score**, **Wave N/M** or **Boss**, **Chain**, **Lives** (hearts), weapon/upgrades. **Timer** removed in preview (optional future mode).
     

6. **Alignment with existing docs**
   - **GDD / implementation-plan:** The above maps to Phase 2 “Logic” and “Gameplay/UX” as described in `implementation-plan.md`, with this file as the **single source of truth** for Phase 2 enemy/upgrade/weapon behaviour.
   - **Stack:** Flutter host; assets from Figma (SVG/PNG in `assets/images/`); code-first animation and Rive fallback per `game-architecture.md`.
   - **Dev order:** Use the step-by-step list in §4, but read it **through the lens of the new framework** in §8–§9 (e.g. when implementing enemy attacks, also respect health scaling and wave difficulty curve). Preview uses **clear-to-advance** waves + **boss gate**, not a 60s timer.

---

---

## 10. Phase 2.4 — Boss win → mission complete (preview)

**Figma:** [Gratification screen — node 2273:84529](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2273-84529).

**Implemented in `preview/gameplay.html`:**

1. **Boss destroyed** — Existing per-hit **VIBGYOR ripple** (`drawRipples`) remains. **Added:** extra stacked ripples at the boss position, plus **~72 additive “spark” particles** cycling VIBGYOR colours (`VIBGYOR_SPARK_RGB`, `victorySparks`, `drawVictorySparks`) for a denser celebratory burst.
2. **Exit beat** — After `VICTORY_SPARKS_MS`, the ship **auto-ascends** (normalized `playerY` → ~1.48) while **“Awesome”** is drawn center-screen (`drawVictoryAwesome`). Player input does not move the ship during this phase (victory update returns before pointer lerp).
3. **Mission complete UI** — After `VICTORY_FLYOUT_MS`, an HTML overlay (`.mission-overlay`) matches the Figma structure: **MISSION COMPLETE** gradient title, **Sector 7 Alpha Secured**, bento grid (**Unlocked reward** / **Tactical Evaluation** with 1–3 stars from laser hit ratio, **Score Total**, **Accuracy** from laser shots fired vs hits), **Retry Mission** (full `resetRunState()`), **Exit to Menu** → `index.html`.
4. **Loop change** — Defeating the boss **no longer** immediately starts fodder wave 1; the run pauses on the gratification screen until **Retry**. **Lose** (0 lives) still shows **OUT OF LIVES** on canvas only.

**Tuning constants:** `VICTORY_SPARKS_MS`, `VICTORY_FLYOUT_MS`, `TIER_REWARD_TITLE` (placeholder copy for data reward line).

---

*Generated from Phase 2 implementation.docx for dev handoff. Update this file as clarifications are answered and as the high-level framework in §8 evolves.*
