from manim import *

class Smoke(Scene):
    def construct(self):
        self.camera.background_color = "#0E1525"
        c = Circle(radius=1.5, color="#A98BFF", fill_opacity=0.3)
        t1 = Text("The cat sat on the", font="JetBrains Mono", color="#7CB2FF").scale(0.6).next_to(c, DOWN)
        t2 = Text("−ln p · 46%", font="Inter", weight=SEMIBOLD, color="#FFB84D").scale(0.6).next_to(c, UP)
        self.play(Create(c), FadeIn(t1), FadeIn(t2), rate_func=rate_functions.ease_out_cubic)
        self.wait(0.5)
