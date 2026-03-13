---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
inputDocuments: ['game-brief.md']
documentCounts:
  briefs: 1
  research: 0
  brainstorming: 0
  projectDocs: 0
workflowType: gdd
lastStep: 14
project_name: MobileGame
user_name: jeremiah007
date: '2025-03-05'
game_type: shooter
game_name: Data Run
---

# Data Run - Game Design Document

**Author:** jeremiah007  
**Game Type:** Shooter (vertical-scroll, hypercasual)  
**Target Platform(s):** Mobile (iOS, Android)

---

## Executive Summary

### Core Concept

Data Run is a vertical-scrolling space shooter where one run equals one session. Players pick a tier ("win up to" 100MB / 500MB / 1GB); the **actual data pack won is variable** (business rule)—messaging is "win up to," not "get exactly." **Levels** (Level 1, 2, …) are tied to **power-ups**: progression unlocks better power-ups to tackle harder bosses. Play a short run (1–3 min) with 3 lives, defeat a tier-scaled boss, and claim a random data pack (up to tier cap) plus vouchers. One-finger controls (dodge, shoot, collect) and a fixed session boundary support both casual play and users who are primarily there for free data.

### Target Audience

- **Primary:** Mobile-first users in regions where data costs matter; hypercasual or light arcade players; short sessions (1–3 min); motivated by free data/vouchers and simple shooter action.
- **Secondary:** Rewards-only users (easiest tier); core arcade fans (higher tiers, boss variety).

### Unique Selling Points (USPs)

1. **Shooting feel (primary USP)** — Lasers, electricity emitters/shockers, and hypnotic-style attacks are designed to be cool and dopamine-releasing. These are prototyped and iterated in a **code-first testing environment** (shooting/VFX sandbox); if they feel good in code, the full game is built on that; otherwise Rive or other options are considered.
2. **Integrated play-for-rewards** — One product: game + data + vouchers; tier choice = difficulty; no separate “reward mode.”
3. **Session control** — One run = one session; fixed length, 3 lives; clear for analytics, partners, and player psychology.
4. **Engine for multiple loops** — Same rewards layer can support shooter, runner, puzzle later; one integration for brands/telcos.

---

## Goals and Context

### Project Goals

- Deliver a minimum viable vertical shooter with real-world rewards (data packs, vouchers) and tiered difficulty.
- Establish a rewards engine (tiers, anti-grind, run result contract) that can support additional core loops in the future.
- Achieve clear session boundaries (one run = one session) for measurement, fairness, and partner reporting.

### Background and Rationale

- Combines proven hypercasual shooter engagement (e.g. Galaxy Attack, Galaxiga) with rewards-platform demand (free data, vouchers).
- Tiered difficulty tied to reward value keeps stakes transparent and fair; 3 lives and end boss give a clear “gate” before rewards.
- Design supports both “play for fun” and “play for data” segments without separate products.

---

## Core Gameplay

### Game Pillars

1. **One run = one session** — Fixed run length (1–3 min), 3 lives per run, binary outcome (win = pack + vouchers / fail = try again). No mid-run save.
2. **Difficulty follows reward** — Player chooses **tier** (which data pack they’re playing for: e.g. 100MB / 500MB / 1GB). Actual pack won is variable (business); message win up to. *Tier = reward cap, not “Level 1, Level 2.”* Difficulty and boss scale with tier. No separate “hard mode.”
3. **Levels = power-ups** — Levels (Level 1, 2, …) unlock or improve power-ups to tackle harder bosses. Tier = run difficulty; level = player tools.
4. **One finger, three verbs** — Dodge (move), shoot (tap or auto), collect (overlap pickups). Single input channel.
5. **Real rewards, real stakes** — Vouchers and data are real-world value; anti-grind and transparent end screen build trust.

**Pillar priority:** Session control and difficulty–reward fairness first; then control simplicity and reward clarity.

### Core Gameplay Loop

1. **Pre-run:** Player selects tier ("win up to" e.g. 100MB / 500MB / 1GB). Difficulty and boss parameters are set by tier. Power-ups available from player's level.
2. **Run:** Vertical scroll; player dodges (move ship), shoots (tap or auto-fire), collects (voucher pickups and power-ups). 3 lives; run length fixed (e.g. 90 sec or 2 min).
3. **Boss:** Final wave is a boss; variant and difficulty scale with tier. Defeat boss to win.
4. **Resolution:** Win → random data pack (up to tier cap) + vouchers collected; Fail → no pack, option to start new run.
5. **End screen:** Show rewards (actual pack won, voucher count); option “Play again” (same or different tier) or “Claim and exit.”

### Win/Loss Conditions

- **Win:** Player defeats the end boss before losing all 3 lives. Rewards: random data pack (up to chosen tier cap) + all vouchers collected during the run.
- **Loss:** Player loses all 3 lives before defeating the boss. No data pack; vouchers collected during run may be kept or forfeit (design decision). Player can start a new run.

---

