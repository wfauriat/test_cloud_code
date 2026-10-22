"""Shared visual system (spec §2): palette, type, layout, motion, and reusable pieces."""
import html
import textwrap

import numpy as np
from manim import *
from manim.animation.animation import prepare_animation

# ---------------------------------------------------------------- palette (§2.2)
BG = "#0E1525"
SURFACE, SURFACE_2 = "#172036", "#1F2A44"
TEXT, TEXT_DIM = "#EAF0FA", "#8EA0BF"
CONTEXT = "#7CB2FF"   # known text
PREDICT = "#FFB84D"   # predictions, candidates
TRUTH = "#4ADE9A"     # the real next token
ERROR = "#FF6B6B"     # loss, miss
MODEL = "#A98BFF"     # the model, parameters

SANS, MONO = "Inter", "JetBrains Mono"

# ---------------------------------------------------------------- stage units
# The spec is written in 1920x1080 pixels, origin top-left; Manim works in units
# (14.22 x 8, origin centre). px()/P() convert, fs() converts a px type size.
FW = config.frame_width
PX = FW / 1920


def px(v):
    return v * PX


def P(x, y):
    return np.array([(x - 960) * PX, (540 - y) * PX, 0.0])


def fs(size):
    return size * 0.533   # measured: Manim font_size that renders a `size`-px em


# ---------------------------------------------------------------- motion (§2.3)
ENTER, EXIT, EMPH, MOVE, BAR, COUNT, FOCUS, STAGGER = 0.5, 0.35, 0.35, 0.8, 0.9, 0.8, 1.2, 0.08
EASE_OUT = rate_functions.ease_out_cubic
EASE_IN = rate_functions.ease_in_cubic
EASE_IO = rate_functions.ease_in_out_cubic


def there_and_back_io(t):
    return rate_functions.ease_in_out_sine(1 - abs(2 * t - 1))


_DUMMY = Mobject()


class Tween(Animation):
    """Drives plain Python attributes. `setup()` runs when the tween starts (so it
    reads the state at that moment) and returns f(eased_alpha)."""
    no_add = True

    def __init__(self, setup, run_time, rate_func=EASE_IO):
        super().__init__(_DUMMY, run_time=run_time, rate_func=rate_func)
        self.setup = setup

    def begin(self):
        self.f = self.setup()

    def interpolate(self, alpha):
        self.f(self.rate_func(alpha))

    def finish(self):
        self.interpolate(1)

    def update_mobjects(self, dt):
        pass

    def clean_up_from_scene(self, scene):
        pass


def tween(obj, run_time, rate_func=EASE_IO, **targets):
    """Tween numeric attributes of `obj` from their current values to `targets`."""
    def setup():
        start = {k: getattr(obj, k) for k in targets}

        def f(a):
            for k, v in targets.items():
                setattr(obj, k, start[k] + (v - start[k]) * a)
        return f
    return Tween(setup, run_time, rate_func)


class Call(Tween):
    """Runs `fn` once, at the moment it starts."""

    def __init__(self, fn):
        super().__init__(lambda: (fn(), lambda a: None)[1], 1 / 120, linear)


class Cue(Animation):
    """Starts an animation `delay` seconds into a play() call. The animation is
    built by `make()` only when it starts, so it sees the state left by earlier
    cues, and it is finished and cleaned up as soon as it ends."""

    def __init__(self, delay, make, duration):
        self.delay, self.make, self.duration = delay, make, max(duration, 1e-3)
        self.inner, self.done = None, False
        super().__init__(_DUMMY, run_time=delay + self.duration, rate_func=linear)

    def _setup_scene(self, scene):
        self.scene = scene

    def begin(self):
        pass

    def _start(self):
        made = self.make()
        if made is None:
            self.done = True
            return
        self.inner = prepare_animation(made)
        self.inner._setup_scene(self.scene)
        mob = self.inner.mobject
        if not getattr(self.inner, "no_add", False) and not self.inner.is_introducer() \
                and mob not in self.scene.get_mobject_family_members():
            self.scene.add(mob)
        self.inner.begin()

    def interpolate(self, alpha):
        t = alpha * self.run_time
        if self.done or t < self.delay:
            return
        if self.inner is None:
            self._start()
            if self.done:
                return
        local = min(1.0, (t - self.delay) / self.duration)
        if local >= 1.0:
            self._end()
        else:
            self.inner.interpolate(local)

    def _end(self):
        self.inner.finish()
        self.inner.clean_up_from_scene(self.scene)
        self.done = True

    def update_mobjects(self, dt):
        pass

    def finish(self):
        if not self.done:
            if self.inner is None:
                self._start()
            if not self.done:
                self._end()

    def clean_up_from_scene(self, scene):
        pass


