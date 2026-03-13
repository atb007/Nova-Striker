---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9]
workflowType: game-architecture
project_name: MobileGame
user_name: jeremiah007
date: '2025-03-05'
inputDocuments: ['gdd.md', 'game-brief.md', 'implementation-plan.md']
---

# Data Run — Game Architecture

**Author:** jeremiah007  
**Date:** 2025-03-05  
**Status:** Draft  
**Context:** GDD-driven; flexible split: menus = Figma + code; animation/shooting/crash = code first, Rive fallback; Flutter host.

---

## Executive Summary

Data Run uses a **flexible architecture**: **menus and UI** are designed in **Figma** and implemented in **code** (Flutter); all menu assets are provided and laid out in code. **Animation, shooting, and crash mechanics** are handled in **code first**; if that doesn’t achieve the desired feel, **Rive** is used as fallback (e.g. for character animation or VFX). The **host** is **Flutter** (Android + iOS); it handles input (touch), run result API, persistence, and—with Figma assets—all menu screens. Rive is optional and used only where code-first doesn’t suffice. Official Rive docs: [Runtimes Getting Started](https://rive.app/docs/runtimes/getting-started), [Scripting Getting Started](https://rive.app/docs/scripting/getting-started).

---

## Decision Summary

| Category | Decision | Version / reference | Affects Epics | Rationale |
|----------|----------|--------------------|---------------|-----------|
| **Menus & UI** | **Figma + code** | Figma designs; Flutter layouts and assets | Core loop, Polish, Rewards | Menus (main, tier select, end screen) designed in Figma; implemented in Flutter with provided assets; no Rive for menus. |
| **Host runtime** | **Flutter** (Android + iOS) | [Rive Flutter](https://rive.app/docs/runtimes/flutter), `package:rive` (optional) | Core loop, Rewards | Single codebase; touch, run result API, persistence; Rive only if needed for game feel. |
| **Animation, shooting, crash** | **Code first; Rive fallback** | Flutter (e.g. animations, hit reactions); Rive if needed | Core loop, Enemies, Polish | Try code for animation, shooting, crash mechanics; use Rive only if code doesn’t deliver the feel. |
| **Rive (optional)** | Game feel only when code isn’t enough | Rive runtimes + [Scripting](https://rive.app/docs/scripting/getting-started) | Enemies, Polish | Optional: character/VFX animation, complex motion; not used for menus. |
| **Host responsibility** | Input (touch), menus (Figma assets + code), run result, persistence, backend client | — | All | All menu logic and layout in code; run result and services in host. |
| **Run result contract** | `{ tier, win, livesLeft?, collectiblesEarned[], level? }` → backend returns `{ dataPack, vouchers[] }` | GDD | Rewards | Single API for rewards; engine-ready for multiple loops later. |
| **Beginner path** | State Machines + Data Binding first; add Rive Scripting (Luau) when ready | [Rive Docs](https://rive.app/docs/runtimes/getting-started) | All | Reduces risk; Rive examples (Snake, Slot Machine, Plinko) show scripting can handle full game logic. |

---

## Project Structure

```
MobileGame/
├── assets/
│   ├── images/                  # Figma exports (menu screens, HUD, icons)
│   └── rive/                    # Optional .riv files (only if used for game feel)
│       └── (e.g. characters.riv, vfx.riv when code-first isn't enough)
├── lib/                         # Flutter host app
│   ├── main.dart
│   ├── sandbox/                 # Shooting / VFX testing environment (Phase 0)
│   │   └── (lasers, electricity, hypnotic effects; iterate on feel; gate before full game)
│   ├── ui/                      # Screens from Figma: main menu, tier select, end screen (code + assets)
│   ├── game/                    # Run state, difficulty, level; animation/shooting/crash (code first)
│   ├── rive/                    # Optional: Rive loaders/drivers when Rive is used
│   ├── rewards/                 # Run result builder, backend client
│   └── persistence/            # Level, wallet (local or backend)
├── backend/ or api/             # Stub or real: run result → grant data/vouchers
└── docs/
    └── _bmad-output/            # GDD, brief, this architecture
```

*(Backend may be separate repo.)*

---

## Epic to Architecture Mapping

| Epic | Figma + code | Rive (optional) | Notes |
|------|--------------|-----------------|------|
| **Core loop and run** | Menus (Figma assets + Flutter); run timer, lives, input (touch) in code. | — | Menu flow and HUD implemented in code using Figma assets. |
| **Enemies and boss** | Spawn logic, difficulty (tier), win/fail, hit/crash in **code first**. | Use Rive only if code animation/crash feel isn’t good enough. | Try Flutter animations; add Rive for characters/VFX if needed. |
| **Rewards integration** | End screen built in code (Figma layout); run result, backend call in host. | — | Dynamic text (data pack, voucher count) in Flutter. |
| **Vouchers and collectibles** | Pickup logic, collection list, HUD counter in code; assets from Figma. | Optional: pickup/VFX in Rive if desired. | Host = “collected” list and run result payload. |
| **Polish and feel** | SFX from code; animation/shooting/crash in code first. | Rive for VFX or character animation only if code doesn’t suffice. | Flexible: add Rive where it clearly improves feel. |
| **Engine readiness** | Run result API in host. | Same run result contract if Rive is used later. | No change to API; new loop = new screens (Figma + code), same run result. |

---

## Technology Stack Details

### Core Technologies

| Layer | Technology | Role |
|-------|------------|------|
| **Authoring** | Rive Editor | State machines, artboards, animations, optional Luau scripts. Export `.riv`. |
| **Runtime (Rive)** | Rive runtime for chosen platform | Load `.riv`; control [State Machine inputs](https://rive.app/docs/runtimes/state-machines), [Data Binding](https://rive.app/docs/runtimes/data-binding); [cache .riv](https://rive.app/docs/runtimes/caching-a-rive-file) when reusing. |
| **Runtime (host)** | **Flutter** | App shell (Android + iOS), touch input, run result API, persistence. [Rive Flutter](https://rive.app/docs/runtimes/flutter) (`package:rive`). |
| **Backend** | Stub or service | Accept run result; return `{ dataPack, vouchers[] }`; anti-grind (caps). |

### Flexible Split: Figma + Code First, Rive Fallback

**Figma + code (menus and UI):**

- **Menus:** Main menu, tier select, end screen (win/fail) are **designed in Figma**. All assets are **provided** (exports or specs). **Implemented in Flutter** (layouts, navigation, buttons). No Rive for menus.
- **HUD:** In-run HUD (lives, tier label, etc.) from Figma assets; layout and logic in code.
- **Dynamic content:** Tier label, “win up to X MB”, lives left, voucher count, actual data pack won — all driven by Flutter (state and backend response).

**Code first (animation, shooting, crash):**

- **Animation, shooting, crash mechanics:** Implemented in **Flutter/code first** (e.g. Flutter animations, hit reactions, simple VFX). If the result doesn’t feel good enough, **add Rive** for those parts only (e.g. character animation, impact VFX).
- **Input:** Touch (drag = move, tap = shoot) in Flutter; game state and run logic in code.

**Shooting / VFX testing environment (Phase 0):**

- **Purpose:** The primary USP is shooting feel (lasers, electricity/shockers, hypnotic-style attacks). Before full game build, a **sandbox** (`lib/sandbox/` or equivalent) is used to prototype and iterate these effects in **code** (e.g. CustomPainter, Flutter animations). No run loop or rewards—just VFX and shooting feel.
- **Gate:** If the sandbox proves code can deliver the desired dopamine-releasing feel, the full game is built on that. If not, Rive or other options are used for those effects. See implementation-plan.md Phase 0.

**Rive (optional fallback):**

- **When to use:** Only when code-first animation, shooting, or crash feel isn’t sufficient. Examples: character idle/hit/destroy, bullet trails, boss phase VFX.
- **What Rive does:** .riv files with artboards/state machines; Flutter loads via `package:rive` and drives with state machine inputs or data binding. Not used for menus.

**Host (Flutter) always:**

- **Run result:** On run end, build `{ tier, win, livesLeft?, collectiblesEarned[], level? }`; call backend; get `{ dataPack, vouchers[] }`.
- **Persistence:** Player level, wallet, tier caps or anti-grind state.
- **Loading:** Figma assets in `assets/images/`; optional `.riv` in `assets/rive/` only if Rive is used.

### Integration Points

- **Figma → Flutter:** Use Figma exports (PNG, SVG, or design tokens) in `assets/images/`; implement screens in `lib/ui/` with Flutter widgets. Provide all assets as required; code handles layout and navigation.
- **Host → Rive (only if used):** State machine inputs (e.g. `hit`, `destroy`), data binding. See [State Machine Playback](https://rive.app/docs/runtimes/state-machines) and [Data Binding](https://rive.app/docs/runtimes/data-binding). Use only for game-feel fallback.
- **Host → Backend:** Run result POST; response = rewards. Auth and identity handled by host/backend.

---

## Rive: Optional, Code-First

- **Default:** Implement **animation, shooting, crash** in **Flutter/code**. Menus and UI from **Figma** in code. No Rive required for MVP.
- **When to add Rive:** If code-based animation or impact feel isn’t good enough, add Rive for specific elements (e.g. ship/enemy hit/destroy, boss VFX). Use [State Machines](https://rive.app/docs/runtimes/state-machines) and [Data Binding](https://rive.app/docs/runtimes/data-binding); optionally [Scripting](https://rive.app/docs/scripting/getting-started) (Luau).
- **Caching (if using Rive):** Load each `.riv` once and reuse. [Caching a Rive File](https://rive.app/docs/runtimes/caching-a-rive-file).

---

## Implementation Patterns

1. **Menus = Figma + code:** All menu screens (main, tier select, end screen) are designed in Figma. Team provides all assets; Flutter implements layout and navigation. No Rive for menus.
2. **Game feel = code first:** Animation, shooting, crash mechanics implemented in Flutter. Add Rive only for parts where code doesn’t achieve the desired feel.
3. **Run result in host:** Only Flutter builds the run result payload and calls the backend. End screen (Figma layout in code) displays the result; no Rive required.
4. **One finger in code:** Touch events in Flutter; map to “move” and “shoot”; game state and run logic in code. If Rive is used for characters, host still owns input and sends inputs to Rive (e.g. `hit`, `destroy`).
5. **Rive naming (if used):** Use consistent names for state machine inputs and data binding (e.g. `hit`, `destroy`, `dataPackMB`). Document in repo (e.g. `docs/rive-bindings.md`).

---

## Consistency Rules

### Naming Conventions

- **Rive state machine inputs:** `camelCase` (e.g. `startRun`, `bossHit`, `gameOver`).
- **Data binding names:** `camelCase` (e.g. `dataPackMB`, `voucherCount`, `livesLeft`).
- **.riv files:** `snake_case` (e.g. `ui_menu.riv`, `gameplay.riv`).

### Code Organization

- Host: separate modules for Rive loader/driver, game/run state, rewards client, persistence.
- Rive: one file per “domain” (menus, gameplay HUD, characters) or one file with multiple artboards; avoid one giant .riv for everything.

### Error Handling

- Host: run result API failures → show retry or “claim later”; do not block Rive UI.
- Rive: optional “error” state in state machine for network or validation errors if host signals them.

### Logging

- Host: log run result send/receive, tier/level choices; no PII in logs.
- Rive: use [Debugging](https://rive.app/docs/scripting/debugging/debug-panel) for scripts during development.

---

## Data Architecture

- **Run state (host or Rive):** tier, level, lives left, run phase (pre-run / run / boss / end), collectibles collected this run. Prefer host if backend needs level/tier; Rive can mirror for display.
- **Run result (host):** `{ tier, win, livesLeft?, collectiblesEarned[], level? }` — built at run end and sent to backend.
- **Backend response:** `{ dataPack: { amountMB, label? }, vouchers: [{ id, label? }] }` (or similar). Host stores and passes to Rive for end screen data binding.
- **Persistence:** Level (and optionally wallet) in host (local storage or backend). Rive does not persist; host restores and re-applies to Rive on launch.

---

## API Contracts

### Run result (client → backend)

```json
POST /run/complete
{
  "tier": "500MB",
  "win": true,
  "livesLeft": 1,
  "collectiblesEarned": ["voucher_1", "voucher_2"],
  "level": 2
}
```

### Grant response (backend → client)

```json
{
  "dataPack": { "amountMB": 250, "label": "250 MB" },
  "vouchers": [
    { "id": "v1", "label": "Brand A 10% off" }
  ]
}
```

*(Exact field names to match backend; auth/identity omitted.)*

---

## Security Architecture

- **Run result:** Sent over HTTPS; no sensitive PII in payload (user identity via auth token/session).
- **Anti-grind:** Enforced server-side (caps, cooldowns); client sends run result, server decides grant.
- **.riv files:** Shipped with app or loaded from trusted CDN; no user-supplied .riv in MVP.

---

## Performance Considerations

- **Rive:** [Cache .riv files](https://rive.app/docs/runtimes/caching-a-rive-file) when reusing (e.g. same enemy type); limit simultaneous instances if needed.
- **Host:** Run result sent within 5 s of run end (per GDD); show “Claiming…” in Rive while waiting.
- **60 fps:** Use recommended Rive renderer for platform ([Choose a Renderer](https://rive.app/docs/runtimes/choose-a-renderer)); keep draw calls and state machine updates bounded.

---

## Deployment Architecture

- **Client:** Mobile (iOS/Android) or Web; host app + bundled or CDN-hosted .riv files.
- **Backend:** Stub (e.g. JSON file or simple server) for MVP; real service for production (run result → grant, anti-grind, redemption).

---

## Development Environment

### Prerequisites

- [Rive Editor](https://rive.app/) (desktop or web) for authoring .riv files.
- Host SDK: Flutter / Node + React or Vite / React Native (choose one).
- Backend: minimal (e.g. Express, Firebase, or static stub).

### Rive Documentation (reference)

- [Getting Started with Rive Runtimes](https://rive.app/docs/runtimes/getting-started) — Load and control .riv on your platform.
- [Rive Scripting Getting Started](https://rive.app/docs/scripting/getting-started) — Luau scripts, protocols, inputs, data binding in editor.
- [State Machine Playback](https://rive.app/docs/runtimes/state-machines) — Drive state machines from host.
- [Data Binding](https://rive.app/docs/runtimes/data-binding) — Update text, numbers, images at runtime.
- [Caching a Rive File](https://rive.app/docs/runtimes/caching-a-rive-file) — Reuse one .riv for many instances.
- [Feature Support](https://rive.app/docs/feature-support) — Check runtime/version for your platform.

### AI Tooling (MCP Servers)

- No Rive-specific MCP required; use general code/documentation tools. Figma MCP can stay for UI reference if you use Figma alongside Rive.

### Setup Commands

```bash
# Flutter + Rive (locked)
flutter create .
flutter pub add rive
# Add .riv files under assets/rive/ and register in pubspec.yaml:
#   flutter:
#     assets:
#       - assets/rive/
```

---

## Architecture Decision Records (ADRs)

| ID | Decision | Context | Rationale |
|----|----------|---------|-----------|
| ADR-1 | Menus = Figma + code | Menus in Figma; assets provided; Flutter implements “heavy lifting in Rive”; beginner/intermediate with Rive | Single design source; code for layout and navigation; no Rive for UI. |
| ADR-2 | Code first for animation/shooting/crash; Rive fallback | Try code; add Rive only if feel insufficient | Keeps Rive optional. |
| ADR-3 | Host owns run result and backend call | Rewards and anti-grind are server-authoritative | Flutter builds payload and calls backend; end screen (Figma + code) displays result. |

---

_Generated for Data Run (GDD + implementation plan). Flexible: Figma + code for menus; code first for animation/shooting/crash, Rive fallback; Flutter host._  
_Date: 2025-03-05 | Author: jeremiah007_
