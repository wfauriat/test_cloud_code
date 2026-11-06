"""Smoke test: LaTeX, axes, and a shape kept in sync with a model via ValueTracker."""
import numpy as np
from manim import *


class Preflight(Scene):
    def construct(self):
        eq = MathTex(r"I(\theta) = I_0 \, e^{-\mu L(\theta)}").to_edge(UP)
        axes = Axes(x_range=[0, PI, PI / 4], y_range=[0, 1.1, 0.5], x_length=6, y_length=3).to_edge(DOWN)
        theta = ValueTracker(0.0)

        def model(t):
            return np.exp(-1.5 * (1 + 0.6 * np.sin(2 * t)))

        curve = always_redraw(lambda: axes.plot(model, x_range=[0, max(theta.get_value(), 1e-3)], color=YELLOW))
        dot = always_redraw(lambda: Dot(axes.c2p(theta.get_value(), model(theta.get_value())), color=RED))
        bar = always_redraw(lambda: Rectangle(width=3, height=0.4, color=BLUE)
                            .rotate(theta.get_value()).move_to(UP * 1.2 + LEFT * 4))
        self.add(eq, axes, curve, dot, bar)
        self.play(theta.animate.set_value(PI), run_time=3, rate_func=linear)
        self.wait(0.5)
