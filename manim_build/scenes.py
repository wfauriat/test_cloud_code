"""Uniaxial tomography explainer. Render e.g.:  manim -ql scenes.py S1_Setup"""
import numpy as np
from manim import *

import model as M
from theme import *


def setup_parts(rho=M.RHO_TRUE):
    return make_source(), make_casing(), make_object(rho), make_screen()


# =====================================================================================
class S1_Setup(Scene):
    """The experiment: source -> casing -> object -> screen."""

    def construct(self):
        ttl = title("Uniaxial X-ray tomography")
        src, cas, obj, scr = setup_parts()
        obj_lab = Text("Object: concentric shells", font_size=22, color=OBJ_LINE)
        obj_lab.next_to(obj[0], UP, buff=0.12)

        self.play(Write(ttl), run_time=1)
        self.play(FadeIn(src, shift=RIGHT * 0.3), Create(cas[0]), FadeIn(cas[1]), run_time=1.5)
        self.play(LaggedStart(*[GrowFromPoint(s, OBJ_C) for s in obj[0]], lag_ratio=0.3),
                  FadeIn(obj[1]), FadeIn(obj_lab), run_time=2)
        self.play(FadeIn(scr), run_time=0.8)

        cap = caption("The object is circular and symmetric: one half-slice describes it.")
        self.play(FadeIn(cap), Indicate(obj[1], scale_factor=1.03, color=OBJ_LINE), run_time=1.5)
        self.wait(1)

        rays = make_rays()
        cap2 = caption("X-rays are absorbed by the casing walls and by every shell they cross.")
        self.play(FadeOut(cap), FadeIn(cap2))
        self.play(LaggedStart(*[Create(r, lag_ratio=1, rate_func=linear) for r in rays], lag_ratio=0.15),
                  run_time=3)
        meas = M.measurement()
        self.play(*[scr[0][j].animate.set_fill(intensity_color(meas[j])) for j in range(M.N)], run_time=1)
        self.wait(1)

        eq = MathTex(r"I_{\text{screen}}(y)", "=", r"I_0(y)", r"\cdot", r"T_{\text{casing}}(y)", r"\cdot",
                     r"T_{\text{object}}(y)", font_size=40).to_edge(UP, buff=0.3)
        eq[2].set_color("#B8860B"); eq[4].set_color(CASING); eq[6].set_color(OBJ_LINE)
        self.play(ReplacementTransform(ttl, eq), run_time=1.5)
        self.wait(1)

        eq2 = MathTex(r"T_{\text{object}}(y) = \exp\big(-\textstyle\sum_k \rho_k\, L_k(y)\big)",
                      font_size=34, color=OBJ_LINE)
        known = MathTex(r"\rho_k", r"\text{ unknown}", r"\qquad I_0,\ T_{\text{casing}},\ L_k \text{ known}",
                        font_size=32)
        known[0].set_color(ACCENT)
        bottom = VGroup(eq2, known).arrange(RIGHT, buff=0.8).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(cap2), Write(eq2), run_time=1.5)
        self.play(FadeIn(known), run_time=1)
        self.wait(3)


