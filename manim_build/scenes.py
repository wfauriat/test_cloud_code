"""Uniaxial tomography explainer. Render e.g.:  manim -ql scenes.py S1_Setup

Notation: row / pixel i = 1..N (top -> axis), shell k = 1..N (outer -> inner),
D = dose, A = attenuation factor in [0, 1], L_ik = path length of row i in shell k.
"""
import numpy as np
from manim import *

import model as M
from theme import *


def play_rays(scene, rays, run_time=2.5):
    scene.play(LaggedStart(*[Create(r, lag_ratio=1, rate_func=linear) for r in rays], lag_ratio=0.12),
               run_time=run_time)


def fill_screen(screen, values, cmap=dose_color):
    return [screen[0][i].animate.set_fill(cmap(values[i])) for i in range(M.N)]


def swap_caption(scene, old, text, **kw):
    new = caption(text)
    scene.play(FadeOut(old), FadeIn(new), **kw)
    return new


# =====================================================================================
class S1_Setup(Scene):
    """The experiment: source -> casing -> object -> screen."""

    def construct(self):
        ttl = title("Uniaxial X-ray tomography")
        src, cas, obj, scr = make_source(), make_casing(), make_object(M.RHO_TRUE), make_screen()
        rows = row_labels(scr[0])
        obj_lab = Text("Object: concentric shells", font_size=22, color=OBJ_LINE).next_to(obj[0], UP, buff=0.12)

        self.play(Write(ttl), run_time=1)
        self.play(FadeIn(src, shift=RIGHT * 0.3), Create(cas[0]), FadeIn(cas[1]), run_time=1.5)
        self.play(LaggedStart(*[GrowFromPoint(s, OBJ_C) for s in reversed(obj[0])], lag_ratio=0.25),
                  FadeIn(obj[1]), FadeIn(obj_lab), run_time=2)
        self.play(FadeIn(scr), run_time=0.8)

        cap = caption("The object is circular and symmetric: one half-slice describes it.")
        self.play(FadeIn(cap), Indicate(obj[1], scale_factor=1.03, color=OBJ_LINE), run_time=1.5)
        self.wait(0.8)
        cap = swap_caption(self, cap, "The screen has one pixel per row i, and one row per shell.")
        self.play(LaggedStart(*[FadeIn(r, shift=LEFT * 0.2) for r in rows], lag_ratio=0.2), run_time=1.2)
        self.wait(0.8)

        cap = swap_caption(self, cap, "X-rays are absorbed by the casing walls and by every shell they cross.")
        play_rays(self, make_rays())
        self.play(*fill_screen(scr, M.measurement()), run_time=1)
        self.wait(1)

        eq = MathTex(r"D_{\text{mes}}(i)", "=", r"D_0(i)", r"\cdot", r"A_{\text{casing}}(i)", r"\cdot",
                     r"A_{\text{object}}(i)", font_size=40).to_edge(UP, buff=0.3)
        eq[2].set_color(SOURCE_TXT); eq[4].set_color(CASING); eq[6].set_color(OBJ_LINE)
        self.play(ReplacementTransform(ttl, eq), run_time=1.5)
        cap = swap_caption(self, cap, "D: dose.   A: fraction of the dose let through (between 0 and 1).")
        self.wait(2)

        eq2 = MathTex(r"A_{\text{object}}(i) = \exp\big(-\textstyle\sum_k \rho_k\, L_{ik}\big)",
                      font_size=34, color=OBJ_LINE)
        known = MathTex(r"\rho_k", r"\text{ unknown}", r"\qquad D_0,\ A_{\text{casing}},\ L_{ik} \text{ known}",
                        font_size=32)
        known[0].set_color(ACCENT)
        VGroup(eq2, known).arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(cap), Write(eq2), run_time=1.5)
        self.play(FadeIn(known), run_time=1)
        self.wait(3)


