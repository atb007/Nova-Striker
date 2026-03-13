---
stepsCompleted: [1, 2, 3, 4, 5, 6, 7, 8]
inputDocuments: ['brainstorming-session-2025-03-05.md']
documentCounts:
  brainstorming: 1
  research: 0
  notes: 0
workflowType: game-brief
lastStep: 8
project_name: MobileGame
user_name: jeremiah007
date: '2025-03-05'
game_name: Data Run
---

# Game Brief: Data Run

**Date:** 2025-03-05  
**Author:** jeremiah007  
**Status:** Draft for GDD Development

---

## Executive Summary

**Data Blaster** is a hypercasual vertical-scrolling space shooter where players dodge, shoot, and collect in short (1–3 min) runs to earn **real-world rewards**: brand vouchers and free data. Players choose a tier (e.g. "win up to 100MB / 500MB / 1GB"); the **actual data pack won is variable** (business rule)—messaging is "win up to," not "get exactly." Difficulty and end-boss scale with tier. **Levels** (Level 1, 2, …) are tied to **power-ups**: progression unlocks better power-ups to tackle harder bosses. Each run gives 3 lives; winning grants a random data pack (within tier cap) plus vouchers collected. One-finger controls, fixed run length, and a clear “one run = one session” boundary support both casual play and users who are primarily there for free data. The design is built so a shared rewards engine can later support multiple core loops (e.g. shooter, runner, puzzle) with the same business model.

---

## Game Vision

### Core Concept

A vertical-scrolling space shooter where one run equals one session: pick your tier ("win up to" X data), play a short run with 3 lives and power-ups from your level, beat the tier-scaled boss, and claim a random data pack (up to tier cap) plus vouchers—all with one-finger controls.

### Elevator Pitch

**Data Blaster** is a fast-paced vertical space shooter (think Galaxy Attack / Galaxiga) with a twist: you’re playing for real rewards. Choose how much free data you’re going for (100MB to 1GB), dodge and shoot through waves in under two minutes, take down the boss, and walk away with data and brand vouchers. One finger, three verbs—dodge, shoot, collect. Same loop whether you’re here for the game or for the data.

### Vision Statement

We want players to feel that their skill and time directly translate into tangible value: every run has a clear stake (tier = "win up to" X; actual pack is variable), a clear outcome (win = random pack up to tier cap + vouchers), and a fair difficulty curve; levels give power-ups to take on harder bosses. The experience should feel like a focused arcade session—short, repeatable, and rewarding—while supporting a sustainable rewards platform for brands and telcos. The game is the vehicle; the rewards are the reason to come back.

---

## Target Market

### Primary Audience

- **Demographics:** Mobile-first users in regions where data costs matter (e.g. emerging markets, prepaid users); broad age range (teens to 40s).
- **Gaming preferences:** Hypercasual or light arcade players; comfortable with short sessions (1–3 min); may prefer “earn while you play” over pure high-score chase.
- **Motivations:** Get free data and/or vouchers with minimal friction; enjoy simple shooter action; want a clear cause (effort) and effect (rewards).

### Secondary Audience

- **Rewards-only users:** People who mainly want free data and will tolerate simple gameplay if it’s short and fair. Served by the easiest tier and optional future “quick data” run.
- **Core arcade fans:** Players who like vertical shooters and will engage for the game first, with rewards as a bonus. Served by higher tiers and boss variety.

### Market Context

- **Similar successful games:** Space Shooter – Galaxy Attack, Galaxiga (vertical shooters, one-finger, hypercasual). Rewards apps and telco promos (free data, vouchers) have proven demand.
- **Market opportunity:** Combine proven shooter engagement with real rewards in one product; one integration for brands/telcos; clear session and reward boundaries for analytics and fairness.
- **Competition:** Other hypercasual shooters (attention); other rewards apps (data/vouchers). Differentiator: integrated “play for rewards” with tiered difficulty and transparent stakes.

---

## Game Fundamentals

### Core Gameplay Pillars

1. **One run = one session** — Fixed run length (1–3 min), 3 lives per run, binary outcome (win = pack + vouchers / fail = try again). No mid-run save; session boundary is clear for player and platform.
2. **Difficulty follows reward** — Player chooses **tier** ("win up to" e.g. 100MB / 500MB / 1GB). *Actual data pack won is variable (business); we message "win up to," not "get exactly."* Difficulty and boss scale with tier. Higher tier = harder run, bigger possible reward. No separate “hard mode”; fairness is “bigger reward = harder run.”
3. **Levels = power-ups** — **Levels** (Level 1, 2, …) unlock or improve **power-ups** so players can tackle harder bosses. Tier sets run difficulty; level sets what tools the player has.
4. **One finger, three verbs** — Dodge (move), shoot (tap or auto), collect (overlap pickups). All actions map to one input channel; hypercasual clarity and low cognitive load.
5. **Real rewards, real stakes** — Vouchers and data are real-world value; anti-grind and transparent end screen build trust. Collectibles (vouchers) can double as power-ups or lane objectives.