# =====================================================================================
class S2_Calibration(Scene):
    """Step 1: remove source and casing contributions with a calibration shot."""

    def construct(self):
        src, cas, obj, scr = setup_parts()
        obj_lab = Text("Object: concentric shells", font_size=22, color=OBJ_LINE).next_to(obj[0], UP, buff=0.12)
        ttl = title("Step 1 - isolate the object")
        self.add(src, cas, obj, obj_lab, scr)
        self.play(Write(ttl), run_time=1)

        # --- calibration shot (no object)
        cap = caption("Calibration shot: same source and casing, no object.")
        self.play(FadeIn(cap), FadeOut(obj), FadeOut(obj_lab), run_time=1.2)
        rays = make_rays(with_object=False)
        cal = M.calibration_shot()
        self.play(LaggedStart(*[Create(r, lag_ratio=1, rate_func=linear) for r in rays], lag_ratio=0.15), run_time=2)
        self.play(*[scr[0][j].animate.set_fill(intensity_color(cal[j])) for j in range(M.N)], run_time=0.8)
        cal_screen = scr[0].copy()
        cal_tag = MathTex(r"I_{\text{cal}}", font_size=34).next_to(scr[0], RIGHT, buff=0.25)
        self.play(FadeIn(cal_tag))
        self.wait(1)

        # --- measurement shot (with object)
        cap2 = caption("Measurement shot: the object is back in place.")
        rays2 = make_rays()
        meas = M.measurement()
        self.play(FadeOut(rays), FadeOut(cal_tag), FadeIn(obj), FadeIn(obj_lab), FadeOut(cap), FadeIn(cap2), run_time=1.2)
        self.play(LaggedStart(*[Create(r, lag_ratio=1, rate_func=linear) for r in rays2], lag_ratio=0.15), run_time=2)
        self.play(*[scr[0][j].animate.set_fill(intensity_color(meas[j])) for j in range(M.N)], run_time=0.8)
        meas_tag = MathTex(r"I_{\text{meas}}", font_size=34).next_to(scr[0], RIGHT, buff=0.25)
        self.play(FadeIn(meas_tag))
        self.wait(1)

        # --- comparison panel
        meas_screen = scr[0].copy()
        self.play(*[FadeOut(m) for m in (src, cas, obj, obj_lab, rays2, scr, meas_tag, cap2)], run_time=1)
        xs = [-5.6, -3.4, -1.2]
        cols = [meas_screen, cal_screen, scr[0].copy()]
        tobj = M.measurement() / M.calibration_shot()
        set_screen(VGroup(cols[2], VGroup()), tobj)
        heads = [MathTex(r"I_{\text{meas}}", font_size=36), MathTex(r"I_{\text{cal}}", font_size=36),
                 MathTex(r"T_{\text{object}}", font_size=36, color=OBJ_LINE)]
        vals = [meas, cal, tobj]
        panel = VGroup()
        for c, x, h, v in zip(cols, xs, heads, vals):
            c.move_to([x, 0, 0])
            h.next_to(c, UP, buff=0.25)
            nums = VGroup(*[DecimalNumber(v[j], num_decimal_places=2, font_size=24).next_to(c[j], RIGHT, buff=0.12)
                            for j in range(M.N)])
            panel.add(VGroup(c, h, nums))
        ops = VGroup(MathTex(r"\div", font_size=48).move_to([(xs[0] + xs[1]) / 2 + 0.3, 0, 0]),
                     MathTex(r"=", font_size=48).move_to([(xs[1] + xs[2]) / 2 + 0.3, 0, 0]))
        self.play(FadeIn(panel[0]), FadeIn(panel[1]), run_time=1)
        cap3 = caption("Dividing by the calibration cancels the source and the casing.")
        self.play(FadeIn(ops[0]), FadeIn(cap3))
        self.play(FadeIn(ops[1]), FadeIn(panel[2], shift=LEFT * 0.3), run_time=1.2)
        self.wait(1.5)

        # --- log domain: optical depth (what step 2 works with)
        p = M.P_OBS
        base_x, bar_y = 1.0, [c.get_center()[1] for c in cols[2]]
        arrow = MathTex(r"\xrightarrow{\;-\ln\;}", font_size=44).move_to([0.45, 0, 0])
        bars = VGroup(*[Rectangle(width=p[j] * 1.8, height=PIX_H * 0.7, fill_color=OBJ_LINE, fill_opacity=0.85,
                                  stroke_width=0).move_to([base_x + 0.35 + p[j] * 0.9, bar_y[j], 0])
                        for j in range(M.N)])
        bar_nums = VGroup(*[DecimalNumber(p[j], num_decimal_places=2, font_size=24).next_to(bars[j], RIGHT, buff=0.12)
                            for j in range(M.N)])
        p_head = MathTex(r"p = \ln I_{\text{cal}} - \ln I_{\text{meas}}", font_size=34, color=OBJ_LINE)
        p_head.next_to(bars, UP, buff=0.25).align_to(bars, LEFT)
        cap4 = caption("In log scale it is a plain difference: p is the absorption due to the object only.")
        self.play(FadeIn(arrow), FadeOut(cap3), FadeIn(cap4))
        self.play(LaggedStart(*[GrowFromEdge(b, LEFT) for b in bars], lag_ratio=0.15), FadeIn(bar_nums),
                  Write(p_head), run_time=1.8)
        self.wait(3)


