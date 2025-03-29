from manim import *
from reactive_manim import *

import manimforge as mf
mf.setup()

TITLE_FONTSIZE = 45
NOMINAL_WAIT_TIME = 2
PAUSE_WAIT_TIME = 5

# class Intro(Scene):
#     def construct(self):

# !!!!! ADD THIS QUOTE David Hestenes
# Mathematics is taken for granted in the physics curriculum—a body of immutable truths to be assimilated and applied. The profound influence of mathematics on our conceptions of the physical world is never analyzed. The possibility that mathematical tools used today were invented to solve problems in the past and might not be well suited for current problems is never considered.

#         self.next_section("Intro", skip_animations=False)
#         # Video Title
#         title = MarkupText(
#             f'Geometric Algebra in Quantum Mechanics', color=BLUE_D,
#             font_size=TITLE_FONTSIZE
#         )
#         self.play(Write(title), run_time=3)
#         self.wait(2)

#         # Author
#         name = MarkupText(
#             f'by Filobateer Ghaly', color=BLUE_D, font_size=int(2.5*TITLE_FONTSIZE/3)
#         ).shift(DOWN)

#         self.play(Write(name), run_time=2, shift=DOWN*2)
#         self.wait(2)

#         # Shift the title up
#         new_title = MarkupText(
#             f'Geometric Algebra', color=BLUE_D,
#             font_size=45
#         ).to_edge(UP)

#         self.play(Transform(title, new_title), FadeOut(name), run_time=1)


# class Bivectors(VectorScene):
# # class GeometricAlgebra(ThreeDScene):
#     def construct(self):
#         self.next_section("Scalars and Vectors", skip_animations=True)

#         title = MarkupText(
#             "Geometric Algebra", color=BLUE_D, font_size=TITLE_FONTSIZE
#         ).to_edge(UP)
#         self.add(title)

#         # * Scalar
#         point = np.array([-3, 0, 0])
#         dot = Dot(point, color=WHITE)
#         dot_name = MathTex(
#             "Scalar", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).next_to(dot, UP)
#         self.play(Create(dot), Write(dot_name), run_time=1)
#         self.wait(NOMINAL_WAIT_TIME)

#         # * Vector
#         vector = self.add_vector(
#             [1.5, 1.5],
#             color=WHITE,
#         )

#         # vector = A(np.array([0, 0, 0]), np.array([1.5, 1.5, 0]), color=WHITE)
#         vector_name = MathTex(
#             "Vector", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).next_to(vector, UP)
#         self.play(
#             Create(vector),
#             Write(vector_name), run_time=1)
#         self.wait(2)

#         # * ______________________________________________________________________
#         self.next_section("Bivectors", skip_animations=True)
#         # * ______________________________________________________________________

#         # Move both to the left using coordinates
#         self.play(
#             dot.animate.shift(LEFT * 3),
#             dot_name.animate.shift(LEFT * 3),
#             vector.animate.shift(LEFT * 4),
#             vector.animate.shift(LEFT * 4),
#             vector_name.animate.shift(LEFT * 4.5),
#             run_time=1,
#         )
#         self.wait(NOMINAL_WAIT_TIME)

#         # * -------------------------------------
#         # * Construct a bivector
#         # * -------------------------------------
#         bivector_1 = vector.copy().shift(RIGHT * 2.5)
#         bivector_1_name = MathTex(
#             "\\vec{u}", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(bivector_1.get_center() + LEFT * 0.8)

#         self.play(
#             Transform(vector.copy(), bivector_1), Write(bivector_1_name), run_time=1
#         )
#         self.wait(NOMINAL_WAIT_TIME)

#         bivector_2 = bivector_1.copy()
#         bivector_2_name = MathTex(
#             "\\vec{v}", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(bivector_2.get_center() + DOWN * 1.25)

#         # The rotation should be 90 degrees relative to the bivector_1
#         self.play(
#             bivector_2.animate.rotate(-PI / 4, about_point=bivector_1.get_start()),
#             Write(bivector_2_name),
#             run_time=1,
#         )
#         self.wait(NOMINAL_WAIT_TIME)

#         bivector_1_line = Line(
#             bivector_1.get_start(), bivector_1.get_end(), color=WHITE
#         )
#         bivector_2_line = Line(
#             bivector_2.get_start(), bivector_2.get_end(), color=WHITE
#         )