**Pillar priority:** When pillars conflict, prioritize (1) session control and (2) difficulty–reward fairness; then (3) control simplicity and (4) reward clarity.

### Primary Mechanics

- **Dodge** — Move ship (drag/hold) to avoid bullets and obstacles; defines survival and lane choice.
- **Shoot** — Tap or auto-fire to destroy enemies; clears space and can drop voucher pickups.
- **Collect** — Overlap voucher pickups (and optionally power-ups); collection is movement-based, no separate button.

**Core loop:** Pick tier ("win up to X") → play run (dodge, shoot, collect; 3 lives; power-ups from level) → reach end boss → defeat boss → win = **random data pack (up to tier cap)** + vouchers collected; fail = no pack, can start new run. **Levels** unlock/improve power-ups to help with harder bosses.

### Player Experience Goals

- **Clarity** — “I know what I’m playing for and what I get if I win.”
- **Fairness** — “The difficulty matches what I chose; I’m not being tricked.”
- **Quick satisfaction** — Short runs, immediate outcome, “one more try” feel.
- **Dual appeal** — Fun for light arcade play; useful for users who want free data with minimal friction.

---

## Scope and Constraints

### Target Platforms

- **Primary:** Mobile (iOS and Android); touch-first, vertical orientation, short sessions.
- **Secondary:** Consider web or lightweight instant-play later if engine supports it.

### Development Timeline

- MVP-first: one loop (shooter), one tier set, 2–3 boss variants, core rewards flow. Timeline to be set by team; scope should fit “minimum playable with real rewards” before adding more content or loops.

### Budget Considerations

- Scope to fit budget: reuse assets (ships, bullets, bosses), minimal narrative, config-driven difficulty. Brand/telco partnerships may offset part of UA or reward cost.

### Team Resources

- To be defined. Roles needed: design, engineering (game + rewards/backend), art/audio (minimal for MVP), and ops/partnerships for vouchers and data fulfillment.

### Technical Constraints

- **Engine:** To be chosen (Unity, Unreal, Godot, or other); must support mobile, one-finger input, and clean “run result” output for rewards layer.
- **Performance:** Target 60fps; short levels and limited on-screen objects to keep load low.
- **Rewards layer:** Backend for tiers, voucher catalog, data pack fulfillment, anti-grind (caps/cooldowns), and redemption; shared so multiple core loops can plug in later.

### Scope Realities

- Ship one core loop (shooter) first; engine and contracts designed so a second loop (e.g. runner, puzzle) can be added without rewriting rewards logic.
- Free-data segment: serve via easiest tier and optional daily cap first; add “quick data run” only if data supports it.

---

## Reference Framework

### Inspiration Games

- **Space Shooter – Galaxy Attack / Galaxiga** — Vertical scroll, one-finger, arcade feel. Taking: pacing, control simplicity, visual readability. Not taking: pure score chase; we add real rewards and tiered stakes.
- **Rewards / telco apps** — Free data, vouchers, engagement units. Taking: clear reward boundaries, session-based engagement. Not taking: passive or non-game engagement; we use active play as the gate.

### Competitive Analysis

- Hypercasual shooters compete for attention and retention; we add a tangible reward layer to differentiate.
- Rewards apps compete on offer quality and trust; we add a game layer to differentiate and increase engagement per session.

### Key Differentiators

- **Shooting feel as USP** — The primary differentiator is how satisfying and dopamine-releasing the shooting experience is: **lasers**, **electricity emitters / shockers**, and **hypnotic-style attacks**. These VFX and attack types are designed to feel cool and rewarding in code; feasibility is validated in a dedicated **testing environment** (shooting/VFX sandbox) before building the full game on top.
- **Integrated play-for-rewards:** One product: game + data + vouchers; tier choice = difficulty; no separate “reward mode.”
- **Session control:** One run = one session; fixed length and 3 lives; clear for analytics, partners, and player psychology.
- **Engine for multiple loops:** Same rewards layer can support shooter, runner, puzzle, etc.; one integration for brands/telcos, multiple games for retention and testing.

---

## Content Framework

### World and Setting

- Space/sci-fi setting: ship, enemies, bullets, pickups, boss. Minimal lore; focus on readability and feedback. Can support thematic skins or “brand seasons” (e.g. food week, tech week) for voucher campaigns later.

### Narrative Approach

- No story required for MVP. Optional light framing (e.g. “earn data for your crew”) can be added later; world is a wrapper for mechanics and rewards.

### Content Volume