# =====================================================================================
class S3_ForwardModel(Scene):
    """Step 2a: the screen value is a weighted sum of shell densities (weights = path lengths)."""

    def construct(self):
        ttl = title("Step 2 - what each pixel sees")
        obj = make_object(M.RHO_TRUE)
        labs = shell_labels()
        lab_bg = VGroup(*[BackgroundRectangle(l, color=WHITE, fill_opacity=0.85, buff=0.04).set_z_index(9) for l in labs])
        self.play(Write(ttl), FadeIn(obj), run_time=1)
        self.play(FadeIn(lab_bg), FadeIn(labs), run_time=1)

        y = ValueTracker(M.Y_PIX[0])
        x0, x1 = OBJ_C[0] - S - 0.6, OBJ_C[0] + S + 0.3
        ray = always_redraw(lambda: Line([x0, y_scene(y.get_value()), 0], [x1, y_scene(y.get_value()), 0],
                                         stroke_color=RAY, stroke_width=3))
        segs = always_redraw(lambda: chord_segments(y.get_value()))

        # live bar chart of path lengths L_k(y)
        bx, base, scale = [3.7, 4.5, 5.3, 6.1], OBJ_C[1], 1.9
        axis = Line([3.3, base, 0], [6.6, base, 0], stroke_color=INK, stroke_width=2)
        names = VGroup(*[MathTex(rf"L_{k + 1}", font_size=30, color=SHELL_HUES[k]).move_to([bx[k], base - 0.35, 0])
                         for k in range(M.N)])
        bars = always_redraw(lambda: VGroup(*[
            Rectangle(width=0.55, height=max(M.chord_in_shell(k, y.get_value()) * scale, 1e-3),
                      fill_color=SHELL_HUES[k], fill_opacity=0.85, stroke_width=0)
            .move_to([bx[k], base, 0], aligned_edge=DOWN) for k in range(M.N)]))
        chart_title = Text("path length in each shell", font_size=22).move_to([4.9, OBJ_C[1] + 2.2, 0])

        cap = caption("A ray crosses each shell over a length L fixed by the geometry.")
        self.play(Create(ray), FadeIn(cap), run_time=1)
        self.play(FadeIn(segs), Create(axis), FadeIn(names), FadeIn(bars), FadeIn(chart_title), run_time=1.2)
        self.wait(1)
        cap2 = caption("Higher rays cross fewer shells; the outer shell is seen by every ray.")
        self.play(FadeOut(cap), FadeIn(cap2))
        self.play(y.animate.set_value(0.97), run_time=4, rate_func=smooth)
        self.play(y.animate.set_value(M.Y_PIX[0]), run_time=2.5, rate_func=smooth)
        self.wait(0.5)

        eq = MathTex(r"p_j", "=", r"\sum_k L_{jk}\,\rho_k", font_size=42).move_to([4.9, 2.9, 0])
        cap3 = caption("Absorption seen by pixel j = sum over shells of (path length x density).")
        self.play(FadeOut(cap2), FadeIn(cap3), FadeOut(ttl), Write(eq), run_time=1.5)
        self.wait(1.5)

        # --- build the matrix row by row (top pixel first, as on the screen)
        self.play(FadeOut(VGroup(axis, names, chart_title)), FadeOut(bars), FadeOut(eq), FadeOut(cap3), run_time=0.8)
        self.remove(bars)
        left = VGroup(obj, lab_bg, labs)
        self.play(left.animate.shift(LEFT * 2.6), run_time=1)
        shift = LEFT * 2.6
        ray.clear_updaters(); segs.clear_updaters()
        self.remove(ray, segs)
        ray = always_redraw(lambda: Line([x0, y_scene(y.get_value()), 0], [x1, y_scene(y.get_value()), 0],
                                         stroke_color=RAY, stroke_width=3).shift(shift))
        segs = always_redraw(lambda: chord_segments(y.get_value()).shift(shift))
        self.add(ray, segs)

        rows = list(range(M.N - 1, -1, -1))   # top ray first
        entries = [[("0" if M.L[j, k] < 1e-9 else f"{M.L[j, k]:.2f}") for k in range(M.N)] for j in rows]
        mat = Matrix(entries, h_buff=1.15, element_to_mobject_config={"font_size": 30})
        pvec = Matrix([[rf"p_{j + 1}"] for j in rows], element_to_mobject_config={"font_size": 30})
        rvec = Matrix([[rf"\rho_{k + 1}"] for k in range(M.N)], element_to_mobject_config={"font_size": 30})
        for k, col in enumerate(mat.get_columns()):
            for e, j in zip(col, rows):
                e.set_color(GREY_B if M.L[j, k] < 1e-9 else SHELL_HUES[k])
        for k, e in enumerate(rvec.get_entries()):
            e.set_color(SHELL_HUES[k])
        system = VGroup(pvec, MathTex("="), mat, rvec).arrange(RIGHT, buff=0.2).scale(0.85).move_to([3.4, 0.2, 0])
        for m in (pvec, mat, rvec):
            for e in m.get_entries():
                e.set_opacity(0)
        cap4 = caption("One equation per screen pixel: a linear system p = L ρ.")
        self.play(FadeIn(VGroup(pvec.get_brackets(), system[1], mat.get_brackets(), rvec.get_brackets())),
                  FadeIn(cap4), *[e.animate.set_opacity(1) for e in rvec.get_entries()], run_time=1)
        for i, j in enumerate(rows):
            self.play(y.animate.set_value(M.Y_PIX[j]), run_time=0.9)
            self.play(*[e.animate.set_opacity(1) for e in mat.get_rows()[i]],
                      pvec.get_entries()[i].animate.set_opacity(1), run_time=0.6)
        cap5 = caption("Triangular structure: top pixels only see outer shells.")
        self.play(FadeOut(cap4), FadeIn(cap5))
        self.wait(3)