## Game Mechanics

### Primary Mechanics

- **Dodge** — Move ship via drag/hold (one finger). Avoids enemy bullets and obstacles; defines lane choice and survival. Movement is continuous; no separate “dodge button.”
- **Shoot** — Tap to fire or auto-fire. Destroys enemies; may trigger voucher drops. Single weapon type for MVP; no ammo or reload.
- **Collect** — Overlap ship with voucher pickups (and optionally power-ups). No separate collect button; collection is movement-based.

**Secondary (optional for MVP):** Voucher-as-power-up (e.g. short shield or burst); lane-based voucher vs danger lanes.

### Controls and Input

- **Platform:** Touch (mobile). Single-finger only for MVP.
- **Mapping:** Drag/hold = move ship (dodge). Tap or auto = shoot. Overlap = collect.
- **No:** Second finger, virtual joystick, or separate collect/shoot buttons. Keep all actions on one finger to preserve hypercasual clarity.

---

## Shooter Specific Elements

### Weapon Systems

- **MVP:** One weapon type: forward-firing (or spread) primary weapon. No weapon swap or upgrades in-run.
- **Stats (tunable):** Fire rate, projectile speed, damage per hit. Same weapon for all tiers; difficulty comes from enemy count, bullet density, and boss health/speed.
- **Feel (USP):** Shooting feel is the main differentiator. Target VFX types for iteration in the **shooting/VFX sandbox**: **lasers** (beams, tracers), **electricity emitters / shockers** (arcs, chains), **hypnotic-style attacks** (swirls, pulses). Sandbox is used to prove feasibility in code; full game builds on what works.
- **Feedback:** Snappy SFX and visual feedback; no recoil or reload. Optional: brief “burst” power-up from voucher pickup.

### Aiming and Combat Mechanics

- **Aiming:** No explicit aim—ship fires forward (or fixed spread). Player aims by positioning the ship (move to align with enemies).
- **Hit detection:** Projectile-based; bullets hit enemies on overlap. No hitscan.
- **No:** Critical hits, weak points, or melee for MVP. Keep combat simple and readable.

### Enemy Design and AI

- **Enemy types (MVP):** Fodder (simple movement, few shots), possibly one mid-tier type; boss (unique pattern, tier-scaled health/damage/speed).
- **AI:** Simple patterns (e.g. move in lane, fire at intervals). No flanking or cover; vertical scroll keeps encounters readable.
- **Spawn:** Wave-based; waves advance over fixed run length. Spawn rate and density scale with tier.
- **Difficulty scaling:** Higher tier = more enemies, faster bullets, more bullet density, boss with more health and faster patterns. All driven by tier config.

### Arena and Level Design

- **Structure:** Vertical scroll; screen moves upward (or player ship fixed, background scrolls). Lanes or free movement within screen bounds.
- **Flow:** Waves of enemies; optional voucher pickup lanes; final wave = boss. No discrete “levels”; one run = one continuous scroll to boss.
- **Cover:** No cover system. Dodging is the only avoidance.
- **Placement:** Voucher pickups in lanes or from enemy drops; boss at end. Power-ups (if any) placed to create risk/reward (e.g. voucher in dangerous lane).

### Multiplayer Considerations

- **Out of scope for MVP.** Single-player only. No PvP, co-op, or leaderboards in MVP. May be considered later (e.g. leaderboards by tier or region).

---

## Progression and Balance

### Player Progression

- **Levels:** Level 1, 2, … unlock or improve power-ups (e.g. shield, burst). Higher level = better tools for harder bosses. Progression by wins, play count, or XP (TBD).
- **In-run:** No progression within a run. Player has 3 lives and power-ups from their level; collect vouchers; reach boss; win or fail.
- **Between runs:** Persistent wallet: accumulated data and vouchers. Optional: first-win-of-the-day bonus, daily caps per tier (anti-grind).

### Difficulty Curve

- **Per run:** Difficulty is set by tier choice (100MB = easiest, 1GB = hardest). No curve within run—maintain tier difficulty throughout.
- **Tier mapping:** Back-end config maps tier to: enemy spawn rate, bullet speed, boss health/damage/speed. Tuning goal: higher tier feels noticeably harder but fair.

### Economy and Resources

- **In-run resources:** Lives (3), voucher pickups (collectibles). No in-run currency.
- **Meta resources:** Data pack (granted on win); vouchers (collected in-run, redeemed post-run). Voucher catalog and data pack sizes defined by partners/backend.
- **Anti-grind:** Caps or cooldowns on high-value tier wins (e.g. limit 1GB wins per day) to protect sustainability and fairness.

---

## Level Design Framework

### Level Types

- **Single run type for MVP:** One continuous vertical-scroll “level” per run. Length fixed by time or wave count (e.g. 90 sec or N waves then boss).
- **No discrete levels.** Variation comes from tier (difficulty), boss variant, and optional voucher placement.

### Level Progression

