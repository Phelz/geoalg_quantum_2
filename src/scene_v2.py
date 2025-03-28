from manim import *


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


# class GeometricAlgebra(VectorScene):
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



class CrossProduct(ThreeDScene):

    def construct(self):
        # * ______________________________________________________________________
        self.next_section("Axes", skip_animations=False)
        # * ______________________________________________________________________
        
        axes = ThreeDAxes(
            x_range=(-10, 10, 1),
            y_range=(-10, 10, 1),
            z_range=(-8, 8, 1),
            x_length=8,
            y_length=8,
            z_length=5,
        )
        circle=Circle()
        self.play(ShowCreation(circle),ShowCreation(axes))
        self.move_camera(phi=30*DEGREES,theta=-45*DEGREES,run_time=3)
        self.wait()


#     def construct(self):
#         # *______________________________________________________________________
#         self.next_section("Axes", skip_animations=True)
#         # *______________________________________________________________________
#         #
        
#         # * ------------------------------------- 
#         # * Set up axes
#         # * ------------------------------------- 
#         self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

#         self.begin_ambient_camera_rotation(
#             rate=PI/10, about="theta"
#         )
#         # axes.set_width(FRAME_WIDTH)
#         # axes.center()

# #         # self.frame.reorient(43, 76, 1, IN, 10)
# #         # self.frame.add_updater(lambda m, dt: m.increment_theta(dt * 3 * DEGREES))

#         self.next_section("Basis Vectors", skip_animations=False)
#         self.play(FadeIn(axes), run_time=3)

# #         # Create the basis vectors
#         i_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([1, 0, 0]), color=RED)
#         j_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([0, 1, 0]), color=GREEN)
#         k_hat = Arrow3D(np.array([0, 0, 0]), 2*np.array([0, 0, 1]), color=BLUE)
#         self.play(
#             Write(i_hat),
#             Write(j_hat),
#             Write(k_hat),
#             run_time=2
#         )

#         # self.play(
#         #     GrowArrow(i_hat),
#         #     GrowArrow(j_hat),
#         #     GrowArrow(k_hat),
#         #     run_time=2
#         # )

#         self.next_section("Trivector", skip_animations=False)

#         cube = Cube(side_length=2, fill_opacity=0.5, fill_color=BLUE)
#         cube.move_to(np.array([1, 1, 1]))
#         # cube.init_points(
#         #     [
#         #     np.array([0, 0, 0]),
#         #     np.array([1, 0, 0]),
#         #     np.array([1, 1, 0]),
#         #     np.array([0, 1, 0]),
#         #     np.array([0, 0, 1]),
#         #     np.array([1, 0, 1]),
#         #     np.array([1, 1, 1]),
#         #     np.array([0, 1, 1]),
#         #     ]

#         # )
#         self.play(Create(cube), run_time=2)



#         # # Create a volume element trivector
#         # convex_hull_3D_pts = [
#         #     np.array([0, 0, 0]),
#         #     np.array([1, 0, 0]),
#         #     np.array([1, 1, 0]),
#         #     np.array([0, 1, 0]),
#         #     np.array([0, 0, 1]),
#         #     np.array([1, 0, 1]),
#         #     np.array([1, 1, 1]),
#         #     np.array([0, 1, 1]),
#         # ]
#         # hull = ConvexHull3D(
#         #         *convex_hull_3D_pts,
#         #         faces_config = {"stroke_opacity": 0},
#         #         graph_config = {
#         #             "vertex_type": Dot3D,
#         #             "edge_config": {
#         #                 "stroke_color": BLUE,
#         #                 "stroke_width": 2,
#         #                 "stroke_opacity": 0.05,
#         #             }
#         #         }
#         #     )

#         # dots = VGroup(*[Dot3D(pt) for pt in convex_hull_3D_pts])
#         # self.play(Create(hull), Create(dots), run_time=1)

