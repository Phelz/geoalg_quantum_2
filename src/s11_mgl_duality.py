from manimlib import *
from src.definitions import *

COLORMAP_DICT = {"A": RED, "B": BLUE}


class _11_Duality(Scene):
    def construct(self):

        A_term = "A"
        B_term = "B"
        times = "\\times"
        equal = "="; plus = "+"; wedge = r"\wedge"; space = " \ "; minus = "-"
        
        lbracket = "("
        rbracket = ")"
        
        pseudoscalar_dagger = r"\mathbb{I}^\dagger"
        pseudoscalar = r"\mathbb{I}"
        e1 = "\\mathbf{e_1}"
        e2 = "\\mathbf{e_2}"
        e3 = "\\mathbf{e_3}"
        
        color_dict_3d = {
            e1: RED_B,
            e2: BLUE_B,
            e3: GREEN_B,
        }

        final_formula = Tex(A_term, space, wedge, space, B_term, space, equal, space,
                           lbracket, A_term, space, times, space, B_term, rbracket, space,
                           '\\mathbb{I}')
        
        final_formula.fix_in_frame()
        
        final_formula.set_color_by_tex_to_color_map(COLORMAP_DICT)

        final_formula_box = Polygon(
            final_formula.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            final_formula.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            final_formula.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            final_formula.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        
        final_formula.to_corner(UL).shift(DOWN*0.25+ RIGHT*0.25),
        final_formula_box.to_corner(UL)
        
        final_formula_box.fix_in_frame()
        self.add(
            final_formula_box,
            final_formula
        )
        
        # * ________________________________________________________________________
        
        # * What about in 2D
        
        question = Tex(
            "What \ about \ in \ 2D?",
            color=WHITE,
            font_size=int(3 * TITLE_FONTSIZE / 3)
        ).move_to(final_formula.get_center()).shift(DOWN * 1)
        question.fix_in_frame()
        
        question_2 = Tex(
            r"What", space, "is", space,  "perpindicular", space, "to", space, e1,  "?"
        ).move_to(question.get_center()).shift(DOWN * 1).to_edge(LEFT).shift(RIGHT * 0.4).set_color_by_tex_to_color_map(color_dict_3d)
        question_2.fix_in_frame()
        
        self.play(
            Write(question),
            run_time=2
        )
        self.play(
            Write(question_2),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        

        
        dual_to_e1 = Tex(
            e2, 
            color=WHITE,
        ).set_color_by_tex_to_color_map(color_dict_3d).move_to(question_2.get_center()).shift(DOWN * 1.5)
        
        self.play(
            Write(dual_to_e1),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        dual_to_e1_iter_1 = Tex(
            e2, space, equal, space, e2, space, "1").set_color_by_tex_to_color_map(color_dict_3d).move_to(dual_to_e1.get_center())
        self.play(
            TransformMatchingTex(dual_to_e1, dual_to_e1_iter_1),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)    
        
        dual_to_e1_iter_2 = Tex(
            e2, space, equal, space, e2, space, e1, e1).set_color_by_tex_to_color_map(color_dict_3d).move_to(dual_to_e1.get_center())
        
        self.play(
            TransformMatchingTex(dual_to_e1_iter_1, dual_to_e1_iter_2,
                                 key_map={"1": e1, }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        dual_to_e1_iter_3 = Tex(
            e2, space, equal, space, minus, space, e1, space, e2, space, e1).set_color_by_tex_to_color_map(color_dict_3d).move_to(dual_to_e1.get_center())
        self.play(
            TransformMatchingTex(dual_to_e1_iter_2, dual_to_e1_iter_3,
                                    key_map={e1: e1, e2: e2}),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        dual_to_e1_iter_4 = Tex(
            e2, space, equal, space, e1, space, e1, e2).set_color_by_tex_to_color_map(color_dict_3d).move_to(dual_to_e1.get_center())
        self.play(
            TransformMatchingTex(dual_to_e1_iter_3, dual_to_e1_iter_4,
                                    key_map={e1: e1, e2: e2}),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw a brance under the final e1 e2
        dual_to_e1_iter_4_brace_label = BraceLabel(
            dual_to_e1_iter_4[-4:], 
            pseudoscalar,
            color=WHITE,
        )
        self.play(
            Write(dual_to_e1_iter_4_brace_label),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * WHAT  ABOUT e2
        # * ________________________________________________________________________
        
        question_3 = Tex(
            "What",  space, "about", space,  e2, "?"
        ).shift(UP*3.5 + RIGHT*4).set_color_by_tex_to_color_map(color_dict_3d)
        question_2.fix_in_frame()
        
        # Draw a line down the middle of the screen (verical)
        line = Line(
            ORIGIN + RIGHT + UP*3,
            ORIGIN + RIGHT + DOWN*3,
            color=WHITE,
            stroke_width=1
        )
        
        self.play(
            TransformFromCopy(question_2, question_3),
            run_time=2
        )
        self.play(
            ShowCreation(line),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)

        dual_to_e1_iter_5 = Tex(
            e2, space, equal, space, e1, space, pseudoscalar).move_to(question_3.get_center()).shift(DOWN * 1).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformFromCopy(dual_to_e1_iter_4, dual_to_e1_iter_5),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Multiply by pseudoscalar on the right on both sides
        dual_to_e1_iter_6 = Tex(
            e2, space, pseudoscalar, space, equal, space, e1, space, pseudoscalar, pseudoscalar).move_to(dual_to_e1_iter_5.get_center()).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformMatchingTex(dual_to_e1_iter_5, dual_to_e1_iter_6,
                                 key_map={e1: e1, e2: e2, equal: equal}),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        pseudoscalar_squared = r"\mathbb{I}^2"
        
        dual_to_e1_iter_7 = Tex(
            e2, space, pseudoscalar, space, equal, space, e1, space, pseudoscalar_squared).move_to(dual_to_e1_iter_5.get_center()).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformMatchingTex(dual_to_e1_iter_6, dual_to_e1_iter_7,
                                 key_map={e1: e1, e2: e2, equal: equal,
                                          }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw a horizontal line right under dual_to_e1_iter_7
        line = Line(
            dual_to_e1_iter_7.get_bottom() + DOWN*0.5 + LEFT*2,
            dual_to_e1_iter_7.get_bottom() + DOWN*0.5 + RIGHT*2,
            color=WHITE,
            stroke_width=1
        )
        self.play(
            ShowCreation(line),
            run_time=2
        )
        
        pseudo_squared_to_minus_1_a = Tex(
            pseudoscalar_squared, space, equal, space, 
            lbracket, e1, e2, ")^2").move_to(dual_to_e1_iter_7.get_center()).shift(DOWN * 1.5 + LEFT*0.25).set_color_by_tex_to_color_map(color_dict_3d)
        
        self.play(
            Write(pseudo_squared_to_minus_1_a),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        pseudo_squared_to_minus_1_b = Tex(
            equal, space,
            e1, e2, space, e1, e2).move_to(pseudo_squared_to_minus_1_a.get_center()).shift(DOWN * 0.75 + 0.55*RIGHT).set_color_by_tex_to_color_map(color_dict_3d)
        
        self.play(
            TransformMatchingTex(pseudo_squared_to_minus_1_a.copy(),
                        pseudo_squared_to_minus_1_b,
                                    key_map={e1: e1, e2: e2, equal: equal,
                                             pseudoscalar_squared: equal
                                             }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        pseudo_squared_to_minus_1_c = Tex(
            equal, space,
            minus, space, e2, e1, space, e1, e2).move_to(pseudo_squared_to_minus_1_b.get_center()).shift(DOWN * 0.75 + 0.275*RIGHT).set_color_by_tex_to_color_map(color_dict_3d)
        
        self.play(
            TransformMatchingTex(pseudo_squared_to_minus_1_b.copy(),
                        pseudo_squared_to_minus_1_c,
                                    key_map={e1: e1, e2: e2, equal: equal,
                                             
                                             }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # The e1 e1 cancels out
        pseudo_squared_to_minus_1_d = Tex(
            equal, space,
            minus, space, e2,e2).move_to(pseudo_squared_to_minus_1_c.get_center()).shift(DOWN * 0.75 + 0.6*LEFT).set_color_by_tex_to_color_map(color_dict_3d)
        
        self.play(
            TransformMatchingTex(pseudo_squared_to_minus_1_c.copy(),
                        pseudo_squared_to_minus_1_d,
                                    key_map={e1: e1, e2: e2, equal: equal,
                                             }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        pseudo_squared_to_minus_final = Tex(
            pseudoscalar_squared, space,
            equal, space, minus, "1").move_to(pseudo_squared_to_minus_1_a.get_center()).shift(DOWN * 0.75*4.1).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformMatchingTex(pseudo_squared_to_minus_1_d.copy(),
                        pseudo_squared_to_minus_final,
                                    key_map={ e2: "1", equal: equal,
                                             }),
            run_time=2
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        # Put a box around the final formula
        pseudo_squared_to_minus_final_box = Polygon(
            pseudo_squared_to_minus_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            pseudo_squared_to_minus_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            pseudo_squared_to_minus_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            pseudo_squared_to_minus_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        pseudo_squared_to_minus_final_box.set_color(WHITE)
        pseudo_squared_to_minus_final_box.fix_in_frame()
        
        self.play(
            Write(pseudo_squared_to_minus_final_box),
            run_time=2
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        # Fade out a, b, ... but only keep the final formula
        self.play(
            FadeOut(pseudo_squared_to_minus_1_a),
            FadeOut(pseudo_squared_to_minus_1_b),
            FadeOut(pseudo_squared_to_minus_1_c),
            FadeOut(pseudo_squared_to_minus_1_d),
            pseudo_squared_to_minus_final_box.animate.shift(UP*2.9 + RIGHT*0.25),
            pseudo_squared_to_minus_final.animate.shift(UP*2.9 + RIGHT*0.25),
            run_time=2    
        )
        
        # Draw a line under the final formula
        line = Line(
            pseudo_squared_to_minus_final_box.get_bottom() + DOWN*0.5 + LEFT*2,
            pseudo_squared_to_minus_final_box.get_bottom() + DOWN*0.5 + RIGHT*2,
            color=WHITE,
            stroke_width=1
        )
        self.play(
            ShowCreation(line),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Now the dual to e2 is - e1
        dual_to_e2 = Tex(
            e2,space, pseudoscalar, space, equal, space, minus, e1).move_to(pseudo_squared_to_minus_final.get_center()).shift(DOWN * 1.5).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformMatchingTex(dual_to_e1_iter_7.copy(), dual_to_e2,
                                 key_map={e1: e1, e2: e2, equal: equal,
                                        #   space:space,
                                          pseudoscalar: pseudoscalar,
                                        #   pseudoscalar_squared: minus
                                          }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        dual_to_e2_iter_1 = Tex(
            e2,space, lbracket, e1, e2, rbracket, space, equal, space, minus, e1).move_to(dual_to_e2.get_center()).shift(DOWN * 0.75 + LEFT*0.6).set_color_by_tex_to_color_map(color_dict_3d)

        self.play(
            TransformFromCopy(dual_to_e2, dual_to_e2_iter_1),
            run_time=2)

        self.wait(NOMINAL_WAIT_TIME)
        
        dual_to_e2_iter_2 = Tex(
            minus, e2, e2, e1, space, equal, space, minus, e1).move_to(dual_to_e2_iter_1.get_center()).shift(DOWN * 0.75 + RIGHT*0.1).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformMatchingTex(dual_to_e2_iter_1.copy(), dual_to_e2_iter_2,
                                 key_map={e1: e1, e2: e2, equal: equal,
                                        #   minus: minus,
                                          }),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Put a brace under the e2 e1 and call it pseudoscalar_dagger
        dual_to_e2_iter_2_brace_label = BraceLabel(
            dual_to_e2_iter_2[3:7],
            pseudoscalar_dagger,
            color=WHITE,
        )
        self.play(
            Write(dual_to_e2_iter_2_brace_label),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)

        # Now the final formula is
        dual_to_e2_final = Tex(
            e2, space, pseudoscalar_dagger, space, equal, space, e1).move_to(dual_to_e2_iter_2.get_center()).set_color_by_tex_to_color_map(color_dict_3d)
        
        self.play(
            TransformMatchingTex(dual_to_e2_iter_2, dual_to_e2_final,
                                 key_map={e1: e1, e2: e2, equal: equal,
                                          }),
            
            # Fade away the brace and the label
            FadeOut(dual_to_e2_iter_2_brace_label),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Flip the order about the equal sign
        dual_to_e2_final_flipped = Tex(
            e1, space, equal, space, e2, space, pseudoscalar_dagger).move_to(dual_to_e2_final.get_center()).shift(DOWN*0.5 + RIGHT*0.5).set_color_by_tex_to_color_map(color_dict_3d)
        self.play(
            TransformMatchingTex(dual_to_e2_final, dual_to_e2_final_flipped,
                                 key_map={e1: e1, e2: e2, equal: equal,
                                          }),
            run_time=2,
        )
        # Put a box around the final formula
        dual_to_e2_final_flipped_box = Polygon(
            dual_to_e2_final_flipped.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            dual_to_e2_final_flipped.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            dual_to_e2_final_flipped.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            dual_to_e2_final_flipped.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        dual_to_e2_final_flipped_box.set_color(WHITE)
        dual_to_e2_final_flipped_box.fix_in_frame()
        self.play(
            ShowCreation(dual_to_e2_final_flipped_box),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Now bring that to the left, and Fadeout the original brace, and also transform the final formula for dual to e1
        
        dual_to_e1_final = Tex(
            e2, space, equal, space, e1, space, pseudoscalar).move_to(dual_to_e1_iter_4.get_center()).set_color_by_tex_to_color_map(color_dict_3d)
        

        
        self.play(
            FadeOut(dual_to_e1_iter_4_brace_label),
            TransformMatchingTex(dual_to_e1_iter_4, dual_to_e1_final,
                                 key_map={e1: e1, e2: e2, equal: equal,
                                          }),
        )
        self.play(
            dual_to_e1_final.animate.shift(UP*0.25),
            run_time=2
        )
        
                # Draw  a box around the dual to e1 final
        dual_to_e1_final_box = Polygon(
            dual_to_e1_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            dual_to_e1_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            dual_to_e1_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            dual_to_e1_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        dual_to_e1_final_box.set_color(WHITE)
        dual_to_e1_final_box.fix_in_frame()
        
        self.play(
            ShowCreation(dual_to_e1_final_box),
            run_time=2
        )
        
        self.play(
            dual_to_e2_final_flipped_box.animate.move_to(dual_to_e1_final_box.get_center()).shift(DOWN*1.5),
            dual_to_e2_final_flipped.animate.move_to(dual_to_e1_final_box.get_center()).shift(DOWN*1.5),
            
            run_time=2
        )
        
        # Fade out everyting on the right side
        # self.play(
        #     FadeOut(dual_to_e1_iter_5),
        #     FadeOut(dual_to_e1_iter_6),
        #     FadeOut(dual_to_e1_iter_7),
        #     FadeOut(pseudo_squared_to_minus_final),
        #     FadeOut(pseudo_squared_to_minus_final_box),
        #     # FadeOut(dual_to_e2_iter_1),
        #     FadeOut(dual_to_e2_iter_2),
        #     FadeOut(question_3),
        #     FadeOut(question),
        #     FadeOut(question_2),
        #     FadeOut(line),
        #     FadeOut
            
            
        )
        
                # # * Title
        # title = Title(
        #     f'Duality', include_underline=True, 
        #     match_underline_width_to_text=True,
        #     font_size=TITLE_FONTSIZE*1.5,)
        # title.to_corner(UL)
        # title.set_color(BLUE_D)
        # title.fix_in_frame()
        # self.play(
        #     Write(title),
        #     run_time=3,
        # )
        # self.wait(NOMINAL_WAIT_TIME)