from manimlib import *
# from manimlib.mobject.svg.old_tex_mobject import *


from src.definitions import TITLE_FONTSIZE, NOMINAL_WAIT_TIME, PAUSE_WAIT_TIME

LATEX_TEMPLATE = r"\usepackage{amsbsy}"



class _9_OuterProduct(Scene):
    def construct(self):
        
        # * Title
        title = TexText(f'The Outer Product', font_size=TITLE_FONTSIZE*1.5).set_color(BLUE).to_edge(UP)
        self.play(Write(title), run_time=3)
        self.wait(NOMINAL_WAIT_TIME)

        # * Summation equation
        
        # Individual Terms
        equal = "="; plus = "+"; wedge = r"\wedge"; space = " \ "
        
        A_term = "A"; B_term = "B"
        a_i = "a_i"; b_j = "b_j"
        
        e_i = r"\mathbf{e}_i"; e_j = r"\mathbf{e}_j"
        sum_i = r"\sum_{i}"; sum_j = r"\sum_{j}"

        A_term_sum = [ sum_i, a_i, e_i]
        B_term_sum = [ sum_j, b_j, e_j]

        individual_terms = [
            A_term, wedge, B_term,
            equal, plus, 
            e_i, e_j,
            *A_term_sum, *B_term_sum
            
        ]
        
        A_wedge_B = Tex(A_term, space, wedge, space, B_term,
                t2c={A_term: RED, B_term: BLUE, wedge: WHITE},
                font_size=int(4 * TITLE_FONTSIZE / 3),
                isolate=individual_terms,
                
                ).to_edge(UP).shift(DOWN * 1)
        
        self.play(Write(A_wedge_B), run_time=3)
        self.wait(NOMINAL_WAIT_TIME)
        self.wait(NOMINAL_WAIT_TIME)
        
        A_wedge_B_summation_notation =Tex(
            A_term, space, wedge, space, B_term, space,
            equal, space,
            *A_term_sum, space, wedge, space, *B_term_sum,
            isolate=individual_terms,
            t2c={A_term: RED, B_term: BLUE, wedge: WHITE, 
                 A_term_sum[0]: RED, A_term_sum[1]: RED, A_term_sum[2]: WHITE,
                 B_term_sum[0]: BLUE, B_term_sum[1]: BLUE, B_term_sum[2]: WHITE},
            font_size=int(3.5 * TITLE_FONTSIZE / 3),
            
            
        ).to_edge(UP).shift(DOWN * 1)
        
        
        self.play(
            TransformMatchingStrings(A_wedge_B, A_wedge_B_summation_notation, run_time=2,
                key_map={A_term: sum_i, 
                         B_term: sum_j,
                        wedge: wedge,
                         },
                                     
                                     )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Expanded Summation equation
        # * _______________________________________________________________________
        
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
            A_term, space, wedge, space, B_term, space,
            equal, space,
            *A_sum_expanded, space, wedge, space, *B_sum_expanded,
            isolate=individual_terms,
        ).to_edge(UP).shift(DOWN * 1)
        
        colormap_dict = {A_term: RED, B_term: BLUE, wedge: WHITE, equal:WHITE, plus:WHITE,
                a1: RED, a2: RED, a3: RED,
                b1: BLUE, b2: BLUE, b3: BLUE,}
        
        expanded_sum.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformMatchingTex(A_wedge_B_summation_notation, expanded_sum, run_time=3,
                                 key_map={
                                     
                                    sum_i: a1,
                                    a_i: a2,
                                    e_i: a3,
                                    wedge: wedge,
                                    equal: equal,
                                    sum_j: b1,
                                    b_j: b2,
                                    e_j: b3,
                                 }
                                 )
        )
        self.wait(NOMINAL_WAIT_TIME)
    
        # * Full Expansion
        # * _______________________________________________________________________
        
        e1e1_term = [a1, e1, space, wedge, space, b1, e1]
        e1e2_term = [a1, e1, space, wedge, space, b2, e2]
        e1e3_term = [a1, e1, space, wedge, space, b3, e3]
        
        e2e1_term = [a2, e2, space, wedge, space, b1, e1]
        e2e2_term = [a2, e2, space, wedge, space, b2, e2]
        e2e3_term = [a2, e2, space, wedge, space, b3, e3]
        
        e3e1_term = [a3, e3, space, wedge, space, b1, e1]
        e3e2_term = [a3, e3, space, wedge, space, b2, e2]
        e3e3_term = [a3, e3, space, wedge, space, b3, e3]
                
        wedge_fully_expanded_1 = [equal, space, *e1e1_term,space, plus, space, *e1e2_term, space, plus, space, *e1e3_term]
        wedge_fully_expanded_2 = [plus, space, *e2e1_term, space, plus, space, *e2e2_term, space, plus, space, *e2e3_term]
        wedge_fully_expanded_3 = [plus, space, *e3e1_term, space, plus, space, *e3e2_term, space, plus, space, *e3e3_term]
        
        group_lines = VGroup(
            Tex(*wedge_fully_expanded_1, isolate=individual_terms),
            Tex(*wedge_fully_expanded_2, isolate=individual_terms),
            Tex(*wedge_fully_expanded_3, isolate=individual_terms)
        )
        
        group_lines.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5)
        for line in group_lines:
            line.set_color_by_tex_to_color_map(colormap_dict)
        
        def generate_line(self, line_num, term):
            
            km={    A_term: "",
                     B_term: "",
                     
                     term:term,
                    #  a2: "",
                    #  a3: "",
                     
                     b1: b1,
                     b2: b2,
                     b3: b3,
                     
                     e1: e1,
                     e2: e2,
                     e3: e3,
                     
                     wedge: wedge,
                     equal: equal,
                     plus : plus,
                     }
            
            self.play(
                Indicate(expanded_sum[term], scale_factor=1.5),
                Indicate(expanded_sum[b1], scale_factor=1.5),
                Indicate(expanded_sum[b2], scale_factor=1.5),
                Indicate(expanded_sum[b3], scale_factor=1.5),
            )
            
        
            self.play(
                TransformMatchingTex(expanded_sum.copy().set_opacity(0), group_lines[line_num],  path_arc=5*DEGREES, 
                                        key_map=km,
                                    lag_ratio=.4,

                                    ),
                run_time=1,
            )    
        
        generate_line(self, 0, a1)
        generate_line(self, 1, a2)
        generate_line(self, 2, a3)
        
        # Before crossing terms, Transform the orginal expanded sum into just A wedge B, and move everything below up 
        new_a_wedge_b = Tex(
            A_term, space, wedge, space, B_term,).to_edge(UP).shift(DOWN * 1.35 + LEFT * 5)
        
        new_a_wedge_b.set_color_by_tex_to_color_map(colormap_dict)
        self.play(
            TransformMatchingTex(expanded_sum, new_a_wedge_b),
            group_lines.animate.shift(UP * 1),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Cancellation
        # * _______________________________________________________________________

        
        cross_1 = Cross(group_lines[0][1:10], color=RED, stroke_width=5)
        cross_2 = Cross(group_lines[1][11:20], color=RED, stroke_width=5)
        cross_3 = Cross(group_lines[2][-9:], color=RED, stroke_width=5)
        
        self.play(
            Indicate(group_lines[0][1:10], scale_factor=1.25),
            Indicate(group_lines[1][11:20], scale_factor=1.25),
            Indicate(group_lines[2][-9:], scale_factor=1.25),
            ShowCreation(cross_1),
            ShowCreation(cross_2),
            ShowCreation(cross_3),
            
            run_time=3
        )        
        
        new_line_1 = Tex(*wedge_fully_expanded_1[:2], *wedge_fully_expanded_1[12:])
        new_line_2 = Tex(*wedge_fully_expanded_2[:11], *wedge_fully_expanded_2[21:])
        new_line_3 = Tex(*wedge_fully_expanded_3[:-10])
        
        new_group_lines = VGroup(
            new_line_1,
            new_line_2,
            new_line_3
        )
        
        new_group_lines.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5 + UP*1)
        
        for line in [new_line_1, new_line_2, new_line_3]:
            line.set_color_by_tex_to_color_map(colormap_dict)
        
        
        self.play(
            FadeOut(cross_1),
            FadeOut(cross_2),
            FadeOut(cross_3),
            TransformMatchingTex(group_lines[0], new_line_1, run_time=2, lag_ratio=0.25,),
            TransformMatchingTex(group_lines[1], new_line_2, run_time=2, lag_ratio=0.25,),
            TransformMatchingTex(group_lines[2], new_line_3, run_time=2, lag_ratio=0.25,),
            new_a_wedge_b.animate.shift(RIGHT * 1.5),
        )
        
            # Indicate the terms I'm about to shuffle
        self.play(
            Indicate(new_line_1[3:6], scale_factor=1.25, color=YELLOW),
            Indicate(new_line_1[8:10], scale_factor=1.25, color=YELLOW),
            
            Indicate(new_line_2[3:6], scale_factor=1.25, color=YELLOW),
            Indicate(new_line_2[8:10], scale_factor=1.25, color=YELLOW),
            run_time=1,
        )
        self.wait(0.5)
        
        self.play(
            Indicate(new_line_1[-2:], scale_factor=1.25, color=YELLOW),
            Indicate(new_line_1[-7:-4], scale_factor=1.25, color=YELLOW),
            
            Indicate(new_line_3[3:6], scale_factor=1.25, color=YELLOW),
            Indicate(new_line_3[8:10], scale_factor=1.25, color=YELLOW),
            run_time=1,
        )
        self.wait(0.5)
        
        self.play(
            Indicate(new_line_2[-2:], scale_factor=1.25, color=YELLOW),
            Indicate(new_line_2[-7:-4], scale_factor=1.25, color=YELLOW),
            
            Indicate(new_line_3[-2:], scale_factor=1.25, color=YELLOW),
            Indicate(new_line_3[-7:-4], scale_factor=1.25, color=YELLOW),
            run_time=1,
        )
        self.wait(0.5)
        
        # * Rearranging Terms
        # * _______________________________________________________________________
        
        
        new_line_1_rearranged = Tex(equal, space, *e1e2_term, space, plus, space, *e2e1_term)
        new_line_2_rearranged = Tex(plus, space, *e3e2_term, space, plus, space, *e2e3_term)
        new_line_3_rearranged = Tex(plus, space, *e3e1_term, space, plus, space, *e1e3_term)
        
        new_group_lines_rearranged = VGroup(
            new_line_1_rearranged,
            new_line_2_rearranged,
            new_line_3_rearranged
        )
        new_group_lines_rearranged.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5 + UP*1)
        for line in [new_line_1_rearranged, new_line_2_rearranged, new_line_3_rearranged]:
            line.set_color_by_tex_to_color_map(colormap_dict)
        
        # ! Cant be sophisticated
        # self.play(
        #     FadeOut(new_line_1[-8:]),
        #     TransformMatchingTex(new_line_2.copy().set_opacity(0), new_line_1_rearranged, run_time=2,
        #     key_map = {k: v for k, v in zip(e1e2_term, e1e3_term)}
        #                          ),
            
        # )
        
        self.play(
            FadeOut(new_line_1),
            FadeOut(new_line_2),
            FadeOut(new_line_3),
            TransformMatchingTex(new_line_2.copy().set_opacity(0), new_line_1_rearranged, run_time=2, lag_ratio=0.5, rate_func=double_smooth,
            # key_map={
            #     "".join(e1e2_term): "".join(e1e2_term),
            #     "".join(e2e1_term): "".join(e2e1_term),
            #     "".join(e3e2_term): "".join(e3e2_term),
            #     "".join(e3e1_term): "".join(e3e1_term),
            #     "".join(e2e3_term): "".join(e2e3_term),
            #     "".join(e1e3_term): "".join(e1e3_term),
                
            #     a1: a1,
            #     a2: a2,
            #     a3: a3,
            #     b1: b1,
            #     b2: b2,
            #     b3: b3,
            # }
            ),
            TransformMatchingTex(new_line_3.copy().set_opacity(0), new_line_2_rearranged, run_time=2, lag_ratio=0.5, rate_func=double_smooth,
            # key_map={
            #     "".join(e1e2_term): "".join(e1e2_term),
            #     "".join(e2e1_term): "".join(e2e1_term),
            #     "".join(e3e2_term): "".join(e3e2_term),
            #     "".join(e3e1_term): "".join(e3e1_term),
            #     "".join(e2e3_term): "".join(e2e3_term),
            #     "".join(e1e3_term): "".join(e1e3_term),
                
            #     a1: a1,
            #     a2: a2,
            #     a3: a3,
            #     b1: b1,
            #     b2: b2,
            #     b3: b3,
            # }
            ),
            TransformMatchingTex(new_line_1.copy().set_opacity(0), new_line_3_rearranged, run_time=2, lag_ratio=0.5, rate_func=double_smooth,
            # key_map={
            #     "".join(e1e2_term): "".join(e1e2_term),
            #     "".join(e2e1_term): "".join(e2e1_term),
            #     "".join(e3e2_term): "".join(e3e2_term),
            #     "".join(e3e1_term): "".join(e3e1_term),
            #     "".join(e2e3_term): "".join(e2e3_term),
            #     "".join(e1e3_term): "".join(e1e3_term),
                
            #     a1: a1,
            #     a2: a2,
            #     a3: a3,
            #     b1: b1,
            #     b2: b2,
            #     b3: b3,
            # }
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Now, rearrange the terms, putting everything in the same order (e1 wedge e2), (e2 wedge e3) (e1 wedge e3)
        
        # e2e1_term_rev = [b1, e1, space, wedge, space, a2, e2]
        # e3e2_term_rev = [b2, e2, space, wedge, space, a3, e3]
        # e3e1_term_rev = [b1, e1, space, wedge, space, a3, e3]
        
        
        # new_line_1_reorder_wedge = Tex(equal, space, *e1e2_term, space, plus, space, *e2e1_term_rev)
        # new_line_2_reorder_wedge = Tex(plus, space, *e3e2_term_rev, space, plus, space, *e2e3_term)
        # new_line_3_reorder_wedge = Tex(plus, space, *e3e1_term_rev, space, plus, space, *e1e3_term)
        # new_group_lines_rearranged = VGroup(
        #     new_line_1_reorder_wedge,
        #     new_line_2_reorder_wedge,
        #     new_line_3_reorder_wedge
        # )
        # new_group_lines_rearranged.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5 + UP*1)
        # for line in [new_line_1_reorder_wedge, new_line_2_reorder_wedge, new_line_3_reorder_wedge]:
        #     line.set_color_by_tex_to_color_map(colormap_dict)
        
        

        
        # self.play(
            
        #     TransformMatchingTex(new_line_1_rearranged, new_line_1_reorder_wedge, run_time=2, path_arc=90*DEGREES, lag_ratio=0.1),
        #     TransformMatchingTex(new_line_2_rearranged, new_line_2_reorder_wedge, run_time=2, path_arc=90*DEGREES, lag_ratio=0.1),
        #     TransformMatchingTex(new_line_3_rearranged, new_line_3_reorder_wedge, run_time=2, path_arc=90*DEGREES, lag_ratio=0.1),
            
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        # * Put the scalars behind
        
        new_line_1_scalars = Tex(equal, space, 
                                 a1, b2, space, e1, space, wedge, space, e2,
                                 space, plus, space, 
                                    a2, b1, space, e2, space, wedge, space, e1,
                                    )
        new_line_2_scalars = Tex(plus, space, a3, b2, space, e3, space, wedge, space, e2,
                                 space, plus, space, 
                                    a2, b3, space, e2, space, wedge, space, e3,
                                    )
        new_line_3_scalars = Tex(plus, space, a3, b1, space, e3, space, wedge, space, e1,
                                 space, plus, space, 
                                    a1, b3, space, e1, space, wedge, space, e3,
                                    )
        new_group_lines_scalars = VGroup(
            new_line_1_scalars,
            new_line_2_scalars,
            new_line_3_scalars
        )
        new_group_lines_scalars.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5 + UP*1)
        for line in [new_line_1_scalars, new_line_2_scalars, new_line_3_scalars]:
            line.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformMatchingTex(new_line_1_rearranged, new_line_1_scalars, run_time=2, path_arc=90*DEGREES, lag_ratio=0.1, key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                wedge:wedge, plus:plus}),
            TransformMatchingTex(new_line_2_rearranged, new_line_2_scalars, run_time=2, path_arc=90*DEGREES, lag_ratio=0.1, key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                wedge:wedge, plus:plus}),
            TransformMatchingTex(new_line_3_rearranged, new_line_3_scalars, run_time=2, path_arc=90*DEGREES, lag_ratio=0.1, key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                wedge:wedge, plus:plus}),
            
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Flip the wedges
        # * _______________________________________________________________________
        minus = "-"

        new_line_1_flip_wedge = Tex(equal, space, 
                                 a1, b2, space, e1, space, wedge, space, e2,
                                 space, minus, space, 
                                    a2, b1, space, e1, space, wedge, space, e2,
                                    )
        new_line_2_flip_wedge = Tex(minus, space, a3, b2, space, e2, space, wedge, space, e3,
                                 space, plus, space, 
                                    a2, b3, space, e2, space, wedge, space, e3,
                                    )
        new_line_3_flip_wedge = Tex(minus, space, a3, b1, space, e1, space, wedge, space, e3,
                                 space, plus, space, 
                                    a1, b3, space, e1, space, wedge, space, e3,
                                    )
        new_group_lines_flip_wedge = VGroup(
            new_line_1_flip_wedge,
            new_line_2_flip_wedge,
            new_line_3_flip_wedge
        )
        new_group_lines_flip_wedge.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5 + UP*1)
        for line in [new_line_1_flip_wedge, new_line_2_flip_wedge, new_line_3_flip_wedge]:
            line.set_color_by_tex_to_color_map(colormap_dict)
        
        # # ! Cant be sophisticated
        # # self.play(
        # #     TransformMatchingTex(new_line_1_scalars, new_line_1_flip_wedge, run_time=3, path_arc=115*DEGREES, lag_ratio=0.1, key_map={wedge:wedge, plus:plus, e2:e1, e2:e1}),
        # #     TransformMatchingTex(new_line_2_scalars, new_line_2_flip_wedge, run_time=3, path_arc=115*DEGREES, lag_ratio=0.1, key_map={wedge:wedge, plus:plus, e2:e3, e3:e2}),
        # #     TransformMatchingTex(new_line_3_scalars, new_line_3_flip_wedge, run_time=3, path_arc=115*DEGREES, lag_ratio=0.1, key_map={wedge:wedge, plus:plus, e1:e3, e3:e1}),
            
            
        # )
        self.play(
            TransformMatchingTex(new_line_1_scalars, new_line_1_flip_wedge, run_time=2, path_arc=90*DEGREES,
            key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                wedge:wedge, plus:plus, minus:minus
            }
            ),
            TransformMatchingTex(new_line_2_scalars, new_line_2_flip_wedge, run_time=2, path_arc=90*DEGREES,
            key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                wedge:wedge, plus:plus, minus:minus
            }
            ),
            TransformMatchingTex(new_line_3_scalars, new_line_3_flip_wedge, run_time=2, path_arc=90*DEGREES,
            key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                wedge:wedge, plus:plus, minus:minus
            }
            ),
            
            
        )        
        # self.play(
        #     TransformMatchingShapes(new_line_1_scalars, new_line_1_flip_wedge, run_time=2, path_arc=115*DEGREES),
        #     TransformMatchingShapes(new_line_2_scalars, new_line_2_flip_wedge, run_time=2, path_arc=115*DEGREES),
        #     TransformMatchingShapes(new_line_3_scalars, new_line_3_flip_wedge, run_time=2, path_arc=115*DEGREES),
            
            
        # )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Group the terms
        # * _______________________________________________________________________
        
        new_line_1_flip_wedge_grouped = Tex(equal, space, 
                                    lbracket, a1, b2, space, minus, space, a2, b1, rbracket, 
                                    space, e1, space, wedge, space, e2,
                                    )
        new_line_2_flip_wedge_grouped = Tex(plus, space,
                                    lbracket, a2, b3, space, minus, space, a3, b2, rbracket,
                                    space, e2, space, wedge, space, e3,
                                    )
        new_line_3_flip_wedge_grouped = Tex(plus, space,
                                    lbracket, a1, b3, space, minus, space, a3, b1, rbracket,
                                    space, e1, space, wedge, space, e3,
                                    )
        

        new_group_lines_flip_wedge = VGroup(
            new_line_1_flip_wedge_grouped,
            new_line_2_flip_wedge_grouped,
            new_line_3_flip_wedge_grouped,
        )
        new_group_lines_flip_wedge.arrange(DOWN, buff=0.5).shift(RIGHT * 0.5 + UP*1)
        
        for line in [new_line_1_flip_wedge_grouped, new_line_2_flip_wedge_grouped, new_line_3_flip_wedge_grouped]:
            
            line.set_color_by_tex_to_color_map(colormap_dict)
        
        # ! Cant be sophisticated
        # self.play(
        #     TransformMatchingTex(new_line_1_scalars, new_line_1_flip_wedge, run_time=3, path_arc=115*DEGREES, lag_ratio=0.1, key_map={wedge:wedge, plus:plus, e2:e1, e2:e1}),
        #     TransformMatchingTex(new_line_2_scalars, new_line_2_flip_wedge, run_time=3, path_arc=115*DEGREES, lag_ratio=0.1, key_map={wedge:wedge, plus:plus, e2:e3, e3:e2}),
        #     TransformMatchingTex(new_line_3_scalars, new_line_3_flip_wedge, run_time=3, path_arc=115*DEGREES, lag_ratio=0.1, key_map={wedge:wedge, plus:plus, e1:e3, e3:e1}),
            
            
        # )
        
        self.play(
            TransformMatchingTex(new_line_1_flip_wedge, new_line_1_flip_wedge_grouped, 
                run_time=3, 
                path_arc=90*DEGREES,
                key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                minus:minus, plus:plus, wedge:wedge
            }),
            TransformMatchingTex(new_line_2_flip_wedge, new_line_2_flip_wedge_grouped, 
                run_time=3, 
                path_arc=90*DEGREES,
                key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                minus:minus, plus:plus, wedge:wedge
            }),
            TransformMatchingTex(new_line_3_flip_wedge, new_line_3_flip_wedge_grouped, 
                run_time=3, 
                path_arc=90*DEGREES,
                key_map={
                e1:e1, e2:e2, e3:e3, a1:a1, a2:a2, a3:a3, b1:b1, b2:b2, b3:b3,
                minus:minus, plus:plus, wedge:wedge
            }),
            
            # Also shift new_a_wedge_b up and to the right
            new_a_wedge_b.animate.shift(UP * 0.05 + RIGHT * 0.55),
            
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Do these terms remind you of anything?
        # Indicate
        self.play(
            
            FlashAround(new_line_1_flip_wedge_grouped[1:12], color=YELLOW, time_width=0.5, buff=0.2),
            FlashAround(new_line_2_flip_wedge_grouped[1:12], color=YELLOW, time_width=0.5, buff=0.2),
            FlashAround(new_line_3_flip_wedge_grouped[1:12], color=YELLOW, time_width=0.5, buff=0.2),
            
            run_time=2,
        )
        
        
        
        
        
        
        
        # * The e1 wedge e2 term 
        # * _______________________________________________________________________

        # Create a copy that spawns from the original
        e1_wedge_e2_copy = Tex(
            e1, space, wedge, space, e2,
        ).move_to(new_line_1_flip_wedge_grouped[-6:].get_center()).shift(UP * 0.5 + LEFT * 0.5).set_opacity(0)
        
        e1_wedge_e2_copy_2 = e1_wedge_e2_copy.copy().move_to(ORIGIN).to_edge(LEFT).shift(RIGHT*1+ DOWN*1).set_opacity(1)

        
        self.play(
            FocusOn(new_line_1_flip_wedge_grouped[-5:], remover=False),
            run_time=2,
        )
        
        self.play(
            TransformMatchingTex(e1_wedge_e2_copy, e1_wedge_e2_copy_2, 
                                 key_map={e1: e1, e2: e2, wedge: wedge},
                                 
                                 lag_ratio=0.3),
            run_time=2
        )
        
        # * The e2 wedge e3 term is = e1 e2
        e1_wedge_e2_geo_prod = Tex(e1, space, wedge, space, e2, space, equal, space, e1, e2)
        e1_wedge_e2_geo_prod.move_to(e1_wedge_e2_copy_2.get_center()).shift(RIGHT)

        self.play(
            TransformMatchingTex(e1_wedge_e2_copy_2, e1_wedge_e2_geo_prod, 
                                 key_map={e1: e1, e2: e2, wedge: wedge, equal: equal}),
            
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        e1_wedge_e2_geo_prod_extended = Tex(e1, space, wedge, space, e2, space, equal, space, e1, e2, e3, e3)
        # Color the e3 with Green
        e1_wedge_e2_geo_prod_extended.set_color_by_tex(e3, GREEN_C)
        e1_wedge_e2_geo_prod_extended.move_to(e1_wedge_e2_geo_prod.get_center()).shift(RIGHT*0.25)

                
        self.play(
            TransformMatchingTex(e1_wedge_e2_geo_prod, e1_wedge_e2_geo_prod_extended,
                                 key_map={e1: e1, e2: e2, wedge: wedge, equal: equal, },
                                 run_time=2,
                                 )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        e1_wedge_e2_geo_prod_extended_rearranged = Tex(e1, space, wedge, space, e2, space, equal, space,  e3, space, e1, e2, e3)
        # Color the e3 with Green
        e1_wedge_e2_geo_prod_extended_rearranged.set_color_by_tex(e3, GREEN_C)
        e1_wedge_e2_geo_prod_extended_rearranged.move_to(e1_wedge_e2_geo_prod_extended.get_center())
        
        # self.play(
        #     TransformMatchingShapes(e1_wedge_e2_geo_prod_extended, e1_wedge_e2_geo_prod_extended_rearranged, run_time=2, 
        #                             path_arc=90*DEGREES)
        # )
        self.play(
            TransformMatchingTex(e1_wedge_e2_geo_prod_extended, e1_wedge_e2_geo_prod_extended_rearranged, 
                                 key_map={e1: e1, e2: e2, wedge: wedge, equal: equal, e3: e3},
                                 run_time=2, 
                                 path_arc=90*DEGREES,
)
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        eps_123 = r"\epsilon_{123}"
        
        e1_wedge_e2_geo_prod_levi_civita = Tex(e1, space, wedge, space, e2, space, equal, space, eps_123,  e3, space, e1, e2, e3)
        # Color the e3 with Green
        e1_wedge_e2_geo_prod_levi_civita.set_color_by_tex(e3, GREEN_C)
        e1_wedge_e2_geo_prod_levi_civita.set_color_by_tex(eps_123, GREEN_C)
        e1_wedge_e2_geo_prod_levi_civita.move_to(e1_wedge_e2_geo_prod_extended_rearranged.get_center())
        
        self.play(
            TransformMatchingTex(e1_wedge_e2_geo_prod_extended_rearranged, e1_wedge_e2_geo_prod_levi_civita, 
                                 key_map={e1: e1, e2: e2, wedge: wedge, equal: equal, e3: e3},
                                 
                                 run_time=2,)
        )
        self.wait(NOMINAL_WAIT_TIME*2)
        
        # Bring back old result
        
        levi_civita_relation = Tex( e_i, space, "\\times", space,  e_j, space, equal, space, "\\epsilon_{ijk}", space, r"\mathbf{e}_k").scale(1)
        levi_civita_relation.to_edge(RIGHT).shift(LEFT*1+ DOWN*1)
        
        # Put a box around it
        box_levi_civita = Polygon(
            levi_civita_relation.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            levi_civita_relation.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            levi_civita_relation.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            levi_civita_relation.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

        )
        
        self.play(
            Write(levi_civita_relation),
            ShowCreation(box_levi_civita),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        I = r"\mathbf{e}_1 \mathbf{e}_2 \mathbf{e}_3"
        
        e1_wedge_e2_geo_prod_cross = Tex(e1, space, wedge, space, e2, space, equal, space,
                                               r"\left(" + e1 + "\\times" +  e2 + r"\right)", 
                                                space, I,
                                                isolate = [r"\left(" + e1 + "\\times" +  e2 + r"\right)"]
                                                )
        # Color the e3 with Green
        e1_wedge_e2_geo_prod_cross.set_color_by_tex(I, BLUE_B)
        e1_wedge_e2_geo_prod_cross.move_to(e1_wedge_e2_geo_prod_levi_civita.get_center())

        self.play(
            TransformMatchingTex(e1_wedge_e2_geo_prod_levi_civita, e1_wedge_e2_geo_prod_cross,
                                 key_map={e1: e1, e2: e2, wedge: wedge, equal: equal, e3: e3,
                                          eps_123: r"\left(" + e1 +   "\\times" + e2 + r"\right)",},
                                 run_time=2, 
                                 # path_arc=90*DEGREES
            )
        )
        
        # self.play(
        #     ReplacementTransform(e1_wedge_e2_geo_prod_levi_civita, e1_wedge_e2_geo_prod_cross, run_time=2)
        # )
        self.wait(NOMINAL_WAIT_TIME)
        
        # self.remove(e1_wedge_e2_geo_prod_levi_civita)
        
        self.play(
            FlashAround(e1_wedge_e2_geo_prod_cross[-6:], color=BLUE_D, time_width=0.5, buff=0.2),
            run_time=2,
        )
        
        
        pseudo_scalar = Tex(r"\mathbb{I}", space, equal, space, I)
        
        pseudo_scalar.move_to(box_levi_civita.get_center()).shift(DOWN*1.5)
        
        # Put a box around it
        box_pseudoscalar = Polygon(
            pseudo_scalar.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            pseudo_scalar.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            pseudo_scalar.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            pseudo_scalar.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

        )
        
        self.play(
            Write(pseudo_scalar),
            ShowCreation(box_pseudoscalar),
            run_time=2
        )
        
        e1_wedge_e2_geo_prod_I = Tex(e1, space, wedge, space, e2, space, equal, space,
                                               r"\left(" + e1 + "\\times" + e2 + r"\right)",
                                                space, "\\mathbb{I}")
        # Color the e3 with Green
        e1_wedge_e2_geo_prod_I.move_to(e1_wedge_e2_geo_prod_cross.get_center())
        
        self.play(
            TransformMatchingTex(e1_wedge_e2_geo_prod_cross, e1_wedge_e2_geo_prod_I,
                                 key_map={e1: e1, e2: e2, wedge: wedge, equal: equal, e3: e3,
                                r"\left(" + e1 + "\\times" + e2 + r"\right)": r"\left(" + e1 + "\\times" + e2 + r"\right)",
                                          },
                                 run_time=2,)
                                 # path_arc=90*DEGREES  
                                 
        )
        
        # self.play(
        #     ReplacementTransform(e1_wedge_e2_geo_prod_cross, e1_wedge_e2_geo_prod_I, run_time=2, lag_ratio=0.4,)
        # )
        self.wait(NOMINAL_WAIT_TIME)        

        # * Final Result
        surrounding_box_final_result = Polygon(
            e1_wedge_e2_geo_prod_I.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            e1_wedge_e2_geo_prod_I.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            e1_wedge_e2_geo_prod_I.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            e1_wedge_e2_geo_prod_I.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        
        self.play(
            ShowCreation(surrounding_box_final_result),
            FadeOut(box_levi_civita),
            FadeOut(box_pseudoscalar),
            FadeOut(levi_civita_relation),
            FadeOut(pseudo_scalar),
            run_time=2
        )
        
        # Move the final result to the center
        self.play(
            e1_wedge_e2_geo_prod_I.animate.move_to(ORIGIN + DOWN*1.5),
            surrounding_box_final_result.animate.move_to(ORIGIN + DOWN*1.5),
            run_time=2
        )
        
        
        
        
        # * Rewrite all wedges
        # * _______________________________________________________________________
        
        times = "\\times"
        
        new_line_1_flip_wedge_I = Tex(equal, space, 
                                    lbracket, a1, b2, space, minus, space, a2, b1, rbracket, 
                                    space,
                                    lbracket, e1, space, times, space, e2, rbracket,
                                    "\\mathbb{I}",
        )
        new_line_2_flip_wedge_I = Tex(plus, space,
                                    lbracket, a2, b3, space, minus, space, a3, b2, rbracket,
                                    space,
                                    lbracket, e2, space, times, space, e3, rbracket,
                                    "\\mathbb{I}",
        )
        new_line_3_flip_wedge_I = Tex(plus, space,
                                    lbracket, a1, b3, space, minus, space, a3, b1, rbracket,
                                    space,
                                    lbracket, e1, space, times, space, e3, rbracket,
                                    "\\mathbb{I}",
        )
        new_group_lines_flip_wedge_I = VGroup(
            new_line_1_flip_wedge_I,
            new_line_2_flip_wedge_I,
            new_line_3_flip_wedge_I,
        )
        new_group_lines_flip_wedge_I.arrange(DOWN, buff=0.5).shift(RIGHT * 0.8 + UP*1)
        for line in [new_line_1_flip_wedge_I, new_line_2_flip_wedge_I, new_line_3_flip_wedge_I]:
            line.set_color_by_tex_to_color_map(colormap_dict)

        self.play(
            ReplacementTransform(new_line_1_flip_wedge_grouped, new_line_1_flip_wedge_I, run_time=2, lag_ratio=0.05),
            ReplacementTransform(new_line_2_flip_wedge_grouped, new_line_2_flip_wedge_I, run_time=2, lag_ratio=0.05),
            ReplacementTransform(new_line_3_flip_wedge_grouped, new_line_3_flip_wedge_I, run_time=2, lag_ratio=0.05),
        )

        self.wait(NOMINAL_WAIT_TIME)
        
        # Do these terms remind you of anything?
        # Indicate
        
        self.play(
            FadeOut(surrounding_box_final_result),
            FadeOut(e1_wedge_e2_geo_prod_I),
            run_time=2
        )
        
        self.play(
            
            FlashAround(new_line_1_flip_wedge_I[-7:-2], color=YELLOW_B, time_width=0.5, buff=0.2),
            FlashAround(new_line_2_flip_wedge_I[-7:-2], color=YELLOW, time_width=1, buff=0.2, stroke_width=7),
            Indicate(new_line_2_flip_wedge_I[-7:-2], color=YELLOW, scale_factor=1.2),
            FlashAround(new_line_3_flip_wedge_I[-7:-2], color=YELLOW_B, time_width=0.5, buff=0.2),
            
            run_time=5,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Replace unit vectors cross product
        
        new_line_1_cross_vector = Tex(equal, space, 
                                    lbracket, a1, b2, space, minus, space, a2, b1, rbracket, 
                                    space, e3, space, "\\mathbb{I}")
        new_line_2_cross_vector = Tex(plus, space,
                                    lbracket, a2, b3, space, minus, space, a3, b2, rbracket,
                                    space, minus, e2, space, "\\mathbb{I}")
        new_line_3_cross_vector = Tex(plus, space,
                                    lbracket, a1, b3, space, minus, space, a3, b1, rbracket,
                                    space, e1, space, "\\mathbb{I}")
        
        new_group_lines_cross_vector = VGroup(
            new_line_1_cross_vector,
            new_line_2_cross_vector,
            new_line_3_cross_vector,
        )
        new_group_lines_cross_vector.arrange(DOWN, buff=0.5).shift(RIGHT * 1 + UP*1)
        for line in [new_line_1_cross_vector, new_line_2_cross_vector, new_line_3_cross_vector]:
            line.set_color_by_tex_to_color_map(colormap_dict)

        self.play(
            ReplacementTransform(new_line_1_flip_wedge_I, new_line_1_cross_vector, run_time=2, lag_ratio=0.05),
            ReplacementTransform(new_line_2_flip_wedge_I, new_line_2_cross_vector, run_time=2, lag_ratio=0.05),
            ReplacementTransform(new_line_3_flip_wedge_I, new_line_3_cross_vector, run_time=2, lag_ratio=0.05),
            # Move the entire group to the left
        )
        self.wait(0.5)

        self.play(
            new_group_lines_cross_vector.animate.shift(LEFT * 0.8),

        )

        self.wait(NOMINAL_WAIT_TIME)
        
        
        self.play(
            new_line_2_cross_vector[-2].animate.set_color(YELLOW),
            new_line_2_cross_vector[-3].animate.set_color(YELLOW),
            new_line_2_cross_vector[-4].animate.set_color(YELLOW),
            lag_ratio=0.1,
            rate_func=double_smooth,
            run_time=3
        )
        
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
        
        