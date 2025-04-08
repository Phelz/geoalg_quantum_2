
from manimlib import *
from src.definitions import *



class _12_DualVisualized(ThreeDScene):
    def construct(self):
        
        e1 = r"\mathbf{e_1}"
        e2 = r"\mathbf{e_2}"
        e3 = r"\mathbf{e_3}"
        space = r" \ "
        equal = r"="
        wedge = r"\wedge"
        minus = r"-"
        pseudoscalar_dagger = r"\mathbb{I}^\dagger"
        e2_dual = r"\mathbf{e^2}"

        color_dict_3d = {
            e1: RED_B,
            e2: BLUE_B,
            e3: GREEN_B,
            wedge: WHITE,
            pseudoscalar_dagger: WHITE,
            e2_dual: BLUE,
        }
        
        # * Formula on top
        title = Title(
            "Duality",
            stroke_color=BLUE,
            include_underline=True,
            match_underline_width_to_text=True,
            underline_style=dict(stroke_width=3, stroke_color=WHITE),
        ).to_corner(UL).set_color(BLUE)
        
        
        
        title.fix_in_frame()
        self.add(title)
        
        formula = Tex(
            e2_dual, space, equal, space, minus, space, e1, space, wedge, space, e3, space, pseudoscalar_dagger
            
        ).set_color_by_tex_to_color_map(color_dict_3d)
        formula.move_to( title.get_center()).shift(1.5*DOWN + RIGHT*1)
        formula.fix_in_frame()
        
        box_around_formula = Polygon(
            formula.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            formula.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            formula.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            formula.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        box_around_formula.set_color(WHITE)
        box_around_formula.fix_in_frame()
        
        self.add(
            box_around_formula,
            formula
        )
        
        # FadeOut the box
        self.play(
            FadeOut(box_around_formula),
            run_time=1,
        )
        
        
        
        
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
        
        # Set height (zoom in)
        self.camera.frame.set_height(5)

        self.play(
            ShowCreation(axes),
            
            self.camera.frame.animate.set_euler_angles(
                theta=90*DEGREES + 30*DEGREES,
                phi=60*DEGREES,
            ),
            run_time=3,
        )
        
        # * Show basis vectors
        e1_vec = Vector(1.75*np.array([1, 0, 0])).set_color(RED_B)
        e2_vec = Vector(1.75*np.array([0, 1, 0])).set_color(BLUE)
        e3_vec = Vector(1.75*np.array([0, 0, 1])).set_color(GREEN_B)
        
        e2_vec.set_opacity(0)
        neg_e2 = Vector(1.75*np.array([0, -1, 0])).set_color(BLUE_B)
        neg_e2.set_opacity(0)
        self.add(neg_e2)
        # self.add(e1, e2, e3)
        
        self.play(
            GrowFromCenter(e1_vec),
            GrowFromCenter(e3_vec),
            run_time=2,
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
                  
        e1_vec_line = Line(
            e1_vec.get_start(), e1_vec.get_end(), color=WHITE
        )
        e3_vec_line = Line(
            e3_vec.get_start(), e3_vec.get_end(), color=WHITE
        )

        # Shift e1_vec_line's tail to the tip of e3_vec
        self.play(
            e1_vec_line.animate.shift(
                e3_vec.get_end() - e1_vec_line.get_start()
            ),
            e3_vec_line.animate.shift(
                e1_vec.get_end() - e3_vec_line.get_start()
            ),
            run_time=1,
        )

        # Create a filled polygon from the tails of all 4 points
        polygon_pts = [
            e1_vec.get_start(),
            e1_vec.get_end(),
            e3_vec_line.get_end(),
            e1_vec_line.get_start(),
        ]

        bivector_polygon = Polygon(
            *polygon_pts,
            color=WHITE,
            fill_color=BLUE_A,
            fill_opacity=0.25,
        )
        self.add(e2_vec)
        
        self.play(
            ShowCreation(bivector_polygon),
            run_time=2,
        )
        
        # * Write e_1 \\wedge e_3 on top of the bivector
        
        label = Tex(
            e1, space, wedge, space, e3,
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
            
        ).set_color_by_tex_to_color_map(color_dict_3d)
        label.next_to(bivector_polygon, OUT).shift(UP*0.5)
        label.rotate(PI/2, axis=RIGHT).rotate(PI, axis=OUT).shift(OUT*0.25 + RIGHT*0.75)
        
        
        #  * Rotate it so it faces the e2 axis
        
        self.play(
            Write(label),
            run_time=2,
        
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        # * Now draw e2 only
        self.play(
            # GrowFromCenter(e2),
            e2_vec.animate.set_opacity(1),
            run_time=2,
        )
        
        # * Rotate the camera 90 degrees
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=self.camera.frame.get_euler_angles()[0] - 90*DEGREES,
            ),
            label.animate.rotate(-PI, axis=OUT).shift(IN*0.25 + LEFT*0.75),
            run_time=1,
            
        )
        self.play(
            neg_e2.animate.set_opacity(1),
            run_time=1,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Solve the equation
        
        # Turn e1 wedge e3 into e1 e3 and write the pseudoscalar dagger as e3 e2 e1
        e2_dual_solving_1 = Tex(
            e2_dual, space, equal, space, minus, space, e1, e3, space, 
            e3, e2, e1,
            
        ).set_color_by_tex_to_color_map(color_dict_3d)
        e2_dual_solving_1.move_to(formula.get_center()).shift(RIGHT*0.5)
        e2_dual_solving_1.fix_in_frame()
        
        self.play(
            TransformMatchingTex(
                formula,
                e2_dual_solving_1,
                key_map={
                    e1: e1,
                    e2: e2,
                    e3: e3,
                    wedge: wedge,
                    minus: minus,
                    equal: equal,
                },
                run_time=2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # The e3 e_3 turn to 1
        e2_dual_solving_2 = Tex(
            e2_dual, space, equal, space, minus, space, e1, e2, e1,
        ).set_color_by_tex_to_color_map(color_dict_3d)
        e2_dual_solving_2.move_to(e2_dual_solving_1.get_center()).shift(LEFT*0.5)
        e2_dual_solving_2.fix_in_frame()
        self.play(
            TransformMatchingTex(
                e2_dual_solving_1,
                e2_dual_solving_2,
                key_map={
                    e1: e1,
                    e2: e2,
                    e3: e3,
                    wedge: wedge,
                    minus: minus,
                    equal: equal,
                },
                run_time=2,
            )
        )
        self.wait(2)
        
        # Switch the e2 witth the e1 and the minus sign disappears
        e2_dual_solving_3 = Tex(
            e2_dual, space, equal, space, e2, e1, e1,
        ).set_color_by_tex_to_color_map(color_dict_3d)
        e2_dual_solving_3.move_to(e2_dual_solving_2.get_center()).shift(LEFT*0.5)
        e2_dual_solving_3.fix_in_frame()
        
        self.play(
            TransformMatchingTex(
                e2_dual_solving_2,
                e2_dual_solving_3,
                key_map={
                    e1: e1,
                    e2: e2,
                    e3: e3,
                    wedge: wedge,
                    minus: minus,
                    equal: equal,
                },
                run_time=2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Finally, e2_dual = e2
        e2_dual_solving_4 = Tex(
            e2_dual, space, equal, space, e2,
        ).set_color_by_tex_to_color_map(color_dict_3d)
        e2_dual_solving_4.move_to(e2_dual_solving_3.get_center()).shift(LEFT*0.5)
        e2_dual_solving_4.fix_in_frame()
        self.play(
            TransformMatchingTex(
                e2_dual_solving_3,
                e2_dual_solving_4,
                key_map={
                    e1: e1,
                    e2: e2,
                    e3: e3,
                    wedge: wedge,
                    minus: minus,
                    equal: equal,
                },
                run_time=2,
            )
        )
        self.wait(1)
        # Box the result
        box_around_result = Polygon(
            e2_dual_solving_4.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            e2_dual_solving_4.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            e2_dual_solving_4.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            e2_dual_solving_4.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),
        )
        box_around_result.set_color(WHITE)
        box_around_result.fix_in_frame()

        # * Rotate back the camera
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=self.camera.frame.get_euler_angles()[0] + 90*DEGREES,
            ),
            label.animate.rotate(PI, axis=OUT).shift(OUT*0.25 + RIGHT*0.75),
            ShowCreation(box_around_result),
            run_time=2,
            
        )
        self.wait(PAUSE_WAIT_TIME)
        self.wait(PAUSE_WAIT_TIME)
        
        
        # * General formula, turn the 2 in e2_dual and e2 into i
        ei = r"\mathbf{e_i}"
        ei_dual = r"\mathbf{e^i}"
        ei_dual_formula = Tex(
            ei_dual, space, equal, space, ei,
        ).set_color_by_tex_to_color_map(color_dict_3d)
        ei_dual_formula.move_to(e2_dual_solving_4.get_center())
        ei_dual_formula.fix_in_frame()
        self.play(
            TransformMatchingTex(
                e2_dual_solving_4,
                ei_dual_formula,
                key_map={
                    wedge: wedge,
                    minus: minus,
                    equal: equal,
                    e2: ei,
                    e2_dual: ei_dual,
                },
                run_time=2,
            )
        )
        self.wait(PAUSE_WAIT_TIME)
        self.wait(PAUSE_WAIT_TIME)
        
        # * Fade to black
        self.play(
            FadeOut(
                VGroup(
                    axes,
                    e1_vec,
                    e3_vec,
                    e2_vec,
                    neg_e2,
                    bivector_polygon,
                    label,
                    box_around_result,
                    ei_dual_formula,
                    title,
                    e1_vec_line,
                    e3_vec_line,
                )
            ),
            run_time=2,
        )
        