# =====================================================================================
class S2_Separate(Scene):
    """Step 1: separate the object's contribution from the source and the casing."""

    def construct(self):
        src, cas, obj, scr = make_source(), make_casing(), make_object(M.RHO_TRUE), make_screen()
        rows = row_labels(scr[0])
        obj_lab = Text("Object: concentric shells", font_size=22, color=OBJ_LINE).next_to(obj[0], UP, buff=0.12)
        ttl = title("Step 1 - separate the object's contribution from the rest", size=29)
        self.add(src, cas, obj, obj_lab, scr, rows)
        self.play(Write(ttl), run_time=1.2)

        # --- blank shot: calibration shot or simulation without the object
        cap = caption("Calibration shot, or simulation without the object (a blank virtual shot).")
        self.play(FadeIn(cap), FadeOut(obj), FadeOut(obj_lab), run_time=1.2)
        rays = make_rays(with_object=False)
        void = M.void_shot()
        play_rays(self, rays, 2)
        self.play(*fill_screen(scr, void), run_time=0.8)
        void_screen = scr[0].copy()
        void_tag = MathTex(r"D_{\text{void}}", font_size=34).next_to(rows, RIGHT, buff=0.2)
        self.play(FadeIn(void_tag))
        self.wait(1.2)

        # --- measurement shot
        rays2 = make_rays()
        meas = M.measurement()
        self.play(FadeOut(rays), FadeOut(void_tag), FadeIn(obj), FadeIn(obj_lab), run_time=1)
        cap = swap_caption(self, cap, "Measurement shot: the object is in place.")
        play_rays(self, rays2, 2)
        self.play(*fill_screen(scr, meas), run_time=0.8)
        meas_tag = MathTex(r"D_{\text{mes}}", font_size=34).next_to(rows, RIGHT, buff=0.2)
        self.play(FadeIn(meas_tag))
        self.wait(1)

        # --- pixel-by-pixel division
        meas_screen = scr[0].copy()
        self.play(*[FadeOut(m) for m in (src, cas, obj, obj_lab, rays2, scr, rows, meas_tag, cap)], run_time=1)
        xs = [-5.7, -3.5, -1.3]
        a_obj = M.A_OBS
        a_screen = make_screen(np.ones(M.N))[0]
        for p in a_screen:
            p.set_fill(WHITE)
        cols = [meas_screen, void_screen, a_screen]
        heads = [MathTex(r"D_{\text{mes}}", font_size=36), MathTex(r"D_{\text{void}}", font_size=36),
                 MathTex(r"A_{\text{object}}", font_size=36, color=OBJ_LINE)]
        nums = []
        for c, x, h, v in zip(cols, xs, heads, (meas, void, a_obj)):
            c.move_to([x, 0.3, 0])
            h.next_to(c, UP, buff=0.25)
            nums.append(VGroup(*[DecimalNumber(v[i], num_decimal_places=2, font_size=24)
                                 .next_to(c[i], RIGHT, buff=0.12) for i in range(M.N)]))
        idx = row_labels(meas_screen, side=LEFT)
        ops = VGroup(MathTex(r"\div", font_size=48).move_to([(xs[0] + xs[1]) / 2 + 0.3, 0.3, 0]),
                     MathTex(r"=", font_size=48).move_to([(xs[1] + xs[2]) / 2 + 0.3, 0.3, 0]))
        cbar = colorbar().next_to(a_screen, DOWN, buff=0.45)
        dose_note = Text("dose", font_size=20, color=SCREEN_EDGE)
        dose_note.next_to(VGroup(meas_screen, void_screen), DOWN, buff=0.45)

        self.play(FadeIn(VGroup(meas_screen, heads[0], nums[0], idx)), FadeIn(VGroup(void_screen, heads[1], nums[1])),
                  FadeIn(dose_note), run_time=1)
        self.play(FadeIn(ops), FadeIn(a_screen), FadeIn(heads[2]), FadeIn(cbar), run_time=1)
        cap = caption("Pixel by pixel, dividing by the blank shot cancels the source and the casing.")
        self.play(FadeIn(cap))

        def row_box(i):
            return SurroundingRectangle(VGroup(meas_screen[i], nums[2][i]), buff=0.06,
                                        stroke_color=ACCENT, stroke_width=3)
        box = row_box(0)
        self.play(Create(box), run_time=0.5)
        for i in range(M.N):
            if i:
                self.play(Transform(box, row_box(i)), run_time=0.35)
            self.play(a_screen[i].animate.set_fill(a_color(a_obj[i])), FadeIn(nums[2][i]), run_time=0.45)
        self.play(FadeOut(box), run_time=0.4)
        self.wait(1.5)

        # --- log domain
        p = M.P_OBS
        base_x = 0.9
        arrow = MathTex(r"\xrightarrow{\;-\ln\;}", font_size=44).move_to([0.35, 0.3, 0])
        bars = VGroup(*[Rectangle(width=p[i] * 1.8, height=PIX_H * 0.7, fill_color=OBJ_LINE, fill_opacity=0.85,
                                  stroke_width=0).move_to([base_x + 0.35 + p[i] * 0.9, a_screen[i].get_y(), 0])
                        for i in range(M.N)])
        bar_nums = VGroup(*[DecimalNumber(p[i], num_decimal_places=2, font_size=24).next_to(bars[i], RIGHT, buff=0.12)
                            for i in range(M.N)])
        p_head = MathTex(r"p_i = -\ln A_{\text{object}}(i)", font_size=34, color=OBJ_LINE)
        p_head.next_to(bars, UP, buff=0.25).align_to(bars, LEFT)
        p_sub = MathTex(r"= \ln D_{\text{void}}(i) - \ln D_{\text{mes}}(i)", font_size=28)
        p_sub.next_to(bars, DOWN, buff=0.35).align_to(bars, LEFT)
        cap = swap_caption(self, cap, "In log scale the division is a plain difference: p is due to the object only.")
        self.play(FadeIn(arrow))
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.12), FadeIn(bar_nums),
                  Write(p_head), run_time=1.8)
        self.play(FadeIn(p_sub), run_time=1)
        self.wait(3)


