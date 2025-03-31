from manim import *
# from manim.opengl import *
from reactive_manim import *
import manimforge as mf
mf.setup()
# import definitions as dfs
from definitions import TITLE_FONTSIZE, NOMINAL_WAIT_TIME, PAUSE_WAIT_TIME


class OuterProduct(Scene):
    def construct(self):
        
        # * ______________________________________________________________________
        self.next_section("Title", skip_animations=True)
        # * ______________________________________________________________________
        
        title = Tex(
            f'The Outer Product', color=BLUE_D,
            font_size=TITLE_FONTSIZE*1.5
        ).to_edge(UP)
        
        self.play(Write(title), run_time=3)
        
        
        # * ______________________________________________________________________
        self.next_section("Summation equation", skip_animations=True)
        # * ______________________________________________________________________
        
        A_term = MathTex("A", color=RED)
        B_term = MathTex("B", color=BLUE)
        wedge_term = MathTex("\\wedge")
        e_i_term = MathTex("\\mathbf{e}_i")
        e_j_term = MathTex("\\mathbf{e}_j")
        # equal = MathTex("=")
        # plus = MathTex("+")
        
        A_term_sum = MathTex("\\sum_{i}", "a_i", "\\mathbf{e}_i",)
        B_term_sum = MathTex("\\sum_{j}", "b_j", "\\mathbf{e}_j",)
        
        # Only set the color of the first two
        A_term_sum[0].set_color(RED)
        A_term_sum[1].set_color(RED)
        
        B_term_sum[0].set_color(BLUE)
        B_term_sum[1].set_color(BLUE)
        
        A_wedge_B = MathTex(A_term, wedge_term, B_term).to_edge(UP).shift(DOWN * 2)
        
        self.play(Write(A_wedge_B), run_time=3)
        self.wait(NOMINAL_WAIT_TIME)
        
        # Write the summation terms
        A_wedge_B.append(["=", A_term_sum, wedge_term.copy(), B_term_sum])
        # A_wedge_B.append(equal)
        # A_wedge_B.append(A_term_sum)
        # A_wedge_B.append(wedge_term)
        # A_wedge_B.append(B_term_sum)

        self.play(
            TransformInStages.progress(A_wedge_B, lag_ratio=0.25),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Expanded Summation equation", skip_animations=True)
        # * ______________________________________________________________________
        
        
        # Expand the sum
        a1, a2, a3 = MathTex("a_1", "a_2", "a_3", color=RED)
        b1, b2, b3 = MathTex("b_1", "b_2", "b_3", color=BLUE)
        e1, e2, e3 = MathTex("\\mathbf{e}_1", "\\mathbf{e}_2", "\\mathbf{e}_3")

        A_sum_expanded = MathTex(a1, e1, "+", a2, e2, "+", a3, e3)
        B_sum_expanded = MathTex(b1, e1, "+", b2, e2, "+", b3, e3)
        
        
        # Copy the A_wedge_B term and transform it into A wedge B = A_sum_expanded wedge B_sum_expanded
        # A_wedge_B_expanded = MathTex(A_wedge_B[0].copy(), A_wedge_B[1].copy(), A_wedge_B[2].copy(), A_wedge_B[3].copy(), Parentheses(A_sum_expanded), wedge_term, Parentheses(B_sum_expanded)).to_edge(UP).shift(DOWN * 3)
        A_wedge_B_expanded = MathTex(A_term, wedge_term, B_term, "=" , Parentheses(A_sum_expanded), wedge_term, Parentheses(B_sum_expanded)).to_edge(UP).shift(DOWN * 1.5)
        
        # print(A_wedge_B_expanded[4])        
        self.play(
            # TransformInStages.from_copy(A_wedge_B, A_wedge_B_expanded, lag_ratio=0.25),
            TransformInStages.replacement_transform(A_wedge_B, A_wedge_B_expanded, lag_ratio=0.25),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)

                
        # * ______________________________________________________________________
        self.next_section("Full expansion", skip_animations=True)
        # * ______________________________________________________________________
        
        # Fully expand the sum 
        e1e1_term = MathTex(a1, e1, wedge_term, b1, e1)
        e1e2_term = MathTex(a1, e1, wedge_term, b2, e2)
        e1e3_term = MathTex(a1, e1, wedge_term, b3, e3)
        
        e2e1_term = MathTex(a2, e2, wedge_term, b1, e1)
        e2e2_term = MathTex(a2, e2, wedge_term, b2, e2)
        e2e3_term = MathTex(a2, e2, wedge_term, b3, e3)
        
        e3e1_term = MathTex(a3, e3, wedge_term, b1, e1)
        e3e2_term = MathTex(a3, e3, wedge_term, b2, e2)
        e3e3_term = MathTex(a3, e3, wedge_term, b3, e3)
        
        full_expansion_line1 = MathTex(A_term, wedge_term, B_term, "=", 
                                      e1e1_term, "+", e1e2_term, "+", e1e3_term).to_edge(UP).shift(DOWN * 3)
        full_expansion_line2 = MathTex("+", e2e1_term, "+", e2e2_term, "+", e2e3_term).to_edge(UP).shift(DOWN * 4+ RIGHT*0.75)
        full_expansion_line3 = MathTex("+", e3e1_term, "+", e3e2_term, "+", e3e3_term).to_edge(UP).shift(DOWN * 5+ RIGHT*0.75)
        
        self.play(
            # TransformInStages.progress(A_wedge_B_expanded, full_expansion, lag_ratio=0.25),
            TransformInStages.from_copy(A_wedge_B_expanded, full_expansion_line1, lag_ratio=0.25, 
            run_time=1),
            # TransformMatchingTex(A_wedge_B_expanded, full_expansion_line1, run_time=1),

            run_time=1
        )
        self.wait(0.5)
        self.play(
            # TransformMatchingTex(full_expansion_line1.copy(), full_expansion_line2, run_time=1),
            TransformInStages.from_copy(A_wedge_B_expanded, full_expansion_line2, lag_ratio=0.25,),
            run_time=1
        )
        self.wait(0.5)
        self.play(
            # TransformMatchingTex(full_expansion_line2.copy(), full_expansion_line3, run_time=1),
            TransformInStages.from_copy(A_wedge_B_expanded, full_expansion_line3, lag_ratio=0.25,),
            run_time=1
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Cancellation", skip_animations=True)
        # * ______________________________________________________________________
        
        # Fade out the wedge_expanded
        self.play(
            FadeOut(A_wedge_B_expanded),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        full_expansion_line1.shift(UP * 2),
        full_expansion_line2.shift(UP * 2),
        full_expansion_line3.shift(UP * 2),
        
        # Move everything else up
        self.play(
            TransformInStages.progress(full_expansion_line1),
            TransformInStages.progress(full_expansion_line2),
            TransformInStages.progress(full_expansion_line3),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw a cross around the terms that cancel out
        cross_e1e1 = Cross(e1e1_term, color=RED_D)
        cross_e2e2 = Cross(e2e2_term, color=RED_D)
        cross_e3e3 = Cross(e3e3_term, color=RED_D)

        self.play(
            Write(cross_e1e1),
            Write(cross_e2e2),
            Write(cross_e3e3),
            Circumscribe(e1e1_term),
            Circumscribe(e2e2_term),
            Circumscribe(e3e3_term),
            run_time=3
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        
        
        # * ______________________________________________________________________
        self.next_section("Removing Orthogonal Terms", skip_animations=True)
        # * ______________________________________________________________________




        # Put e1e2 and e2e1 together
        full_expansion_line1.remove(full_expansion_line1[4])
        full_expansion_line1.remove(full_expansion_line1[4])

        full_expansion_line2.remove(full_expansion_line2[2])
        full_expansion_line2.remove(full_expansion_line2[2])
        
        full_expansion_line3.remove(full_expansion_line3[-1])
        full_expansion_line3.remove(full_expansion_line3[-1])

        
        self.play(
            TransformInStages.progress(full_expansion_line1, lag_ratio=1.5),
            FadeOut(cross_e1e1, lag_ratio=0.2),
            TransformInStages.progress(full_expansion_line2, lag_ratio=1.5),
            FadeOut(cross_e2e2, lag_ratio=0.2),
            TransformInStages.progress(full_expansion_line3, lag_ratio=1.5),
            FadeOut(cross_e3e3, lag_ratio=0.2),
            run_time=3
        )
        
        
        # * ______________________________________________________________________
        self.next_section("Rearranging Terms", skip_animations=False)
        # * ______________________________________________________________________

        # Put the e1e2 and e2e1 terms together
        full_expansion_line1[-1] = full_expansion_line2[1].copy()        
        full_expansion_line2[1] = full_expansion_line1[-1].copy()
        
        self.play(
            TransformInStages.progress(full_expansion_line1, lag_ratio=0.25),
            TransformInStages.progress(full_expansion_line2, lag_ratio=0.25),
            run_time=3
        )
