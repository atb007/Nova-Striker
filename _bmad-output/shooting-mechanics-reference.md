# Shooting Mechanics & Ammo Reference (from Video Analysis)

**Source:** Video agent analysis of reference footage (`new.mp4`)  
**Game context:** Data Run (vertical space shooter)  
**Use:** Define shooting mechanics, ammo types, and asset list for implementation.

---

## 1. Reference Summary

**What the reference showed:**  
Retro-style 2D space shooter with a player ship and enemy targets. Rapid-fire projectiles (lasers/plasma), score at top left, starry background, small muzzle flashes at the rear of the ship, visible tracers, and square/rectangular impact effects.

---

## 2. Shooting Mechanics to Define

Use this section to lock in values and feel for Data Run.

### 2.1 Weapon & Fire Behaviour

| Aspect | Reference | Data Run (to decide) |
|--------|-----------|----------------------|
| **Weapon type** | Rapid-fire projectiles (lasers/plasma) | _e.g. laser, electric, hypnotic (per GDD)_ |
| **Fire mode** | Automatic or rapid semi-auto | _Auto / tap / hold?_ |
| **Recoil** | Not visibly simulated | _None / light screen shake / ship nudge?_ |
| **Reload** | Not visible (infinite or very large mag) | _Infinite / mag size / reload animation?_ |

### 2.2 Ammo Types (if multiple)

Define each ammo/weapon variant:

| Ammo / weapon name | Fire rate | Damage / effect | Visual (tracer, colour) | Unlock / tier |
|--------------------|-----------|------------------|---------------------------|---------------|
| **Three-way laser** (implemented) | ~250 ms spread | 1 hit = 1 kill | Cyan bars, 18° left/center/right spread, muzzle flash | Default |
| **Fire Blaster** (implemented) | Continuous stream | Instant | Central thick fire column, alive/random particles; switch F/2 or tap top-right; trigger later: upgrades from enemies | Testing: switch; later: drop |
| **Electric Shock** (implemented) | Auto-target | Instant | Procedural lightning from ship to up to 3 enemies; jagged animated bolts + branches; switch F (cycle) or 3/E | Testing: switch; later: drop |
| _e.g. Electric burst_ | | | | |
| _e.g. Hypnotic_ | | | | |

### 2.3 Visual Feedback (Shooting)

| Element | Reference | Data Run (to decide) |
|---------|-----------|----------------------|
| **Muzzle flash** | Small, brief at rear of ship | _Size, duration, colour, sprite?_ |
| **Tracers** | Short, solid lines | _Length, thickness, colour, fade?_ |
| **Impacts** | Small square/rect effects | _Shape, size, particles, colour?_ |
| **Screen effects** | Starry bg, faint speckles | _Damage vignette? Screen shake?_ |

---

## 3. HUD / UI (Shooting-Related)

| Element | Reference | Data Run (to decide) |
|---------|-----------|----------------------|
| **Score** | Top left, increasing | _Position, style, scale with tier?_ |
| **Health** | Not visible in reference | _Lives (3) / health bar / both?_ |
| **Ammo** | Not visible | _Show or hide? Mag count / infinite indicator?_ |
| **Hit markers** | Not visible | _On hit? On kill? Style?_ |

---

## 4. Asset List for Shooting & Ammo

Use as a checklist for art and VFX. Tick when created or delegated.

### 4.1 Player & Weapon

- [ ] Player spaceship (2D sprite)
- [ ] Player ship firing animation (if any)
- [ ] Muzzle flash sprite(s) – size/colour variants if needed
- [ ] Projectile sprite(s) – one per ammo type (laser, electric, etc.)

### 4.2 Enemies & Impacts

- [ ] Enemy ship/target sprites (shapes/variants)
- [ ] Explosion / impact effect sprite(s)
- [ ] Enemy destruction animation (if any)

### 4.3 Environment & UI

- [ ] Background (e.g. starfield)
- [ ] Background particles / speckles (optional)
- [ ] Score display UI asset
- [ ] Ammo indicator (if used)
- [ ] Hit marker / damage feedback (if used)
- [ ] Game over / win screen (if not already in GDD)

### 4.4 Audio

- [ ] Player weapon fire (per ammo type if different)
- [ ] Enemy hit
- [ ] Enemy destruction
- [ ] Background music

---

## 5. Implementation Notes

- **Fire detection in reference:** Brightness-based analysis did not detect clear muzzle-flash spikes (retro/small flashes). Rely on LLM description and this doc for design; tune in-code feel in the shooting sandbox (per GDD).
- **Levels = power-ups:** Map ammo/weapon variants to level unlocks and tier balance (see GDD Core Gameplay).
- **One finger:** Shooting should work with tap or auto-fire; ammo types should not add extra input complexity unless designed for it.

---

## 6. Implemented (Preview Build — Phase 1 scaffolding complete)

- **Ship (Figma-aligned):** Main Body Hull (vector shape or image asset), elongated; orange outline + soft glow. Cockpit Glass: vertical pill, cyan border + gradient (Figma 2154:992). Wing structures above thrusters; orange stroke (top edge thin 10% + glow); strong orange glow on all edges. Engine intake bar; blue thruster flames and blue glow below nozzles.
- **Movement:** Smooth X+Y; pointer/touch sets target; lerp (smooth factor 0.12). Ship Y range: 28%–86% of canvas height.
- **Thrusters:** Blue exhaust (cyan/blue gradients, particles) and blue glow below nozzles.
- **Weapon:** Three-way laser spread (18°), projectile speed 16, fire interval 240 ms.
- **Fire Blaster:** Implemented. Central thick fire stream, continuous; layered fire + particles; instant kill. Switch F/2 or tap top-right. Trigger later: upgrades from enemies.
- **Electric Shock:** Implemented. Procedural lightning auto-targets up to 3 nearest enemies in range; jagged, animated bolts with small branches; instant kill. Switch F (cycle) or 3/E.

---

## 7. Next phase (Phase 2) — Frameworks

- **Enemy flanking:** Groups of enemies enter from sides (left/right), not only from top.
- **Formations:** Enemies spawn in defined formations (V, line, wedge, etc.).
- **Enemy attacks:** Enemies can attack the player (projectiles, beams).
- **Enemy positioning:** After flanking/entering, enemies take position and stay static or move relative to player (constant distance); not only top-to-bottom motion.
- **Spaceship upgrades:** Upgrades change ship visuals and/or bullet types (unlock/enhance Fire Blaster, Electric Shock, spread).
- **Drops on kill:** Enemies drop upgrades when destroyed; pickups drive weapon unlocks and progression.

---

*Document generated from video agent output. Update the “Data Run (to decide)” columns and checkboxes as you lock design and complete assets.*
