#!/usr/bin/env bash
# Update BMAD installation in WebApp from this workspace.
# BMAD commands are symlinked from WebApp into MobileGame/.cursor/commands;
# this script updates the source (WebApp's _bmad and .cursor/commands).

set -e
BMAD_PROJECT_ROOT="/Users/udai.deori/Desktop/CursorAI/VST/Matilda/WebApp"

echo "Updating BMAD at: $BMAD_PROJECT_ROOT"
echo "Running: npx bmad-method install --directory \"$BMAD_PROJECT_ROOT\" --action quick-update --yes"
echo ""

npx bmad-method install \
  --directory "$BMAD_PROJECT_ROOT" \
  --action quick-update \
  --yes

echo ""
echo "Done. BMAD commands in this workspace (symlinked from WebApp) will reflect the update."
echo "Reload the Cursor window if slash commands don't show new changes."
