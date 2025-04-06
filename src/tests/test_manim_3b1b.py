from manimlib import *
# from manimlib.mobject.svg.old_tex_mobject import *


from src.definitions import TITLE_FONTSIZE, NOMINAL_WAIT_TIME, PAUSE_WAIT_TIME

LATEX_TEMPLATE = r"\\usepackage{amsmath} \\usepackage{amssymb}"


class OuterProduct(Scene):
    def construct(self):
        # * ______________________________________________________________________
        # self.next_section("Title", skip_animations=True)
        # * ______________________________________________________________________
        
        ## Title
        title = TexText(f'The Outer Product', font_size=TITLE_FONTSIZE*1.5).set_color(BLUE_D).to_edge(UP)
        self.play(Write(title), run_time=3)
        
        
        # * ______________________________________________________________________
        # self.next_section("Summation equation", skip_animations=True)
        # * ______________________________________________________________________
        
        # Individual Terms
        equal = "="
        plus = "+"
        A_term = "A"
        B_term = "B"
        wedge_term = "\\wedge"
        space = " \\ "
        e_i_term = "\\mathbf{e}_i"
        e_j_term = "\\mathbf{e}_j"
        
        sum_i = "\\sum_{i}"
        sum_j = "\\sum_{j}"
        a_i = "a_i"
        b_j = "b_j"

        A_term_sum = [ sum_i, a_i, e_i_term]
        B_term_sum = [ sum_j, b_j, e_j_term]

        individual_terms = [
            A_term, wedge_term, B_term,
            equal, plus, 
            e_i_term, e_j_term,
            *A_term_sum, *B_term_sum
            
        ]
        
        A_wedge_B = Tex(A_term, space, wedge_term, space, B_term,
                t2c={A_term: RED, B_term: BLUE, wedge_term: WHITE},
                font_size=int(4 * TITLE_FONTSIZE / 3),
                # isolate=individual_terms,
                ).to_edge(UP).shift(DOWN * 1)
        
        self.play(Write(A_wedge_B), run_time=3)
        self.wait(NOMINAL_WAIT_TIME)
        
        
        A_wedge_B_summation_notation =Tex(
            A_term, space, wedge_term, space, B_term, space,
            equal, space,
            *A_term_sum, space, wedge_term, space, *B_term_sum,
            # isolate=individual_terms,
            t2c={A_term: RED, B_term: BLUE, wedge_term: WHITE, 
                 A_term_sum[0]: RED, A_term_sum[1]: RED, A_term_sum[2]: WHITE,
                 B_term_sum[0]: BLUE, B_term_sum[1]: BLUE, B_term_sum[2]: WHITE},
            font_size=int(3.5 * TITLE_FONTSIZE / 3),
        ).to_edge(UP).shift(DOWN * 1)
        
        
        self.play(
            TransformMatchingStrings(A_wedge_B, A_wedge_B_summation_notation, run_time=2)
        )
        self.wait(NOMINAL_WAIT_TIME)
        # * ______________________________________________________________________
        # * ______________________________________________________________________
        
        lbracket = "("
        rbracket = ")"
        
        # Expanded Sum 
        a1, a2, a3 = "a_1", "a_2", "a_3"
        b1, b2, b3 = "b_1", "b_2", "b_3"
        e1, e2, e3 = "\\mathbf{e}_1", "\\mathbf{e}_2", "\\mathbf{e}_3"

        # Add to list of individual terms
        individual_terms.extend([a1, a2, a3, b1, b2, b3, e1, e2, e3, 
                                 lbracket, rbracket])


        A_sum_expanded = [lbracket, a1, e1, space, plus, space, a2, e2, space, plus, space, a3, e3, rbracket]
        B_sum_expanded = [lbracket, b1, e1, space, plus, space, b2, e2, space, plus, space, b3,e3, rbracket]

        expanded_sum = Tex(
            A_term, space, wedge_term, space, B_term, space,
            equal, space,
            *A_sum_expanded, space, wedge_term, space, *B_sum_expanded,
            isolate=individual_terms,
        ).to_edge(UP).shift(DOWN * 1)
        
        
        expanded_sum.set_color_by_tex_to_color_map({
            A_term: RED, B_term: BLUE, wedge_term: WHITE, equal:WHITE, plus:WHITE,
            a1: RED, a2: RED, a3: RED,
            b1: BLUE, b2: BLUE, b3: BLUE,
        })
        
        self.play(
            TransformMatchingTex(A_wedge_B_summation_notation, expanded_sum, run_time=3,
                                #  key_map={
                                #     "a1" : "a_i"
                                #  }
                                 
                                 )
        )
        
        # * _______________________________________________________________________
        
        e1e1_term = [a1, e1, space, wedge_term, space, b1, e1]
        e1e2_term = [a1, e1, space, wedge_term, space, b2, e2]
        e1e3_term = [a1, e1, space, wedge_term, space, b3, e3]
        
        e2e1_term = [a2, e2, space, wedge_term, space, b1, e1]
        e2e2_term = [a2, e2, space, wedge_term, space, b2, e2]
        e2e3_term = [a2, e2, space, wedge_term, space, b3, e3]
        
        e3e1_term = [a3, e3, space, wedge_term, space, b1, e1]
        e3e2_term = [a3, e3, space, wedge_term, space, b2, e2]
        e3e3_term = [a3, e3, space, wedge_term, space, b3, e3]
                
        wedge_fully_expanded_1 = [equal, space,
                                 *e1e1_term,space, plus, space, *e1e2_term, space, plus, space, *e1e3_term]
        wedge_fully_expanded_2 = [plus, space, *e2e1_term, space, plus, space, *e2e2_term, space, plus, space, *e2e3_term]
        wedge_fully_expanded_3 = [plus, space, *e3e1_term, space, plus, space, *e3e2_term, space, plus, space, *e3e3_term]
        
        group_lines = VGroup(
            Tex(*wedge_fully_expanded_1, isolate=individual_terms),
            Tex(*wedge_fully_expanded_2, isolate=individual_terms),
            Tex(*wedge_fully_expanded_3, isolate=individual_terms)
        )
        
        group_lines.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5)
        for line in group_lines:
            line.set_color_by_tex_to_color_map({
                A_term: RED, B_term: BLUE, wedge_term: WHITE, equal:WHITE, plus:WHITE,
                a1: RED, a2: RED, a3: RED,
                b1: BLUE, b2: BLUE, b3: BLUE,
            })
        
        # group_lines[1].shift(RIGHT * 0.75)
        # group_lines[2].shift(RIGHT * 0.75)
        
        self.play(
            TransformMatchingTex(expanded_sum.copy(), group_lines[0], run_time=3, path_arc=100*DEGREES
                                #  key_map={
                                #      "a_1": "a_1",
                                #      "b_1": "b_1"
                                #  }
                                 )
        )            
        
        self.play(
            TransformMatchingTex(expanded_sum.copy(), group_lines[1], run_time=3)
        )
        self.play(
            TransformMatchingTex(expanded_sum.copy(), group_lines[2], run_time=3, path_arc=100*DEGREES)
        )
        
        #     A_wedge_B_summation_notation,
            
        
        
        # self.play(
        #     TransformMatchingShapes(A_wedge_B, A_wedge_B_summation_notation, run_time=2,))
        #                          key_map={
        #                                 "A": "a"
        #                          }
                                 
        #                          ),
        # )
        
        
        
        # Simple example
        
        # self.remove(a_b)
        # self.remove(a_b_2)
        
        # some_terms = [
        #     'c', 'd', 'f'
        # ]
        
        # a_b = Tex("a", plus, "b", *some_terms)
        # a_b_2 = Tex("a", plus, "b^2")
        # self.add(a_b)
        
        
        # # Transform
        # self.play(
        #     TransformMatchingTex(a_b, a_b_2, run_time=2,
        #                          key_map={
        #                              "b": "b^2"
        #                          })
        # )
        
        
        # self.play(
        #     TransformMatchingTex(A_wedge_B, A_wedge_B_summation_notation, run_time=3,
        #                          key_map=
        #                          {
        #                              A_term: A_term,
        #                              wedge_term: wedge_term,
        #                              B_term: B_term,
        #                              equal: equal,
        #                              A_term_sum[0]: A_term,
        #                              A_term_sum[1]: A_term,
        #                              A_term_sum[2]: A_term,
        #                              plus: plus,
        #                              B_term_sum[0]: B_term,
        #                              B_term_sum[1]: B_term,
        #                              B_term_sum[2]: B_term
        #                          })
        # )
        
        
        # Write the summation terms
        # A_wedge_B.append(["=", A_term_sum, wedge_term.copy(), B_term_sum])

        # A_wedge_B.append(equal)
        # A_wedge_B.append(A_term_sum)
        # A_wedge_B.append(wedge_term)
        # A_wedge_B.append(B_term_sum)

        # self.play(
        #     TransformInStages.progress(A_wedge_B, lag_ratio=0.25),
        #     run_time=3
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        # self.next_section("Expanded Summation equation", skip_animations=True)
        # * ______________________________________________________________________
        

                
        # * ______________________________________________________________________
        # self.next_section("Full expansion", skip_animations=True)
        # * ______________________________________________________________________
        
        # # Fully expand the sum 
        # e1e1_term = MathTex(a1, e1, wedge_term, b1, e1)
        # e1e2_term = MathTex(a1, e1, wedge_term, b2, e2)
        # e1e3_term = MathTex(a1, e1, wedge_term, b3, e3)
        
        # e2e1_term = MathTex(a2, e2, wedge_term, b1, e1)
        # e2e2_term = MathTex(a2, e2, wedge_term, b2, e2)
        # e2e3_term = MathTex(a2, e2, wedge_term, b3, e3)
        
        # e3e1_term = MathTex(a3, e3, wedge_term, b1, e1)
        # e3e2_term = MathTex(a3, e3, wedge_term, b2, e2)
        # e3e3_term = MathTex(a3, e3, wedge_term, b3, e3)
        
        # full_expansion_line1 = MathTex(A_term, wedge_term, B_term, "=", 
        #                               e1e1_term, "+", e1e2_term, "+", e1e3_term).to_edge(UP).shift(DOWN * 3)
        # full_expansion_line2 = MathTex("+", e2e1_term, "+", e2e2_term, "+", e2e3_term).to_edge(UP).shift(DOWN * 4+ RIGHT*0.75)
        # full_expansion_line3 = MathTex("+", e3e1_term, "+", e3e2_term, "+", e3e3_term).to_edge(UP).shift(DOWN * 5+ RIGHT*0.75)
        
        # self.play(
        #     # TransformInStages.progress(A_wedge_B_expanded, full_expansion, lag_ratio=0.25),
        #     TransformInStages.from_copy(A_wedge_B_expanded, full_expansion_line1, lag_ratio=0.25, 
        #     run_time=1),
        #     # TransformMatchingTex(A_wedge_B_expanded, full_expansion_line1, run_time=1),

        #     run_time=1
        # )
        # self.wait(0.5)
        # self.play(
        #     # TransformMatchingTex(full_expansion_line1.copy(), full_expansion_line2, run_time=1),
        #     TransformInStages.from_copy(A_wedge_B_expanded, full_expansion_line2, lag_ratio=0.25,),
        #     run_time=1
        # )
        # self.wait(0.5)
        # self.play(
        #     # TransformMatchingTex(full_expansion_line2.copy(), full_expansion_line3, run_time=1),
        #     TransformInStages.from_copy(A_wedge_B_expanded, full_expansion_line3, lag_ratio=0.25,),
        #     run_time=1
        # )
        
        # self.wait(NOMINAL_WAIT_TIME)
        
        
        # # * ______________________________________________________________________
        # # self.next_section("Cancellation", skip_animations=True)
        # # * ______________________________________________________________________
        
        # # Fade out the wedge_expanded
        # self.play(
        #     FadeOut(A_wedge_B_expanded),
        #     run_time=2
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        # full_expansion_line1.shift(UP * 2),
        # full_expansion_line2.shift(UP * 2),
        # full_expansion_line3.shift(UP * 2),
        
        # # Move everything else up
        # self.play(
        #     TransformInStages.progress(full_expansion_line1),
        #     TransformInStages.progress(full_expansion_line2),
        #     TransformInStages.progress(full_expansion_line3),
        #     run_time=2
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        # # Draw a cross around the terms that cancel out
        # cross_e1e1 = Cross(e1e1_term, color=RED_D)
        # cross_e2e2 = Cross(e2e2_term, color=RED_D)
        # cross_e3e3 = Cross(e3e3_term, color=RED_D)

        # self.play(
        #     Write(cross_e1e1),
        #     Write(cross_e2e2),
        #     Write(cross_e3e3),
        #     Circumscribe(e1e1_term),
        #     Circumscribe(e2e2_term),
        #     Circumscribe(e3e3_term),
        #     run_time=3
        # )
        
        # self.wait(NOMINAL_WAIT_TIME)
        
        
        
        # * ______________________________________________________________________
        # self.next_section("Removing Orthogonal Terms", skip_animations=True)
        # * ______________________________________________________________________




        # # Put e1e2 and e2e1 together
        # full_expansion_line1.remove(full_expansion_line1[4])
        # full_expansion_line1.remove(full_expansion_line1[4])

        # full_expansion_line2.remove(full_expansion_line2[2])
        # full_expansion_line2.remove(full_expansion_line2[2])
        
        # full_expansion_line3.remove(full_expansion_line3[-1])
        # full_expansion_line3.remove(full_expansion_line3[-1])

        
        # self.play(
        #     TransformInStages.progress(full_expansion_line1, lag_ratio=1.5),
        #     FadeOut(cross_e1e1, lag_ratio=0.2),
        #     TransformInStages.progress(full_expansion_line2, lag_ratio=1.5),
        #     FadeOut(cross_e2e2, lag_ratio=0.2),
        #     TransformInStages.progress(full_expansion_line3, lag_ratio=1.5),
        #     FadeOut(cross_e3e3, lag_ratio=0.2),
        #     run_time=3
        # )
        
        
        # * ______________________________________________________________________
        # self.next_section("Rearranging Terms", skip_animations=False)
        # * ______________________________________________________________________

        # # Swap locations of the e1e3 and e2e1 terms
        # self.play(
        #     e1e3_term.animate.move_to(e2e1_term),
        #     e2e1_term.animate.move_to(e1e3_term),
        #     run_time=2
        # )