# ---------------------------------------------------------------- text
_cache = {}


def txt(s, size, color=TEXT, font=SANS, weight=NORMAL, spacing=0.0, tnum=False):
    """Glyphs of `s` (spaces dropped), with `.anchor_dy` = offset of the glyph box
    centre above the cap-height centre, so baselines line up across labels."""
    key = (s, size, color, font, weight, spacing, tnum)
    if key not in _cache:
        if spacing or tnum:
            attrs = (f' letter_spacing="{int(spacing * fs(size) * 284)}"' if spacing else "") + \
                    (' font_features="tnum"' if tnum else "")
            full = MarkupText(f'<span{attrs}>H{html.escape(s)}</span>', font=font, weight=weight,
                              font_size=fs(size), color=color)
        else:
            full = Text("H" + s, font=font, weight=weight, font_size=fs(size), color=color)
        glyphs = VGroup(*full[1:])
        glyphs.anchor_dy = glyphs.get_center()[1] - full[0].get_center()[1]
        _cache[key] = glyphs
    return _cache[key].copy()


def put(m, x, y, align="left"):
    """Place text from txt() with its cap-height centre on y (px) and its
    left/centre/right edge on x (px)."""
    tx, ty = P(x, y)[:2]
    m.set_y(ty + m.anchor_dy)
    if align == "left":
        m.shift((tx - m.get_left()[0]) * RIGHT)
    elif align == "right":
        m.shift((tx - m.get_right()[0]) * RIGHT)
    else:
        m.set_x(tx)
    return m


# ---------------------------------------------------------------- chips
CHIP_H, CHIP_GAP = 88, 16
CHIP_KINDS = {  # outline/text colour, dashed outline
    "context": (CONTEXT, False),
    "predict": (PREDICT, False),
    "slot": (PREDICT, True),
    "truth": (TRUTH, False),
    "hidden": (TRUTH, True),
}


def chip_width(text, size=44):
    k = size / 44
    return max(CHIP_H * k, txt(text, size, font=MONO).width / PX + 2 * 28 * k)


def chip(text, kind="context", x=0, y=190, size=44):
    """Token chip with its left edge at x (px), centred on y (px)."""
    color, dashed = CHIP_KINDS[kind]
    k = size / 44
    w, h = chip_width(text, size), CHIP_H * k
    bg = RoundedRectangle(width=px(w), height=px(h), corner_radius=px(20 * k),
                          stroke_width=0, fill_color=SURFACE, fill_opacity=1)
    edge = RoundedRectangle(width=px(w), height=px(h), corner_radius=px(20 * k),
                            stroke_color=color, stroke_width=3, fill_opacity=0)
    if dashed:
        edge = DashedVMobject(edge, num_dashes=max(8, int(2 * (w + h) / 22)), dashed_ratio=0.55)
    bg.move_to(P(x + w / 2, y))
    edge.move_to(P(x + w / 2, y))
    label = put(txt(text, size, color, MONO), x + w / 2, y, "center")
    g = VGroup(bg, edge, label)
    g.bg, g.edge, g.label, g.w, g.x = bg, edge, label, w, x
    return g


# ---------------------------------------------------------------- HUD pieces
def chapter_label(text):
    return put(txt(text.upper(), 28, TEXT_DIM, spacing=0.12), 120, 70)


def footer():
    return put(txt("illustrative numbers", 22, TEXT_DIM), 120, 1040)


def caption(text):
    lines = textwrap.wrap(text, 62)
    t = Text("\n".join(lines), font=SANS, weight=MEDIUM, font_size=fs(34), color=TEXT, line_spacing=0.9)
    back = RoundedRectangle(width=t.width + px(64), height=t.height + px(34), corner_radius=px(16),
                            stroke_width=0, fill_color=BG, fill_opacity=0.6)
    back.move_to(P(960, 1020) + UP * back.height / 2)
    t.move_to(back)
    return VGroup(back, t)


# ---------------------------------------------------------------- bar chart (§2.1)
ROW_Y0, ROW_STEP, ROW_H, BAR_H = 362, 100, 84, 52
LABEL_X, TRACK_X, TRACK_W = 200, 600, 900
CHART_ORIGIN = (LABEL_X, 320)


class Row:
    """State of one bar row; the Chart redraws from it every frame."""

    def __init__(self, label, p, others):
        self.a = self.b = label    # label crossfade a -> b
        self.xf = 1.0
        self.p, self.others = p, others
        self.enter = 0.0           # 0 hidden .. 1 shown (fade + rise + scale)
        self.op = 1.0              # focus dimming
        self.pop = 1.0             # scale of the percent text
        self.hl, self.hl_color = 0.0, PREDICT   # outline around the row


