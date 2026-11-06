"""Shared look, layout and model->scene helpers. Every drawn quantity is computed from model.py."""
import numpy as np
from manim import *

import model as M

# ---------------------------------------------------------------- palette (from the sketch)
BG = WHITE
INK = "#222222"
CASING = "#0070C0"
SOURCE = "#FFC000"
RAY = "#F08C00"
OBJ_LINE = "#3B5E2B"
GREEN_LO = "#E2F0D9"   # density 0
GREEN_HI = "#1E3B12"   # density RHO_MAX
RHO_MAX = 1.6
SCREEN_EDGE = "#7F7F7F"
ACCENT = "#C00000"

for cls in (Text, MathTex, Tex, DecimalNumber, Integer):
    cls.set_default(color=INK)

# ---------------------------------------------------------------- layout (scene units)
OBJ_C = np.array([-0.6, -0.65, 0.0])  # object centre
S = 2.3                              # scene units per model unit
X_SOURCE = -5.6
CASING_X = (-4.0, 2.8)
CASING_Y = (-3.15, 2.3)
CASING_W = 0.14                      # drawn wall thickness
X_SCREEN = 4.4
PIX_W = 0.45
PIX_H = S * M.R / M.N


def y_scene(y_model):
    return OBJ_C[1] + y_model * S


def shell_color(rho):
    return interpolate_color(ManimColor(GREEN_LO), ManimColor(GREEN_HI), float(np.clip(rho / RHO_MAX, 0, 1)))


def intensity_color(i):
    return interpolate_color(ManimColor(BLACK), ManimColor(WHITE), float(np.clip(i, 0, 1)))


# ---------------------------------------------------------------- mobject builders
def caption(text, size=26):
    return Text(text, font_size=size).to_edge(DOWN, buff=0.25)


def title(text, size=34):
    return Text(text, font_size=size, weight=BOLD).to_edge(UP, buff=0.3)


def make_source():
    fan = Sector(radius=0.75, angle=PI / 2.6, start_angle=-PI / 5.2, arc_center=ORIGIN,
                 fill_color=SOURCE, fill_opacity=1, stroke_color="#7F6000", stroke_width=1.5)
    fan.move_to([X_SOURCE, y_scene(0.5), 0])
    label = Text("Source (X-rays)", font_size=22, color="#B8860B").next_to(fan, DOWN, buff=1.0)
    return VGroup(fan, label)


def make_casing():
    w, h = CASING_X[1] - CASING_X[0], CASING_Y[1] - CASING_Y[0]
    box = Rectangle(width=w, height=h, stroke_color=CASING, stroke_width=CASING_W * 100)
    box.move_to([(CASING_X[0] + CASING_X[1]) / 2, (CASING_Y[0] + CASING_Y[1]) / 2, 0])
    label = Text("Confinement casing", font_size=22, color=CASING).next_to(box, UP, buff=0.12)
    return VGroup(box, label)


def make_object(rho, ghost_opacity=0.18, edge=True):
    """Concentric shells: full colour on the top half (what the screen sees), ghosted bottom half."""
    top, bottom = VGroup(), VGroup()
    for k in range(M.N):
        kw = dict(inner_radius=M.RADII[k] * S, outer_radius=M.RADII[k + 1] * S, angle=PI,
                  arc_center=OBJ_C, fill_color=shell_color(rho[k]),
                  stroke_color=OBJ_LINE, stroke_width=1.5 if edge else 0)
        top.add(AnnularSector(start_angle=0, fill_opacity=1, **kw))
        bottom.add(AnnularSector(start_angle=PI, fill_opacity=ghost_opacity,
                                 stroke_opacity=ghost_opacity, **kw))
    return VGroup(top, bottom)


def recolor_object(obj, rho):
    for k in range(M.N):
        obj[0][k].set_fill(shell_color(rho[k]))
        obj[1][k].set_fill(shell_color(rho[k]))
    return obj