# =====================================================================================
class S3_ForwardModel(Scene):
    """Step 2a: each pixel row sees a weighted sum of shell densities (weights = path lengths)."""

    def construct(self):
        ttl = title("Step 2 - what each pixel row sees")
        obj = make_object(M.RHO_TRUE)
        labs = shell_labels()
        self.play(Write(ttl), FadeIn(obj), run_time=1)
        self.play(FadeIn(labs), run_time=1)

        shift = np.zeros(3)
        x0, x1 = OBJ_C[0] - S - 0.6, OBJ_C[0] + S + 0.3

        def ray_state(i):
            y = y_scene(M.Y_PIX[i])
            line = Line([x0, y, 0], [x1, y, 0], stroke_color=RAY, stroke_width=3)
            lab = MathTex(rf"i={i + 1}", font_size=28, color=SCREEN_EDGE).next_to(line, LEFT, buff=0.15)
            return VGroup(line, chord_segments(M.Y_PIX[i]), lab).shift(shift)

        # bar chart of path lengths L_ik for the current row
        bx = [3.4 + 0.78 * k for k in range(M.N)]
        base, scale = OBJ_C[1], 1.9
        axis = Line([bx[0] - 0.5, base, 0], [bx[-1] + 0.5, base, 0], stroke_color=INK, stroke_width=2)
        names = VGroup(*[MathTex(rf"L_{{i{k + 1}}}", font_size=28, color=SHELL_HUES[k]).move_to([bx[k], base - 0.35, 0])
                         for k in range(M.N)])

        def bars_state(i):
            return VGroup(*[Rectangle(width=0.55, height=max(M.L[i, k] * scale, 1e-3), fill_color=SHELL_HUES[k],
                                      fill_opacity=0.85, stroke_width=0).move_to([bx[k], base, 0], aligned_edge=DOWN)
                            for k in range(M.N)])

        def bar_values(i):
            return VGroup(*[DecimalNumber(M.L[i, k], num_decimal_places=2, font_size=20, color=SHELL_HUES[k])
                            .move_to([bx[k], base + M.L[i, k] * scale + 0.2, 0])
                            for k in range(M.N) if M.L[i, k] > 0])
        chart_title = Text("path length in each shell", font_size=22).move_to([(bx[0] + bx[-1]) / 2,
                                                                                       base + 2.3, 0])

        ray, bars, vals = ray_state(0), bars_state(0), bar_values(0)
        cap = caption("Row i crosses each shell over a length L_ik, fixed by the geometry.")
        self.play(FadeIn(ray), FadeIn(cap), run_time=1)
        self.play(Create(axis), FadeIn(names), FadeIn(bars), FadeIn(vals), FadeIn(chart_title), run_time=1.2)
        self.wait(1.2)
        cap = swap_caption(self, cap, "Row i crosses shells 1 to i only: the outer shell is seen by every row.")
        for i in range(1, M.N):
            new_ray, new_bars, new_vals = ray_state(i), bars_state(i), bar_values(i)
            self.play(FadeOut(ray), FadeOut(vals), run_time=0.25)
            self.play(FadeIn(new_ray), Transform(bars, new_bars), FadeIn(new_vals), run_time=0.5)
            ray, vals = new_ray, new_vals
            self.wait(1.0)

        eq = MathTex(r"p_i", "=", r"\sum_k L_{ik}\,\rho_k", font_size=42).move_to([(bx[0] + bx[-1]) / 2, 2.9, 0])
        cap = swap_caption(self, cap, "What pixel i sees = sum over shells of (path length x density).")
        self.play(FadeOut(ttl), Write(eq), run_time=1.5)
        self.wait(1.5)

        # --- build the linear system row by row
        self.play(FadeOut(VGroup(axis, names, chart_title, bars, vals, eq, cap, ray)), run_time=0.8)
        shift = LEFT * 2.6
        self.play(VGroup(obj, labs).animate.shift(shift), run_time=1)

        entries = [[("0" if M.L[i, k] < 1e-9 else f"{M.L[i, k]:.2f}") for k in range(M.N)] for i in range(M.N)]
        mat = Matrix(entries, h_buff=1.05, element_to_mobject_config={"font_size": 28})
        pvec = Matrix([[rf"p_{i + 1}"] for i in range(M.N)], element_to_mobject_config={"font_size": 28})
        rvec = Matrix([[rf"\rho_{k + 1}"] for k in range(M.N)], element_to_mobject_config={"font_size": 28})
        for k, col in enumerate(mat.get_columns()):
            for i, e in enumerate(col):
                e.set_color(GREY_B if M.L[i, k] < 1e-9 else SHELL_HUES[k])
        for k, e in enumerate(rvec.get_entries()):
            e.set_color(SHELL_HUES[k])
        system = VGroup(pvec, MathTex("="), mat, rvec).arrange(RIGHT, buff=0.2).scale(0.85).move_to([3.4, 0.0, 0])
        for m in (pvec, mat):
            for e in m.get_entries():
                e.set_opacity(0)
        cap = caption("One equation per pixel row: a linear system p = L ρ.")
        self.play(FadeIn(VGroup(pvec.get_brackets(), system[1], mat.get_brackets(), rvec)), FadeIn(cap), run_time=1)
        ray = None
        for i in range(M.N):
            new_ray = ray_state(i)
            if ray is not None:
                self.play(FadeOut(ray), run_time=0.2)
            self.play(FadeIn(new_ray), run_time=0.3)
            self.play(*[e.animate.set_opacity(1) for e in mat.get_rows()[i]],
                      pvec.get_entries()[i].animate.set_opacity(1), run_time=0.5)
            ray = new_ray
        cap = swap_caption(self, cap, "Triangular structure: row i only depends on shells 1 to i.")
        self.wait(3)