#         # Shift bivector_1_line's tail to the tip of bivector_2
#         self.play(
#             bivector_1_line.animate.shift(
#                 bivector_2.get_end() - bivector_1_line.get_start()
#             ),
#             bivector_2_line.animate.shift(
#                 bivector_1.get_end() - bivector_2_line.get_start()
#             ),
#             run_time=1,
#         )

#         # Create a filled polygon from the tails of all 4 points
#         polygon_pts = [
#             bivector_1.get_start(),
#             bivector_1.get_end(),
#             bivector_2_line.get_end(),
#             bivector_1_line.get_start(),
#         ]

#         bivector_polygon = Polygon(
#             *polygon_pts,
#             color=WHITE,
#             fill_color=WHITE,
#             fill_opacity=0.25,
#         )

#         self.play(Create(bivector_polygon), run_time=1)

#         u_wedge_v_tex = (
#             MathTex(
#                 "\\vec{u} \\wedge \\vec{v}",
#                 color=WHITE,
#                 font_size=int(4 * TITLE_FONTSIZE / 3),
#             )
#             .next_to(bivector_2_name, DOWN)
#             .shift(DOWN * 0.5)
#         )

#         bivector_title = (
#             MathTex("Bivector", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3))
#             .next_to(vector_name, RIGHT)
#             .shift(RIGHT * 3)
#         )

#         self.play(Write(u_wedge_v_tex), Write(bivector_title), run_time=1)
#         self.wait(NOMINAL_WAIT_TIME)

#         # Draw a rotation symbol
#         rotation_symbol = MathTex(
#             "\\circlearrowright", color=WHITE, font_size=int(5 * TITLE_FONTSIZE / 3)
#         )
#         # Put it at the center of the two vectors (u + v) / 2
#         rotation_symbol.move_to((bivector_1.get_end() + bivector_2.get_end()) / 2)

#         self.play(Write(rotation_symbol), run_time=1)
#         self.wait(PAUSE_WAIT_TIME)

#         # *______________________________________________________________________
#         self.next_section("Bivector Orientation", skip_animations=True)
#         # *______________________________________________________________________

#         self.play(
#             ShowPassingFlash(bivector_polygon.copy().set_color(BLUE).set_opacity(1)),
#             run_time=3,
#         )
#         self.wait(NOMINAL_WAIT_TIME)

#         # * -------------------------------------
#         # * Mirror the bivector
#         # * -------------------------------------
#         left_rotation_symbol = MathTex(
#             "\\circlearrowleft", color=WHITE, font_size=int(5 * TITLE_FONTSIZE / 3)
#         )
#         left_rotation_symbol.move_to(rotation_symbol.get_center())

#         group = VGroup(
#             bivector_1,
#             bivector_2,
#             bivector_1_line,
#             bivector_2_line,
#             bivector_polygon,
#             rotation_symbol,
#             # u_wedge_v_tex,
#         )
#         group_copy = group.copy()
#         bivector_1_name_copy = (
#             bivector_1_name.copy().shift(RIGHT * 8.25).set_color(WHITE)
#         )
#         bivector_2_name_copy = (
#             bivector_2_name.copy().shift(RIGHT * 6.5).set_color(WHITE)
#         )
#         # u_wedge_v_tex_copy = u_wedge_v_tex.copy().shift(RIGHT * 6.5).set_color(WHITE)

#         mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
#         # group_copy.apply_matrix(mirror_matrix)
#         self.play(
#             group_copy.animate.apply_matrix(mirror_matrix),
#             #   group_copy.animate.shift(RIGHT * 4),
#             run_time=0.5,
#         )
#         self.play(
#             group_copy.animate.shift(RIGHT * 5),
#             TransformFromCopy(bivector_1_name, bivector_1_name_copy),
#             TransformFromCopy(bivector_2_name, bivector_2_name_copy),
#             # TransformFromCopy(u_wedge_v_tex, u_wedge_v_tex_copy),
#             run_time=1,
#         )
#         self.play(
#             ShowPassingFlash(group_copy[-2].copy().set_color(BLUE).set_opacity(1)),
#             run_time=3,
#         )

#         self.wait(PAUSE_WAIT_TIME)

#         # * -------------------------------------
#         # * Color everything
#         # * -------------------------------------

#         bivector_1_name_redone = MathTex(
#             "\\mathbf{u}", color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(bivector_1_name.get_center())
#         bivector_2_name_redone = MathTex(
#             "\\mathbf{v}", color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(bivector_2_name.get_center())

