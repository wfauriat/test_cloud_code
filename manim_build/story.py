"""LLM explainer, Part A (Manim): one MovingCameraScene playing S1-S6 (spec §1.4).

Render:  python -m manim -ql story.py Story          (iterate)
         python -m manim -r 1920,1080 --fps 30 story.py Story   (final)
"""
import numpy as np
from manim import *

from captions import CUES, SCENES
from data import *
from theme import *

HUD_OFF = RIGHT * 400   # HUD templates live off-stage; each frame a copy is mapped into the camera view


class Dice(VGroup):
    """Dice icon redrawn from (x, y, angle, face, enter) every frame."""
    PIPS = {1: [(0, 0)], 2: [(-1, 1), (1, -1)], 3: [(-1, 1), (0, 0), (1, -1)],
            4: [(-1, 1), (1, 1), (-1, -1), (1, -1)], 5: [(-1, 1), (1, 1), (0, 0), (-1, -1), (1, -1)],
            6: [(-1, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, -1)]}

    def __init__(self, x, y):
        super().__init__()
        self.x, self.y, self.angle, self.face, self.enter = x, y, 0.0, 5, 0.0
        self.add_updater(lambda m: m.redraw())

    def redraw(self):
        if self.enter <= 0.002:
            self.submobjects = []
            return
        body = RoundedRectangle(width=px(72), height=px(72), corner_radius=px(16), fill_color=SURFACE_2,
                                fill_opacity=1, stroke_color=TEXT_DIM, stroke_width=2)
        pips = [Dot(px(19) * (i * RIGHT + j * UP), radius=px(6.5), color=TEXT) for i, j in self.PIPS[self.face]]
        g = VGroup(body, *pips).rotate(self.angle).move_to(P(self.x, self.y + 16 * (1 - self.enter)))
        self.submobjects = [g.scale(0.96 + 0.04 * self.enter).set_opacity(self.enter)]


