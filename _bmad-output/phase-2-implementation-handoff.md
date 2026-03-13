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
| L1 fight | 2181-1064 | [L1 fight](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2181-1064) |
| L1 Boss fight | 2195-749 | [L1 Boss fight](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2195-749) |

---

## 3. Clarification checklist (for product/design before or during dev)

- [ ] **Red blur edges:** Spec (width, opacity, animation) and whether it’s a full-screen overlay or viewport-edge only.
- [ ] **Entry paths:** Authored per wave (e.g. in data/JSON) vs procedural (e.g. bezier/circle by spawn side).
- [ ] **Mid enemy:** When will mid-type design be ready? Use placeholder until then?
- [ ] **Level 2+ assets:** Plan for fodder/mid/boss variants and upgraded ship for later levels.
- [ ] **Blur rendering:** List assets that use blur; decide: export as PNG with blur baked in, or implement blur in engine (e.g. shader/post-process) to match Figma.
- [ ] **SVG vs PNG:** Which assets are canonical as SVG for runtime (e.g. enemies, ship, pickups)? Use PNG only for ref or for specific cases?

---

## 4. Implementation alignment with existing docs

- **GDD / implementation-plan:** Phase 2 “Logic” (implementation-plan §2) covers core loop, tier/level, run result, polish. This handoff is the **gameplay/UX Phase 2** (flanking, formations, attacks, positioning, upgrades, drops).
- **Stack:** Flutter host; assets from Figma (SVG/PNG in `assets/images/`); code-first animation, Rive fallback per `game-architecture.md`.
- **Suggested dev order (for this handoff):** (1) Flanking + red blur edges + entry path/formation, (2) Enemy types (fodder L1, boss L1, placeholder mid), (3) Enemy attacks after formation, (4) Drops on kill + upgrade pickup asset, (5) Ship upgrade (visual + weapon unlock) and upgraded ship L1 asset.

---

## 5. Asset delivery note (from doc)

> Along with SVG, PNG files are provided in images folder with proper naming for reference.

Ensure dev has: **images folder** (or equivalent) with named SVG/PNG for fodder 1 & 2, boss L1, upgraded ship L1, upgrade pickup; and any viewport-edge/blur assets if they are separate.

---

*Generated from Phase 2 implementation.docx for dev handoff. Update this file as clarifications are answered.*
