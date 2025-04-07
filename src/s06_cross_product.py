from manim import *
from reactive_manim import *
import manimforge as mf
mf.setup()
from definitions import *


class _6_CrossProduct(ThreeDScene):

    def construct(self):
        # * ______________________________________________________________________
        self.next_section("Title", skip_animations=False)
        # * ______________________________________________________________________
        title = Text(
            f'The Cross Product', color=BLUE,
            font_size=TITLE_FONTSIZE
        )
        title.to_corner(UL)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=2)



        # * ______________________________________________________________________
        self.next_section("Axes", skip_animations=False)
        # * ______________________________________________________________________

        CONFIG = {
            "x_axis_label": "$x$",
            "y_axis_label": "$y$",
            "z_axis_label": "$z$",
            "basis_i_color": GREEN_D,
            "basis_j_color": RED_D,
            "basis_k_color": BLUE_D
        }
        
        axes = ThreeDAxes(
            x_range=(-3.5, 3.5, 1),
            y_range=(-3.5, 3.5, 1),
            z_range=(-3.5, 3.5, 1),
            x_length=7,
            y_length=7,
            z_length=7,
        ).set_opacity(0.75)
        self.play(
            Create(axes),
            run_time=1,
        )
        self.move_camera(phi=70*DEGREES,theta=45*DEGREES + 15*DEGREES,run_time=1)
        self.wait(NOMINAL_WAIT_TIME)
        phi, theta, focal_distance, gamma, distance_to_origin = self.camera.get_value_trackers()
        
        # Zoom in and shift axes to the right
        # self.play(
        #     distance_to_origin.animate.set_value(1.5),
        #     axes.animate.move_to(LEFT*2)
        # )
        

        # * ______________________________________________________________________
        self.next_section("Vectors", skip_animations=False)
        # * ______________________________________________________________________
        origin = axes.c2p(0,0,0)

        # Create three vectors, A, B and C
        vec_a_num = 0.35*np.array([4, -3, 2])
        vec_b_num = 0.35*np.array([2,  1.5, -1.5])
        vec_n_num = np.cross(vec_a_num, vec_b_num)
        
        vec_a = Arrow3D(origin, axes.c2p(*vec_a_num), color = RED)
        vec_b = Arrow3D(origin, axes.c2p(*vec_b_num), color = BLUE)
        vec_n = Arrow3D(origin, axes.c2p(*vec_n_num), color = YELLOW)
        
        for vec in [vec_a, vec_b]:
            self.play(
                Create(vec),
                runtime=1
            )
        
        vec_a_label = MathTex("A",
            color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(vec_a, RIGHT)
        vec_b_label = MathTex("B",
            color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(vec_b, UP)
        
        for label in [vec_a_label, vec_b_label]:
            self.add_fixed_orientation_mobjects(label)
            self.play(
                Write(label, run_time=1),
                
            )
        
        # # * ______________________________________________________________________
        # self.next_section("Zoom and Shift", skip_animations=False)
        # # * ______________________________________________________________________
        
        # # self.begin_ambient_camera_rotation(rate = - 0.4)
        
        # self.play(
        #     Create(
        #         vec_n
        #     ),
        #     runtime=3
        # )

        # self.wait(NOMINAL_WAIT_TIME*2)
        # # self.play(
        # #     gamma.animate.set_value(0.5),
        # # )
        # # self.wait(NOMINAL_WAIT_TIME*2)
        # # self.play(
            
        # # )
        
        # self.play(
        #     axes.animate.rotate(PI/2, axis=OUT, about_point=ORIGIN),
        # )
        
        # self.play(
        #     # distance_to_origin.animate.set_value(1.5)
        #     focal_distance.animate.set_value(25)
            
        # )
        # # Zoom in and move everything to the right
        # self.wait(5)
        
        # * ______________________________________________________________________
        self.next_section("Plane", skip_animations=False)
        # * ______________________________________________________________________
        
        self.play(
            distance_to_origin.animate.set_value(1.5)
            # focal_distance.animate.set_value(25)
        )
        
        self.begin_ambient_camera_rotation(rate = - 0.16)
        
        lines_kwags = {"stroke_width": 2, "color": BLUE_B, "stroke_opacity": 0.2}
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

        big_rect = ThreeDVMobject()
        big_rect.set_points_as_corners([
            lines_a[0].get_start(),
            lines_b[0].get_end(), 
            lines_a[-1].get_end(),
            lines_b[-1].get_start(),
            lines_a[0].get_start()
        ])
        big_rect.set_fill(color = BLUE_B, opacity = 0.3)
        big_rect.set_stroke(width = 0.5, color = GREY)
        self.play(Create(big_rect), Create(lines_a), Create(lines_b), run_time = 2)
        # self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            Create(vec_n),
        )

        
        vec_n_label = MathTex("A", "\\times", "B",
            color=YELLOW, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(vec_n, OUT).shift(UP*1)
        self.add_fixed_orientation_mobjects(vec_n_label)
        
        
        # * ______________________________________________________________________
        self.next_section("Shift", skip_animations=False)
        # * ______________________________________________________________________
        
        self.play(
            Write(vec_n_label),
            # phi.animate.set_value(60*DEGREES),
            run_time=1
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        # Group everything in this scene and shift it all to the left*2
        everything = VGroup(
            axes, vec_a, vec_b, vec_n, lines_a, lines_b, big_rect,
            vec_a_label, vec_b_label, vec_n_label
        )
        self.stop_ambient_camera_rotation()
        
        self.play(
            everything.animate.shift(RIGHT*1 + UP*1 ),
            run_time=1
        )
        
          
        # * ______________________________________________________________________
        self.next_section("Definition", skip_animations=False)
        # * ______________________________________________________________________



        A_term             = MathTex("\\mathbf{A}", color=RED)
        B_term             = MathTex("\\mathbf{B}", color=BLUE)
        a_i_term           = MathTex("a_i")
        b_i_term           = MathTex("b_i")
        e_k_term           = MathTex("\\mathbf{e}_k", color=YELLOW)
        levi_civita_symbol = MathTex("\\epsilon_{ijk}", color=WHITE)

        cross_product_def = MathTex(A_term, "\\times", B_term, "=", levi_civita_symbol, a_i_term, b_i_term, e_k_term,
            font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_corner(UL).shift(DOWN * 1)

        levi_civita_tex = Tex(
            "Levi-Civita Tensor",
            color=BLUE_B, font_size=int(3 * TITLE_FONTSIZE / 3)
        )
        levi_civita_tex.to_corner(UL).shift(DOWN * 2)
        
        A_term_sum = MathTex(A_term, "=", "\\sum_{i=1}^3", a_i_term, "\\mathbf{e}_i", color=RED)
        B_term_sum = MathTex(B_term, "=", "\\sum_{j=1}^3", b_i_term, "\\mathbf{e}_j", color=BLUE)
        A_term_sum.to_corner(UL).shift(DOWN * 2.75)
        B_term_sum.to_corner(UL).shift(DOWN * 4.5)

        for latex_term in [cross_product_def, levi_civita_tex, A_term_sum, B_term_sum]:
            self.add_fixed_in_frame_mobjects(latex_term)
            self.remove(latex_term)
            self.play(Write(latex_term), run_time=2)
            self.wait(NOMINAL_WAIT_TIME)
            
        self.wait(NOMINAL_WAIT_TIME)
        # Fade out A_sum and B_sum
        self.play(
            FadeOut(A_term_sum),
            FadeOut(B_term_sum),
            FadeOut(cross_product_def),
            run_time=1
        )
        self.wait(1)
        
        new_cross_product_def = MathTex(
            "\\mathbf{e}_i", "\\times", "\\mathbf{e}_j", "=", "\\epsilon_{ijk}", "\\mathbf{e}_k",
            font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_corner(UL).shift(DOWN * 1)
        new_cross_product_def[0].set_color(RED)
        new_cross_product_def[2].set_color(BLUE)
        new_cross_product_def[5].set_color(YELLOW)
        
        self.add_fixed_in_frame_mobjects(new_cross_product_def)
        self.play(
            Write(new_cross_product_def),
            run_time=2
        )
        self.wait(PAUSE_WAIT_TIME*5)
        

        
        # Fade everything out
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )
        