class Story(MovingCameraScene):
    def construct(self):
        self.camera.background_color = BG
        self.T = self.clock = 0.0
        self.chap = None
        self.caps = {}
        self.cap_events = sorted([(a, 1, i) for i, (a, b, _) in enumerate(CUES)] +
                                 [(b, 0, i) for i, (a, b, _) in enumerate(CUES)])
        self.setup_grid()
        self.hud_view = VGroup()
        self.add(self.hud_view)
        self.add_updater(self.sync_hud)
        for name, start, end, label in SCENES:
            if not hasattr(self, name):
                break
            getattr(self, name)(start, end, label)
            assert abs(self.renderer.time - end) <= 0.3, (name, self.renderer.time)
            print(f"[timing] {name} ends at {self.renderer.time:.2f}s (spec {end:.1f}s)")

    # ------------------------------------------------------------ infrastructure
    def setup_grid(self):
        """Faint dot grid (6 % opacity) drifting 8 px/s; it follows the camera in
        whole grid steps, so it reads as an infinite plane. Also ticks the clock."""
        sp, cols, rows, r = 48, 51, 31, px(1.6)
        k = 0.5523 * r   # cubic Bézier handle for a quarter circle
        quarter = [((r, 0), (r, k), (k, r), (0, r)), ((0, r), (-k, r), (-r, k), (-r, 0)),
                   ((-r, 0), (-r, -k), (-k, -r), (0, -r)), ((0, -r), (k, -r), (r, -k), (r, 0))]
        pts = []
        for i in range(cols):
            for j in range(rows):
                cx, cy = px(sp) * (i - cols // 2), px(sp) * (j - rows // 2)
                pts += [[cx + qx, cy + qy, 0] for q in quarter for qx, qy in q]
        grid = VMobject(fill_color=TEXT, fill_opacity=0.06, stroke_width=0)
        grid.set_points(np.array(pts))

        def follow(m, dt):
            self.clock += dt
            c, step, drift = self.camera.frame.get_center(), px(sp), px(8) * self.clock
            m.move_to([np.round(c[0] / step) * step, np.round((c[1] - drift) / step) * step + drift, 0])
        grid.add_updater(follow)
        self.add(grid)

    def hud(self, m):
        """Register a screen-space element (chapter label, caption, counters)."""
        m.shift(HUD_OFF)
        m.is_hud = True
        return m

    def sync_hud(self, dt):
        fr = self.camera.frame
        s, c = fr.width / FW, fr.get_center()
        self.hud_view.submobjects = [m.copy().clear_updaters().shift(-HUD_OFF).scale(s, about_point=ORIGIN).shift(c)
                                     for m in self.mobjects if getattr(m, "is_hud", False)]
        self.hud_view.set_z_index(100)
        # Manim keeps a per-play draw list that never drops removed mobjects;
        # clearing it makes the renderer draw the live scene every frame.
        self.moving_mobjects = []

    def run(self, end, items):
        """Play every (start, duration, make) item at its absolute start time, plus
        the caption cues that fall in [T, end); return when the clock reaches `end`."""
        items = list(items)
        while self.cap_events and self.cap_events[0][0] < end - 1e-6:
            t, is_in, i = self.cap_events.pop(0)
            if is_in:
                self.caps[i] = self.hud(caption(CUES[i][2]))
                items.append(self.enter(t, self.caps[i], 0.3))
            else:
                items.append((t, 0.25, lambda i=i: FadeOut(self.caps[i], rate_func=EASE_IN)))
        for t, dur, _ in items:
            assert self.T - 1e-6 <= t and t + dur <= end + 1e-6, (t, dur, self.T, end)
        cues = [Cue(max(0.0, t - self.T), make, dur) for t, dur, make in items]
        cues.append(Cue(end - self.T - 1e-3, lambda: None, 1e-3))
        self.play(*cues)
        self.T = end

    # item builders: (absolute start, duration, factory) -----------------------
    def enter(self, t, m, dur=ENTER):
        return t, dur, lambda: FadeIn(m, shift=UP * px(16), scale=0.96, rate_func=EASE_OUT)

    def exit(self, t, m):
        return t, EXIT, lambda: FadeOut(m, scale=0.98, rate_func=EASE_IN)

    def call(self, t, fn):
        return t, 1 / 120, lambda: Call(fn)

    def tw(self, t, dur, obj, rate=EASE_IO, **targets):
        return t, dur, lambda: tween(obj, dur, rate, **targets)

    def cam(self, t, dur, zoom, center, rate=EASE_IO):
        return t, dur, lambda: self.camera.frame.animate(rate_func=rate).scale_to_fit_width(FW / zoom).move_to(P(*center))

    def pulse(self, t, m, factor=1.06):
        return t, EMPH, lambda: ScaleInPlace(m, factor, rate_func=there_and_back_io)

    def chapter(self, t, text):
        items = [self.exit(t, self.chap)] if self.chap else []
        self.chap = self.hud(chapter_label(text))
        return items + [self.enter(t + (0.2 if items else 0.0), self.chap)]

    def fly(self, t, dur, get_mob, end, s1, lift=150):
        """Move the mobject returned by get_mob() on a quadratic arc to `end`, scaling it by s1."""
        def setup():
            mob = get_mob()
            base, start = mob.copy(), mob.get_center()
            ctrl = np.array([start[0] * 0.25 + end[0] * 0.75, max(start[1], end[1]) + px(lift), 0])

            def f(a):
                p = (1 - a) ** 2 * start + 2 * (1 - a) * a * ctrl + a ** 2 * end
                mob.become(base.copy().scale(1 + (s1 - 1) * a).move_to(p))
            return f
        return t, dur, lambda: Tween(setup, dur, EASE_IO)

    # ------------------------------------------------------------ S1  The game
    def s1(self, a, b, label):
        text = "The cat sat on the"
        sent = txt(text, 64, TEXT, MONO)
        slot_x = 960 - (sent.width / PX + 24 + chip_width("?", 64)) / 2 + sent.width / PX + 24
        put(sent, slot_x - 24 - sent.width / PX, 540)
        big_slot = chip("?", "slot", slot_x, 540, size=64)
        cursor = Rectangle(width=px(5), height=px(76), stroke_width=0, fill_color=PREDICT, fill_opacity=1)
        cursor.move_to(P(0, 540))
        self.cursor_on = 1.0

        def typewriter(m):   # 40 ms per character from 0.3 s, blinking cursor after the last one
            k = int(np.clip(np.floor((self.clock - 0.3) / 0.04) + 1, 0, len(text)))
            n = sum(c != " " for c in text[:k])
            for i, g in enumerate(m):
                g.set_opacity(1.0 if i < n else 0.0)
            x = m[n - 1].get_right()[0] + px(6) if n else m.get_left()[0]
            if k and text[k - 1] == " ":
                x += px(38.4)
            cursor.set_x(x + px(3))
            blink = k < len(text) or (self.clock * 1.8) % 2 < 1.1
            cursor.set_opacity(self.cursor_on if blink else 0.0)

        sent.add_updater(typewriter)
        self.add(sent, cursor)

        # out: words become chips on the top row, the slot follows them
        words, xs, x = ["The", "cat", "sat", "on", "the"], [], LABEL_X
        for w in words:
            xs.append(x)
            x += chip_width(w) + CHIP_GAP
        self.chips = [chip(w, "context", xi) for w, xi in zip(words, xs)]
        self.slot = chip("?", "slot", x)
        spans, n0 = [], 0
        for w in words:
            spans.append(VGroup(*sent[n0:n0 + len(w)]))
            n0 += len(w)

        boxes = []
        for g, c in zip(spans, self.chips):
            box = VGroup(c.bg.copy(), c.edge.copy())
            boxes.append(box.stretch_to_fit_width(g.width + px(40)).stretch_to_fit_height(px(104)).move_to(g).set_opacity(0))

        def split():   # boxes go below the words in draw order
            sent.clear_updaters()
            self.remove(sent)
            self.add(*boxes, *spans)

        out = [self.call(7.2, split), self.cam(7.2, MOVE, 1.0, (960, 540)),
               (7.2, MOVE, lambda: ReplacementTransform(big_slot, self.slot, rate_func=EASE_IO))]
        for g, c, box in zip(spans, self.chips, boxes):
            out += [(7.2, MOVE, lambda g=g, c=c: ReplacementTransform(g, c.label, rate_func=EASE_IO)),
                    (7.2, MOVE, lambda box=box, c=c: ReplacementTransform(box, VGroup(c.bg, c.edge), rate_func=EASE_IO))]

        self.run(b, self.chapter(a, label) + [
            self.cam(0.0, 7.2, 1.06, (960, 540)),
            self.call(2.8, lambda: setattr(self, "cursor_on", 0.0)),
            self.enter(2.8, big_slot),
            self.pulse(5.0, big_slot),
            self.call(7.19, lambda: self.remove(cursor)),
        ] + out)

    # ------------------------------------------------------------ S2  A probability for every token
    def s2(self, a, b, label):
        ch = self.chart = Chart(D_TRAINED)
        self.add(ch)
        items = self.chapter(a, label) + [self.enter(a, self.hud(footer()))]
        items += ch.enter_anims(8.6)
        items += [(8.9 + i * STAGGER, BAR, lambda r=r, p=p: tween(r, BAR, EASE_OUT, p=p))
                  for i, (r, (_, p)) in enumerate(zip(ch.rows, D_TRAINED))]

        # 13 s: what a token is
        card = VGroup(RoundedRectangle(width=px(620), height=px(160), corner_radius=px(20), stroke_width=0,
                                       fill_color=SURFACE_2, fill_opacity=1).move_to(P(1490, 190)),
                      put(txt("token = a word or a word-piece", 30, TEXT_DIM), 1490, 146, "center"))
        whole = put(txt("unbelievable", 40, TEXT, MONO), 1490, 226, "center")
        pieces, seps, cuts = [], [], [0, 2, 8, 12]
        widths = [VGroup(*whole[i:j]).width / PX for i, j in zip(cuts, cuts[1:])]
        x = 1490 - (sum(widths) + 2 * 44) / 2
        for (i, j), w in zip(zip(cuts, cuts[1:]), widths):
            pieces.append(put(txt("unbelievable"[i:j], 40, TEXT, MONO), x, 226))
            if j < 12:
                seps.append(put(txt("|", 40, PREDICT, MONO), x + w + 22, 226, "center"))
            x += w + 44
        spans = [VGroup(*whole[i:j]) for i, j in zip(cuts, cuts[1:])]

        def split():
            self.remove(whole)
            self.add(*spans)
        items += [self.enter(13.0, VGroup(card, whole)),
                  self.call(13.9, split)]
        items += [(13.9, ENTER, lambda s=s, p=p: ReplacementTransform(s, p, rate_func=EASE_IO))
                  for s, p in zip(spans, pieces)]
        items += [self.enter(14.2, VGroup(*seps)),
                  (15.6, EXIT, lambda: FadeOut(VGroup(card, *pieces, *seps), scale=0.98, rate_func=EASE_IN))]

        # 16 s: focus on "mat"; 20 s: pull back, Σ = 100 %
        mat, rest = ch.rows[0], ch.rows[1:]
        items += [self.cam(16.0, FOCUS, 1.25, (760, 400))]
        items += [self.tw(16.0, FOCUS, r, op=0.35) for r in rest]
        items += [self.tw(16.8, 0.6, mat, pop=1.4)]
        items += [self.cam(20.0, FOCUS, 1.0, (960, 540)), self.tw(20.0, 0.6, mat, pop=1.0)]
        items += [self.tw(20.0, FOCUS, r, op=1.0) for r in rest]
        brace = Brace(Line(P(1540, 326), P(1540, 898)), RIGHT, color=TEXT_DIM, buff=0)
        total = put(txt("Σ = 100%", 38, TEXT, SANS, SEMIBOLD), 1600, 612)
        items += [(20.6, 0.6, lambda: GrowFromCenter(brace, rate_func=EASE_OUT)),
                  self.enter(21.0, total),
                  (23.4, EXIT, lambda: FadeOut(VGroup(brace, total), scale=0.98, rate_func=EASE_IN))]
        self.run(b, items)

    # ------------------------------------------------------------ S3  Predict, append, repeat
    def s3(self, a, b, label):
        ch, dice = self.chart, Dice(1650, 268)
        self.add(dice)
        self.counter = None

        def set_counter(n):
            if self.counter:
                self.remove(self.counter)
            lab = put(txt("TOKENS GENERATED", 24, TEXT_DIM, spacing=0.12), 1750, 70, "right")
            num = put(txt(str(n), 28, TEXT, SANS, SEMIBOLD, tnum=True), 1800, 70, "right")
            self.counter = self.hud(VGroup(lab, num))
            self.add(self.counter)

        set_counter(0)
        self.remove(self.counter)
        items = self.chapter(a, label) + [self.enter(a, self.counter), self.tw(a, ENTER, dice, EASE_OUT, enter=1.0)]

        def roll(face):
            def setup():
                a0 = dice.angle

                def f(a):
                    dice.angle = a0 - TAU * a
                    dice.face = face if a > 0.8 else (int(a * 9) % 6) + 1
                return f
            return Tween(setup, 0.4, EASE_OUT)

        nxt = [D_NEXT1, D_NEXT2, None]
        for k, ((dist, idx), face) in enumerate(zip(SAMPLES, [4, 2, 5])):
            r = 24.5 if k == 0 else 24.0 + 4 * k
            row, tok, slot = ch.rows[idx], dist[idx][0], self.slot
            c = chip(tok, "predict", slot.x)
            new_slot = chip("?", "slot", c.x + c.w + CHIP_GAP)
            holder = {}

            def launch(idx=idx, slot=slot, holder=holder):
                self.remove(slot)
                self.add(slot.bg, slot.edge, slot.label)
                holder["m"] = ch.label_mob(idx).set_color(PREDICT)
                self.add(holder["m"])

            def land(c=c, holder=holder, n=k + 1):
                self.remove(holder["m"])
                self.add(c.label)
                set_counter(n)

            items += [(r, 0.4, lambda face=face: roll(face)),
                      self.tw(r + 0.45, 0.4, dice, y=ch.row_y(idx)),
                      (r + 0.45, EMPH, lambda row=row: tween(row, EMPH, EASE_OUT, hl=1.0)),
                      self.call(r + 0.95, launch),
                      (r + 0.95, 0.3, lambda slot=slot: FadeOut(slot.label, rate_func=EASE_IN)),
                      self.fly(r + 0.96, 0.69, lambda holder=holder: holder["m"], c.label.get_center(), 44 / 38),
                      (r + 1.3, 0.35, lambda slot=slot, c=c: ReplacementTransform(slot.bg, c.bg, rate_func=EASE_IO)),
                      (r + 1.3, 0.35, lambda slot=slot, c=c: ReplacementTransform(slot.edge, c.edge, rate_func=EASE_IO)),
                      self.call(r + 1.66, land),
                      (r + 2.0, EMPH, lambda c=c: AnimationGroup(c.edge.animate.set_stroke(CONTEXT),
                                                                 c.label.animate.set_fill(CONTEXT))),
                      (r + 2.0, EXIT, lambda row=row: tween(row, EXIT, EASE_IN, hl=0.0)),
                      self.tw(r + 2.0, 0.5, dice, y=268),
                      self.enter(r + 2.3, new_slot)]
            if nxt[k]:
                items.append((r + 2.6, MOVE, lambda d=nxt[k]: ch.morph(d)))
            self.chips.append(c)
            self.slot = new_slot

        # out: vertical push, the stage slides up ("going deeper")
        items += [(35.2, EXIT, lambda: FadeOut(self.counter, rate_func=EASE_IN)),
                  self.tw(35.2, EXIT, dice, EASE_IN, enter=0.0),
                  self.cam(35.2, MOVE, 1.0, (960, 540 + 1080))]
        self.run(b, items)