#         bivector_1_name_copy_redone = MathTex(
#             "\\mathbf{u}", color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(bivector_1_name_copy.get_center())
#         bivector_2_name_copy_redone = MathTex(
#             "\\mathbf{v}", color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(bivector_2_name_copy.get_center())

#         # Color the vectors as well
#         bivector_1.z_index = 10
#         bivector_2.z_index = 10
#         group_copy[0].z_index = 10
#         group_copy[1].z_index = 10

#         self.play(
#             Transform(bivector_1_name, bivector_1_name_redone),
#             Transform(bivector_2_name, bivector_2_name_redone),
#             Transform(bivector_1_name_copy, bivector_1_name_copy_redone),
#             Transform(bivector_2_name_copy, bivector_2_name_copy_redone),
#             Transform(bivector_1, bivector_1.copy().set_color(RED)),
#             Transform(bivector_2, bivector_2.copy().set_color(BLUE)),
#             Transform(group_copy[0], group_copy[0].copy().set_color(RED)),
#             Transform(group_copy[1], group_copy[1].copy().set_color(BLUE)),
#             run_time=1,
#         )

#         u_wedge_v_tex_redone = MathTex(
#             "\\mathbf{u} \\wedge \\mathbf{v}",
#             tex_to_color_map={"\\mathbf{u}": RED, "\\mathbf{v}": BLUE},
#             font_size=int(4 * TITLE_FONTSIZE / 3),
#         ).move_to(u_wedge_v_tex.get_center())

#         self.play(
#             Transform(u_wedge_v_tex, u_wedge_v_tex_redone),
#             # Transform(u_wedge_v_tex_copy, u_wedge_v_tex_copy_redone),
#             Transform(bivector_1_name_copy, bivector_1_name_copy_redone),
#             Transform(bivector_2_name_copy, bivector_2_name_copy_redone),
#             run_time=1,
#         )
#         self.remove(bivector_1_name_copy, bivector_2_name_copy)

#         # * -------------------------------------
#         # * Flip Orientation
#         # * -------------------------------------

#         # Swap u and v in the copy
#         right_rotation_symbol = rotation_symbol.copy().move_to(
#             (group_copy[0].get_end() + group_copy[1].get_end()) / 2
#         )

#         self.play(
#             group_copy[0].animate.rotate(PI / 4, about_point=group_copy[1].get_start()),
#             group_copy[1].animate.rotate(
#                 -PI / 4, about_point=group_copy[0].get_start()
#             ),
#             # Move u text to v's position and vice versa
#             Swap(bivector_1_name_copy_redone, bivector_2_name_copy_redone),
#             Transform(group_copy[-1], right_rotation_symbol),
#             run_time=1,
#         )

#         self.wait(PAUSE_WAIT_TIME)

#         # * -------------------------------------
#         # * Mirror the bivector - again
#         # * -------------------------------------
#         # Rotate the copy by 180 degrees about its center
#         # Ensure an update function that always moves v text to the left of the vector and u text under the vector
#         text_draw = always_redraw(
#             lambda: VGroup(
#                 bivector_1_name_copy_redone.move_to(
#                     group_copy[0].get_center() + DOWN * 0.5
#                 ),
#                 bivector_2_name_copy_redone.move_to(
#                     group_copy[1].get_center() + LEFT * 0.5
#                 ),
#             )
#         )
#         self.add(text_draw)

#         group_copy_center = group_copy.get_center()
#         self.play(
#             group_copy.animate.rotate(PI / 2, about_point=group_copy_center),
#             run_time=1,
#         )
#         self.play(
#             group_copy.animate.rotate(PI / 2, about_point=group_copy_center),
#             run_time=1,
#         )

#         # Flip across y-axis
#         mirror_matrix = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])
#         self.play(
#             group_copy.animate.apply_matrix(mirror_matrix),
#             run_time=1,
#         )
#         # Now move it up
#         diff = bivector_1.get_end() - group_copy[1].get_end()
#         diff += np.array([4, 0, 0])

#         self.play(
#             group_copy.animate.shift(diff),
#             # group_copy.animate.shift(abs(diff[1])),
#             run_time=1,
#         )
#         self.wait(NOMINAL_WAIT_TIME)

