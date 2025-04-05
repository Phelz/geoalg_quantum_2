
from manimlib import *
from src.definitions import *



class _12_DualVisualized(ThreeDScene):
    def construct(self):
        
        # * Formula on top
        title = Title(
            "Duality",
            stroke_color=BLUE_D,
            include_underline=True,
            match_underline_width_to_text=True,
            underline_style=dict(stroke_width=3, stroke_color=WHITE),
        ).to_corner(UL).set_color(BLUE_D)
        
        
        
        title.fix_in_frame()
        self.add(title)
        
        formula = Tex(
            r"\mathbf{e_1} \wedge \mathbf{e_3} \ \mathbb{I}^\dagger ",
            font_size=int(4 * TITLE_FONTSIZE / 3),
        )        
        formula.next_to(title, DOWN).shift(DOWN*0.5).to_edge(LEFT).shift(RIGHT*0.1)
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
        e1 = Vector(1.75*np.array([1, 0, 0])).set_color(BLUE_A)
        e2 = Vector(1.75*np.array([0, 1, 0])).set_color(YELLOW_C)
        e3 = Vector(1.75*np.array([0, 0, 1])).set_color(BLUE_A)
        
        e2.set_opacity(0)
        neg_e2 = Vector(1.75*np.array([0, -1, 0])).set_color(YELLOW_C)
        neg_e2.set_opacity(0)
        self.add(neg_e2)
        # self.add(e1, e2, e3)
        
        self.play(
            GrowFromCenter(e1),
            GrowFromCenter(e3),
            run_time=2,
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
                  
        e1_line = Line(
            e1.get_start(), e1.get_end(), color=WHITE
        )
        e3_line = Line(
            e3.get_start(), e3.get_end(), color=WHITE
        )

        # Shift e1_line's tail to the tip of e3
        self.play(
            e1_line.animate.shift(
                e3.get_end() - e1_line.get_start()
            ),
            e3_line.animate.shift(
                e1.get_end() - e3_line.get_start()
            ),
            run_time=1,
        )

        # Create a filled polygon from the tails of all 4 points
        polygon_pts = [
            e1.get_start(),
            e1.get_end(),
            e3_line.get_end(),
            e1_line.get_start(),
        ]

        bivector_polygon = Polygon(
            *polygon_pts,
            color=WHITE,
            fill_color=BLUE_A,
            fill_opacity=0.25,
        )
        self.add(e2)
        
        self.play(
            ShowCreation(bivector_polygon),
            run_time=2,
        )
        
        # * Write e_1 \\wedge e_3 on top of the bivector
        
        label = Tex(
            r"\mathbf{e_1}  \wedge \mathbf{e_3}",
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(bivector_polygon, OUT).shift(UP*0.5)
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
            e2.animate.set_opacity(0.5),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Rotate the camera 180 degrees
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=self.camera.frame.get_euler_angles()[0] - 90*DEGREES,
            ),
            label.animate.rotate(-PI, axis=OUT).shift(IN*0.25 + LEFT*0.75),
            run_time=2,
            
        )
        self.play(
            neg_e2.animate.set_opacity(1),
            run_time=2,
        )