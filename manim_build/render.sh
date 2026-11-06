#!/usr/bin/env bash
# Usage: ./render.sh [l|m|h|k] [Scene ...]
#   l = 480p15 draft, m = 720p30, h = 1080p60, k = 2160p60
# Renders the scenes, then joins them into media/tomography_explainer_<res>.mp4
set -e
cd "$(dirname "$0")"
Q=${1:-l}; shift || true
ALL="S1_Setup S2_Separate S3_ForwardModel S4_BrickFit S5_Gradient"
SCENES=${@:-$ALL}
MANIM=${MANIM:-manim}
for s in $SCENES; do $MANIM -q$Q --progress_bar none scenes.py "$s"; done

case $Q in l) RES=480p15;; m) RES=720p30;; h) RES=1080p60;; k) RES=2160p60;; esac
DIR=media/videos/scenes/$RES
LIST=$(mktemp)
for s in $ALL; do
  [ -f "$DIR/$s.mp4" ] || { echo "missing $DIR/$s.mp4, skipping concat"; exit 0; }
  echo "file '$PWD/$DIR/$s.mp4'" >> "$LIST"
done
ffmpeg -loglevel error -y -f concat -safe 0 -i "$LIST" -c copy "media/tomography_explainer_$RES.mp4"
rm -f "$LIST"
echo "joined -> media/tomography_explainer_$RES.mp4"
