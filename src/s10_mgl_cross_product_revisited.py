
from manimlib import *
from src.definitions import *



COLORMAP_DICT = {"A": RED, "B": BLUE}



class _10_CrossProductRevisited(ThreeDScene):
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
            
            self.camera.frame.animate.set_euler_angles(
                theta=45*DEGREES + 15*DEGREES,
                phi=60*DEGREES,
            ),
            run_time=3,
        )
        self.camera.frame.add_ambient_rotation(10*DEGREES)
        
        # * Vectors 
        # * ________________________________________________________________________
        
        
        # Create three vectors, A, B and C
        vec_a_num = 0.35*np.array([4, -3, 2])
        vec_b_num = 0.35*np.array([2,  1.5, -1.5])
        vec_n_num = np.cross(vec_a_num, vec_b_num)
        
        vec_a = Vector(vec_a_num).set_color(RED)
        vec_b = Vector(vec_b_num).set_color(BLUE)
        vec_n = Vector(vec_n_num).set_color(YELLOW)
        
        
        self.play(
            GrowFromCenter(vec_a),
            GrowFromCenter(vec_b),
            GrowFromCenter(vec_n),
            run_time=2,
        )
        
        # * Plane
        # * ________________________________________________________________________
        
        lines_kwags = {"stroke_width": 2, "color": BLUE_B, "stroke_opacity": 0.4}
        lines_a = VGroup(*[
            Line(
                start = axes.c2p(*[-1.5*comp_a + s*comp_b for comp_a, comp_b in zip(vec_a_num, vec_b_num)]), 
                end  =  axes.c2p(*[+1.5*comp_a + s*comp_b for comp_a, comp_b in zip(vec_a_num, vec_b_num)]), 
                **lines_kwags
            )
            for s in np.linspace(-1.5,1.5,7)
        ])

        lines_b = VGroup(*[
            Line(
                start = axes.c2p(*[r*comp_a - 1.5*comp_b for comp_a, comp_b in zip(vec_a_num, vec_b_num)]), 
                end  =  axes.c2p(*[r*comp_a + 1.5*comp_b for comp_a, comp_b in zip(vec_a_num, vec_b_num)]), 
                **lines_kwags
            )
            for r in np.linspace(-1.5,1.5,7)
        ])
        neg_vec_n = Vector(-1*vec_n_num).set_color(YELLOW).set_opacity(0)
        self.add(neg_vec_n)
        
        big_rect = VGroup3D()
        big_rect.set_points_as_corners([
            lines_a[0].get_start(),
            lines_b[0].get_end(), 
            lines_a[-1].get_end(),
            lines_b[-1].get_start(),
            lines_a[0].get_start()
        ])
        big_rect.set_fill(color = BLUE_B, opacity = 0.1)
        big_rect.set_stroke(width = 0.1, color = GREY)
        
        
        self.play(ShowCreation(lines_a), ShowCreation(lines_b), 
                  ShowCreation(big_rect),
                  run_time = 2)
        self.wait(NOMINAL_WAIT_TIME*3)

        # Stop ambient rotation
        self.camera.frame.remove_updater(
            self.camera.frame.get_updaters()[0]
        )
        
        self.play(
            neg_vec_n.animate.set_opacity(0.5),
            # Rotate the camerea frame
            self.camera.frame.animate.set_euler_angles(
                theta=self.camera.frame.get_euler_angles()[0] - 40*DEGREES,
                phi=self.camera.frame.get_euler_angles()[1] + 60*DEGREES,
                # gamma=-10*DEGREES,
            ),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            Indicate(neg_vec_n, color=YELLOW, scale_factor=1.5),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=self.camera.frame.get_euler_angles()[0] + 30*DEGREES,
                phi=self.camera.frame.get_euler_angles()[1] - 50*DEGREES,
                # gamma=-10*DEGREES,
            ),
            FadeOut(neg_vec_n),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            FadeOut(big_rect),
            FadeOut(lines_a),
            FadeOut(lines_b),
            
        )
        
                
        vec_a_line = Line(
            vec_a.get_start(), vec_a.get_end(), color=WHITE
        )
        vec_b_line = Line(
            vec_b.get_start(), vec_b.get_end(), color=WHITE
        )

        # Shift vec_a_line's tail to the tip of vec_b
        self.play(
            vec_a_line.animate.shift(
                vec_b.get_end() - vec_a_line.get_start()
            ),
            vec_b_line.animate.shift(
                vec_a.get_end() - vec_b_line.get_start()
            ),
            run_time=1,
        )

        # Create a filled polygon from the tails of all 4 points
        polygon_pts = [
            vec_a.get_start(),
            vec_a.get_end(),
            vec_b_line.get_end(),
            vec_a_line.get_start(),
        ]

        bivector_polygon = Polygon(
            *polygon_pts,
            color=WHITE,
            fill_color=BLUE_A,
            fill_opacity=0.5,
        )
        # bivector_polygon.set_stroke(color=BLUE_A, width=10,)
        
        # Now draw a curved arrowc
        cur_arr = CurvedArrow(
            vec_a.get_end(),
            vec_b.get_end(),
            color=YELLOW,
            angle=PI/2,
        )
        
        self.play(
            ShowCreation(cur_arr),
            run_time=2,
        )       
        
        
        self.play(
            ShowCreation(bivector_polygon),
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # * Indicate the bivector
        self.play(
            Indicate(bivector_polygon, color=YELLOW, scale_factor=1.05),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Indicate the pseudo-scalar in the formula
        self.play(
            Indicate(final_formula[-1], color=YELLOW, scale_factor=1.25),
            FlashAround(
                final_formula[-1], color=YELLOW, 
                time_width=0.5,
            ),
            run_time=3,
        )
        self.wait(PAUSE_WAIT_TIME)
        
        
        # Fade out everything
        self.play(
            FadeOut(vec_a),
            FadeOut(vec_b),
            FadeOut(vec_n),
            FadeOut(vec_a_line),
            FadeOut(vec_b_line),
            FadeOut(bivector_polygon),
            FadeOut(cur_arr),
            FadeOut(axes),
            # FadeOut(final_formula_box),
            # FadeOut(final_formula),
            run_time=2,
        )
