
from manimlib import *
from src.definitions import *



COLORMAP_DICT = {"A": RED, "B": BLUE}



class CrossProductRevisited(ThreeDScene):
    def construct(self):
        
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
            x_range=(-3.5, 3.5, 0.5),
            y_range=(-3.5, 3.5, 0.5),
            z_range=(-3.5, 3.5, 0.5),
        ).set_opacity(0.75)
        
        # axes.add_coordinate_labels(
        #     font_size=TITLE_FONTSIZE,
        #     x_label="x",
        #     y_label="y",
        #     z_label="z",
        # )
        
        
        self.play(
            ShowCreation(axes),
            run_time=3,
        )
        
        # self.play(
        #     self.camera.frame.animate.set_euler_angles(
        #         theta=45*DEGREES + 15*DEGREES,
        #         phi=70*DEGREES,
        #     ),
        #     run_time=3,
        # )
        
        origin = axes.c2p(0,0,0)

        # Create three vectors, A, B and C
        vec_a_num = 0.35*np.array([4, -3, 2])
        vec_b_num = 0.35*np.array([2,  1.5, -1.5])
        vec_n_num = np.cross(vec_a_num, vec_b_num)
        
        # vec_a = StrokeArrow(origin, axes.c2p(*vec_a_num)).set_color(RED)
        # vec_b = StrokeArrow(origin, axes.c2p(*vec_b_num)).set_color(BLUE)
        # vec_n = StrokeArrow(origin, axes.c2p(*vec_n_num)).set_color(YELLOW)
        
        vec_a = StrokeArrow(ORIGIN, vec_a_num).set_color(RED)
        vec_b = StrokeArrow(ORIGIN, axes.c2p(*vec_b_num)).set_color(BLUE)
        vec_n = StrokeArrow(ORIGIN, axes.c2p(*vec_n_num)).set_color(YELLOW)
        
        self.play(
            GrowFromCenter(vec_a),
            GrowFromCenter(vec_b),
            GrowFromCenter(vec_n),
            run_time=3,
        )
        
        vec_a_label = Tex("A", font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(vec_a, RIGHT).set_color(RED)
        vec_b_label = Tex("B",  font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(vec_b, UP).set_color(BLUE)
        
        for label in [vec_a_label, vec_b_label]:
            label.fix_in_frame()
            self.play(
                Write(label, run_time=1),
                
            )
        
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