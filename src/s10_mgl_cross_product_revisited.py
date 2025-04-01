
from manimlib import *
from src.definitions import *




class CrossProductRevisited(Scene):
    def construct(self):
        
        # * Title
        title = TexText(f'The Outer Product', font_size=TITLE_FONTSIZE*1.5).set_color(BLUE_D).to_edge(UP)
        self.play(Write(title), run_time=3)



        final_formula = Tex(A_term, space, wedge, space, B_term, space, equal, space,
                            lbracket, A_term, space, times, space, B_term, rbracket, space, '\\mathbb{I}')
        
        # Transform both the new_a_wedge_b and the new_group_lines_cross_vector into the final formula
        final_formula.move_to(new_a_wedge_b.get_center()).shift(RIGHT*1.5)
        final_formula.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformMatchingTex(new_a_wedge_b, final_formula, run_time=2, lag_ratio=0.05),
            FadeOut(new_group_lines_cross_vector),
            # TransformMatchingTex(new_group_lines_cross_vector, final_formula, run_time=2, lag_ratio=0.05),
        )
        self.play(
            final_formula.animate.move_to(ORIGIN).to_edge(UP).shift(DOWN*1.5),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw a box around the final for
        # 89mula
        final_formula_box = Polygon(
            final_formula.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            final_formula.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            final_formula.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            final_formula.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        self.play(
            ShowCreation(final_formula_box),
            run_time=3
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # Move to upper left corner and fadeout the title
        self.play(
            FadeOut(title),
            final_formula.animate.to_corner(UL).shift(DOWN*0.25+ RIGHT*0.25),
            final_formula_box.animate.to_corner(UL),
            run_time=2,
            )
        