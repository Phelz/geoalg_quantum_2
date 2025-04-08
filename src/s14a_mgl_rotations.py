
from manimlib import *
from src.definitions import *

class _14A_Rotations(Scene):
    def construct(self):

        # * Symbols
        sigma_1 = r"\mathbf{\sigma_1}"
        sigma_2 = r"\mathbf{\sigma_2}"
        sigma_3 = r"\mathbf{\sigma_3}"
        
        sigma_i = r"\mathbf{\sigma_i}"
        
        exp_sigma_3 = r"e^{-\mathbb{I} \mathbf{\sigma_3}  \theta}"
        
        exp_sigma_3_theta2 = r"e^{-\mathbb{I} \mathbf{\sigma_3}  \theta/2}"
        exp_sigma_3_theta2_dagger = r"e^{\mathbb{I} \mathbf{\sigma_3}  \theta/2}"
        
        sigma_x_hat = r"\hat{\sigma}_x"
        sigma_y_hat = r"\hat{\sigma}_y"
        sigma_z_hat = r"\hat{\sigma}_z"

        exp_sigma_z = r"e^{-i \hat{\sigma}_z \theta}"
        
        exp_sigma_z_theta2 = r"e^{-i \hat{\sigma}_z \theta/2}"
        exp_sigma_z_theta2_inv = r"e^{i \hat{\sigma}_z  \theta/2}"
        
        R_theta = r"R(\theta)"
        R_theta_dagger = r"R(\theta)^\dagger"
        
        cos_theta_over_2 = r"\cos(\frac{\theta}{2})"
        sin_theta_over_2 = r"\sin(\frac{\theta}{2})"
        cos_theta = r"\cos(\theta)"
        sin_theta = r"\sin(\theta)"
        
        equal = "="; plus = "+"; minus = "-"; 
        wedge = r"\wedge"; space = " \ "
        lbracket = "("
        rbracket = ")"
        
        imaginary_i = "i"
        pseudoscalar = r"\mathbb{I}"
        
        colormap_dict = {
            sigma_1: RED_B,
            sigma_2: BLUE_C,
            sigma_3: GREEN_B,
            
            sigma_x_hat: RED_D,
            sigma_y_hat: BLUE_D,
            sigma_z_hat: GREEN_D,
        }
        
        
        # * The quantum mechanics version of the rotation operator
        
        euler_quantum = Tex(
            exp_sigma_z, space, equal, space,
            cos_theta, space, minus, space,
            imaginary_i, sigma_z_hat, space, sin_theta
        ).scale(1).to_edge(UP).shift(DOWN*0.5 + RIGHT*2)
        euler_quantum.set_color_by_tex_to_color_map(colormap_dict)
        
        euler_quantum_text = Tex(
            r"\text{Quantum Mechanics:}"
        )
        euler_quantum_text.scale(1).next_to(euler_quantum, LEFT).shift(LEFT*0.5)
        self.play(Write(euler_quantum))
        self.wait(PAUSE_WAIT_TIME)
        self.play(Write(euler_quantum_text))
        self.wait(PAUSE_WAIT_TIME)
        
        # * The Geometric Algebra version
        euler_geometric = Tex(
            exp_sigma_3, space, equal, space,
            cos_theta, space, minus, space,
            pseudoscalar, sigma_3, space, sin_theta
        ).scale(1).next_to(euler_quantum, DOWN).shift(DOWN*1).set_color(BLUE_B)
        
        euler_geometric.set_color_by_tex_to_color_map(colormap_dict)
        
        euler_geometric_text = Tex(
            r"\text{Geometric Algebra:}"
        )
        euler_geometric_text.scale(1).next_to(euler_geometric, LEFT).shift(LEFT*0.5).set_color(BLUE_B)
        
        self.play(
            TransformMatchingTex(
                euler_quantum.copy(), euler_geometric,
                key_map={
                    cos_theta: cos_theta,
                    sin_theta: sin_theta,
                    imaginary_i: pseudoscalar,
                    sigma_z_hat: sigma_3,
                    equal: equal,
                    minus: minus,
                    space: space,
                    exp_sigma_z: exp_sigma_3,
                },
            )
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(euler_geometric_text))
        self.wait(PAUSE_WAIT_TIME)
        
        # * Remind the audience that 
        # * 1. Sigma Vectors are unitary
        # * 2. The Pseudoscalar acts like the imaginary unit
        
        unitarity_tex = Tex(
            lbracket, sigma_i, rbracket + "^2", space, equal, space, "1"
            ).scale(1).to_edge(LEFT).shift(DOWN*0.5 + RIGHT*1)
        
        unitarity_tex.set_color(BLUE_B)
        
        box_unitarity = Polygon(
            unitarity_tex.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            unitarity_tex.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            unitarity_tex.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            unitarity_tex.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
            color=BLUE_B, fill_opacity=0.25,
            stroke_width=3, fill_color=BLUE_B

        )
        
        self.play(FadeIn(unitarity_tex),
                  FadeIn(box_unitarity),
        )
        self.wait(PAUSE_WAIT_TIME)
        
        
        # * Imaginary Pseudoscalar
        imaginary_tex = Tex(
            pseudoscalar + "^2", space, equal, space, "-1")
        imaginary_tex.scale(1).next_to(unitarity_tex, DOWN).shift(DOWN*1)
        #.shift(RIGHT*3 + DOWN*1)
        imaginary_tex.set_color(BLUE_B)
        
        box_imaginary = Polygon(
            imaginary_tex.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            imaginary_tex.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            imaginary_tex.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            imaginary_tex.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
            color=BLUE_B, fill_opacity=0.25,
            stroke_width=3, fill_color=BLUE_B
        )
        self.play(FadeIn(imaginary_tex),
                  FadeIn(box_imaginary),
        )
        self.wait(PAUSE_WAIT_TIME)
        self.wait(PAUSE_WAIT_TIME)
        
        
        # * Line separator
        line = Line(
            start=unitarity_tex.get_corner(UR) + RIGHT + UP*0.5,
            end=unitarity_tex.get_corner(UR) + RIGHT + DOWN*3,
            color=WHITE)
        self.play(ShowCreation(line))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Now onto Rotations: Rotating sigma_x about sigma_z
        # * 1. Quantum Mechanics
        
        rotation_quantum_p1 = Tex(
            exp_sigma_z_theta2, space, sigma_x_hat, space, exp_sigma_z_theta2_inv, 
            space, equal, space,
            r"\left(" + cos_theta_over_2 + space + minus + space + imaginary_i + sigma_z_hat + space + sin_theta_over_2 + r"\right)", 
            isolate=[sigma_x_hat, sigma_z_hat],
        ).next_to(line, RIGHT).shift(UP + LEFT*0.5).scale(0.85)
        rotation_quantum_p1.set_color_by_tex_to_color_map(colormap_dict)
        
        rotation_quantum_p2 = Tex(
                        space, sigma_x_hat, space,
            r"\left(" + cos_theta_over_2 + space + plus + space + imaginary_i + sigma_z_hat + space + sin_theta_over_2 + r"\right)",
            isolate=[sigma_x_hat, sigma_z_hat],
            )
        rotation_quantum_p2.next_to(rotation_quantum_p1, DOWN).shift(RIGHT*0.5)
        rotation_quantum_p2.scale(0.85)
        rotation_quantum_p2.set_color_by_tex_to_color_map(colormap_dict)
        
        
        self.play(Write(rotation_quantum_p1))
        self.play(Write(rotation_quantum_p2))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Reduced version
        rotation_quantum_reduced = Tex(
            exp_sigma_z_theta2, space, sigma_x_hat, space, exp_sigma_z_theta2_inv, 
            space, equal, space,
            sigma_x_hat, space, cos_theta, 
            space, plus, space,
            sigma_y_hat, space, sin_theta,
            isolate=[sigma_x_hat, sigma_y_hat, sigma_z_hat],
        ).move_to(rotation_quantum_p1.get_center())
        rotation_quantum_reduced.scale(0.85)
        rotation_quantum_reduced.set_color_by_tex_to_color_map(colormap_dict)
        
        # Transform both 
        self.play(
            TransformMatchingTex(
                rotation_quantum_p1, rotation_quantum_reduced,
                key_map={
                    cos_theta_over_2: cos_theta,
                    sin_theta_over_2: sin_theta,
                    imaginary_i: pseudoscalar,
                    sigma_z_hat: sigma_z_hat,
                    equal: equal,
                    minus: minus,
                    plus: plus,
                    space: space,
                    exp_sigma_z_theta2: exp_sigma_z_theta2,
                    exp_sigma_z_theta2_inv: exp_sigma_z_theta2_inv,
                    sigma_x_hat: sigma_x_hat
                },
            ),
            FadeOut(rotation_quantum_p2),
        )
        self.wait(NOMINAL_WAIT_TIME)

        # * 2. Geometric Algebra
        rotation_geometric_alg = Tex(
            exp_sigma_3_theta2, space, sigma_1, space, exp_sigma_3_theta2_dagger, 
            space, equal, space,
            sigma_1, space, cos_theta,
            space, plus, space,
            sigma_2, space, sin_theta,
            isolate=[sigma_1, sigma_2, sigma_3],
 
        ).next_to(rotation_quantum_reduced, DOWN).shift(DOWN*1).scale(0.85)
        rotation_geometric_alg.set_color(BLUE_B)
        rotation_geometric_alg.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformMatchingTex(
                rotation_quantum_reduced.copy(), rotation_geometric_alg,
                key_map={
                    cos_theta: cos_theta,
                    sin_theta: sin_theta,
                    imaginary_i: pseudoscalar,
                    sigma_z_hat: sigma_3,
                    sigma_x_hat: sigma_1,
                    sigma_y_hat: sigma_2,
                    equal: equal,
                    minus: minus,
                    plus: plus,
                    space: space,
                    exp_sigma_z_theta2: exp_sigma_3_theta2,
                    exp_sigma_z_theta2_inv: exp_sigma_3_theta2_dagger,

                },
            )
        )
        self.wait(PAUSE_WAIT_TIME)
        self.wait(PAUSE_WAIT_TIME)
        
        
        # * Clean up the scene by fading out everythin except the rotation_geometric_alg
        self.play(
            FadeOut(euler_quantum),
            FadeOut(euler_quantum_text),
            FadeOut(euler_geometric),
            FadeOut(euler_geometric_text),
            
            FadeOut(unitarity_tex),
            FadeOut(imaginary_tex),
            FadeOut(box_unitarity),
            FadeOut(box_imaginary),
            
            FadeOut(line),
            
            FadeOut(rotation_quantum_reduced),
            
            # move the rotation_geometric_alg to top and scale it up
            rotation_geometric_alg.animate.center().to_edge(UP).scale(1.3),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Put a Bracelabel underneath the rotor
        rotor_label = BraceLabel(
            rotation_geometric_alg[:8],
            r"\text{Rotor}",
        )
        
        self.play(
            Write(rotor_label),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Indicate that sigma_1 is sent to sigma_1 and sigma_2
        self.play(
            Indicate(
                rotation_geometric_alg[8:10],
                color=RED,
                scale_factor=1.3,
            ),
            FlashAround(
                rotation_geometric_alg[8:10],
                color=RED,
                buff=0.2,
            ),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.play(
            Indicate(
                rotation_geometric_alg[18:20],
                color=RED,
                scale_factor=1.3,
            ),
            FlashAround(
                rotation_geometric_alg[18:20],
                color=RED,
                buff=0.2,
            ),
            
            Indicate(
                rotation_geometric_alg[-8:-6],
                color=BLUE,
                scale_factor=1.3,
            ),
            FlashAround(
                rotation_geometric_alg[-8:-6],
                color=BLUE,
                buff=0.2,
            ),
            
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Now copy the rotor term
        sigma_3_peudoscalar_term = Tex(
            pseudoscalar, sigma_3, 
        )
        
        # Move it down a bit
        sigma_3_peudoscalar_term.move_to(rotation_geometric_alg.get_corner(DL) + DOWN*2 + RIGHT)
        sigma_3_peudoscalar_term.scale(1.5)
        sigma_3_peudoscalar_term.set_color(BLUE_B)
        sigma_3_peudoscalar_term.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformFromCopy(
                rotation_geometric_alg[2:5].copy(), sigma_3_peudoscalar_term,
            )
        )
        
        # * Expand the pseudoscalar term
        sigma_3_peudoscalar_term_expanded = Tex(
            pseudoscalar, sigma_3, space, equal, space,
            sigma_1, sigma_2, sigma_3, space, sigma_3)
        
        sigma_3_peudoscalar_term_expanded.next_to(sigma_3_peudoscalar_term, RIGHT)
        sigma_3_peudoscalar_term_expanded.scale(1.5)
        sigma_3_peudoscalar_term_expanded.set_color(BLUE_B)
        sigma_3_peudoscalar_term_expanded.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformMatchingTex(
                sigma_3_peudoscalar_term, sigma_3_peudoscalar_term_expanded,
                key_map={
                    sigma_1: sigma_1,
                    sigma_2: sigma_2,
                    sigma_3: sigma_3,
                    equal: equal,
                    space: space,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * The sigma_3 sigma_3 at the end vanishes
        sigma_3_peudoscalar_term_expanded_final = Tex(
            pseudoscalar, sigma_3, space, equal, space,
            sigma_1, sigma_2)
        
        sigma_3_peudoscalar_term_expanded_final.move_to(sigma_3_peudoscalar_term_expanded.get_center())
        sigma_3_peudoscalar_term_expanded_final.scale(1.5)
        sigma_3_peudoscalar_term_expanded_final.set_color(BLUE_B)
        sigma_3_peudoscalar_term_expanded_final.set_color_by_tex_to_color_map(colormap_dict)
        
        self.play(
            TransformMatchingTex(
                sigma_3_peudoscalar_term_expanded, sigma_3_peudoscalar_term_expanded_final,
                key_map={
                    sigma_1: sigma_1,
                    sigma_2: sigma_2,
                    # sigma_3: sigma_3,
                    equal: equal,
                    space: space,
                    pseudoscalar: pseudoscalar,
                },
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Put a brace label under the simga_1 sigma_2 in the final term and call it the simga_1 sigma_2 plane
        sigma_1_sigma_2_plane = BraceLabel(
            sigma_3_peudoscalar_term_expanded_final[-4:],
            sigma_1 + sigma_2 + r"\text{-plane}",
        )
        self.play(
            Write(sigma_1_sigma_2_plane),
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # * Clean up scene:
        # * 1. Fade out everything except the rotation_geometric_alg
        self.play(
            FadeOut(rotor_label),
            FadeOut(sigma_1_sigma_2_plane),
            FadeOut(sigma_3_peudoscalar_term_expanded_final),

        )
        
        # ! AWESOME WAY TO FADE OUT PARTS OF A TEX OBJECT SO WE CAN DO CLEANER TRANSFORMS
        self.play(
            FadeOut(rotation_geometric_alg[exp_sigma_3_theta2]),
            FadeOut(rotation_geometric_alg[exp_sigma_3_theta2_dagger]),
            run_time=0.5,
        )
        rotation_geometric_alg[exp_sigma_3_theta2].set_opacity(0)
        rotation_geometric_alg[exp_sigma_3_theta2_dagger].set_opacity(0)
        
        # * 2. Instead of an equal sign, put a right arrow, and remove the exp_sigma_3_theta2 and exp_sigma_3_theta2_dagger terms
        rotation_geometric_alg_final = Tex(
            sigma_1, space, r"\rightarrow",
            space, sigma_1, space, cos_theta,
            space, plus, space,
            sigma_2, space, sin_theta,
            isolate=[sigma_1, sigma_2],
        ).move_to(rotation_geometric_alg.get_center())
        
        rotation_geometric_alg_final.set_color(BLUE_B)
        rotation_geometric_alg_final.set_color_by_tex_to_color_map(colormap_dict)
        
              
        self.play(
            TransformMatchingTex(
                rotation_geometric_alg, rotation_geometric_alg_final,
                key_map={
                    sigma_1: sigma_1,
                    sigma_2: sigma_2,
                    equal: r"\rightarrow",
                    space: space,
                    plus: plus,
                    cos_theta: cos_theta,
                    sin_theta: sin_theta,
                },
            ),
            run_time=1,
        )
        self.play(
            rotation_geometric_alg_final.animate.to_corner(UL),
        )
        
        