- **No level progression.** Each run is independent. “Progression” is player choosing higher tier for bigger reward and harder run.
- **Optional later:** Themed “seasons” or rotation (e.g. different boss set per week) without changing core structure.

---

## Art and Audio Direction

### Art Style

- Clear, readable shapes: ship, bullets, enemies, pickups, boss. High contrast for lanes and obstacles. Style: simple geometric or soft sci-fi; avoid clutter.
- **UI:** Minimal HUD—lives, optional “distance to boss” or tier label. End screen: rewards only (data pack size, voucher count, claim/play again).
- **Figma:** When available, Figma designs for HUD, end screen, tier-select, and main menu will be linked here to align art and implementation. *Supply Figma when you have: tier-select screen, in-run HUD, end screen (win/fail), and main menu.*

### Audio and Music

- **SFX:** Shoot, collect, hit, damage (player), win, fail. Short and satisfying; support game feel.
- **Music:** Optional; light track for run and boss. Low priority for MVP.

---

## Technical Specifications

### Performance Requirements

- **Target:** 60 fps on target mobile devices. Short runs and limited on-screen objects to keep load low.
- **Run result:** Client must output a structured “run result” (tier, win/fail, list of collectibles earned) for the rewards backend. No PII in run result; user identity handled by backend.

### Platform-Specific Details

- **Mobile:** Touch-only; support portrait orientation (vertical scroll). Consider safe areas and notches.
- **Backend:** Tiers, voucher catalog, data pack fulfillment, anti-grind rules, redemption. API contract: accept run result; return grant status.

### Asset Requirements

- **MVP:** Player ship, 1–2 enemy types, 1–2 bullet types, 2–3 boss variants, voucher pickup art, basic UI (tier select, HUD, end screen). Reuse and recolor where possible.
- **Figma:** UI screens (tier-select, HUD, end screen, main menu) can be supplied via Figma for implementation reference. Link or export when ready.

---

## Development Epics

### Epic Structure

1. **Epic: Core loop and run** — Tier select, run setup (difficulty from tier), vertical scroll, player movement, shoot, collect, 3 lives, run end (time or wave).
2. **Epic: Enemies and boss** — Enemy spawn and simple AI, bullet patterns, boss variants and tier-scaled stats, boss defeat = win.
3. **Epic: Rewards integration** — Run result contract, backend API (tiers, grant data/vouchers), end screen (show rewards, claim/play again), anti-grind (caps/cooldowns).
4. **Epic: Vouchers and collectibles** — Voucher pickups in-run, collection tracking, voucher catalog integration, optional voucher-as-power-up.
5. **Epic: Polish and feel** — SFX, basic VFX, HUD, tier-select and main menu; 60 fps and mobile tuning.
6. **Epic: Engine readiness (optional for MVP)** — Run result as shared contract; structure so a second core loop (e.g. runner) could plug in later without rewriting rewards.

---

## Success Metrics

### Technical Metrics

- 60 fps during run on target devices; run result sent to backend within 5 s of run end; no critical bugs on win/fail/claim flow.

### Gameplay Metrics

- Run completion rate (reach boss); win rate by tier; session length (align with target 1–3 min); retention (D1/D7). For free-data segment: completion and win rate on easiest tier.

### Business Metrics

- Reward claim rate, redemption rate, cost per rewarded user; partner reporting (sessions, rewards per user). Anti-grind effectiveness (no abnormal farming).

---

## Out of Scope

- Multiple core loops (runner, puzzle) in MVP—design only; implement post-MVP.
- Narrative, story, or lore in MVP.
- Multiplayer, leaderboards, or social features in MVP.
- Complex weapon progression, character levels, or skill trees in MVP.
- Localization beyond one language for MVP (to be confirmed).

---

## Assumptions and Dependencies

- **Assumptions:** Partner(s) provide data pack sizes and voucher catalog; backend can fulfill data and voucher grants; tier–difficulty mapping is tunable without client release.
- **Dependencies:** Flutter client; rewards backend (tiers, run result API, anti-grind, redemption); Figma for menus (assets provided); Rive optional for game feel (animation, shooting, crash)—code first, Rive fallback if needed.

---

## Figma and Visual Design

**Menus = Figma only, implemented in code.** All menu assets will be provided from Figma; Flutter implements layouts and logic. **When to supply Figma (or other UI designs):**

- **Now (optional):** If you have tier-select, in-run HUD, end screen (win/fail), or main menu, you can share Figma links or exports. I’ll reference them in Art and Audio and Technical Specifications and ensure the GDD matches the layouts.
- **When we implement UI:** As soon as you have screens for tier-select, HUD, and end screen, supply them so implementation can match. Main menu and onboarding can follow.

**Where Figma will be used in this GDD:**

- **Art and Audio Direction** — Visual style, HUD layout, end screen layout.
- **Technical Specifications / Asset Requirements** — UI screens as implementation reference.

You can add Figma links or files at any time; I’ll integrate them into the GDD and call out any gaps (e.g. missing states or resolutions).
