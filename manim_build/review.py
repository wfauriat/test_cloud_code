"""Review loop (spec §3.2): extract frames at given times and tile them into a contact sheet.

    python review.py VIDEO [OUT.png] [t1 t2 ...]
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageDraw, ImageFont

SPEC_TIMES = [4, 12, 20, 30, 42, 49, 60, 74]


def contact_sheet(video, out="contact_sheet.png", times=SPEC_TIMES, cols=4, width=640):
    tiles = []
    with tempfile.TemporaryDirectory() as tmp:
        for t in times:
            f = os.path.join(tmp, f"f_{t}.png")
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", str(t), "-i", video,
                            "-frames:v", "1", f], check=True)
            im = Image.open(f).convert("RGB")
            tiles.append((t, im.resize((width, round(width * im.height / im.width)))))
    h = tiles[0][1].height
    sheet = Image.new("RGB", (cols * width, -(-len(tiles) // cols) * (h + 28)), "#05080f")
    draw = ImageDraw.Draw(sheet)
    try:
        font = ImageFont.truetype("Inter", 18)
    except OSError:
        font = ImageFont.load_default()
    for k, (t, im) in enumerate(tiles):
        x, y = (k % cols) * width, (k // cols) * (h + 28)
        sheet.paste(im, (x, y + 28))
        draw.text((x + 8, y + 4), f"t = {t} s", fill="#EAF0FA", font=font)
    sheet.save(out)
    return out


if __name__ == "__main__":
    video = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else "contact_sheet.png"
    times = [float(t) for t in sys.argv[3:]] or SPEC_TIMES
    print(contact_sheet(video, out, times))