- **MVP:** One core loop; 2–3 boss variants; 3 tiers (e.g. 100MB, 500MB, 1GB); voucher pool and data pack catalog as defined by partners. Expand bosses and tiers post-MVP.

---

## Art and Audio Direction

### Visual Style

- Clear, readable shapes (ship, bullets, enemies, pickups); high contrast for lanes and obstacles. Style can be simple geometric or soft sci-fi; avoid visual clutter that obscures one-finger play.

### Audio Style

- Short, satisfying SFX (shoot, collect, hit, win/fail); optional light music for run and boss. Audio supports feedback and “game feel,” not narrative.

### Production Approach

- Reuse and recolor where possible; prioritize clarity and performance over visual richness for MVP. Art/audio can scale with budget and post-MVP content.

---

## Risk Assessment

### Key Risks

- **Reward sustainability:** Data and voucher cost vs. engagement and partner revenue; mitigated by tiered difficulty, anti-grind, and caps.
- **Free-data segment churn:** Users who only want data may drop if difficulty feels unfair; mitigated by easy lowest tier and optional quick data run if needed.
- **Fraud/abuse:** Multi-account or exploit to farm high-tier packs; mitigated by anti-grind, caps, and clear run-result auditing.

### Technical Challenges

- Tying difficulty tightly to tier (bullet speed, spawn rate, boss params) without bugs or perceived unfairness; clean “run result” API for rewards engine.

### Market Risks

- Hypercasual and rewards markets are competitive; differentiation depends on execution (feel, fairness, partner deals) and clear positioning.

### Mitigation Strategies

- Lock session control and difficulty–reward coupling as non-negotiable; test with real users on easiest and hardest tiers; iterate on boss feel and voucher placement; design engine for multiple loops from the start to reduce future rework.

---

## Success Criteria

### MVP Definition

- **Playable:** One vertical-shooter loop: pick tier, play run (3 lives, fixed length), defeat tier-scaled boss, see win/fail and rewards (data pack + vouchers).
- **Rewards:** At least one data pack tier set and one voucher pool; end screen shows earned rewards; claim/redemption flow (or stub) in place.
- **Controls:** One-finger (dodge, shoot, collect); no score required unless it feeds reward logic.
- **Scope:** 2–3 bosses, 3 tiers; no second core loop or narrative; engine structured for future loops.

### Success Metrics

- **Engagement:** Run completion rate, sessions per user per day, retention (D1/D7).
- **Rewards:** Claim rate, redemption rate, cost per rewarded user; balance between reward value and sustainability.
- **Fairness:** Perceived difficulty fairness (e.g. surveys or support tickets); anti-grind effectiveness (no abnormal farming).
- **Product:** Time to complete a run; drop-off at boss; free-data segment completion on easiest tier.

### Launch Goals

- MVP live on at least one mobile platform with one partner (telco or brand) for data/vouchers; clear session and reward metrics; foundation for adding a second core loop or more content.

---

## Next Steps

### Immediate Actions

1. Lock this brief with stakeholders; confirm game name (Data Run or final title) and tier structure.
2. Create or update Game Design Document (GDD) from this brief (mechanics, economy, boss design, rewards flow).
3. Define technical architecture: game client, “run result” contract, rewards backend, anti-grind rules.
4. Prioritize prototype: one tier, one boss, 3 lives, mock rewards; validate feel and session length.

### Research Needs

- Partner requirements for data pack sizes, voucher catalog, and caps.
- Competitive benchmarks: run length and completion rates in similar shooters and rewards apps.
- Accessibility: ensure one-finger design and end screen work for target audiences.

### Open Questions

- Final game name and tier labels (100MB/500MB/1GB or partner-specific).
- Whether first-win-of-the-day or tutorial bonus is in MVP.
- Exact run length (90 sec vs. 2 min) and boss count for MVP.

---

## Appendices

### A. Research Summary

- Input: Locked brainstorming session (2025-03-05) with 15 ideas, refinements (3 tries, end boss, free-data seekers), engine direction, and Party Mode perspectives on session control. No separate market research doc; competitive and audience notes drawn from brainstorm and standard rewards/shooter context.

### B. Stakeholder Input

- Primary participant: jeremiah007. Business premise: simple shooter, vouchers + free data, difficulty scales with data pack value, vouchers as collectibles; MVP scope; engine to support multiple core loops later.

### C. References

- Brainstorming session: `_bmad-output/brainstorming-session-2025-03-05.md`  
- Inspiration: Space Shooter – Galaxy Attack, Galaxiga; rewards/telco apps.

---

*This Game Brief serves as the foundational input for Game Design Document (GDD) creation.*

*Next Steps: Use the Game Brief as input to create detailed game design documentation (GDD), then architecture and sprint planning.*
