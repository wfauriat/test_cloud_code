#!/usr/bin/env bash
# Usage: ./render.sh [l|m|h] [Scene ...]   (l = 480p15 draft, h = 1080p60 final)
set -e
cd "$(dirname "$0")"
Q=${1:-l}; shift || true
SCENES=${@:-S1_Setup S2_Separate S3_ForwardModel S4_BrickFit}
MANIM=${MANIM:-manim}
for s in $SCENES; do $MANIM -q$Q --progress_bar none scenes.py "$s"; done