#         # Add - v wedge u text
#         v_wedge_u_tex = MathTex(
#             "\\mathbf{u} \\wedge \\mathbf{v} = -\\mathbf{v} \\wedge \\mathbf{u}",
#             tex_to_color_map={"\\mathbf{u}": RED, "\\mathbf{v}": BLUE},
#             font_size=int(4 * TITLE_FONTSIZE / 3),
#         ).move_to(u_wedge_v_tex.get_center() + RIGHT * 2)

#         self.play(Transform(u_wedge_v_tex, v_wedge_u_tex), runtime=1)
#         self.play(
#             Indicate(group_copy[-1], rate_func=there_and_back),
#             Indicate(rotation_symbol, rate_func=there_and_back),
#             run_time=3,
#         )
#         self.wait(NOMINAL_WAIT_TIME)

#         # Box the result
#         box = SurroundingRectangle(
#             u_wedge_v_tex, buff=0.3, color=WHITE, corner_radius=0.005
#         )

#         # Now all those should become a group
#         # wedge_product_group = VGroup(u_wedge_v_tex, box)

#         self.play(Create(box), run_time=1)
#         # self.play(wedge_product_group.animate.to_edge(LEFT), run_time=1)
#         self.wait(PAUSE_WAIT_TIME)

#         # self.next_section("Trivectors", skip_animations=False)

#         # * Create a 3d scene within the current scene
#         # * -------------------------------------
#         # * Set up axes
#         # * -------------------------------------
#         # self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
#         # Fade everything away
#         self.play(
#             *[FadeOut(mob)for mob in self.mobjects]
#         )



# class Trivectors(ThreeDScene):

#     def construct(self):
#         # * ______________________________________________________________________
#         self.next_section("Title", skip_animations=False)
#         # * ______________________________________________________________________
#         title = Text(
#             f'Trivectors', color=BLUE_D,
#             font_size=TITLE_FONTSIZE
#         )
#         title.to_corner(UL)
        
#         basis_vectors_text = MathTex(
#             " \{ \\mathbf{e}_1 , \\mathbf{e}_2 , \\mathbf{e}_3 \}",
#             color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).to_corner(UL).shift0.75)
        
#         self.add_fixed_in_frame_mobjects(title)
#         self.play(Write(title), run_time=3)


#         # * ______________________________________________________________________
#         self.next_section("Axes", skip_animations=False)
#         # * ______________________________________________________________________

#         CONFIG = {
#             "x_axis_label": "$x$",
#             "y_axis_label": "$y$",
#             "z_axis_label": "$z$",
#             "basis_i_color": GREEN_D,
#             "basis_j_color": RED_D,
#             "basis_k_color": BLUE_D
#         }
        
#         axes = ThreeDAxes(
#             x_range=(-10, 10, 1),
#             y_range=(-10, 10, 1),
#             z_range=(-8, 8, 1),
#             x_length=8,
#             y_length=8,
#             z_length=5,
#         ).set_opacity(0.5)
#         self.add_fixed_in_frame_mobjects(basis_vectors_text)
#         self.play(
#             Create(axes),
#             Write(basis_vectors_text),
#             run_time=3,
#         )
#         self.move_camera(phi=70*DEGREES,theta=45*DEGREES + 15*DEGREES,run_time=3)
#         self.wait(NOMINAL_WAIT_TIME)


        

#         # * ______________________________________________________________________
#         self.next_section("Basis Vectors", skip_animations=False)
#         # * ______________________________________________________________________

#         # Create 3 basis vectors
#         i_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([1, 0, 0]), color=CONFIG["basis_i_color"])
#         j_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([0, 1, 0]), color=CONFIG["basis_j_color"])
#         k_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([0, 0, 1]), color=CONFIG["basis_k_color"])
        
#         for vector in [i_hat, j_hat, k_hat]:
#             self.play(
#                 Write(vector, run_time=1),
#                 # GrowArrow(vector, run_time=1),
#                 # vector.animate.Create(), runtime=1
#             )
        
#         # Add labeling math tex for each vector
#         i_hat_label = MathTex(
#             "\\mathbf{e}_1", color=CONFIG["basis_i_color"], font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).next_to(i_hat, RIGHT) #.set_stroke(width=0, family=False).set_shaded_in_3d(True)
#         j_hat_label = MathTex(
#             "\\mathbf{e}_2", color=CONFIG["basis_j_color"], font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).next_to(j_hat, UP) #.set_stroke(width=0, family=False).set_shaded_in_3d(True)
#         k_hat_label = MathTex(
#             "\\mathbf{e}_3", color=CONFIG["basis_k_color"], font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).next_to(k_hat, OUT).shift(UP*.75) #.set_stroke(width=0, family=False).set_shaded_in_3d(True)

        
#         for obj in [i_hat_label, j_hat_label, k_hat_label]:
#             self.add_fixed_orientation_mobjects(obj)
#             obj.z_index = 10  # Ensure the labels are on top of the axes
#             self.play(
#                 Write(obj, run_time=1),
#             )
        

