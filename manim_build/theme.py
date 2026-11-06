"""Shared look, layout and model->scene helpers. Every drawn quantity is computed from model.py."""
import numpy as np
from manim import *

import model as M

# ---------------------------------------------------------------- palette (from the sketch)
BG = WHITE
INK = "#222222"
CASING = "#0070C0"
SOURCE = "#FFC000"
SOURCE_TXT = "#B8860B"
RAY = "#F08C00"
OBJ_LINE = "#3B5E2B"
GREEN_LO = "#E2F0D9"   # density 0
GREEN_HI = "#1E3B12"   # density RHO_MAX
RHO_MAX = 1.6
SCREEN_EDGE = "#7F7F7F"
ACCENT = "#C00000"
# shell identity colours (not density): shell 1 (outer) ... shell 5 (inner)
SHELL_HUES = ["#17A2B8", "#9467BD", "#1F77B4", "#E377C2", "#D62728"]
# unitless attenuation factor A in [0, 1], two colours: red (high absorption) -> blue (low absorption)
A_STOPS = ["#C0272D", "#2C6FB7"]

# ---------------------------------------------------------------- typography
FONT = "Inter"                      # all plain text
TEX = TexTemplate()                 # matching sans-serif maths (and sans \text{...})
TEX.add_to_preamble(r"\usepackage[eulergreek]{sansmath}\sansmath\renewcommand{\familydefault}{\sfdefault}")
config.tex_template = TEX
Text.set_default(color=INK, font=FONT)
for cls in (MathTex, Tex, DecimalNumber, Integer):
    cls.set_default(color=INK)

TITLE_SIZE = 32
CAPTION_SIZE = 24

# ---------------------------------------------------------------- layout (scene units)
OBJ_C = np.array([-0.6, -0.65, 0.0])  # object centre
S = 2.3                               # scene units per model unit
X_SOURCE = -5.6
CASING_X = (-4.0, 2.8)
CASING_Y = (-3.15, 2.3)
CASING_W = 0.14
X_SCREEN = 4.4
PIX_W = 0.45
PIX_H = S * M.R / M.N


def y_scene(y_model):
    return OBJ_C[1] + y_model * S


def shell_color(rho):
    return interpolate_color(ManimColor(GREEN_LO), ManimColor(GREEN_HI), float(np.clip(rho / RHO_MAX, 0, 1)))


def dose_color(d):
    """Radiation level on the screen: black (no dose) -> white (full dose)."""
    return interpolate_color(ManimColor(BLACK), ManimColor(WHITE), float(np.clip(d, 0, 1)))


def a_color(a):
    """Colormap for the unitless factor A."""
    a = float(np.clip(a, 0, 1)) * (len(A_STOPS) - 1)
    j = min(int(a), len(A_STOPS) - 2)
    return interpolate_color(ManimColor(A_STOPS[j]), ManimColor(A_STOPS[j + 1]), a - j)


# ---------------------------------------------------------------- text helpers
def caption(text, size=CAPTION_SIZE):
    c = Text(text, font_size=size)
    if c.width > config.frame_width - 0.8:
        c.scale_to_fit_width(config.frame_width - 0.8)
    return c.to_edge(DOWN, buff=0.28)


def title(text, size=TITLE_SIZE, max_width=None):
    """Scene title: one style everywhere, en dash after the step number, shrunk to fit if long."""
    t = Text(text.replace(" - ", " – "), font_size=size, weight=SEMIBOLD)
    mw = max_width or config.frame_width - 1.0
    if t.width > mw:
        t.scale_to_fit_width(mw)
    return t.to_edge(UP, buff=0.3)


# ---------------------------------------------------------------- set-up parts
def make_source():
    fan = Sector(radius=0.75, angle=PI / 2.6, start_angle=-PI / 5.2, arc_center=ORIGIN,
                 fill_color=SOURCE, fill_opacity=1, stroke_color="#7F6000", stroke_width=1.5)
    fan.move_to([X_SOURCE, y_scene(0.5), 0])
    label = Text("Source (X-rays)", font_size=22, color=SOURCE_TXT).next_to(fan, DOWN, buff=1.0)
    return VGroup(fan, label)


