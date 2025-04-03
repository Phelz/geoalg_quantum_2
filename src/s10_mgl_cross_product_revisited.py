
from manimlib import *
from src.definitions import *



COLORMAP_DICT = {"A": RED, "B": BLUE}



class CrossProductRevisited(ThreeDScene):
    def construct(self):
        # * Formula on top
        
        A_term = "A"
        B_term = "B"
        times = "\\times"
        equal = "="; plus = "+"; wedge = r"\wedge"; space = " \ "
        
        lbracket = "("
        rbracket = ")"

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
            run_time=3,
        )
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=45*DEGREES + 15*DEGREES,
                phi=70*DEGREES,
            ),
            run_time=3,
        )
        self.camera.frame.add_ambient_rotation(10*DEGREES)
        
        origin = axes.c2p(0,0,0)

        # Create three vectors, A, B and C
        vec_a_num = 0.35*np.array([4, -3, 2])
        vec_b_num = 0.35*np.array([2,  1.5, -1.5])
        vec_n_num = np.cross(vec_a_num, vec_b_num)
        
        vec_a = Line3D(ORIGIN, vec_a_num).set_color(RED)
        vec_b = Line3D(ORIGIN, vec_b_num).set_color(BLUE)
        vec_n = Line3D(ORIGIN, vec_n_num).set_color(YELLOW)
        
        tip_a = Cone(u_range=(1, 1), v_range=(1, 1), radius=0.4, axis=vec_a_num).set_color(RED).move_to(vec_a.get_end())
        tip_b = Cone(u_range=(1, 1), v_range=(1, 1), radius=0.4, axis=vec_b_num).set_color(BLUE).move_to(vec_b.get_end())
        tip_n = Cone(u_range=(1, 1), v_range=(1, 1), radius=0.4, axis=vec_n_num).set_color(YELLOW).move_to(vec_n.get_end())
        
        self.play(
            GrowFromCenter(vec_a),
            GrowFromCenter(vec_b),
            GrowFromCenter(vec_n),

            run_time=3,
        )
        
        self.play(
            GrowFromCenter(tip_a),
            GrowFromCenter(tip_b),
            GrowFromCenter(tip_n),
        )
        self.wait(10)
        # Draw a plane like we had in the s06_cross_product.py
        plane = Polygon(
            vec_a.get_start(),
            vec_a.get_end(),
            vec_b.get_end(),
            vec_b.get_start(),
            color=BLUE_B,
            fill_opacity=0.5,

        )
        
        self.play(
            ShowCreation(plane),
            run_time=3,
        )
        
        # vec_a_label = Tex("A", font_size=int(3 * TITLE_FONTSIZE / 3)
        # ).next_to(vec_a, RIGHT).set_color(RED)
        # vec_b_label = Tex("B",  font_size=int(3 * TITLE_FONTSIZE / 3)
        # ).next_to(vec_b, UP).set_color(BLUE)
        
        # for label in [vec_a_label, vec_b_label]:
        #     label.fix_in_frame()
        #     self.play(
        #         Write(label, run_time=1),
                
        #     )
        
        # for vec in [vec_a, vec_b]:
        #     self.play(
        #         Create(vec),
        #         runtime=2
        #     )
        # self.wait(dfs.NOMINAL_WAIT_TIME)
        
        
        # # Zoom in and shift axes to the right
        # self.play(
        #     self.camera.frame.animate.set_field_of_view(50),
        # )
        
        # Create three vectors like we had in the s06_cross_product.py
        # A_vector = 