def make_screen(values=None, x=X_SCREEN, label="Screen (1 slice)", label_size=22):
    pix = VGroup()
    for j in range(M.N):
        r = Rectangle(width=PIX_W, height=PIX_H, stroke_color=SCREEN_EDGE, stroke_width=2,
                      fill_color=WHITE if values is None else intensity_color(values[j]), fill_opacity=1)
        r.move_to([x, y_scene(M.Y_PIX[j]), 0])
        pix.add(r)
    lab = Text(label, font_size=label_size, color=SCREEN_EDGE).next_to(pix, UP, buff=0.2)
    return VGroup(pix, lab)


def set_screen(screen, values):
    for j in range(M.N):
        screen[0][j].set_fill(intensity_color(values[j]))
    return screen


def screen_values_labels(screen, values, side=RIGHT, digits=2, size=24):
    return VGroup(*[DecimalNumber(values[j], num_decimal_places=digits, font_size=size)
                    .next_to(screen[0][j], side, buff=0.15) for j in range(M.N)])


# ---------------------------------------------------------------- rays with Beer-Lambert attenuation
def _mu_along(xs, y_model, rho, with_casing, with_object):
    """Attenuation per scene unit along a horizontal ray at model height y_model."""
    mu = np.zeros_like(xs)
    if with_casing:
        per_wall = -np.log(M.casing_transmission(y_model)) / 2
        for x0 in (CASING_X[0], CASING_X[1]):
            inside = np.abs(xs - x0) <= CASING_W / 2
            mu[inside] += per_wall / CASING_W
    if with_object:
        r = np.sqrt(((xs - OBJ_C[0]) / S) ** 2 + y_model ** 2)
        k = np.searchsorted(M.RADII, r, side="right") - 1
        inside = (k >= 0) & (k < M.N)
        mu[inside] += np.asarray(rho)[k[inside]] / S
    return mu


def ray_profile(y_model, rho=M.RHO_TRUE, with_casing=True, with_object=True, x_end=X_SCREEN - PIX_W / 2):
    xs = np.linspace(X_SOURCE + 0.3, x_end, 2400)
    mu = _mu_along(xs, y_model, rho, with_casing, with_object)
    tau = np.concatenate([[0], np.cumsum((mu[1:] + mu[:-1]) / 2 * np.diff(xs))])
    return xs, M.source_profile(y_model) * np.exp(-tau)


def make_ray(y_model, rho=M.RHO_TRUE, with_casing=True, with_object=True, n_seg=160, width=5):
    xs, I = ray_profile(y_model, rho, with_casing, with_object)
    idx = np.linspace(0, len(xs) - 1, n_seg + 1).astype(int)
    y = y_scene(y_model)
    segs = VGroup()
    for a, b in zip(idx[:-1], idx[1:]):
        segs.add(Line([xs[a], y, 0], [xs[b], y, 0], stroke_color=RAY, stroke_width=width,
                      stroke_opacity=float(np.clip(I[(a + b) // 2], 0.04, 1))))
    return segs


def make_rays(**kw):
    return VGroup(*[make_ray(yj, **kw) for yj in M.Y_PIX])


# ---------------------------------------------------------------- shell identity colours (not density)
SHELL_HUES = ["#D62728", "#1F77B4", "#9467BD", "#17A2B8"]   # shell 1 (inner) ... shell 4 (outer)


def chord_segments(y_model, width=9):
    """Thick coloured segments marking where a horizontal ray at y_model is inside each shell."""
    g = VGroup()
    y = y_scene(y_model)
    for k in range(M.N):
        h_out, h_in = M.half_chord(M.RADII[k + 1], y_model), M.half_chord(M.RADII[k], y_model)
        if h_out <= 1e-9:
            continue
        for sgn in (-1, 1):
            a, b = OBJ_C[0] + sgn * h_in * S, OBJ_C[0] + sgn * h_out * S
            g.add(Line([a, y, 0], [b, y, 0], stroke_color=SHELL_HUES[k], stroke_width=width))
    return g


def shell_labels(size=24):
    out = VGroup()
    for k in range(M.N):
        rm = (M.RADII[k] + M.RADII[k + 1]) / 2 * S
        ang = 72 * DEGREES
        out.add(MathTex(rf"\rho_{k + 1}", font_size=size, color=SHELL_HUES[k]).set_z_index(10)
                .move_to(OBJ_C + rm * np.array([np.cos(ang), np.sin(ang), 0])))
    return out
