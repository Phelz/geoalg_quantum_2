from manimlib import *
from src.definitions import *


class _7_LeviCevita(Scene):
    def construct(self):
        
        # * Title
        title = Title(
            f'The Levi-Civita Tensor',
            include_underline=False,
        ).set_color(BLUE)
        title.to_edge(UP)

        self.play(Write(title), run_time=2)
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * OG Definition
        levi_cevita = Tex(
            "\\epsilon_{ijk} = \\begin{cases} 1 & \\text{if } (i,j,k) \\text{ is an even permutation of } (1,2,3), \\\\ -1 & \\text{if } (i,j,k) \\text{ is an odd permutation of } (1,2,3), \\\\ 0 & \\text{otherwise.} \\end{cases}"
        )

        self.play(Write(levi_cevita, run_time=3))
        self.wait(NOMINAL_WAIT_TIME)
        # Make it smaller and move it up a bit
        self.play(levi_cevita.animate.shift(UP))
        # Provide examples
        
        
        lc_ex_text = Tex("\\epsilon_{123} = \\ 1",
                         isolate=["1", "2", "3",]
                         ).shift(DOWN*1.5).scale(2)
        # Color the "3"
        
        cmap_dict = {"3": YELLOW}
        lc_ex_text.set_color_by_tex_to_color_map(cmap_dict)
        
        self.play(Write(lc_ex_text), run_time=1)
        self.wait(4)

        
        lc_ex_text_move_3 = Tex(
            "\\epsilon_{132} = -1",
            isolate=["1", "2", "3",]
        ).move_to(lc_ex_text).scale(2)
        lc_ex_text_move_3.set_color_by_tex_to_color_map(cmap_dict)
        
        self.play(
            TransformMatchingTex(lc_ex_text, lc_ex_text_move_3),
        )
        self.wait(4)
        
        lc_ex_text_move_3_again = Tex(
            "\\epsilon_{312} = 1",
            isolate=["1", "2", "3",]
        ).move_to(lc_ex_text).scale(2)
        lc_ex_text_move_3_again.set_color_by_tex_to_color_map(cmap_dict)
        
        self.play(
            TransformMatchingTex(lc_ex_text_move_3, lc_ex_text_move_3_again),
        )
        self.wait(4)
        
        # * Two indices are the same
        lc_ex_text_same = Tex(
            "\\epsilon_{332} = 0",
            isolate=["1", "2", "3",]
        ).move_to(lc_ex_text).scale(2)
        lc_ex_text_same.set_color_by_tex_to_color_map(cmap_dict)
        self.play(
            TransformMatchingTex(lc_ex_text_move_3_again, lc_ex_text_same),
        )
        self.wait(4)
        
        # * Fade to black
        self.play(
            FadeOut(title),
            FadeOut(levi_cevita),
            FadeOut(lc_ex_text_same),
            run_time=2
        )
        
        