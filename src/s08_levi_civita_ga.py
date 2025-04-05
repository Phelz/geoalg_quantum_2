from manim import *
# from manim.opengl import *
# from reactive_manim import *
import manimforge as mf
mf.setup()
# import definitions as dfs
from definitions import TITLE_FONTSIZE, NOMINAL_WAIT_TIME, PAUSE_WAIT_TIME


class _8_LeviCivitaGA(Scene):
    def construct(self):
        
        title = Tex(
            f'Geometric Algebra Definition', color=BLUE_D,
            font_size=TITLE_FONTSIZE
        ).to_edge(UP)
        
        self.play(Write(title), run_time=3)
        
        levi_cevita_ga_def = MathTex(
            "\\epsilon_{ijk}", "=", "\\mathbf{e}_i", "\\wedge", "\\mathbf{e}_j", "\\wedge", "\\mathbf{e}_k", "\\mathbb{I}^{\\dagger}",
            color=WHITE,
        ).to_edge(UP).shift(DOWN * 1)
        
        self.play(Write(levi_cevita_ga_def), run_time=3)
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            levi_cevita_ga_def.animate.to_edge(LEFT)
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Define the dagger
        pseudoscalar_dagger = MathTex("\\mathbb{I}^{\\dagger}", "=", "\\mathbf{e}_3", "\\wedge", "\\mathbf{e}_2", "\\wedge", "\\mathbf{e}_1", color=WHITE).next_to(levi_cevita_ga_def, RIGHT*12)
                                      
        self.play(
                  TransformMatchingTex(levi_cevita_ga_def.copy(), pseudoscalar_dagger),
                  run_time=3
                  )
        self.wait(NOMINAL_WAIT_TIME)
        


        pseudoscalar_dagger_outer_prod = MathTex("\\mathbb{I}^{\\dagger}", "=", "\\mathbf{e}_3", "\\mathbf{e}_2", "\\mathbf{e}_1", color=WHITE).next_to(levi_cevita_ga_def, RIGHT*15)
        self.play(
            Transform(pseudoscalar_dagger, pseudoscalar_dagger_outer_prod), 
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw the rectangle manually
        rect_corners = [
            pseudoscalar_dagger_outer_prod.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            pseudoscalar_dagger_outer_prod.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            pseudoscalar_dagger_outer_prod.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            pseudoscalar_dagger_outer_prod.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        ]
        
        pseudoscalar_dagger_box = Polygon(*rect_corners, color=WHITE)
        self.play(Create(pseudoscalar_dagger_box), run_time=2)
        self.wait(NOMINAL_WAIT_TIME)
        
        
        case1_tex = Tex(
            "Case 1: Same Indices",
            color=BLUE_C,
            font_size=45
        )
        case1_tex.next_to(levi_cevita_ga_def, DOWN*2.5).to_edge(LEFT)
        # Put a line underneath
        line = Line(
            start=case1_tex.get_left(),
            end=case1_tex.get_right(),
            color=BLUE_C,
            stroke_width=2
        ).shift(DOWN*0.5)
        self.play(Write(case1_tex), Create(line), run_time=2)
        self.wait(NOMINAL_WAIT_TIME)
        
        case_1_levi_civita = MathTex("\\epsilon_{112}", "=", "\\mathbf{e}_1",  "\\wedge", "\\mathbf{e}_1", "\\wedge", "\\mathbf{e}_2", "\\mathbb{I}^{\\dagger}", color=BLUE_B).next_to(case1_tex, DOWN*2).to_edge(LEFT).shift(RIGHT*0.25)
                                            
        self.play(
                  TransformMatchingTex(levi_cevita_ga_def.copy(), case_1_levi_civita),
                  run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # Indicate the e_1 \wedge e_1
        indicate_term = case_1_levi_civita[2:5]
        cross_around_term  = Cross(indicate_term, color=YELLOW, stroke_width=2)
        self.play(
            Indicate(indicate_term, rate_func=there_and_back),
            Create(cross_around_term),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Copy the indicate term and move it below
        case_1_levi_civita_final = MathTex(
            "\\epsilon_{112}", "=", "0",
            color=BLUE_B,
        ).next_to(case_1_levi_civita, DOWN*2).to_edge(LEFT).shift(RIGHT*0.25)
        self.play(
            TransformMatchingTex(case_1_levi_civita.copy(), case_1_levi_civita_final),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # Draw a box around the final result
        case_1_levi_civita_final_box_corners = [
            case_1_levi_civita_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            case_1_levi_civita_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            case_1_levi_civita_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            case_1_levi_civita_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        ]
        case_1_levi_civita_final_box = Polygon(*case_1_levi_civita_final_box_corners, color=BLUE_B)
        self.play(
            Create(case_1_levi_civita_final_box),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * ______________________________________________________________________
        
        # Case 2: Cyclic Permutations
        case2_tex = Tex(
            "Case 2: Cyclic Permutations",
            color=BLUE_C,
            font_size=45
        )
        case2_tex.move_to(case1_tex.get_center()).shift(RIGHT*7)
        
        # Put a line underneath
        line2 = Line(
            start=case2_tex.get_left(),
            end=case2_tex.get_right(),
            color=BLUE_C,
            stroke_width=2
        ).shift(DOWN*0.5)
        self.play(Write(case2_tex), Create(line2), run_time=2)
        self.wait(NOMINAL_WAIT_TIME)
        
        case_2_levi_civita = MathTex("\\epsilon_{123}", "=", "\\mathbf{e}_1", "\\wedge", "\\mathbf{e}_2", "\\wedge", "\\mathbf{e}_3", "\\mathbb{I}^{\\dagger}", color=BLUE_B).next_to(case2_tex, DOWN*2)
        self.play(
            TransformMatchingTex(levi_cevita_ga_def.copy(), case_2_levi_civita),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        case_2_levi_civita_pseudo = MathTex("\\epsilon_{123}", "=", "\\mathbf{e}_1", "\\wedge", "\\mathbf{e}_2", "\\wedge", "\\mathbf{e}_3", 
        "\\mathbf{e}_3",  "\\mathbf{e}_2",  "\\mathbf{e}_1",
                                            color=BLUE_B).next_to(case2_tex, DOWN*2)
        

        
        self.play(
            Transform(case_2_levi_civita, case_2_levi_civita_pseudo),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        case_2_levi_civita_pseudo_2 = MathTex("\\epsilon_{123}", "=", "\\mathbf{e}_1", "\\mathbf{e}_2", "\\mathbf{e}_3", "\\mathbf{e}_3",  "\\mathbf{e}_2",  "\\mathbf{e}_1",
                                            color=BLUE_B).next_to(case_2_levi_civita_pseudo, DOWN*2)
        
        self.play(
            TransformMatchingTex(case_2_levi_civita_pseudo.copy(), case_2_levi_civita_pseudo_2),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Indicate the e_3 \e_3 term
        indicate_term_case_2 = case_2_levi_civita_pseudo_2[4:6]
        self.play(
            Indicate(indicate_term_case_2, rate_func=there_and_back, run_time=3),
            run_time=3
        ) 
        self.wait(NOMINAL_WAIT_TIME)
        
        
        case_2_levi_civita_pseudo_3 = MathTex("\\epsilon_{123}", "=", "\\mathbf{e}_1", "\\mathbf{e}_2",  "\\mathbf{e}_2",  "\\mathbf{e}_1",
                                            color=BLUE_B).next_to(case_2_levi_civita_pseudo_2, DOWN*2)
        
        self.play(
            TransformMatchingTex(case_2_levi_civita_pseudo_2.copy(), case_2_levi_civita_pseudo_3),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # indicate the e_2 \e_2 term
        indicate_term_case_2_2 = case_2_levi_civita_pseudo_3[3:5]
        self.play(
            Indicate(indicate_term_case_2_2, rate_func=there_and_back, run_time=3),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        case_2_levi_civita_pseudo_final = MathTex("\\epsilon_{123}", "=", "1",
                                            color=BLUE_B).next_to(case_2_levi_civita_pseudo_3, DOWN*2)
        self.play(
            TransformMatchingTex(case_2_levi_civita_pseudo_3.copy(), case_2_levi_civita_pseudo_final),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw a box around the final result
        case_2_levi_civita_pseudo_final_box_corners = [
            case_2_levi_civita_pseudo_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            case_2_levi_civita_pseudo_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            case_2_levi_civita_pseudo_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            case_2_levi_civita_pseudo_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        ]
        case_2_levi_civita_pseudo_final_box = Polygon(*case_2_levi_civita_pseudo_final_box_corners, color=BLUE_B)
        self.play(
            Create(case_2_levi_civita_pseudo_final_box),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)  
        
        # Now fadeout everything for case 1
        case_1_mobs = [
            case_1_levi_civita,
            case_1_levi_civita_final,
            case_1_levi_civita_final_box,
            cross_around_term,
            case1_tex,
            line
        ]
        self.play(
            *[FadeOut(mob) for mob in case_1_mobs],
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # Move everything for case 2 to the left edge + RIGHT * 0.25
        case_2_mobs = [
            case_2_levi_civita_pseudo_final,
            case_2_levi_civita_pseudo_2,
            case_2_levi_civita_pseudo_3,
            case_2_levi_civita,
            case2_tex,
            line2,
        ]
        self.play(
            *[mob.animate.to_edge(LEFT).shift(RIGHT*0.2) for mob in case_2_mobs],
            case_2_levi_civita_pseudo_final_box.animate.to_edge(LEFT),
            
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Case 3: Anti-Cyclic Permutations
        case3_tex = Tex(
            "Case 3: Anti-Cyclic Permutations",
            color=BLUE_C,
            font_size=45
        )
        case3_tex.move_to(case2_tex.get_center()).shift(RIGHT*6.9)
        self.play(Write(case3_tex), Create(line2), run_time=2)
        self.wait(NOMINAL_WAIT_TIME)
        
        # Put a line underneath
        line3 = Line(
            start=case3_tex.get_left(),
            end=case3_tex.get_right(),
            color=BLUE_C,
            stroke_width=2
        ).shift(DOWN*0.5)
        self.play(Write(case3_tex), Create(line3), run_time=2)
        self.wait(NOMINAL_WAIT_TIME)
        
        case_3_levi_civita = MathTex("\\epsilon_{132}", "=", "\\mathbf{e}_1", "\\wedge", "\\mathbf{e}_3", "\\wedge", "\\mathbf{e}_2", "\\mathbb{I}^{\\dagger}", color=BLUE_B).next_to(case3_tex, DOWN*2)
        self.play(
            TransformMatchingTex(levi_cevita_ga_def.copy(), case_3_levi_civita),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        case_3_levi_civita_pseudo = MathTex("\\epsilon_{132}", "=", "\\mathbf{e}_1", "\\wedge", "\\mathbf{e}_3", "\\wedge", "\\mathbf{e}_2",
        "\\mathbf{e}_3",  "\\mathbf{e}_2",  "\\mathbf{e}_1",
                                            color=BLUE_B).next_to(case3_tex, DOWN*2)
        self.play(
            TransformMatchingTex(case_3_levi_civita, case_3_levi_civita_pseudo),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        case_3_levi_civita_pseudo_2 = MathTex("\\epsilon_{132}", "=", "\\mathbf{e}_1", "\\mathbf{e}_3", "\\mathbf{e}_2", "\\mathbf{e}_3",  "\\mathbf{e}_2",  "\\mathbf{e}_1",
                                            color=BLUE_B).next_to(case_3_levi_civita_pseudo, DOWN*2)
        self.play(
            TransformMatchingTex(case_3_levi_civita_pseudo.copy(), case_3_levi_civita_pseudo_2),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # Indicate the e_2 e_3 term
        indicate_term_case_3 = case_3_levi_civita_pseudo_2[4:6]
        self.play(
            Indicate(indicate_term_case_3, rate_func=there_and_back, run_time=3),
            run_time=3
        ) 
        self.wait(NOMINAL_WAIT_TIME)
               
        
        # Swap those terms
        case_3_levi_civita_pseudo_3 = MathTex("\\epsilon_{132}", "=","-", "\\mathbf{e}_1", "\\mathbf{e}_2", "\\mathbf{e}_3", "\\mathbf{e}_3",  "\\mathbf{e}_2",  "\\mathbf{e}_1",
                                            color=BLUE_B).next_to(case_3_levi_civita_pseudo_2, DOWN*2)
        self.play(
            TransformMatchingTex(case_3_levi_civita_pseudo_2.copy(), case_3_levi_civita_pseudo_3),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Indicate the e_3 e_3 term
        indicate_term_case_3_2 = case_3_levi_civita_pseudo_3[5:7]
        self.play(
            Indicate(indicate_term_case_3_2, rate_func=there_and_back, run_time=3),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        case_3_levi_civita_pseudo_final = MathTex("\\epsilon_{132}", "=", "-1",
                                            color=BLUE_B).next_to(case_3_levi_civita_pseudo_3, DOWN*2)
        self.play(
            TransformMatchingTex(case_3_levi_civita_pseudo_3.copy(), case_3_levi_civita_pseudo_final),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Draw a box around the final result
        case_3_levi_civita_pseudo_final_box_corners = [
            case_3_levi_civita_pseudo_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            case_3_levi_civita_pseudo_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            case_3_levi_civita_pseudo_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            case_3_levi_civita_pseudo_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        ]
        case_3_levi_civita_pseudo_final_box = Polygon(*case_3_levi_civita_pseudo_final_box_corners, color=BLUE_B)
        self.play(
            Create(case_3_levi_civita_pseudo_final_box),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # self.wait(NOMINAL_WAIT_TIME)

        # Fade out everything
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)        