# =====================================================================================
class S4_BrickFit(Scene):
    """Step 2b: find densities by stacking bricks until the candidate screen matches the observed one."""

    def construct(self):
        ttl = title("Step 2 - stack bricks until the screens match")
        self.play(Write(ttl), run_time=1)

        # candidate object (left)
        cand = make_object(np.zeros(M.N), ghost_opacity=0.0)
        cand_grp = VGroup(cand).scale(0.55).move_to([-5.45, 0.2, 0])
        cand_lab = Text("candidate object", font_size=22).next_to(cand_grp, UP, buff=0.3)

        # brick stacks (middle)
        bx = [-2.7, -1.8, -0.9, 0.0]
        base, bw, bh = -2.6, 0.75, 0.36
        floor = Line([bx[0] - 0.6, base, 0], [bx[-1] + 0.6, base, 0], stroke_color=INK, stroke_width=2)
        col_names = VGroup(*[MathTex(rf"\rho_{k + 1}", font_size=32, color=SHELL_HUES[k]).move_to([bx[k], base - 0.35, 0])
                             for k in range(M.N)])
        stack_lab = Text("density bricks (inner -> outer)", font_size=22).move_to([(bx[0] + bx[-1]) / 2, 0.9, 0])

        # screens (right): observed (from step 1) vs candidate
        obs = M.object_transmission(M.RHO_TRUE)
        sx_obs, sx_cand = 2.2, 3.9
        scr_obs = make_screen(obs, x=sx_obs, label="observed", label_size=20)
        scr_obs.shift(UP * (0.2 - scr_obs[0].get_center()[1]))
        scr_cand = make_screen(np.ones(M.N), x=sx_cand, label="candidate", label_size=20)
        scr_cand.shift(UP * (0.2 - scr_cand[0].get_center()[1]))
        mis_lab = Text("mismatch", font_size=22).move_to([5.8, 1.6, 0])
        hist = M.brick_fit()
        mis = DecimalNumber(M.misfit(hist[0]), num_decimal_places=3, font_size=30).next_to(mis_lab, DOWN, buff=0.15)
        mis_bar_max = 2.5
        mis_bar = Rectangle(width=0.35, height=mis_bar_max, fill_color=ACCENT, fill_opacity=0.8, stroke_width=0)
        mis_bar.move_to([5.8, -2.6, 0], aligned_edge=DOWN)
        m0 = M.misfit(hist[0])

        self.play(FadeIn(cand_grp), FadeIn(cand_lab), Create(floor), FadeIn(col_names), FadeIn(stack_lab),
                  FadeIn(scr_obs), FadeIn(scr_cand), FadeIn(mis_lab), FadeIn(mis), FadeIn(mis_bar), run_time=1.5)
        cap = caption("Start empty: the candidate screen is fully bright, far from the observation.")
        self.play(FadeIn(cap))
        self.wait(1.5)

        cap2 = caption("Each move adds the one brick that best reduces the mismatch.")
        self.play(FadeOut(cap), FadeIn(cap2))
        counts = [0] * M.N
        for step in range(1, len(hist)):
            k = int(np.flatnonzero(hist[step] - hist[step - 1])[0])
            rho = hist[step] * M.BRICK
            pred = M.object_transmission(rho)
            brick = Rectangle(width=bw, height=bh, fill_color=SHELL_HUES[k], fill_opacity=0.85,
                              stroke_color=WHITE, stroke_width=2)
            brick.move_to([bx[k], base + (counts[k] + 0.5) * bh, 0])
            counts[k] += 1
            rt = 1.0 if step <= 3 else 0.45
            m = M.misfit(hist[step])
            self.play(FadeIn(brick, shift=DOWN * 0.6),
                      cand[0][k].animate.set_fill(shell_color(rho[k])),
                      *[scr_cand[0][j].animate.set_fill(intensity_color(pred[j])) for j in range(M.N)],
                      ChangeDecimalToValue(mis, m),
                      mis_bar.animate.stretch_to_fit_height(max(mis_bar_max * m / m0, 1e-3)).move_to(
                          [5.8, -2.6, 0], aligned_edge=DOWN),
                      run_time=rt)
            if step == 3:
                cap3 = caption("Outer shells come first: they are the only ones the top pixels see.")
                self.play(FadeOut(cap2), FadeIn(cap3), run_time=0.6)
                self.wait(1)
                cap2 = cap3

        rho_hat = hist[-1] * M.BRICK
        vals = VGroup(*[DecimalNumber(rho_hat[k], num_decimal_places=1, font_size=28, color=SHELL_HUES[k])
                        .move_to([bx[k], base + counts[k] * bh + 0.3, 0]) for k in range(M.N)])
        cap4 = caption("Screens match: the densities are recovered (true values 0.6, 1.4, 1.0, 0.4).")
        self.play(FadeOut(cap2), FadeIn(cap4), FadeIn(vals),
                  Indicate(scr_cand[0], color=OBJ_LINE, scale_factor=1.05), run_time=1.5)
        self.wait(3)
