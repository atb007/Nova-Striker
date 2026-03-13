# Nova Striker — Preview Gameplay

**Build:** `preview/gameplay.html` (opened via **Battle** on home screen).  
**Status:** Phase 1 scaffolding complete.

---

## Current Implementation

### Controls
- **Movement:** Drag (mouse) or touch to move the ship. **X and Y** movement; smooth lerp so the ship follows the pointer without snapping.
- **Shooting:** Automatic three-way laser spread (no extra input). Weapon switch: **F** (cycle), **2** (Fire), **3** / **E** (Electric), or tap top-right.

### Ship (Figma-aligned)
- **Size:** 80% scale; 96×112 px body reference + thruster glow below.
- **Main Body Hull:** Figma vector shape (pointed nose, wider midsection, broad flat stern). Hull image asset when available; else canvas-drawn path. Orange outline with soft glow (shadowBlur 24).
- **Cockpit Glass:** Vertical pill (24×48), top 16 px; cyan border, dark teal fill, inner gradient (Figma 2154:992). Subtle cyan glow on stroke.
- **Wing structures:** Above thrusters; left/right with single rounded corner per Figma. Orange stroke on left, bottom, right edges; top edge drawn with thin stroke (10% thickness) + same orange glow so glow is visible. Cyan pill overlays (vents). Strong orange glow on all wing edges (shadowBlur 28).
- **Engine intake:** Orange-tinted bar above thrusters.
- **Thrusters:** Blue flame exhaust (layered cyan/blue gradients, particles) and blue glow below nozzles (replacing previous orange).
- **Position bounds:** X 10%–90% of width; Y 28%–86% of play area height.

### Weapons (all retained)
- **Three-way laser (default):** One shot = three projectiles (center + 18° left/right). Fire interval 240 ms, projectile speed 16. Cyan tracers, brief muzzle flash.
- **Fire Blaster:** Central thick fire stream, continuous; turbulent fire + particles; instant kill. Switch: **F** / **2** or tap top-right. *Trigger later: upgrades from enemies.*
- **Electric Shock:** Procedural lightning from ship to up to 3 nearest enemies; auto-targets, instant kill. Jagged animated bolts + branches. Switch: **F** (cycle) or **3** / **E**.

### Enemies & VFX
- **Enemies:** Diamond (cyan) and circle (orange) spawn in waves; sometimes 2–3 at once. Move downward; one hit = destroy + rectangular impact explosion.

### Docs
- `RUN.md` — how to run preview, Phase 1 summary.
- `_bmad-output/shooting-mechanics-reference.md` — ammo table, §6 Implemented.

---

## Phase 1 scaffolding

Ship art and layout match Figma (hull, cockpit, wings, thrusters). All three ammo types work; weapon switching is for testing; upgrade drops to trigger Fire/Electric are planned for Phase 2.

---

## Next phase (Phase 2) — Overarching frameworks

1. **Enemy flanking from sides** — Groups of enemies enter from the left and/or right (flanking), not only from the top.
2. **Formations** — Enemies spawn and move in defined formations (e.g. V, line, wedge) rather than only random single/duo/trio.
3. **Enemy attacks** — Enemies can attack the player (e.g. projectiles, beams); not only movement.
4. **Enemy positioning and holding** — Enemies do not only move top-to-bottom. After flanking (or entering), they take up positions and either stay static or move relative to the player, keeping a constant distance (e.g. orbit, hold offset).
5. **Spaceship upgrades** — Upgrades that change the ship’s overall design (visual) and/or affect attacking bullet types (e.g. unlock or enhance Fire Blaster, Electric Shock, spread).
6. **Upgrades on annihilation** — Enemies drop upgrades when destroyed; these pickups drive progression and weapon unlocks (e.g. Fire Blaster, Electric Shock triggers).

---

## Fire Blaster (implemented)

- **Behaviour:** One central column of thick fire, continuous stream from ship nose (no discrete bullets).
- **Visual:** Layered yellow/orange/red gradient, animated edges, ~14 drifting particles for “alive” feel; soft glow behind.
- **Damage:** Instant kill on contact with stream hitbox (rect, ~36×100 px).
- **Trigger:** For testing: switch with **F** / **2** or tap top-right. *Planned:* trigger from upgrades dropped by enemies (flexible, not fixed).

---

*Preview build for Data Run / Nova Striker. See GDD and game-brief for full design.*