# =====================================================================================
class S4_BrickFit(Scene):
    """Step 2b: stack density bricks, one downhill step at a time, until the screens match."""

    def construct(self):
        ttl = title("Step 2 - stack bricks until the screens match")
        self.play(Write(ttl), run_time=1)
        hist = M.brick_fit()
        n_moves = len(hist) - 1

        # ---- left: candidate object + brick stacks
        cand = make_object(np.zeros(M.N), ghost_opacity=0.0)
        cand.scale(0.45, about_point=OBJ_C).shift(np.array([-5.0, 0.55, 0]) - OBJ_C)
        cand_lab = Text("candidate object", font_size=22).move_to([-5.0, 1.95, 0])
        bx = [-6.4 + 0.7 * k for k in range(M.N)]
        base, bw, bh = -2.75, 0.6, 0.3
        floor = Line([bx[0] - 0.4, base, 0], [bx[-1] + 0.4, base, 0], stroke_color=INK, stroke_width=2)
        col_names = VGroup(*[MathTex(rf"\rho_{k + 1}", font_size=28, color=SHELL_HUES[k]).move_to([bx[k], base - 0.3, 0])
                             for k in range(M.N)])

        # ---- middle: observed vs candidate screens (A colormap), per-pixel mismatch
        sx_obs, sx_cand = -2.25, -0.65
        def screen_at(values, x, label):
            s = make_screen(values, x=x, label=label, label_size=20, cmap=a_color)
            return s.shift(UP * (0.3 - s[0].get_center()[1]))
        scr_obs = screen_at(M.A_OBS, sx_obs, "observed")
        scr_cand = screen_at(np.ones(M.N), sx_cand, "candidate")
        idx = row_labels(scr_obs[0], side=LEFT, size=22, buff=0.12)
        cbar = colorbar().next_to(VGroup(scr_obs[0], scr_cand[0]), DOWN, buff=0.4)
        dx0, dscale = -0.2, 1.8

        def delta_bars(bricks):
            d = M.pixel_mismatch(bricks)
            return VGroup(*[Rectangle(width=max(abs(d[i]) * dscale, 1e-3), height=PIX_H * 0.55, stroke_width=0,
                                      fill_color=ACCENT, fill_opacity=0.8)
                            .move_to([dx0, scr_cand[0][i].get_y(), 0], aligned_edge=LEFT) for i in range(M.N)])
        dbars = delta_bars(hist[0])
        dlab = MathTex(r"|\Delta_i|", font_size=28, color=ACCENT).move_to([dx0 + 0.9, scr_cand[1].get_y(), 0])

        # ---- right: downhill descent of the total mismatch (log scale)
        ax = Axes(x_range=[0, n_moves + 1, 5], y_range=[0, 5, 1], x_length=4.0, y_length=3.7,
                  tips=False, axis_config={"color": INK, "stroke_width": 2, "include_ticks": True},
                  x_axis_config={"numbers_to_include": list(range(0, n_moves + 1, 5)), "font_size": 20,
                                 "decimal_number_config": {"num_decimal_places": 0, "color": INK}})
        ax.move_to([4.85, -0.35, 0])
        ylabels = VGroup(*[MathTex(rf"10^{{{e}}}", font_size=20).next_to(ax.c2p(0, e + 4), LEFT, buff=0.1)
                           for e in (0, -2, -4)])
        xlab = Text("move", font_size=20).next_to(ax.x_axis, DOWN, buff=0.4)
        ylab = MathTex(r"\text{mismatch} = \sum_i \Delta_i^2", font_size=28).next_to(ax, UP, buff=0.3)
        ylab.align_to(ax, LEFT).shift(LEFT * 0.3)
        delta_def = MathTex(r"\Delta_i = A^{\text{cand}}_i - A^{\text{obs}}_i", font_size=24).next_to(ylab, UP, buff=0.12)
        delta_def.align_to(ylab, LEFT)

        def pt(n):
            return ax.c2p(n, np.log10(max(M.misfit(hist[n]), 1e-4)) + 4)
        ball = Dot(pt(0), radius=0.1, color=ACCENT).set_z_index(5)
        mis_val = DecimalNumber(M.misfit(hist[0]), num_decimal_places=4, font_size=26)
        mis_val.next_to(ylab, RIGHT, buff=0.25)

        self.play(FadeIn(cand), FadeIn(cand_lab), Create(floor), FadeIn(col_names),
                  FadeIn(scr_obs), FadeIn(scr_cand), FadeIn(idx), FadeIn(cbar), FadeIn(dbars), FadeIn(dlab),
                  Create(ax), FadeIn(ylabels), FadeIn(xlab), FadeIn(ylab), FadeIn(delta_def), run_time=1.5)
        cap = caption("Start empty: the candidate screen lets everything through, far from the observation.")
        self.play(FadeIn(cap), FadeIn(ball, scale=0.5), FadeIn(mis_val))
        self.wait(2)

        cap = swap_caption(self, cap, "Each move adds the brick that lowers the mismatch most: one step downhill.")
        counts = [0] * M.N
        stairs = VGroup()
        self.add(stairs)
        for n in range(1, n_moves + 1):
            k = int(np.flatnonzero(hist[n] - hist[n - 1])[0])
            rho = hist[n] * M.BRICK
            pred = M.object_factor(rho)
            brick = Rectangle(width=bw, height=bh, fill_color=SHELL_HUES[k], fill_opacity=0.85,
                              stroke_color=WHITE, stroke_width=2)
            brick.move_to([bx[k], base + (counts[k] + 0.5) * bh, 0])
            counts[k] += 1
            p0, p2 = pt(n - 1), pt(n)
            p1 = np.array([p2[0], p0[1], 0])
            step = VMobject(stroke_color=ACCENT, stroke_width=3).set_points_as_corners([p0, p1, p2])
            stairs.add(step)
            rt = 1.1 if n <= 3 else 0.5
            self.play(FadeIn(brick, shift=DOWN * 0.5),
                      cand[0][k].animate.set_fill(shell_color(rho[k])),
                      *[scr_cand[0][i].animate.set_fill(a_color(pred[i])) for i in range(M.N)],
                      Transform(dbars, delta_bars(hist[n])),
                      Create(step), MoveAlongPath(ball, step.copy()),
                      ChangeDecimalToValue(mis_val, M.misfit(hist[n])),
                      run_time=rt)
            if n == 4:
                cap = swap_caption(self, cap, "Outer shells come first: the top rows only see them.", run_time=0.5)
                self.wait(1)

        rho_hat = hist[-1] * M.BRICK
        vals = VGroup(*[DecimalNumber(rho_hat[k], num_decimal_places=1, font_size=24, color=SHELL_HUES[k])
                        .move_to([bx[k], base + counts[k] * bh + 0.25, 0]) for k in range(M.N)])
        match = Text("exact match", font_size=20, color=ACCENT).next_to(ball, UP + LEFT * 0.3, buff=0.1)
        cap = swap_caption(self, cap, "Screens match pixel by pixel: densities recovered (true: 0.4, 1.0, 1.4, 0.8, 0.6).",
                           run_time=1)
        self.play(FadeIn(vals), FadeIn(match), Indicate(scr_cand[0], color=OBJ_LINE, scale_factor=1.05), run_time=1.5)
        self.wait(3)