def make_casing():
    w, h = CASING_X[1] - CASING_X[0], CASING_Y[1] - CASING_Y[0]
    box = Rectangle(width=w, height=h, stroke_color=CASING, stroke_width=CASING_W * 100)
    box.move_to([(CASING_X[0] + CASING_X[1]) / 2, (CASING_Y[0] + CASING_Y[1]) / 2, 0])
    label = Text("Confinement casing", font_size=22, color=CASING).next_to(box, UP, buff=0.12)
    return VGroup(box, label)


def make_object(rho, ghost_opacity=0.18, edge=True):
    """Concentric shells: top half in full colour (what the screen sees), ghosted bottom half.
    obj[0][k] / obj[1][k] = shell k (0 = outermost)."""
    top, bottom = VGroup(), VGroup()
    for k in range(M.N):
        kw = dict(inner_radius=M.SHELL_IN[k] * S, outer_radius=M.SHELL_OUT[k] * S, angle=PI,
                  arc_center=OBJ_C, fill_color=shell_color(rho[k]),
                  stroke_color=OBJ_LINE, stroke_width=1.5 if edge else 0)
        top.add(AnnularSector(start_angle=0, fill_opacity=1, **kw))
        bottom.add(AnnularSector(start_angle=PI, fill_opacity=ghost_opacity,
                                 stroke_opacity=ghost_opacity, **kw))
    return VGroup(top, bottom)


def make_screen(values=None, x=X_SCREEN, label="Screen (1 slice)", label_size=22, cmap=dose_color):
    """screen[0][i] = pixel of row i (0 = top)."""
    pix = VGroup()
    for i in range(M.N):
        r = Rectangle(width=PIX_W, height=PIX_H, stroke_color=SCREEN_EDGE, stroke_width=2,
                      fill_color=WHITE if values is None else cmap(values[i]), fill_opacity=1)
        r.move_to([x, y_scene(M.Y_PIX[i]), 0])
        pix.add(r)
    lab = Text(label, font_size=label_size, color=SCREEN_EDGE).next_to(pix, UP, buff=0.2)
    return VGroup(pix, lab)


def row_labels(pixels, side=RIGHT, size=24, buff=0.15, prefix=True):
    out = VGroup()
    for i, p in enumerate(pixels):
        tex = rf"i={i + 1}" if (prefix and i == 0) else rf"{i + 1}"
        out.add(MathTex(tex, font_size=size, color=SCREEN_EDGE).next_to(p, side, buff=buff))
    if prefix:  # align the numbers, not the "i="
        for m in out[1:]:
            m.align_to(out[0], RIGHT if side is LEFT else LEFT)
            if side is RIGHT:
                m.shift(RIGHT * (out[0].width - m.width))
    return out


def colorbar(width=2.6, height=0.22, n=40, label=r"A"):
    cells = VGroup(*[Rectangle(width=width / n * 1.3, height=height, stroke_width=0, fill_opacity=1,
                               fill_color=a_color((j + 0.5) / n)) for j in range(n)])
    cells.arrange(RIGHT, buff=-width / n * 0.3)  # slight overlap hides anti-aliasing seams
    frame = SurroundingRectangle(cells, buff=0, stroke_color=SCREEN_EDGE, stroke_width=1.5)
    ticks = VGroup(*[MathTex(t, font_size=22).next_to(cells, DOWN, buff=0.08).set_x(cells.get_left()[0] + f * width)
                     for t, f in (("0", 0), ("0.5", 0.5), ("1", 1))])
    lab = MathTex(label, font_size=26).next_to(cells, LEFT, buff=0.15)
    ends = VGroup(Text("high\nabsorption", font_size=15, color=A_STOPS[0], line_spacing=0.7),
                  Text("low\nabsorption", font_size=15, color=A_STOPS[-1], line_spacing=0.7))
    ends[0].next_to(ticks, DOWN, buff=0.08).align_to(cells, LEFT)
    ends[1].next_to(ticks, DOWN, buff=0.08).align_to(cells, RIGHT)
    return VGroup(cells, frame, ticks, lab, ends)