#         # self.stop_ambient_camera_rotation()
#         self.wait(NOMINAL_WAIT_TIME)
        
        
#         # * ______________________________________________________________________
#         self.next_section("Outer Product", skip_animations=False)
#         # * ______________________________________________________________________

#         # Wedge all 3 basis vectors
#         wedge_text = MathTex(
#             "\\mathbf{e}_1 \\wedge \\mathbf{e}_2 \\wedge \\mathbf{e}_3",
#             color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).to_corner(UL).shift(DOWN *2.25)
        
#         pseudoscalar = MathTex(
#             "\\mathbb{I} =  \\mathbf{e}_1 \\wedge \\mathbf{e}_2 \\wedge \\mathbf{e}_3",
#             color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).move_to(wedge_text.get_center()).shift(RIGHT * 0.75)
        
        
#         self.add_fixed_in_frame_mobjects(wedge_text)
#         self.play(
#             Write(wedge_text),
#             runtime=3
#         )
#         self.wait(NOMINAL_WAIT_TIME)
        
#         # Create a volume element trivector
#         cube = Cube(
#             side_length=2,
#             fill_opacity=0.5,
#             fill_color=BLUE
#         )
#         cube.move_to(np.array([1, 1, 1]))
        
#         self.play(
#             Write(cube),
#             run_time=3
#         )
#         self.wait(PAUSE_WAIT_TIME)
        
#         # * The pseudoscalar


#         self.play(
#             ReplacementTransform(wedge_text, pseudoscalar),
#             runtime=3
#         )
#         self.add_fixed_in_frame_mobjects(pseudoscalar)
        
#         self.wait(NOMINAL_WAIT_TIME)
        
        
#         # Add box around the pseudoscalar
#         pseudoscalar_box = SurroundingRectangle(
#             pseudoscalar, buff=0.3, color=WHITE, corner_radius=0.005
#         )
#         self.add_fixed_in_frame_mobjects(pseudoscalar_box)
#         self.play(Create(pseudoscalar_box), run_time=1)
#         self.wait(NOMINAL_WAIT_TIME)
        
#         # *  Indicate the pseudoscalar 
#         pseudoscalar_label = MathTex(
#             "\\text{Pseudoscalar}",
#             color=YELLOW,
#             font_size=int(3 * TITLE_FONTSIZE / 3),
#         ).next_to(pseudoscalar, DOWN).shift(DOWN * 0.5)
#         self.add_fixed_in_frame_mobjects(pseudoscalar_label)

#         self.play(
#             Indicate(pseudoscalar[0][0:1], rate_func=there_and_back),  # Indicate only \mathbb{I}
#             Write(pseudoscalar_label),
#             run_time=4,
#         )
#         self.wait(PAUSE_WAIT_TIME)
        

#         # * ______________________________________________________________________
#         self.next_section("Multivectors", skip_animations=False)
#         # * ______________________________________________________________________ 
#         multivector_title = Text(
#             "Multivectors", color=BLUE_D,
#             font_size=TITLE_FONTSIZE
#         ).to_corner(UR)
        
#         multivector_text = MathTex(
#             "\\mathbf{e}_1 \\wedge \\mathbf{e}_2 \\wedge \\mathbf{e}_3 \\wedge \\mathbf{e}_4 ... \\wedge \\mathbf{e}_n",
#             color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
#         ).to_corner(UR).shift(DOWN *1)
        
#         self.add_fixed_in_frame_mobjects(multivector_title)
#         self.play(
#             Write(multivector_title),
#             runtime=3
#         )
#         self.wait(NOMINAL_WAIT_TIME)
        
#         self.add_fixed_in_frame_mobjects(multivector_text)
#         self.play(
#             Write(multivector_text),
#             runtime=3
#         )
#         self.wait(PAUSE_WAIT_TIME)
        
#         # Fade everything away
#         self.play(
#             *[FadeOut(mob)for mob in self.mobjects]
#         )

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




