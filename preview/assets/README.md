# Gameplay assets

Assets are organized **level-wise**. Each level has its own folder under `assets/images/`.

## Folder structure (level-wise)

- `preview/assets/images/Level 1/` — Level 1 assets (upgrade pickup, etc.). **In use for now.**
- `preview/assets/images/Level 2/` — Level 2 assets (when added).
- Add further levels as needed (Level 3, …).

Paths in code are relative to the preview page (e.g. `assets/images/Level 1/upgrade-pickup.png`).

## Level 1

- **Fodder Type 1:** `Level 1/Fodder Class=Type1.png` — fodder wave slot 1; listed in `LEVEL_FODDER_ASSETS` in `preview/gameplay.html`.
- **Fodder Type 2:** `Level 1/Fodder Class=Type2.png` — fodder wave slot 2; same manifest. **Wave count** in preview = `LEVEL_FODDER_ASSETS.length` plus one **mix** wave when `length ≥ 2`, then **Boss L1** after that cycle.
- **Boss Level 1:** `Level 1/Boss_L1.png` — path in code: `assets/images/Level 1/Boss_L1.png`. Spawns once per cycle after all fodder waves for the level; multi-hit HP, uses `Boss_L1` art when loaded.
- **Upgrade pickup (Phase 2):** `Level 1/upgrade-pickup.png` — path in code: `assets/images/Level 1/upgrade-pickup.png`. Export from Figma (node 2190-4732); used for drop-on-kill pickups.
- **Upgraded spaceship (L1):** `Level 1/spaceship_upgrade_L1.png` — path in code: `assets/images/Level 1/spaceship_upgrade_L1.png`. Shown when the player collects an upgrade (or press [U] to toggle). Fallback: code-drawn neon ship if PNG not loaded.

## Home screen (`preview/index.html`)

**Figma:** [CaseStudies — Body / home, node 2154-410](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2154-410).

Exported assets live under **`assets/images/home/`** (do not hotlink Figma MCP URLs in HTML; they expire).

| File | Role |
|------|------|
| `home/ship.svg` | Central ship silhouette (node 2154:530) |
| `home/strike-line.svg` | Decorative strike line under logo (node 2154:1013) |
| `home/btn-battle-bg.png` | *(Optional)* Exported CTA texture; **not used in `index.html`** — raster included extra top-center art that conflicted with CSS corner brackets; button uses CSS gradient + corners only. |
| `home/icon-points.svg` | Points nav icon (2154:470) |
| `home/icon-vouchers.svg` | Vouchers nav icon (2154:479) |
| `home/icon-settings.svg` | Settings nav icon (2154:488) |

To refresh from Figma: export the same nodes again and replace these files, or re-run an MCP asset fetch and overwrite.

## Other

- **Background:** `clouds 1.png` — path in code: `assets/clouds 1.png` (see `NEBULA_BG_IMAGE_URL` in `gameplay.html`). Can stay at `assets/` or move under a level if you prefer.

**Important:** Open the game via a **local server** (e.g. `python3 -m http.server 8080` then go to http://localhost:8080/preview/) so images load. Opening `gameplay.html` directly as a file can block image loading.