# ---------------------------------------------------------------- rays with Beer-Lambert attenuation
def _mu_along(xs, y_model, rho, with_casing, with_object):
    mu = np.zeros_like(xs)
    if with_casing:
        per_wall = -np.log(M.casing_factor(y_model)) / 2
        for x0 in CASING_X:
            mu[np.abs(xs - x0) <= CASING_W / 2] += per_wall / CASING_W
    if with_object:
        k = M.shell_index(np.sqrt(((xs - OBJ_C[0]) / S) ** 2 + y_model ** 2))
        inside = k >= 0
        mu[inside] += np.asarray(rho)[k[inside]] / S
    return mu


def ray_profile(y_model, rho=M.RHO_TRUE, with_casing=True, with_object=True, x_end=X_SCREEN - PIX_W / 2):
    xs = np.linspace(X_SOURCE + 0.3, x_end, 2400)
    mu = _mu_along(xs, y_model, rho, with_casing, with_object)
    tau = np.concatenate([[0], np.cumsum((mu[1:] + mu[:-1]) / 2 * np.diff(xs))])
    return xs, M.source_dose(y_model) * np.exp(-tau)


def make_ray(y_model, rho=M.RHO_TRUE, with_casing=True, with_object=True, n_seg=160, width=5):
    xs, D = ray_profile(y_model, rho, with_casing, with_object)
    idx = np.linspace(0, len(xs) - 1, n_seg + 1).astype(int)
    y = y_scene(y_model)
    segs = VGroup()
    for a, b in zip(idx[:-1], idx[1:]):
        segs.add(Line([xs[a], y, 0], [xs[b], y, 0], stroke_color=RAY, stroke_width=width,
                      stroke_opacity=float(np.clip(D[(a + b) // 2], 0.04, 1))))
    return segs


def make_rays(**kw):
    return VGroup(*[make_ray(yi, **kw) for yi in M.Y_PIX])


def chord_segments(y_model, width=9):
    """Thick coloured segments marking where a horizontal ray is inside each shell."""
    g = VGroup()
    y = y_scene(y_model)
    for k in range(M.N):
        h_out, h_in = M.half_chord(M.SHELL_OUT[k], y_model), M.half_chord(M.SHELL_IN[k], y_model)
        if h_out <= 1e-9:
            continue
        for sgn in (-1, 1):
            a, b = OBJ_C[0] + sgn * h_in * S, OBJ_C[0] + sgn * h_out * S
            g.add(Line([a, y, 0], [b, y, 0], stroke_color=SHELL_HUES[k], stroke_width=width))
    return g


def shell_labels(size=24):
    """rho_1 (outer) ... rho_N (inner), with white backing so they stay readable.
    Each label sits mid-shell, at the height between two rows, so no ray runs through it."""
    out = VGroup()
    for k in range(M.N):
        rm = (M.SHELL_IN[k] + M.SHELL_OUT[k]) / 2
        yl = M.R - (k + 1) * M.R / M.N + 0.03
        lab = MathTex(rf"\rho_{k + 1}", font_size=size, color=SHELL_HUES[k])
        lab.move_to(OBJ_C + S * np.array([-np.sqrt(max(rm ** 2 - yl ** 2, 0)), yl, 0]))
        bg = BackgroundRectangle(lab, color=WHITE, fill_opacity=0.85, buff=0.03)
        out.add(VGroup(bg, lab).set_z_index(10))
    return out



# ---------------------------------------------------------------- density stacks (bricks, possibly partial)
def density_stack(x, rho, color, base, bh=0.3, width=0.5, n_max=14, brick=M.BRICK):
    """A column whose height is rho (in bricks), with brick separators.
    Fixed structure (rect + n_max separators) so that Transform between two stacks is smooth."""
    h = rho / brick * bh
    g = VGroup()
    rect = Rectangle(width=width, height=max(abs(h), 1e-3), fill_color=color, fill_opacity=0.85, stroke_width=0)
    rect.move_to([x, base, 0], aligned_edge=DOWN if h >= 0 else UP)
    g.add(rect)
    for j in range(1, n_max + 1):
        yj = base + j * bh
        vis = (j * bh) < h - 1e-6
        g.add(Line([x - width / 2, yj, 0], [x + width / 2, yj, 0], stroke_color=WHITE, stroke_width=1.5,
                   stroke_opacity=1.0 if vis else 0.0))
    return g


def brick_column(x, rho, color, base, bh=0.3, width=0.5, dashed=False, brick=M.BRICK):
    """Individual bricks (last one partial). Dashed = second material: light fill, dashed outline."""
    g = VGroup()
    h_tot, y = rho / brick * bh, base
    while h_tot > 1e-6:
        h = min(bh, h_tot)
        r = Rectangle(width=width, height=h, fill_color=color, fill_opacity=0.3 if dashed else 0.85,
                      stroke_color=color if dashed else WHITE, stroke_width=2 if dashed else 1.5)
        r.move_to([x, y, 0], aligned_edge=DOWN)
        if dashed:
            outline = DashedVMobject(r.copy().set_fill(opacity=0), num_dashes=14, dashed_ratio=0.55)
            r.set_stroke(opacity=0)
            g.add(VGroup(r, outline))
        else:
            g.add(r)
        y += h
        h_tot -= h
    return g


def truth_marks(xs, rhos, base, bh=0.3, half=0.3):
    return VGroup(*[DashedLine([x - half, base + r / M.BRICK * bh, 0], [x + half, base + r / M.BRICK * bh, 0],
                               dash_length=0.06, stroke_color=GREY_C, stroke_width=2) for x, r in zip(xs, rhos)])



def hatched_brick(x, y_bottom, h, color, width=0.5, spacing=0.11):
    """Second material: light fill with diagonal lines drawn across the whole brick."""
    r = Rectangle(width=width, height=h, fill_color=color, fill_opacity=0.3, stroke_color=color, stroke_width=2)
    r.move_to([x, y_bottom, 0], aligned_edge=DOWN)
    x0, x1, y0, y1 = x - width / 2, x + width / 2, y_bottom, y_bottom + h
    lines = VGroup()
    d = (x0 - y1) + spacing / 2
    while d < x1 - y0:
        xa, xb = max(x0, y0 + d), min(x1, y1 + d)
        if xb - xa > 1e-3:
            lines.add(Line([xa, xa - d, 0], [xb, xb - d, 0], stroke_color=color, stroke_width=2))
        d += spacing
    return VGroup(r, lines)


def material_column(x, rho, color, base, bh=0.3, width=0.5, material=1, brick=M.BRICK):
    """Bricks of material 1 (plain) or material 2 (hatched); the last brick may be partial."""
    g = VGroup()
    h_tot, y = rho / brick * bh, base
    while h_tot > 1e-6:
        h = min(bh, h_tot)
        if material == 2:
            g.add(hatched_brick(x, y, h, color, width))
        else:
            g.add(Rectangle(width=width, height=h, fill_color=color, fill_opacity=0.85, stroke_color=WHITE,
                            stroke_width=1.5).move_to([x, y, 0], aligned_edge=DOWN))
        y += h
        h_tot -= h
    return g


def density_axis(x, base, top_rho=1.6, bh=0.3, step=0.4, brick=M.BRICK, label="density"):
    """Fixed vertical axis in density units, so that height changes read as real changes."""
    top = base + top_rho / brick * bh
    g = VGroup(Line([x, base, 0], [x, top, 0], stroke_color=INK, stroke_width=2))
    v = 0.0
    while v <= top_rho + 1e-9:
        y = base + v / brick * bh
        g.add(Line([x - 0.07, y, 0], [x + 0.07, y, 0], stroke_color=INK, stroke_width=2))
        g.add(DecimalNumber(v, num_decimal_places=1, font_size=16).next_to([x - 0.07, y, 0], LEFT, buff=0.06))
        v += step
    g.add(Text(label, font_size=16).next_to([x, top, 0], UP, buff=0.12))
    return g
