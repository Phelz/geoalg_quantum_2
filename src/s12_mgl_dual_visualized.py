
from manimlib import *
from src.definitions import *



class DualVisualized(ThreeDScene):
    def construct(self):
        
        # * Formula on top
        
        # A_term = "A"
        # B_term = "B"
        # times = "\\times"
        # equal = "="; plus = "+"; wedge = r"\wedge"; space = " \ "
        
        # lbracket = "("
        # rbracket = ")"

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
        
        # Set height (zoom in)
        self.camera.frame.set_height(5)

        self.play(
            ShowCreation(axes),
            
            self.camera.frame.animate.set_euler_angles(
                theta=45*DEGREES + 15*DEGREES,
                phi=60*DEGREES,
            ),
            run_time=3,
        )
        
        # * Show basis vectors
        e1 = Vector(ORIGIN, np.array([1, 0, 0]), color=BLUE_A)
        e2 = Vector(ORIGIN, np.array([0, 1, 0]), color=BLUE_A)
        e3 = Vector(ORIGIN, np.array([0, 0, 1]), color=YELLOW_C)
        
        