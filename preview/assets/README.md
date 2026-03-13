# Gameplay assets

Put your nebula/space background image here so the gameplay can load it.

- **Filename used in code:** `clouds 1.png`
- **Path in code:** `assets/clouds 1.png` (resolved relative to the gameplay page)

Place your PNG or JPG in this folder as **`clouds 1.png`** (or change `NEBULA_BG_IMAGE_URL` in `gameplay.html` to match your filename).

**Important:** Open the game via a **local server** (e.g. `python3 -m http.server 8080` then go to http://localhost:8080/preview/) so the image loads. Opening `gameplay.html` directly as a file can block image loading.
