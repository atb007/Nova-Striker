# How to Run Scripts

## Do I Always Need to Create `.venv`?

**No.** Create the virtual environment **once** per project. After that:

- **Activate** it when you open a new terminal: `source .venv/bin/activate` (macOS/Linux) or `.venv\Scripts\activate` (Windows)
- Your terminal prompt will show `(.venv)` when it’s active
- Run your scripts as usual; they’ll use the packages installed in that venv

**Alternative:** You can skip the venv and install packages globally (`pip install -r requirements.txt`), but that can cause conflicts between projects. Using a venv is recommended.

---

## Video Agent (Shooting Mechanics Analyzer)

### One-Time Setup

```bash
cd /Users/udai.deori/Desktop/CursorAI/Projects/MobileGame

# Create venv (only needed once)
python3 -m venv .venv

# Activate venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Optional: set your Gemini API key for AI analysis (get one at aistudio.google.com)
export GEMINI_API_KEY="your-key"
```

### Run the Agent

**Drop videos into `vids/`**, then:

```bash
cd /Users/udai.deori/Desktop/CursorAI/Projects/MobileGame
source .venv/bin/activate
python video_agent.py
```

**Or** point at a specific file or folder:

```bash
python video_agent.py vids/my-video.mp4
python video_agent.py /path/to/folder
```

**Save output to a file:**

```bash
python video_agent.py > analysis.json
# or show and save:
python video_agent.py | tee analysis.json
```

### Supported Video Formats

mp4, mov, avi, webm, mkv, m4v

---

## Game Home Preview (Figma → Live)

The **Nova Striker** home screen from [Figma (Case Studies)](https://www.figma.com/design/Iw9q2ANqLYmqfKAsY96kbI/CaseStudies?node-id=2154-410) is implemented as a single HTML preview with subtle motion (starfield, button glow, halo pulse).

### Open the preview

**Option A — Open file in browser**

```bash
open preview/index.html
# or on Windows: start preview/index.html
```

**Option B — Local server (recommended if images from Figma don’t load)**

```bash
cd /Users/udai.deori/Desktop/CursorAI/Projects/MobileGame
python3 -m http.server 8080
```

Then open: **http://localhost:8080/preview/** — click **Battle** to open Gameplay (`preview/gameplay.html`).

**Gameplay (Phase 1 scaffolding complete):** Ship matches Figma: Main Body Hull (vector shape or asset), Cockpit Glass (vertical pill, cyan border + gradient), wing structures above thrusters with orange glow (top edge thin stroke + glow). Blue thruster flames and glow. Smooth X+Y movement; three-way laser, **Fire Blaster**, and **Electric Shock** (cycle with F or 2/3/E / tap top-right). Diamond/circle enemies, impact explosions. See `preview/PREVIEW-GAMEPLAY.md` and `_bmad-output/shooting-mechanics-reference.md` for details.

**Next phase (Phase 2):** Enemy flanking from sides; formations; enemy attacks; enemies that position and hold (or maintain distance to player); spaceship upgrades (visual + bullet types); upgrades dropped on enemy kill. See `preview/PREVIEW-GAMEPLAY.md` § Next phase.

In Cursor you can also use **Simple Browser** (Command Palette → “Simple Browser: Show”) and enter that URL, or open `preview/index.html` from the file explorer.

---

## Other Scripts

### BMAD Update (`scripts/update-bmad.sh`)

Updates the BMAD installation used by this workspace. Run from project root:

```bash
./scripts/update-bmad.sh
```

Requires `npx` and a configured BMAD project path.
