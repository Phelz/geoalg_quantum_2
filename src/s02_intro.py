from manim import *
from reactive_manim import *
import manimforge as mf
mf.setup()
import definitions as dfs


class _2_Intro(Scene):
    def construct(self):

        self.next_section("Intro", skip_animations=False)
        # Video Title
        title = MarkupText(
            f'Geometric Algebra in Quantum Mechanics', color=BLUE,
            font_size=dfs.TITLE_FONTSIZE
        )
        self.play(Write(title), run_time=3)
        self.wait(2)

        # Author
        name = MarkupText(
            f'Filobateer Ghaly', color=BLUE, font_size=int(2.5*dfs.TITLE_FONTSIZE/3)
        ).shift(DOWN)

        self.play(Write(name), run_time=2, shift=DOWN*2)
        self.wait(2)

        # Shift the title up
        new_title = MarkupText(
            f'Geometric Algebra', color=BLUE,
            font_size=45
        ).to_edge(UP)
        self.wait(28)

        self.play(Transform(title, new_title), FadeOut(name), run_time=1)
