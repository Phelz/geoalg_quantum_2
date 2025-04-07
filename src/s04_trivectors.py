from manim import *
# from reactive_manim import *
import manimforge as mf
mf.setup()
from definitions import *


class _4_Trivectors(ThreeDScene):

    def construct(self):
        # * ______________________________________________________________________
        self.next_section("Title", skip_animations=False)
        # * ______________________________________________________________________
        title = Text(
            f'Trivectors', color=BLUE,
            font_size=TITLE_FONTSIZE
        )
        title.to_corner(UL)
        
        basis_vectors_text = MathTex(
            " \{ \\mathbf{e}_1 , \\mathbf{e}_2 , \\mathbf{e}_3 \}",
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_corner(UL).shift(0.75*DOWN)
        
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
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            z_range=(-8, 8, 1),
            x_length=8,
            y_length=8,
            z_length=5,
        ).set_opacity(0.5)
        self.add_fixed_in_frame_mobjects(basis_vectors_text)
        self.play(
            Create(axes),
            Write(basis_vectors_text),
            run_time=2,
        )
        self.move_camera(phi=70*DEGREES,theta=45*DEGREES + 15*DEGREES,run_time=2)
        self.wait(NOMINAL_WAIT_TIME)


        

        # * ______________________________________________________________________
        self.next_section("Basis Vectors", skip_animations=False)
        # * ______________________________________________________________________

        # Create 3 basis vectors
        i_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([1, 0, 0]), color=CONFIG["basis_i_color"])
        j_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([0, 1, 0]), color=CONFIG["basis_j_color"])
        k_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([0, 0, 1]), color=CONFIG["basis_k_color"])
        
        for vector in [i_hat, j_hat, k_hat]:
            self.play(
                Write(vector, run_time=1),
                # GrowArrow(vector, run_time=1),
                # vector.animate.Create(), runtime=1
            )
        
        # Add labeling math tex for each vector
        i_hat_label = MathTex(
            "\\mathbf{e}_1", color=CONFIG["basis_i_color"], font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(i_hat, RIGHT) #.set_stroke(width=0, family=False).set_shaded_in_3d(True)
        j_hat_label = MathTex(
            "\\mathbf{e}_2", color=CONFIG["basis_j_color"], font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(j_hat, UP) #.set_stroke(width=0, family=False).set_shaded_in_3d(True)
        k_hat_label = MathTex(
            "\\mathbf{e}_3", color=CONFIG["basis_k_color"], font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(k_hat, OUT).shift(UP*.75) #.set_stroke(width=0, family=False).set_shaded_in_3d(True)

        
        for obj in [i_hat_label, j_hat_label, k_hat_label]:
            self.add_fixed_orientation_mobjects(obj)
            obj.z_index = 10  # Ensure the labels are on top of the axes
            self.play(
                Write(obj, run_time=0.5),
            )
        

        # self.stop_ambient_camera_rotation()
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Outer Product", skip_animations=False)
        # * ______________________________________________________________________

        # Wedge all 3 basis vectors
        wedge_text = MathTex(
            "\\mathbf{e}_1 \\wedge \\mathbf{e}_2 \\wedge \\mathbf{e}_3",
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_corner(UL).shift(DOWN *2.25)
        
        pseudoscalar = MathTex(
            "\\mathbb{I} =  \\mathbf{e}_1 \\wedge \\mathbf{e}_2 \\wedge \\mathbf{e}_3",
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).move_to(wedge_text.get_center()).shift(RIGHT * 0.75)
        
        
        self.add_fixed_in_frame_mobjects(wedge_text)
        self.play(
            Write(wedge_text),
            runtime=1
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Create a volume element trivector
        cube = Cube(
            side_length=2,
            fill_opacity=0.5,
            fill_color=BLUE
        )
        cube.move_to(np.array([1, 1, 1]))
        
        self.play(
            Write(cube),
            run_time=2
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # * The pseudoscalar


        self.play(
            ReplacementTransform(wedge_text, pseudoscalar),
            runtime=2
        )
        self.add_fixed_in_frame_mobjects(pseudoscalar)
        
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # Add box around the pseudoscalar
        pseudoscalar_box = SurroundingRectangle(
            pseudoscalar, buff=0.3, color=WHITE, corner_radius=0.005
        )
        self.add_fixed_in_frame_mobjects(pseudoscalar_box)
        self.play(Create(pseudoscalar_box), run_time=1)
        self.wait(NOMINAL_WAIT_TIME)
        
        # *  Indicate the pseudoscalar 
        pseudoscalar_label = MathTex(
            "\\text{Pseudoscalar}",
            color=YELLOW,
            font_size=int(3 * TITLE_FONTSIZE / 3),
        ).next_to(pseudoscalar, DOWN).shift(DOWN * 0.5)
        self.add_fixed_in_frame_mobjects(pseudoscalar_label)

        self.play(
            Indicate(pseudoscalar[0][0:1], rate_func=there_and_back),  # Indicate only \mathbb{I}
            Write(pseudoscalar_label),
            run_time=4,
        )
        self.wait(NOMINAL_WAIT_TIME + 1)
        

        # * ______________________________________________________________________
        self.next_section("Multivectors", skip_animations=False)
        # * ______________________________________________________________________ 
        multivector_title = Text(
            "Multivectors", color=BLUE_D,
            font_size=TITLE_FONTSIZE
        ).to_corner(UR)
        
        multivector_text = MathTex(
            "\\mathbf{e}_1 \\wedge \\mathbf{e}_2 \\wedge \\mathbf{e}_3 \\wedge \\mathbf{e}_4 ... \\wedge \\mathbf{e}_n",
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_corner(UR).shift(DOWN *1)
        
        self.add_fixed_in_frame_mobjects(multivector_title)
        self.play(
            Write(multivector_title),
            runtime=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.add_fixed_in_frame_mobjects(multivector_text)
        self.play(
            Write(multivector_text),
            runtime=3
        )
        self.wait(PAUSE_WAIT_TIME*2)
        
        # Fade everything away
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

def construct_bivector(scene, u, v):
    
    u_line = Line(
        u.get_start(), u.get_end(), color=WHITE
    )
    v_line = Line(
        v.get_start(), v.get_end(), color=WHITE
    )

    # Shift u_line's tail to the tip of v
    scene.play(
        u_line.animate.shift(
            v.get_end() - u_line.get_start()
        ),
        v_line.animate.shift(
            u.get_end() - v_line.get_start()
        ),
        run_time=1,
    )

    # Create a filled polygon from the tails of all 4 points
    polygon_pts = [
        u.get_start(),
        u.get_end(),
        v_line.get_end(),
        u_line.get_start(),
    ]

    bivector_polygon = Polygon(
        *polygon_pts,
        color=WHITE,
        fill_color=WHITE,
        fill_opacity=0.25,
    )
    
    

    scene.play(Create(bivector_polygon), run_time=1)
    
    return u_line, v_line, polygon_pts, bivector_polygon


