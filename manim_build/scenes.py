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




# =====================================================================================
WALK = "#B8860B"     # brick-walk colour
GRAD = "#2E7D32"     # gradient colour


def slice_misfit(r1, r2):
    """Mismatch as a function of (rho_1, rho_2), other shells at their true value."""
    rho = M.RHO_TRUE.copy(); rho[0], rho[1] = r1, r2
    return M.rho_misfit(rho)


def slice_grad(r1, r2):
    """d(mismatch)/d(rho_1, rho_2) = -2 sum_i Delta_i A_i L_ik, from dA_i/drho_k = -L_ik A_i."""
    rho = M.RHO_TRUE.copy(); rho[0], rho[1] = r1, r2
    A = M.object_factor(rho)
    return (-2 * M.L.T @ ((A - M.A_OBS) * A))[:2]


class S5_Gradient(Scene):
    """Step 2c, in principle: brick walk vs gradient walk, on the mismatch landscape and as brick stacks.
    Only rho_1 and rho_2 vary; shells 3-5 are fixed at their true value (grey)."""

    def construct(self):
        import contourpy
        cap = None

        # ================================================ left: explanation box + landscape
        box_txt = VGroup(
            VGroup(Text("Brick walk:", font_size=18, color=WALK, weight=BOLD),
                   Text("knows the mismatch only where it tries;", font_size=18)).arrange(RIGHT, buff=0.12),
            Text("probes the neighbours, one brick at a time.", font_size=18),
            VGroup(Text("Gradient:", font_size=18, color=GRAD, weight=BOLD),
                   MathTex(r"\frac{\partial A}{\partial \rho} = -L\,e^{-L\rho}", font_size=30)).arrange(RIGHT, buff=0.15),
            Text("slope known everywhere, all shells at once.", font_size=18),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        box_txt[1].shift(RIGHT * 0.2); box_txt[3].shift(RIGHT * 0.2)
        box = SurroundingRectangle(box_txt, buff=0.15, corner_radius=0.08, stroke_color=SCREEN_EDGE, stroke_width=1.5)
        VGroup(box, box_txt).to_corner(UL, buff=0.25)

        lo, hi, n = 0.0, 1.6, 161
        g = np.linspace(lo, hi, n)
        Z = np.log10(np.array([[slice_misfit(x, y) for x in g] for y in g]) + 1e-6)
        size = 4.2
        ax = Axes(x_range=[lo, hi, 0.4], y_range=[lo, hi, 0.4], x_length=size, y_length=size, tips=False,
                  axis_config={"color": INK, "stroke_width": 2, "include_numbers": True, "font_size": 16,
                               "decimal_number_config": {"num_decimal_places": 1, "color": INK}})
        ax.move_to([-3.75, -0.95, 0])
        xl = MathTex(r"\rho_1", font_size=28, color=SHELL_HUES[0]).next_to(ax.x_axis, RIGHT, buff=0.15)
        yl = MathTex(r"\rho_2", font_size=28, color=SHELL_HUES[1]).next_to(ax.c2p(0, 1.4), LEFT, buff=0.45)
        Zc = np.clip(Z, -3.0, None)
        zn = (Zc - Zc.min()) / (Zc.max() - Zc.min())
        lo_c, hi_c = np.array([255, 250, 228]), np.array([150, 178, 212])
        img = (lo_c + zn[..., None] * (hi_c - lo_c)).astype(np.uint8)[::-1]
        heat = ImageMobject(img).stretch_to_fit_width(size).stretch_to_fit_height(size).move_to(ax.c2p(0.8, 0.8))
        heat.set_z_index(-2)
        cg = contourpy.contour_generator(g, g, Z)
        contours = VGroup()
        for lev in np.arange(-3.0, 0.01, 0.25):
            for line in cg.lines(lev):
                if len(line) > 3:
                    contours.add(VMobject(stroke_color=GREY_C, stroke_width=1.2, stroke_opacity=0.8)
                                 .set_points_smoothly([ax.c2p(x, y) for x, y in line[::3]]))
        target = Star(n=5, outer_radius=0.12, inner_radius=0.055, color=ACCENT, fill_opacity=1).move_to(
            ax.c2p(*M.RHO_TRUE[:2])).set_z_index(9)

        # ================================================ right: two brick panels (walk | gradient)
        ttl = Text("Step 2 - why gradients help", font_size=28, weight=BOLD).move_to([3.95, 3.5, 0])
        bh, base = 0.3, -2.7

        def panel(x0, name, color):
            bx = [x0 + 0.56 * k for k in range(M.N)]
            head = Text(name, font_size=26, color=color).move_to([(bx[0] + bx[-1]) / 2, 2.55, 0])
            floor = Line([bx[0] - 0.33, base, 0], [bx[-1] + 0.33, base, 0], stroke_color=INK, stroke_width=2)
            names = VGroup(*[MathTex(rf"\rho_{k + 1}", font_size=24, color=SHELL_HUES[k] if k < 2 else GREY_B)
                             .move_to([bx[k], base - 0.27, 0]) for k in range(M.N)])
            fixed = VGroup()
            for k in range(2, M.N):
                for j in range(int(round(M.RHO_TRUE[k] / M.BRICK))):
                    fixed.add(Rectangle(width=0.46, height=bh, fill_color=GREY_B, fill_opacity=0.6, stroke_color=WHITE,
                                        stroke_width=1.5).move_to([bx[k], base + (j + 0.5) * bh, 0]))
            flab = Text("fixed", font_size=16, color=GREY_B).move_to([bx[3], base + 7 * bh + 0.2, 0])
            targets = VGroup(*[DashedLine([bx[k] - 0.26, base + M.RHO_TRUE[k] / M.BRICK * bh, 0],
                                          [bx[k] + 0.26, base + M.RHO_TRUE[k] / M.BRICK * bh, 0],
                                          dash_length=0.06, stroke_color=GREY_C, stroke_width=2) for k in range(2)])
            steps_lab = Text("steps:", font_size=20).move_to([bx[1], 2.05, 0])
            steps = Integer(0, font_size=24, color=color).next_to(steps_lab, RIGHT, buff=0.12)
            return bx, VGroup(head, floor, names, fixed, flab, targets, steps_lab, steps), steps

        wbx, wpanel, wsteps = panel(0.55, "Brick walk", WALK)
        gbx, gpanel, gsteps = panel(4.25, "Gradient walk", GRAD)
        dash_note = Text("dashed: true density", font_size=15, color=GREY_C).move_to([3.95, 1.55, 0])

        self.play(FadeIn(ttl), Create(ax), FadeIn(xl), FadeIn(yl), FadeIn(heat), run_time=1.2)
        self.play(Create(contours, lag_ratio=0.02), FadeIn(target, scale=0.5), run_time=1.5)
        cap = caption("Mismatch for every (ρ1, ρ2), shells 3 to 5 fixed: a landscape with one valley (light = small).")
        self.play(FadeIn(cap), FadeIn(wpanel), FadeIn(gpanel), FadeIn(dash_note), run_time=1.2)
        self.wait(1.5)

        # ================================================ brick walk: one brick per step
        cap = swap_caption(self, cap, "Brick walk: try each neighbouring brick, keep the best, repeat.")
        self.play(FadeIn(box), FadeIn(box_txt[:2]), run_time=0.8)
        step = M.BRICK
        p = np.zeros(2)
        walker = Dot(ax.c2p(*p), radius=0.08, color=WALK).set_z_index(6)
        self.play(FadeIn(walker, scale=0.5), run_time=0.4)
        wstacks = [[], []]
        n_w = 0
        while True:
            nbrs = [p + d for d in (np.array([step, 0]), np.array([-step, 0]), np.array([0, step]), np.array([0, -step]))
                    if (p + d).min() >= -1e-9]
            best = min(nbrs, key=lambda q: slice_misfit(*q))
            if slice_misfit(*best) >= slice_misfit(*p):
                break
            n_w += 1
            probe = VGroup(*[Cross(scale_factor=0.07, stroke_color=WALK, stroke_width=3).move_to(ax.c2p(*q))
                             for q in nbrs])
            seg = Line(ax.c2p(*p), ax.c2p(*best), stroke_color=WALK, stroke_width=4).set_z_index(5)
            k = int(np.flatnonzero(np.abs(best - p) > 1e-9)[0])
            if best[k] > p[k]:
                b = Rectangle(width=0.46, height=bh, fill_color=SHELL_HUES[k], fill_opacity=0.85, stroke_color=WHITE,
                              stroke_width=1.5).move_to([wbx[k], base + (len(wstacks[k]) + 0.5) * bh, 0])
                wstacks[k].append(b)
                brick_anim = FadeIn(b, shift=DOWN * 0.4)
            else:
                brick_anim = FadeOut(wstacks[k].pop(), shift=UP * 0.4)
            self.play(FadeIn(probe), run_time=0.35)
            self.play(Create(seg), walker.animate.move_to(ax.c2p(*best)), FadeOut(probe), brick_anim,
                      wsteps.animate.set_value(n_w), run_time=0.55)
            p = best
        self.wait(0.8)

        # ================================================ gradient walk: several (uneven) bricks per step
        cap = swap_caption(self, cap, "The gradient gives the downhill direction at every point, without trying anything.")
        self.play(FadeIn(box_txt[2:]), run_time=0.8)
        field = VGroup()
        for x in np.linspace(0.1, 1.5, 8):
            for y in np.linspace(0.1, 1.5, 8):
                d = -slice_grad(x, y)
                d = d / (np.linalg.norm(d) + 1e-12) * 0.12
                field.add(Arrow(ax.c2p(x - d[0] / 2, y - d[1] / 2), ax.c2p(x + d[0] / 2, y + d[1] / 2), buff=0,
                                color=GRAD, stroke_width=2.5, tip_length=0.09,
                                max_tip_length_to_length_ratio=0.5).set_opacity(0.55))
        self.play(LaggedStart(*[GrowArrow(a) for a in field], lag_ratio=0.01), run_time=1.5)
        self.wait(0.8)

        # steepest-descent path (normalised gradient flow), cut into 4 steps
        n_steps = 4
        q, flow = np.zeros(2), [np.zeros(2)]
        for _ in range(4000):
            d = -slice_grad(*q)
            q = q + 0.002 * d / (np.linalg.norm(d) + 1e-12)
            flow.append(q.copy())
            if np.linalg.norm(q - M.RHO_TRUE[:2]) < 0.004:
                break
        flow.append(M.RHO_TRUE[:2].copy())
        flow = np.array(flow)
        arc = np.concatenate([[0], np.cumsum(np.linalg.norm(np.diff(flow, axis=0), axis=1))])
        marks = [int(np.searchsorted(arc, s)) for s in np.linspace(0, arc[-1], n_steps + 1)]
        marks[-1] = len(flow) - 1

        ball = Dot(ax.c2p(0, 0), radius=0.08, color=GRAD).set_z_index(7)
        gcols = [VGroup(), VGroup()]          # pieces of uneven bricks, per shell
        self.add(*gcols)
        cap = swap_caption(self, cap, "Gradient walk: follow the slope, all densities together, with steps of any size.")
        self.play(FadeIn(ball, scale=0.5), run_time=0.4)

        def column_to(k, rho_new, rho_old):
            """Animations bringing gradient column k from rho_old to rho_new (add a brick, or trim the top)."""
            h_old, h_new = rho_old / M.BRICK * bh, rho_new / M.BRICK * bh
            if h_new >= h_old + 1e-3:
                piece = Rectangle(width=0.46, height=h_new - h_old, fill_color=SHELL_HUES[k], fill_opacity=0.85,
                                  stroke_color=WHITE, stroke_width=1.5).move_to([gbx[k], base + h_old, 0], aligned_edge=DOWN)
                gcols[k].add(piece)
                return [FadeIn(piece, shift=DOWN * 0.4)]
            anims, cut = [], h_old - h_new
            for piece in reversed(list(gcols[k])):
                if cut <= 1e-3:
                    break
                ph = piece.height
                if ph <= cut + 1e-3:
                    anims.append(FadeOut(piece)); gcols[k].remove(piece); cut -= ph
                else:
                    anims.append(piece.animate.stretch_to_fit_height(ph - cut).align_to(piece, DOWN))
                    cut = 0
            return anims

        for j, (a, b) in enumerate(zip(marks[:-1], marks[1:]), start=1):
            r0, r1 = flow[a], flow[b]
            piece = VMobject(stroke_color=GRAD, stroke_width=4.5).set_points_smoothly(
                [ax.c2p(*v) for v in flow[a:b + 1:max(1, (b - a) // 12)]] + [ax.c2p(*r1)]).set_z_index(5)
            d = -slice_grad(*r0); d = d / np.linalg.norm(d) * 0.32
            arrow = Arrow(ax.c2p(*r0), ax.c2p(*(r0 + d)), buff=0, color=GRAD, stroke_width=5,
                          tip_length=0.15).set_z_index(8)
            self.play(GrowArrow(arrow), run_time=0.45)
            bricks = column_to(0, r1[0], r0[0]) + column_to(1, r1[1], r0[1])
            self.play(Create(piece), MoveAlongPath(ball, piece.copy()), FadeOut(arrow), *bricks,
                      gsteps.animate.set_value(j), run_time=1.0)
            if j == 1:
                self.wait(0.6)

        self.play(Indicate(target, color=GRAD), Indicate(VGroup(*gcols), color=GRAD, scale_factor=1.04), run_time=0.9)
        cap = swap_caption(self, cap, f"Same answer: {n_w} single-brick steps vs {n_steps} gradient steps. "
                                      "With N shells, a brick step means 2N trials.")
        self.wait(3.5)