class GeometricProduct(VectorScene):

    def construct(self):
        
        # * ______________________________________________________________________
        self.next_section("Title", skip_animations=True)
        # * ______________________________________________________________________
        title = Text(
            f'The Geometric Product', color=BLUE_D,
            font_size=TITLE_FONTSIZE
        )
        title.to_edge(UP)
        
        # Geo product of u and v
        uterm = MathTex( "\\mathbf{u}" )
        vterm = MathTex( "\\mathbf{v}" )
        
        
        geo_prod_tex = MathTex(
            uterm, vterm, "=", uterm, "\\cdot", vterm, "+", uterm, "\\wedge", vterm,
            # "\\mathbf{u}  \\mathbf{v}  = \\mathbf{u} \\cdot \\mathbf{v} + \\mathbf{u} \\wedge \\mathbf{v}",
            color=WHITE, font_size=int(4 * TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *1.5)
        
        geo_prod_box = SurroundingRectangle(
            geo_prod_tex, buff=0.3, color=WHITE, corner_radius=0.005
        )
        
        self.play(Write(title), run_time=2)
        
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            Write(geo_prod_tex),
            Create(geo_prod_box),
            runtime=3
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("Complex Numbers", skip_animations=True)
        # * ______________________________________________________________________
        
        z1 = MathTex("z_1", "=", "a" "+", "i", "b", 
            # tex_to_color_map={"i": BLUE_C},
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *3 + LEFT*1.75)
        z1[3].set_color(BLUE_C)         
        
        z2 = MathTex(
            # "z_2 = c - i b",
            "z_2", "=", "c", "-", "i", "d",
            # tex_to_color_map={"i": BLUE_C},
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *3 + RIGHT*1.75)
        z2[4].set_color(BLUE_C)
        
        self.play(
            Write(z1),
            runtime=3
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        self.play(
            Write(z2),
            runtime=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        z1_plus_z2 = MathTex(
            "z_1 + z_2", "=", "(a + c)", "+", "(b - d)", "i",
            # "z_1 + z_2 = (a + c) + (b - d) i",
            # tex_to_color_map={"i": BLUE_C},
            color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *4)
        z1_plus_z2[-1].set_color(BLUE_C)

        self.play(
            Write(z1_plus_z2),
            runtime=3
        )
        
        self.wait(PAUSE_WAIT_TIME)
        
        #  FadeOut all complex text
        self.play(
            FadeOut(z1),
            FadeOut(z2),
            FadeOut(z1_plus_z2),
            runtime=2
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            FadeOut(title),
            FadeOut(geo_prod_box),
            runtime=1.5
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Vector Setup", skip_animations=True)
        # * ______________________________________________________________________
        
        
        # Create a grid
        grid = NumberPlane(
            x_range=(-4, 4, 1),
            y_range=(-4, 4, 1),
            x_length=14,
            y_length=14,
            axis_config={"color": WHITE},
        ).set_opacity(0.5)
        
        self.play(
            geo_prod_tex.animate.to_corner(UL).shift(DOWN * 0.75),
            Create(grid),
            run_time=3
        )
        
        u = self.add_vector(1.75*np.array([1, 0, 0]), color=RED)
        v = self.add_vector(1.75*np.array([0, 1, 0]), color=BLUE)
        u.z_index = 10
        v.z_index = 10
        
        # Lavbel the basis vectors u and v (u is red, v is blue)
        u_label = MathTex(
            uterm, color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(u, DOWN)
        v_label = MathTex(
            vterm, color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(v, LEFT)
        
        self.play(
            Write(u_label),
            Write(v_label),
            runtime=2
        )
        
                
        # * ______________________________________________________________________
        self.next_section("Label Setup", skip_animations=True)
        # * ______________________________________________________________________
        
        
        left_rotation_symbol = MathTex(
            "\\circlearrowleft", color=WHITE, font_size=int(5 * TITLE_FONTSIZE / 3)
        ).move_to((u.get_end() + v.get_end()) / 2)

        # * Recolor text
        uterm.set_color(RED)
        vterm.set_color(BLUE)
        
        geo_prod_tex[0] = uterm
        geo_prod_tex[1] = vterm
        self.play( TransformInStages.progress(geo_prod_tex, lag_ratio=0.5))
        
        geo_prod_tex[3] = uterm
        geo_prod_tex[5] = vterm
        self.play( TransformInStages.progress(geo_prod_tex, lag_ratio=0.5))
        
        geo_prod_tex[-3] = uterm
        geo_prod_tex[-1] = vterm
        self.play( TransformInStages.progress(geo_prod_tex, lag_ratio=0.5))

        self.wait(NOMINAL_WAIT_TIME)
        
        e1_term = MathTex( "\\mathbf{e_1}" ).set_color(RED)
        e2_term = MathTex( "\\mathbf{e_2}" ).set_color(BLUE)
        
        geo_prod_tex.shift(RIGHT*0.75)
        
        geo_prod_tex[0] = e1_term
        geo_prod_tex[1] = e2_term
        
        u_label[0] = e1_term
        v_label[0] = e2_term
        
        self.play( 
            TransformInStages.progress(geo_prod_tex, lag_ratio=0.5),
            TransformInStages.progress(u_label, lag_ratio=0.5),
            TransformInStages.progress(v_label, lag_ratio=0.5)
        )
        
        geo_prod_tex[3] = e1_term
        geo_prod_tex[5] = e2_term
        self.play( TransformInStages.progress(geo_prod_tex, lag_ratio=0.5))
        
        geo_prod_tex[-3] = e1_term
        geo_prod_tex[-1] = e2_term
        self.play( TransformInStages.progress(geo_prod_tex, lag_ratio=0.5))
        
                
        # * ______________________________________________________________________
        self.next_section("Parallelogram Setup", skip_animations=True)
        # * ______________________________________________________________________
        

        
        def get_parallelogram():
            return always_redraw(lambda: Polygon(
                ORIGIN,
                u.get_end(),
                u.get_end() + v.get_end(),
                v.get_end(),
                color=BLUE_A,
                fill_opacity=0.25
            ))

        parallelogram = always_redraw(get_parallelogram)
        # self.add(parallelogram)

        self.play(
            Create(parallelogram),
            Write(left_rotation_symbol),
            runtime=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Wedge Simplification", skip_animations=True)
        # * ______________________________________________________________________
        
        cross = Cross(geo_prod_tex[3] +  geo_prod_tex[4] + geo_prod_tex[5] ).scale(0.35)
        self.play(
            Write(cross),
            Indicate(geo_prod_tex[3], rate_func=there_and_back),
            Indicate(geo_prod_tex[4], rate_func=there_and_back),
            Indicate(geo_prod_tex[5], rate_func=there_and_back),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        geo_prod_tex[4:8] = ""
        self.play(
                FadeOut(cross), 
                  TransformInStages.progress(geo_prod_tex, lag_ratio=0.5)
                  )
        
        box_wedge_simple = SurroundingRectangle(
            geo_prod_tex, buff=0.3, color=WHITE, corner_radius=0.005
        )
        
        self.play(
            Create(box_wedge_simple),
            run_time=2
        )
        
        self.wait(PAUSE_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("Zero Wedge", skip_animations=True)
        # * ______________________________________________________________________

        wedge_term = MathTex(geo_prod_tex[-3].copy(), geo_prod_tex[-2].copy(), geo_prod_tex[-1].copy(), 
             font_size=int(4 * TITLE_FONTSIZE / 3)
        ).to_corner(UR).shift(DOWN *0.75 + LEFT*2)
        
        self.play(
            TransformInStages.from_copy(geo_prod_tex, wedge_term, lag_ratio=0.5, run_time=2),
            runtime=2
        )
        
        self.wait(PAUSE_WAIT_TIME)
        
        v_label[0] = e1_term
        v_label.move_to(u_label.get_center() + RIGHT* 0.5)

        self.play(
            v.animate.rotate(-PI / 2, about_point=ORIGIN),
            TransformInStages.progress(v_label, lag_ratio=1, run_time=1.5),
            FadeOut(left_rotation_symbol),
            run_time=2,
        )
        self.wait(1)
        
        wedge_term[2] = e1_term
        anim = TransformInStages.progress(wedge_term, lag_ratio=0.5, run_time=2)
        anim.intercept(v_label).set_source(v_label)

        self.play(
            FadeOut(parallelogram),
            v.animate.set_color(RED),
            anim
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        wedge_term.append("=")
        wedge_term.append("0")
        self.play(
            TransformInStages.progress(wedge_term, lag_ratio=0.5, run_time=2),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("Dot Simplification", skip_animations=True)
        # * ______________________________________________________________________

        e1_e1_tex = MathTex(e1_term, e1_term, "=", e1_term, "\\cdot", e1_term,
                            font_size=int(4 * TITLE_FONTSIZE / 3))
        e1_e1_tex.to_corner(UR).shift(DOWN * 2 + LEFT * 1)

        self.play(
            TransformMatchingTex(v_label.copy(), e1_e1_tex),
            runtime=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        e1_e1_tex.append("=")
        e1_e1_tex.append("1")
        self.play(
            TransformInStages.progress(e1_e1_tex, lag_ratio=0.5, run_time=2),
        )
        # self.wait(NOMINAL_WAIT_TIME)
        wedge_term_center = wedge_term.get_center()
        e1_e1_tex.move_to(wedge_term_center)
        
        self.play(
            FadeOut(wedge_term),
            TransformInStages.progress(e1_e1_tex, lag_ratio=0.5, run_time=2),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Create a box around that final result
        box_dot_simple = SurroundingRectangle(
            e1_e1_tex, buff=0.3, color=WHITE, corner_radius=0.005
        )
        self.play(
            Create(box_dot_simple),
            run_time=2
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("General Case", skip_animations=False)
        # * ______________________________________________________________________
        
        e_i = MathTex(
            "\\mathbf{e}_i", color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
        )
        e_j = MathTex(
            "\\mathbf{e}_j", color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
        )
        
        general_case_wedge = MathTex(e_i, e_j, "=", e_i, "\\wedge", e_j,
            font_size=int(4 * TITLE_FONTSIZE / 3)
        ).move_to(geo_prod_tex.get_center())
        
        general_case_dot = MathTex(e_i, e_i, "=", e_i, "\\cdot", e_i, "=", "1",
            font_size=int(4 * TITLE_FONTSIZE / 3)
        ).move_to(box_dot_simple.get_center())
        
        self.play(
            TransformMatchingTex(e1_e1_tex, general_case_dot),
            TransformMatchingTex(geo_prod_tex, general_case_wedge),
            runtime=3
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # Fade out everything
        self.play(
            [FadeOut(mob) for mob in self.mobjects]
        )
        
        
        
# class GeometricProduct(LinearTransformationScene, MovingCameraScene):
#     def __init__(self):
#         LinearTransformationScene.__init__(
#         self,
#         show_coordinates=False,
#         include_background_plane=False,
#         include_foreground_plane=True,
#         leave_ghost_vectors=True,
#         show_basis_vectors=False,
#         i_hat_color=BLUE,
#         j_hat_color=RED,
#         # background_plane_kwargs={"x_range": [-4, 4, 1], "y_range": [-2.25, 2.25, 1], "x_length": 14.22,
#                                 #  "y_length": 8},
#         foreground_plane_kwargs={"x_range": [-4, 4, 1],
#                                  "y_range": [-4, 4, 1], 
#                                  "x_length": 8,
#                                  "y_length": 8
#                                  },
        
#         background_plane_kwargs={"x_range": [-4, 4, 1],
#                                  "y_range": [-4, 4, 1], 
#                                  "x_length": 8,
#                                  "y_length": 8}
#     )

    # def construct(self):





        
        # u, v = self.get_basis_vectors()
        # u.z_index = 10; u.set_color(RED)
        # v.z_index = 10; v.set_color(BLUE)
        
        # self.play(self.camera.frame.animate.set(width=8))
                
        # # Draw the vectors
        # self.play(
        #     GrowArrow(u),
        #     GrowArrow(v),
        #     run_time=2
        # )
        
        # self.add_unit_square()
        # # self.play(
        # #     Create(self.square),
        # #     runtime=2
        # # )
        # u_coords = np.array([1, 0])
        # v_coords = np.array([0, 1])
        
        
        # transform = self.get_matrix_transformation(np.array([
        #     # self.v_coords, 
        #     # self.w_coords,
        #     u_coords, v_coords,
        #     # u.get_end(), u.get_start(),
        #     # v.get_end(), v.get_start()
        # ]))
        # self.square.apply_function(transform)
        # self.play(
        #     Create(self.square),
        #     *list(map(Animation, [u, v]))
        # )
        # self.wait()
        
        # # Rotate u by 90 degrees and transform the unit area
        # self.play(
        #     v.animate.rotate(PI/2, about_point=v.get_start()),
        #     self.square.animate.apply_function(
        #     lambda p: np.dot([[0, -1], [1, 0]], p[:2])  # 90-degree rotation matrix
        #     ),
        #     run_time=1
        # )