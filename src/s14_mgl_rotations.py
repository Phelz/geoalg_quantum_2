
from manimlib import *
from src.definitions import *






class _14_Rotations(Scene):
    def construct(self):

        sigma_1 = r"\sigma_1"
        sigma_2 = r"\sigma_2"
        sigma_3 = r"\sigma_3"
        
        exp_sigma_3 = r"e^{\sigma_3 \mathbb{I} \theta/2}"
        exp_sigma_3_inv = r"e^{-\sigma_3 \mathbb{I} \theta/2}"
        
        R_theta = r"R(\theta)"
        R_theta_dagger = r"R(\theta)^\dagger"
        
        cos_theta = r"\cos(\theta)"
        sin_theta = r"\sin(\theta)"
        
        equal = "="; plus = "+"; wedge = r"\wedge"; space = " \ "
        lbracket = "("
        rbracket = ")"
        
        rotor_formula = Tex(
            # R_theta, sigma_1, R_theta_dagger, space, equal, space, r"\newline",
            sigma_1, space, cos_theta, 
            space, plus, space,
            sigma_2, space, sin_theta,
            font_size=int(3 * TITLE_FONTSIZE / 3),
        )
        # rotor_formula[4:6].set_color(BLUE_C)
        
        rotor_formula.fix_in_frame()
        rotor_formula.to_corner(UL).shift(DOWN*0.25+ RIGHT*0.25)
        
        self.add(rotor_formula)

        # final_formula = Tex(A_term, space, wedge, space, B_term, space, equal, space,
        #                    lbracket, A_term, space, times, space, B_term, rbracket, space,
        #                    '\\mathbb{I}')
        
        # final_formula.fix_in_frame()
        
        # final_formula.set_color_by_tex_to_color_map(COLORMAP_DICT)

        # final_formula_box = Polygon(
        #     final_formula.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
        #     final_formula.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
        #     final_formula.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
        #     final_formula.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        # )
        
        # final_formula.to_corner(UL).shift(DOWN*0.25+ RIGHT*0.25),
        # final_formula_box.to_corner(UL)
        
        # final_formula_box.fix_in_frame()
        # self.add(
        #     final_formula_box,
        #     final_formula
        # )
        
        
        # * Begin 3D Scene - Create Axes
        # * ________________________________________________________________________
        # Create a 3D axes
        axes = ThreeDAxes(
            x_range=(-2, 2, 1),
            y_range=(-2, 2, 1),
            z_range=(-2, 2, 1),
            height=7,
            width=7,
            depth=6,
            unit_size=2
        ).set_opacity(1)
        axes.add_axis_labels(
            x_tex="\\sigma_1",
            y_tex="\\sigma_2",
            z_tex="\\sigma_3",
            font_size=TITLE_FONTSIZE,
        )
        
        
        self.play(
            ShowCreation(axes),
            run_time=3,
        )
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=45*DEGREES + 15*DEGREES,
                phi=70*DEGREES,
            ),
            run_time=3,
        )

        
        self.camera.frame.add_ambient_rotation(angular_speed=5*DEGREES),       
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * Create SIGMA_1 vector
        # * ________________________________________________________________________
        
        sigma_1_arr = 1.75*np.array([1, 0, 0])
        sigma_1_vector = Vector(sigma_1_arr, stroke_width=3,
                                ).set_color(BLUE_C)
        
        self.play(
            GrowFromCenter(sigma_1_vector),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        trace = TracedPath(
            sigma_1_vector.get_end,
            stroke_width=5,
            stroke_color=BLUE_A,
            time_traced=32
        )
        self.add(trace)
        
        self.play(
            Rotate(sigma_1_vector, angle=PI/4, axis=OUT, about_point=ORIGIN),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            Rotate(sigma_1_vector, angle=PI/4, axis=OUT, about_point=ORIGIN),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Combinations of rotations
        # * ________________________________________________________________________
        
        # Fade out the text
        self.play(
            FadeOut(rotor_formula),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Now rotate the whole way around
        self.play(
            Rotate(sigma_1_vector, angle=PI/2 + PI, axis=OUT, about_point=ORIGIN),
            run_time=5,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # Now rotate in the xz-plane
        self.play(
            Rotate(sigma_1_vector, angle=2*PI, axis=DOWN, about_point=ORIGIN),
            run_time=5,
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        # Now draw a sphere
        unit_sphere = Sphere(
            radius=1.75,
            color=BLUE_C,
            # fill_opacity=0.3,
            # fill_color=BLUE_A,
        ).set_opacity(0.25)
        mesh = SurfaceMesh(unit_sphere).set_stroke(width=1.5, color=BLUE_D, opacity=0.8)
        self.play(
            ShowCreation(mesh, lag_ratio=0.01, run_time=3),
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.play(
            ShowCreation(unit_sphere, lag_ratio=0.01, run_time=3),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * Label the Riemann Sphere
        # * ________________________________________________________________________
        
        Riemann_sphere = Tex(
            "Riemann \ Sphere",
            font_size=int(4 * TITLE_FONTSIZE / 3),
        ).to_corner(UL).shift(DOWN*0.25+ RIGHT*0.5)
        
        # underline it
        Riemann_sphere_underline = Underline(
            Riemann_sphere,
            color=WHITE,
            stroke_width=2,
            buff=0.1,
        )
        Riemann_sphere.fix_in_frame()
        Riemann_sphere_underline.fix_in_frame()
        self.play(
            Write(Riemann_sphere),
            Write(Riemann_sphere_underline),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Describing the Qubit
        # * ________________________________________________________________________
        
        # Change the color of the vector to yellow
        self.play(
            sigma_1_vector.animate.set_color( YELLOW),
            run_time=3,
        )
        
        # Rotate it 
        self.play(
            Rotate(sigma_1_vector, angle=PI/4, axis=OUT, about_point=ORIGIN),
            run_time=2,
        )
        self.play(
            Rotate(sigma_1_vector, angle=PI/4, axis=DOWN, about_point=ORIGIN),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Qubit label
        diag_arr_ket = r" \ket{ \nearrow }"
        down_arr_ket = r" \ket{ \downarrow }"
        up_arr_ket = r" \ket{ \uparrow }"
        w = "w"
        v = "v"
        qubit_label = Tex("Qubit:", font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_corner(UR).shift(DOWN*0.25+ LEFT*1.5)
        qubit_label.set_color(BLUE_B)
        qubit_label.fix_in_frame()
        
        spin_state = Tex(
            diag_arr_ket, space, equal, space,
            v, space, up_arr_ket, space,
            plus, space,
            w, space, down_arr_ket)
        spin_state.set_color(BLUE_B)
        spin_state.next_to(qubit_label, DOWN).shift(DOWN*0.25)
        spin_state.fix_in_frame()
        
        # Write both
        self.play(
            Write(qubit_label),
            Write(spin_state),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        # * Denote that w and z are complex numbers
        
        wz_in_C = Tex(
            v, ",", w, space, "\in \mathbb{C}",
            font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(spin_state, DOWN).shift(DOWN*0.25)
        wz_in_C.set_color(BLUE_B)
        wz_in_C.fix_in_frame()
        self.play(
            Write(wz_in_C),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Fixing the problem - global phase transformation
        # * ________________________________________________________________________
        
        global_phase = Tex(
            "Global \ Phase",
            font_size=int(4 * TITLE_FONTSIZE / 3)
        ).to_corner(UL).shift(DOWN*0.25+ RIGHT*0.5)
        global_phase_underline = Underline(
            global_phase,
            color=WHITE,
            stroke_width=2,
            buff=0.1,
        )
        global_phase.fix_in_frame()
        global_phase_underline.fix_in_frame()
        
        # Transform Riemann sphere into global phase
        self.play(
            ReplacementTransform(Riemann_sphere, global_phase,),
            ReplacementTransform(Riemann_sphere_underline, global_phase_underline,),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # !!! At this point, get the camera's euler angles and set it fixed ther (STOP ROTATION)
        theta, phi, gamma = self.camera.frame.get_euler_angles()
        
        # First remove the camera updater
        self.camera.frame.remove_updater(
            self.camera.frame.get_updaters()[0]
        )
        
        self.camera.frame.set_euler_angles(
            theta=theta,
            phi=phi,
            gamma=gamma,
        )
        
        
        
        
        lambda_term = r"\lambda"
        
        # Scaling with lambda
        lambda_scaled_state = Tex(
            lambda_term, space, diag_arr_ket,
            space, equal, space, diag_arr_ket,
        ).set_color(BLUE_B)
        lambda_scaled_state.fix_in_frame()
        lambda_scaled_state.next_to(global_phase, DOWN).shift(DOWN*0.25)
        self.play(
            Write(lambda_scaled_state),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)

        one_over_v = r"\frac{1}{v}"
        u = "u"
        
        one_over_v_scaled_state = Tex(
            one_over_v, space, diag_arr_ket,
            space, equal, space, up_arr_ket,
            space, plus, space,
            u, space, down_arr_ket,
        ).set_color(BLUE_B)
        one_over_v_scaled_state.fix_in_frame()
        one_over_v_scaled_state.next_to(lambda_scaled_state, DOWN).shift(DOWN*0.25)
        self.play(
            Write(one_over_v_scaled_state),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Define u below
        u_term = Tex(
            u, space, equal, space,
            r"\frac{w}{v}")
        u_term.set_color(BLUE_B)
        u_term.fix_in_frame()
        u_term.next_to(one_over_v_scaled_state, DOWN).shift(DOWN*0.25)
        self.play(
            Write(u_term),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Color the denominator
        self.play(
            u_term.animate.set_color_by_tex_to_color_map(
            {v: RED}
            ),
            run_time=2,
        )
        # !!!
        # self.camera.frame.stop_ambient_camera_rotation() 
        # self.add_updater(lambda m, dt: m.increment_theta(angular_speed * dt))
        # self.camera.clear()
        
        self.play(
            FlashAround(u_term[-1], color=RED),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Fixing the infinity problem
        # * ________________________________________________________________________
        
        # w -> 0
        # u -> infinity
        inf = r"\infty"
        u_term_fixed = Tex(
            u, space, equal, space,
            r"\frac{w}{0}")
        u_term_fixed.set_color(BLUE_B)
        u_term_fixed.fix_in_frame()
        u_term_fixed.next_to(u_term, DOWN).shift(DOWN*0.25)
        
        u_term_fixed.set_color_by_tex_to_color_map(
            {v: RED, "0": RED}
        )
        
        self.play(
            Write(u_term_fixed),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)

        u_term_fixed_w_inf = Tex(
            inf, space, equal, space,
            r"\frac{w}{0}", 
        )
        u_term_fixed_w_inf.set_color(BLUE_B)
        u_term_fixed_w_inf.fix_in_frame()
        u_term_fixed_w_inf.next_to(u_term, DOWN).shift(DOWN*0.25)
        u_term_fixed_w_inf.set_color_by_tex_to_color_map(
            {"0": RED, inf: GREEN_C}
        )
        self.play(
            Transform(u_term_fixed, u_term_fixed_w_inf),
            run_time=3,
        )

        self.wait(PAUSE_WAIT_TIME)
        
        # Fade out everything
        
        
        
        
            
        
        
        
        
