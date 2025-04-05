from manimlib import *
from src.definitions import *


class _13B_EvenSubalgebra(Scene):
    def construct(self):
        
        # * Symbols
        
        lbracket = "("; rbracket = ")"
        lbracket_set = r"\{"; rbracket_set = r"\}"
        
        plus = "+"; minus = "-"; equal = "="; 
        space = r" \ "; comma = r","
        
        dot = r"\cdot"; wedge = r"\wedge"
        
        def_symb = r"\equiv"
        
        gamma_0 = r"\mathbf{\gamma_0}"
        gamma_1 = r"\mathbf{\gamma_1}"
        gamma_2 = r"\mathbf{\gamma_2}"
        gamma_3 = r"\mathbf{\gamma_3}"
        
        gamma_i = r"\mathbf{\gamma_i}"
        gamma_j = r"\mathbf{\gamma_j}"
        
        sigma_1 = r"\mathbf{\sigma_1}"
        sigma_2 = r"\mathbf{\sigma_2}"
        sigma_3 = r"\mathbf{\sigma_3}"

        sigma_i = r"\mathbf{\sigma_i}"
        sigma_j = r"\mathbf{\sigma_j}"
        sigma_k = r"\mathbf{\sigma_k}"
        
        pseudoscalar = r"\mathbb{I}"
        pseudoscalar_dagger = r"\mathbb{I}^\dagger"
        
        eps_ijk = r"\epsilon_{ijk}"

        color_dict = {
            sigma_1: RED,
            sigma_2: BLUE,
            sigma_3: GREEN,
        }
        
        # * Title
        title = Title(
            "The Even Subalgebra",
            stroke_color=BLUE_D,
            include_underline=True,
            match_underline_width_to_text=True,
            underline_style=dict(stroke_width=3, stroke_color=WHITE),
        ).to_corner(UL).set_color(BLUE_D)
        
        
        self.play(Write(title))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Basisc vectors set
        basis_set = Tex(
            lbracket_set,
            gamma_0, comma,
            space,
            gamma_1, comma,
            space,
            gamma_2, comma,
            space,
            gamma_3, rbracket_set
        ).move_to(title.get_center() + DOWN*1.25).to_edge(LEFT)
        
        self.play(Write(basis_set))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Bivector generators, the set gamma_i gamma_0 and gamma_i gamma_j
        sigma_set = Tex(
            lbracket_set,
            gamma_i, gamma_0, 
            rbracket_set)
        sigma_set.move_to(basis_set.get_center()).shift(RIGHT*5)
        
        other_set = Tex(
            lbracket_set,
            gamma_i, gamma_j, 
            rbracket_set)
        other_set.move_to(sigma_set.get_center()).shift(RIGHT*3)
        
        self.play(Write(sigma_set))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(other_set))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Focusing on the sigma set, Indicate and add sigma_i
        
        sigma_i_tex = Tex(
            sigma_i, space, def_symb, space, space
        ).next_to(sigma_set, LEFT, aligned_edge=DOWN)
        
        self.play(FadeIn(sigma_i_tex))
        self.play(
            Indicate(sigma_set, scale_factor=1.2),
            Indicate(sigma_i_tex, scale_factor=1.2),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Generating Scalars: Unitarity
        
        scalars_text = Tex(
            r"\text{Scalars:}",
        ).move_to(basis_set.get_center()).shift(DOWN).to_edge(LEFT)
        
        sigma_i_squared = Tex(
            sigma_i, "^2")
        sigma_i_squared.next_to(scalars_text, RIGHT, aligned_edge=DOWN).shift(RIGHT + DOWN*0.1)
        
        self.play(Write(scalars_text))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(sigma_i_squared))
        self.wait(NOMINAL_WAIT_TIME)
        
        sigma_i_squared_expanded_1 = Tex(
            sigma_i + "^2", space, equal, space,
            sigma_i, sigma_i)
        sigma_i_squared_expanded_1.move_to(sigma_i_squared.get_center()).shift(RIGHT*0.75)
        
        self.play(
            TransformMatchingTex(
                sigma_i_squared,
                sigma_i_squared_expanded_1,
                key_map={
                    sigma_i: sigma_i,
                }
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        sigma_i_squared_expanded_2 = Tex(
            sigma_i, "^2", 
            space, equal, space,
            sigma_i, sigma_i, 
            space, equal, space,
            gamma_i, gamma_0,space,
            gamma_i, gamma_0)
        sigma_i_squared_expanded_2.move_to(sigma_i_squared_expanded_1.get_center()).shift(RIGHT*1.25)
        
        self.play(
            TransformMatchingTex(
                sigma_i_squared_expanded_1,
                sigma_i_squared_expanded_2,
                key_map={
                    sigma_i: sigma_i,
                }
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        sigma_i_squared_expanded_3 = Tex(
            sigma_i, "^2", 
            space, equal, space,
            sigma_i, sigma_i, 
            space, equal, space,
            minus, gamma_0, gamma_i, space,
            gamma_i, gamma_0)
        
        sigma_i_squared_expanded_3.move_to(sigma_i_squared_expanded_2.get_center())
        self.play(
            TransformMatchingTex(
                sigma_i_squared_expanded_2,
                sigma_i_squared_expanded_3,
                key_map={
                    gamma_i: gamma_i,
                    gamma_0: gamma_0,
                    sigma_i: sigma_i,
                    # sigma_i_squared: sigma_i_squared,
                    equal: equal,
                },
                path_arc=PI/2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
                
        sigma_i_squared_expanded_4 = Tex(
            sigma_i, "^2", 
            space, equal, space,
            sigma_i, sigma_i, 
            space, equal, space,
            minus, gamma_0,
            lbracket, "-1", rbracket, gamma_0)
        
        sigma_i_squared_expanded_4.move_to(sigma_i_squared_expanded_3.get_center())
        self.play(
            TransformMatchingTex(
                sigma_i_squared_expanded_3,
                sigma_i_squared_expanded_4,
                key_map={
                    gamma_i: gamma_i,
                    gamma_0: gamma_0,
                    sigma_i: sigma_i,
                    # sigma_i_squared: sigma_i_squared,
                    equal: equal,
                    minus: minus,
                },
                # path_arc=PI/2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        sigma_i_squared_expanded_5 = Tex(
            sigma_i, "^2", 
            space, equal, space,
            sigma_i, sigma_i, 
            space, equal, space,
            gamma_0, gamma_0)
        
        sigma_i_squared_expanded_5.move_to(sigma_i_squared_expanded_4.get_center())
        self.play(
            TransformMatchingTex(
                sigma_i_squared_expanded_4,
                sigma_i_squared_expanded_5,
                key_map={
                    gamma_i: gamma_i,
                    gamma_0: gamma_0,
                    sigma_i: sigma_i,
                    # sigma_i_squared: sigma_i_squared,
                    equal: equal,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        sigma_i_squared_final = Tex(
            sigma_i, "^2", 
            space, equal, space,
            sigma_i, sigma_i, 
            space, equal, space,
            "1")
        
        sigma_i_squared_final.move_to(sigma_i_squared_expanded_5.get_center())
        self.play(
            TransformMatchingTex(
                sigma_i_squared_expanded_5,
                sigma_i_squared_final,
                key_map={
                    gamma_i: gamma_i,
                    gamma_0: "1",
                    sigma_i: sigma_i,
                    # sigma_i_squared: sigma_i_squared,
                    equal: equal,
                },
            )
        )
        
        # * Box the unitarity result
        sigma_i_squared_final_box = Polygon(
            sigma_i_squared_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            sigma_i_squared_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            sigma_i_squared_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            sigma_i_squared_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        sigma_i_squared_final_box.set_color(WHITE)
        self.play(ShowCreation(sigma_i_squared_final_box))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Pseudoscalar of the algebra
        pseudoscalar_text = Tex(
            r"\text{Pseudoscalar:}",
        ).move_to(scalars_text.get_center()).shift(DOWN*1.5).to_edge(LEFT)
        pseudoscalar_tex = Tex(
            pseudoscalar, space, equal, space, sigma_1, sigma_2, sigma_3
        ).next_to(pseudoscalar_text, RIGHT, aligned_edge=DOWN).shift(RIGHT + DOWN*0.1)
        pseudoscalar_tex.set_color_by_tex_to_color_map(color_dict)
        
        self.play(Write(pseudoscalar_text))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(pseudoscalar_tex))
        
        # * Box the pseudoscalar result
        pseudoscalar_tex_box = Polygon(
            pseudoscalar_tex.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            pseudoscalar_tex.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            pseudoscalar_tex.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            pseudoscalar_tex.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        pseudoscalar_tex_box.set_color(WHITE)
        self.play(ShowCreation(pseudoscalar_tex_box))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Levi-Cevita: Add the definition of the levi-cevita symbol within this subalgebra
        levi_cevita_text = Tex(
            r"\text{Levi-Cevita:}",
        ).move_to(pseudoscalar_text.get_center()).shift(DOWN*1.5).to_edge(LEFT)
        levi_cevita_tex = Tex(
            eps_ijk, space, equal, space, 
            sigma_i, space, wedge, space, 
            sigma_j, space, wedge, space,
            sigma_k, space, pseudoscalar_dagger
        ).next_to(levi_cevita_text, RIGHT, aligned_edge=DOWN).shift(RIGHT + DOWN*0.1)
        levi_cevita_tex.set_color(WHITE)
        self.play(Write(levi_cevita_text))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(levi_cevita_tex))
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * Clean up the scene: 
        # * 1. FadeOut the basis set, sigma set, and other set
        # * 2. Move scalars text, pseudoscalar text, unitarity result, and pseudoscalar result up
        # * 3. Move levi cevita to the right side of the screen
        # * 4. Draw a line separating the two sides of the screen
        

        
        self.play(
            FadeOut(basis_set),
            FadeOut(sigma_set),
            FadeOut(other_set),
            FadeOut(sigma_i_tex),
            
            scalars_text.animate.shift(UP*1),
            sigma_i_squared_final_box.animate.shift(UP*1),
            sigma_i_squared_final.animate.shift(UP*1),
            
            pseudoscalar_text.animate.shift(UP*1),
            pseudoscalar_tex_box.animate.shift(UP*1),
            pseudoscalar_tex.animate.shift(UP*1),
            
            levi_cevita_text.animate.to_edge(RIGHT).shift(LEFT*0.25 + LEFT*1 + UP*5),
            levi_cevita_tex.animate.to_edge(RIGHT).shift(LEFT*0.25 + UP*4),
            run_time = 3
            
        )
        
        line_separator = Line(
            levi_cevita_tex.get_left() + LEFT*0.75 + UP*1,
            levi_cevita_tex.get_left() + LEFT*0.75 + DOWN*5, 
            color=WHITE
        )
        
        self.play(ShowCreation(line_separator))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Rewrite the Levi-Cevita symbol
        # * 1. Drop the wedges
        
        levi_cevita_drop_wedges = Tex(
            eps_ijk, space, equal, space, 
            sigma_i, sigma_j, sigma_k,
            space, pseudoscalar_dagger)
        
        levi_cevita_drop_wedges.move_to(levi_cevita_tex.get_center()).shift(DOWN*1)

        self.play(
            TransformMatchingTex(
                levi_cevita_tex.copy(),
                levi_cevita_drop_wedges,
                key_map={
                    wedge: "",
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    sigma_k: sigma_k,
                    eps_ijk: eps_ijk,
                    pseudoscalar_dagger: pseudoscalar_dagger,
                    equal: equal,
                },
            )
        )
        
        
        # * 2. Multiply both sides by the pseudoscalar
        levi_cevita_pseudoscalar_mult = Tex(
            eps_ijk, space, pseudoscalar,
            space, equal, space, 
            sigma_i, sigma_j, sigma_k,
            space, pseudoscalar_dagger, pseudoscalar)
        levi_cevita_pseudoscalar_mult.move_to(levi_cevita_drop_wedges.get_center())
        # levi_cevita_pseudoscalar_mult.shift(DOWN*1)
        levi_cevita_pseudoscalar_mult.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                levi_cevita_drop_wedges,
                levi_cevita_pseudoscalar_mult,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    sigma_k: sigma_k,
                    eps_ijk: eps_ijk,
                    equal: equal,
                    pseudoscalar: pseudoscalar,
                    pseudoscalar_dagger: pseudoscalar_dagger,
                },
            ),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * 3. Back to the right side, expand what pseudoscalar_dagger * pseudoscalar is
        pseudoscalar_dagger_pseudoscalar = Tex(
            pseudoscalar_dagger, pseudoscalar)
        pseudoscalar_dagger_pseudoscalar.move_to(pseudoscalar_text.get_center()).shift(DOWN*1.5 + RIGHT*0.5)
        self.play(
            Indicate(levi_cevita_pseudoscalar_mult[-3:], scale_factor=1.2),
        )
        self.play(
            TransformFromCopy(
                levi_cevita_pseudoscalar_mult[-3:],
                pseudoscalar_dagger_pseudoscalar,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Expand the terms
        pseudoscalar_dagger_pseudoscalar_expanded = Tex(
            pseudoscalar_dagger, pseudoscalar, 
            space, equal, space,
            sigma_3, sigma_2, sigma_1, space,
            sigma_1, sigma_2, sigma_3,)
        pseudoscalar_dagger_pseudoscalar_expanded.move_to(pseudoscalar_dagger_pseudoscalar.get_center()).shift(RIGHT*1.5)
        pseudoscalar_dagger_pseudoscalar_expanded.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                pseudoscalar_dagger_pseudoscalar,
                pseudoscalar_dagger_pseudoscalar_expanded,
                key_map={
                    sigma_1: sigma_1,
                    sigma_2: sigma_2,
                    sigma_3: sigma_3,
                    equal: equal,
                    eps_ijk: eps_ijk,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Turn the sigma_1 sigma_1 into 1
        pseudoscalar_dagger_pseudoscalar_sigma_1_faded = Tex(
            pseudoscalar_dagger, pseudoscalar,
            space, equal, space,
            sigma_3, sigma_2, space,
            lbracket, "1", rbracket, space,
            sigma_2, sigma_3,)
        pseudoscalar_dagger_pseudoscalar_sigma_1_faded.move_to(pseudoscalar_dagger_pseudoscalar_expanded.get_center())
        pseudoscalar_dagger_pseudoscalar_sigma_1_faded.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                pseudoscalar_dagger_pseudoscalar_expanded,
                pseudoscalar_dagger_pseudoscalar_sigma_1_faded,
                key_map={
                    sigma_1: lbracket + "1" + rbracket,
                    sigma_2: sigma_2,
                    sigma_3: sigma_3,
                    equal: equal,
                    eps_ijk: eps_ijk,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * final form: Idagger I = 1
        pseudoscalar_dagger_pseudoscalar_final = Tex(
            pseudoscalar_dagger, pseudoscalar, 
            space, equal, space,
            "1")
        pseudoscalar_dagger_pseudoscalar_final.move_to(pseudoscalar_dagger_pseudoscalar_sigma_1_faded.get_center()).shift(DOWN*1.25)
        
        # * Box the final result
        pseudoscalar_dagger_pseudoscalar_final_box = Polygon(
            pseudoscalar_dagger_pseudoscalar_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            pseudoscalar_dagger_pseudoscalar_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            pseudoscalar_dagger_pseudoscalar_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            pseudoscalar_dagger_pseudoscalar_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        pseudoscalar_dagger_pseudoscalar_final_box.set_color(WHITE)
        self.play(
            TransformMatchingTex(
                pseudoscalar_dagger_pseudoscalar_sigma_1_faded.copy(),
                pseudoscalar_dagger_pseudoscalar_final,
                key_map={
                    sigma_1: "",
                    sigma_2: sigma_2,
                    sigma_3: sigma_3,
                    equal: equal,
                    eps_ijk: eps_ijk,
                },
            ),
        )
        self.play(ShowCreation(pseudoscalar_dagger_pseudoscalar_final_box))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * 4. Fade out the pseudoscalar dagger and pseudoscalar from the levi cevita
        
        levi_cevita_pseudoscalar_mult_fade = Tex(
            eps_ijk, space, pseudoscalar, 
            space, equal, space, 
            sigma_i, sigma_j, sigma_k,
            )
        levi_cevita_pseudoscalar_mult_fade.move_to(levi_cevita_pseudoscalar_mult.get_center(), aligned_edge=DOWN).shift(DOWN*0.25)
        levi_cevita_pseudoscalar_mult_fade.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                levi_cevita_pseudoscalar_mult,
                levi_cevita_pseudoscalar_mult_fade,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    sigma_k: sigma_k,
                    eps_ijk: eps_ijk,
                    equal: equal,
                    pseudoscalar: pseudoscalar,
                    pseudoscalar_dagger: "",
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * 5. Multiply both sides by sigma_k
        levi_cevita_pseudoscalar_mult_sigma_k = Tex(
            eps_ijk, space, pseudoscalar, space, sigma_k,
            space, equal, space,
            sigma_i, sigma_j, sigma_k, sigma_k
            )
        levi_cevita_pseudoscalar_mult_sigma_k.move_to(levi_cevita_pseudoscalar_mult_fade.get_center()).shift(DOWN*1)
        levi_cevita_pseudoscalar_mult_sigma_k.set_color_by_tex_to_color_map(color_dict)
        
        self.play(
            TransformMatchingTex(
                levi_cevita_pseudoscalar_mult_fade.copy(),
                levi_cevita_pseudoscalar_mult_sigma_k,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    sigma_k: sigma_k,
                    eps_ijk: eps_ijk,
                    equal: equal,
                    pseudoscalar: pseudoscalar,
                },
                path_arc=PI/2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)

        # * 6.  Fade out the sigma_k sigma_k at the end 
        levi_cevita_final_result = Tex(
            eps_ijk, space, pseudoscalar, space, sigma_k,
            space, equal, space,
            sigma_i, sigma_j, 
            )
        
        levi_cevita_final_result.move_to(levi_cevita_pseudoscalar_mult_sigma_k.get_center()).shift(DOWN*1.5)
        levi_cevita_final_result.set_color_by_tex_to_color_map(color_dict)

        self.play(
            TransformMatchingTex(
                levi_cevita_pseudoscalar_mult_sigma_k.copy(),
                levi_cevita_final_result,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    sigma_k: sigma_k,
                    eps_ijk: eps_ijk,
                    equal: equal,
                    pseudoscalar: pseudoscalar,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * 7. Box the final result
        levi_cevita_final_result_box = Polygon(
            levi_cevita_final_result.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            levi_cevita_final_result.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            levi_cevita_final_result.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            levi_cevita_final_result.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        levi_cevita_final_result_box.set_color(WHITE)
        self.play(ShowCreation(levi_cevita_final_result_box))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Clean up the scene:
        # * 1. FadeOut everything on the left
        
        self.play(
            FadeOut(scalars_text),
            FadeOut(pseudoscalar_text),
            
            FadeOut(pseudoscalar_dagger_pseudoscalar_final_box),
            FadeOut(pseudoscalar_dagger_pseudoscalar_final),
            FadeOut(pseudoscalar_dagger_pseudoscalar_sigma_1_faded),
            
            FadeOut(pseudoscalar_tex_box),
            FadeOut(pseudoscalar_tex),
            
            FadeOut(sigma_i_squared_final_box),
            FadeOut(sigma_i_squared_final),
        )

        # * The Anti-symmetry of the Levi-Cevita symbol enables us to write sigma_i sigma_j = - sigma_j sigma_i
        
        anti_symmetry_text = Tex(
            r"\text{Anti-symmetry:}",
        ).move_to(title.get_center()).shift(DOWN*1.25).to_edge(LEFT)
        anti_symmetry_text.set_color(WHITE)
        anti_symmetry_tex = Tex(
            sigma_i, sigma_j, space, equal, space,
            minus, sigma_j, sigma_i
        ).next_to(anti_symmetry_text, RIGHT, aligned_edge=RIGHT).shift(RIGHT*2 + DOWN*0.1)
        anti_symmetry_tex.set_color_by_tex_to_color_map(color_dict)
        
        self.play(Write(anti_symmetry_text))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(anti_symmetry_tex))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Some math magic: sigma_i sigma_j + sigma_i sigma_j = 2 sigma_i sigma_j
        anti_symmetry_tex_expanded = Tex(
            sigma_i, sigma_j, 
            space, plus, space,
            sigma_i, sigma_j,
            space, equal, space,
            "2", sigma_i, sigma_j,
        ).move_to(title.get_center()).shift(DOWN*2.5)
        anti_symmetry_tex_expanded.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                anti_symmetry_tex.copy(),
                anti_symmetry_tex_expanded,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    equal: equal,
                    minus: plus,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Swap the order of the second sigma_i sigma_j and pickup a minus sign
        anti_symmetry_tex_expanded_swapped = Tex(
            sigma_i, sigma_j, 
            space, minus, space,
            sigma_j, sigma_i,
            space, equal, space,
            "2", sigma_i, sigma_j,
        ).move_to(anti_symmetry_tex_expanded.get_center())
        anti_symmetry_tex_expanded_swapped.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                anti_symmetry_tex_expanded,
                anti_symmetry_tex_expanded_swapped,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    equal: equal,
                    minus: plus,
                    "2": "2",
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * Now rewrite things in terms of the commutator
        
        self.play(
            Indicate(anti_symmetry_tex_expanded_swapped[:-6], scale_factor=1.2),
            FlashUnder(anti_symmetry_tex_expanded_swapped[:-6], color=YELLOW, time_width=0.5),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        anti_symmetry_tex_expanded_commutator = Tex(
            r"\left[" + sigma_i + comma + space + sigma_j + r"\right]",
             space, equal, space,
            "2", sigma_i, sigma_j,
        ).move_to(anti_symmetry_tex_expanded_swapped.get_center()).shift(DOWN*1)
        anti_symmetry_tex_expanded_commutator.set_color_by_tex_to_color_map(color_dict)
        
        self.play(
            TransformMatchingTex(
                anti_symmetry_tex_expanded_swapped.copy(),
                anti_symmetry_tex_expanded_commutator,
                key_map={
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    equal: equal,
                    minus: plus,
                    "2": "2",
                },
            )
        )
        # * Final form: substitute the sigma_i sigma_j on the left with eps_ijk I sigma_k
        anti_symmetry_tex_final = Tex(
            r"\left[" + sigma_i + comma + space + sigma_j + r"\right]",
             space, equal, space,
            "2", eps_ijk, pseudoscalar, sigma_k,
        ).move_to(anti_symmetry_tex_expanded_commutator.get_center())
        anti_symmetry_tex_final.set_color_by_tex_to_color_map(color_dict)
        self.play(
            TransformMatchingTex(
                anti_symmetry_tex_expanded_commutator,
                anti_symmetry_tex_final,
                key_map={
                    r"\left[" + sigma_i + comma + space + sigma_j + r"\right]": r"\left[" + sigma_i + comma + space + sigma_j + r"\right]",
                    sigma_i: sigma_i,
                    sigma_j: sigma_j,
                    equal: equal,
                    minus: plus,
                    "2": "2",
                    eps_ijk: eps_ijk,
                    sigma_k: sigma_k,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)

        # * Box the final result
        anti_symmetry_tex_final_box = Polygon(
            anti_symmetry_tex_final.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            anti_symmetry_tex_final.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            anti_symmetry_tex_final.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            anti_symmetry_tex_final.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        anti_symmetry_tex_final_box.set_color(WHITE)
        self.play(ShowCreation(anti_symmetry_tex_final_box))
        self.wait(NOMINAL_WAIT_TIME)
        self.wait(PAUSE_WAIT_TIME)

        # * Fade out everything
        self.play(
            
            FadeOut(title),
            
            FadeOut(levi_cevita_text),
            FadeOut(levi_cevita_tex),
            FadeOut(levi_cevita_pseudoscalar_mult_sigma_k),
            
            FadeOut(anti_symmetry_text),
            FadeOut(anti_symmetry_tex),
            # FadeOut(anti_symmetry_tex_expanded),
            FadeOut(anti_symmetry_tex_expanded_swapped),
            
            FadeOut(anti_symmetry_tex_final),
            FadeOut(anti_symmetry_tex_final_box),
            
            FadeOut(line_separator),
            
            FadeOut(levi_cevita_final_result),
            FadeOut(levi_cevita_final_result_box),
            FadeOut(levi_cevita_pseudoscalar_mult_fade),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
            
        
        
 
        
        
        
        
        
        