class Chart(VGroup):
    """Six bar rows (bar width = p x 900 px). Drawn in stage coordinates, then
    scaled by `s` about the chart's top-left corner and shifted by (x, y) px."""

    def __init__(self, dist, x=0.0, y=0.0, s=1.0, grow=True):
        super().__init__()
        self.rows = [Row(l, 0.0 if grow else p, i == len(dist) - 1) for i, (l, p) in enumerate(dist)]
        self.x, self.y, self.s = x, y, s
        self.redraw()
        self.add_updater(lambda m: m.redraw())

    def row_y(self, i):
        return ROW_Y0 + i * ROW_STEP

    def to_stage(self, x, y):
        """Stage px position of a chart-space px point."""
        ox, oy = CHART_ORIGIN
        return ox + (x - ox) * self.s + self.x, oy + (y - oy) * self.s + self.y

    def label_mob(self, i, text=None):
        r = self.rows[i]
        m = put(txt(text or r.b, 38, TEXT_DIM if r.others else TEXT, MONO), LABEL_X, self.row_y(i))
        ox, oy = CHART_ORIGIN
        return m.scale(self.s, about_point=P(ox, oy)).shift(px(self.x) * RIGHT + px(self.y) * DOWN)

    def redraw(self):
        parts = []
        for i, r in enumerate(self.rows):
            if r.enter <= 0.002:
                continue
            y, a = self.row_y(i), r.enter * r.op
            g = VGroup(RoundedRectangle(width=px(TRACK_W), height=px(BAR_H), corner_radius=px(10),
                                        stroke_width=0, fill_color=SURFACE, fill_opacity=a)
                       .move_to(P(TRACK_X + TRACK_W / 2, y)))
            w = max(0.0, r.p) * TRACK_W
            if w > 0.5:
                g.add(RoundedRectangle(width=px(w), height=px(BAR_H), corner_radius=px(min(10, w / 2)),
                                       stroke_width=0, fill_color=TEXT_DIM if r.others else PREDICT,
                                       fill_opacity=a * (0.5 if r.others else 1))
                      .move_to(P(TRACK_X + w / 2, y)))
            col = TEXT_DIM if r.others else TEXT
            for s, k in ((r.a, 1 - r.xf), (r.b, r.xf)):
                if k > 0.01:
                    g.add(put(txt(s, 38, col, MONO), LABEL_X, y).set_opacity(a * k))
            pct = put(txt(f"{round(r.p * 100)}%", 38, col, SANS, SEMIBOLD, tnum=True), TRACK_X + w + 16, y)
            g.add(pct.scale(r.pop, about_edge=LEFT).set_opacity(a))
            if r.hl > 0.01:
                g.add(RoundedRectangle(width=px(1360), height=px(ROW_H), corner_radius=px(16), fill_opacity=0,
                                       stroke_color=r.hl_color, stroke_width=3, stroke_opacity=a * r.hl)
                      .move_to(P(176 + 680, y)))
            g.shift(DOWN * px(16 * (1 - r.enter))).scale(0.96 + 0.04 * r.enter, about_point=P(850, y))
            parts.append(g)
        grp = VGroup(*parts)
        ox, oy = CHART_ORIGIN
        grp.scale(self.s, about_point=P(ox, oy)).shift(px(self.x) * RIGHT + px(self.y) * DOWN)
        self.submobjects = [grp]

    # animations ------------------------------------------------------------
    def enter_anims(self, t0):
        """(start, duration, make) items: rows enter staggered, then bars grow."""
        out = []
        for i, r in enumerate(self.rows):
            out.append((t0 + i * STAGGER, ENTER, lambda r=r: tween(r, ENTER, EASE_OUT, enter=1.0)))
        return out

    def grow(self, dist):
        return [tween(r, BAR, EASE_OUT, p=p) for r, (_, p) in zip(self.rows, dist)]

    def morph(self, dist, run_time=MOVE):
        """Bars morph in place to `dist`; labels crossfade where they change."""
        def setup():
            starts = []
            for r, (lbl, p) in zip(self.rows, dist):
                r.a, r.b, r.xf = (r.b if r.xf >= 0.5 else r.a), lbl, 0.0
                if r.a == r.b:
                    r.xf = 1.0
                starts.append((r, r.p, p, r.a != r.b))

            def f(a):
                for r, p0, p1, swap in starts:
                    r.p = p0 + (p1 - p0) * a
                    if swap:
                        r.xf = a
            return f
        return Tween(setup, run_time, EASE_IO)
