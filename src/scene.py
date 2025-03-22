from manim import *


TITLE_FONTSIZE = 45
NOMINAL_WAIT_TIME = 2
PAUSE_WAIT_TIME = 5

# class Intro(Scene):
#     def construct(self):

#         self.next_section("Intro", skip_animations=True)
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


class GeometricAlgebra(VectorScene):
    def construct(self):
        self.next_section("Scalars and Vectors", skip_animations=True)

        title = MarkupText(
            "Geometric Algebra", color=BLUE_D, font_size=TITLE_FONTSIZE
        ).to_edge(UP)
        self.add(title)

        # * Scalar
        point = np.array([-3, 0, 0])
        dot = Dot(point, color=WHITE)
        dot_name = MathTex(
            "Scalar", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(dot, UP)
        self.play(Create(dot), Write(dot_name), run_time=1)
        self.wait(NOMINAL_WAIT_TIME)

        # * Vector
        vector = self.add_vector(
            [1.5, 1.5],
            color=WHITE,
        )
        vector_name = MathTex(
            "Vector", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(vector, UP)
        self.play(Write(vector_name), run_time=1)
        self.wait(2)
        # * ___________________________________
        self.next_section("Bivectors", skip_animations=True)

        # Move both to the left using coordinates
        self.play(
            dot.animate.shift(LEFT * 3),
            dot_name.animate.shift(LEFT * 3),
            vector.animate.shift(LEFT * 4),
            vector.animate.shift(LEFT * 4),
            vector_name.animate.shift(LEFT * 4.5),
            run_time=1,
        )
        self.wait(NOMINAL_WAIT_TIME)

        # Copy the vector over to the right
        bivector_1 = vector.copy().shift(RIGHT * 2.5)
        bivector_1_name = MathTex(
            "\\vec{u}", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(bivector_1, LEFT)

        self.play(
            Transform(vector.copy(), bivector_1), Write(bivector_1_name), run_time=1
        )
        self.wait(NOMINAL_WAIT_TIME)

        # Createa vector orthogonal to bivector_1
        bivector_2 = bivector_1.copy()
        bivector_2_name = MathTex(
            "\\vec{v}", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(bivector_2, DOWN)

        # The rotation should be 90 degrees relative to the bivector_1
        self.play(
            bivector_2.animate.rotate(-PI / 4, about_point=bivector_1.get_start()),
            Write(bivector_2_name),
            run_time=1,
        )
        self.wait(NOMINAL_WAIT_TIME)

        bivector_1_line = Line(
            bivector_1.get_start(), bivector_1.get_end(), color=WHITE
        )
        bivector_2_line = Line(
            bivector_2.get_start(), bivector_2.get_end(), color=WHITE
        )

        # Shift bivector_1_line's tail to the tip of bivector_2
        self.play(
            bivector_1_line.animate.shift(
                bivector_2.get_end() - bivector_1_line.get_start()
            ),
            bivector_2_line.animate.shift(
                bivector_1.get_end() - bivector_2_line.get_start()
            ),
            run_time=1,
        )

        # Create a filled polygon from the tails of all 4 points
        polygon_pts = [
            bivector_1.get_start(),
            bivector_1.get_end(),
            bivector_2_line.get_end(),
            bivector_1_line.get_start(),
        ]

        bivector_hull = Polygon(
            *polygon_pts,
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=0.25,
        )

        self.play(Create(bivector_hull), run_time=1)

        bivector_name = (
            MathTex(
                "\\vec{u} \\wedge \\vec{v}",
                color=WHITE,
                font_size=int(3 * TITLE_FONTSIZE / 3),
            )
            .next_to(bivector_2_name, DOWN)
            .shift(DOWN * 0.5)
        )

        bivector_title = (
            MathTex("Bivector", color=WHITE, font_size=int(3 * TITLE_FONTSIZE / 3))
            .next_to(vector_name, RIGHT)
            .shift(RIGHT * 3)
        )

        self.play(Write(bivector_name), Write(bivector_title), run_time=1)
        self.wait(NOMINAL_WAIT_TIME)

        # Draw a rotation symbol
        rotation_symbol = MathTex(
            "\\circlearrowright", color=WHITE, font_size=int(5 * TITLE_FONTSIZE / 3)
        )
        # Put it at the center of the two vectors (u + v) / 2
        rotation_symbol.move_to((bivector_1.get_end() + bivector_2.get_end()) / 2)

        self.play(Write(rotation_symbol), run_time=1)
        self.wait(PAUSE_WAIT_TIME)

        # *_____________________________________
        self.next_section("Bivector Orientation")  # , skip_animations=True)

        # Do a PassingFlash on the bivector
        self.play(
            ShowPassingFlash(bivector_hull.copy().set_color(BLUE).set_opacity(1)),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)

        # Transform the rotation symbol to a left rotation
        left_rotation_symbol = MathTex(
            "\\circlearrowleft", color=WHITE, font_size=int(5 * TITLE_FONTSIZE / 3)
        )
        left_rotation_symbol.move_to(rotation_symbol.get_center())

        group = VGroup(
            bivector_1,
            bivector_2,
            bivector_1_line,
            bivector_2_line,
            bivector_hull,
            rotation_symbol,
            # bivector_name,
        )
        group_copy = group.copy()
        bivector_1_name_copy = (
            bivector_1_name.copy().shift(RIGHT * 8.25).set_color(WHITE)
        )
        bivector_2_name_copy = (
            bivector_2_name.copy().shift(RIGHT * 6.5).set_color(WHITE)
        )
        bivector_name_copy = bivector_name.copy().shift(RIGHT * 6.5).set_color(WHITE)


        mirror_matrix = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])
        # group_copy.apply_matrix(mirror_matrix)
        self.play(
            group_copy.animate.apply_matrix(mirror_matrix),
            #   group_copy.animate.shift(RIGHT * 4),
            run_time=0.5,
        )
        self.play(
            group_copy.animate.shift(RIGHT * 5),
            TransformFromCopy(bivector_1_name, bivector_1_name_copy),
            TransformFromCopy(bivector_2_name, bivector_2_name_copy),
            TransformFromCopy(bivector_name, bivector_name_copy),
            run_time=1,
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.play(
            ShowPassingFlash(group_copy[-2].copy().set_color(BLUE).set_opacity(1)),
            run_time=3,
        )

        # Now color all u with RED in TEXT and v with BLUE in TEXT
        # Let's use new tex objects for this, with vectors now denoted with bold symbols
        bivector_1_name_redone = MathTex(
            "\\mathbf{u}", color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(bivector_1, LEFT)
        bivector_2_name_redone = MathTex(
            "\\mathbf{v}", color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).next_to(bivector_2, DOWN)

        bivector_1_name_copy_redone = MathTex(
            "\\mathbf{u}", color=RED, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).move_to(bivector_1_name_copy.get_center())
        bivector_2_name_copy_redone = MathTex(
            "\\mathbf{v}", color=BLUE, font_size=int(3 * TITLE_FONTSIZE / 3)
        ).move_to(bivector_2_name_copy.get_center())

        # Color the vectors as well
        bivector_1.z_index = 10
        bivector_2.z_index = 10
        group_copy[0].z_index = 10
        group_copy[1].z_index = 10

        self.play(
            Transform(bivector_1_name, bivector_1_name_redone),
            Transform(bivector_2_name, bivector_2_name_redone),
            Transform(bivector_1_name_copy, bivector_1_name_copy_redone),
            Transform(bivector_2_name_copy, bivector_2_name_copy_redone),
            Transform(bivector_1, bivector_1.copy().set_color(RED)),
            Transform(bivector_2, bivector_2.copy().set_color(BLUE)),
            Transform(group_copy[0], group_copy[0].copy().set_color(RED)),
            Transform(group_copy[1], group_copy[1].copy().set_color(BLUE)),
            run_time=1,
        )

        # Do the same for the bivector names
        bivector_name_redone = MathTex(
            "\\mathbf{u} \\wedge \\mathbf{v}",
            tex_to_color_map={"\\mathbf{u}": RED, "\\mathbf{v}": BLUE},
            font_size=int(3 * TITLE_FONTSIZE / 3),
        ).move_to(bivector_name.get_center())

        bivector_name_copy_redone = MathTex(
            "\\mathbf{u} \\wedge \\mathbf{v}",
            tex_to_color_map={"\\mathbf{u}": RED, "\\mathbf{v}": BLUE},
            font_size=int(3 * TITLE_FONTSIZE / 3),
        ).move_to(bivector_name_copy.get_center())

        self.play(
            Transform(bivector_name, bivector_name_redone),
            Transform(bivector_name_copy, bivector_name_copy_redone),
            Transform(bivector_1_name_copy, bivector_1_name_copy_redone),
            Transform(bivector_2_name_copy, bivector_2_name_copy_redone),
            run_time=1,
        )
        self.remove(bivector_1_name_copy, bivector_2_name_copy)

        # Swap u and v in the copy
        right_rotation_symbol = rotation_symbol.copy().move_to(
            (group_copy[0].get_end() + group_copy[1].get_end()) / 2
        )

        self.play(
            group_copy[0].animate.rotate(PI / 4, about_point=group_copy[1].get_start()),
            group_copy[1].animate.rotate(
                -PI / 4, about_point=group_copy[0].get_start()
            ),
            # Move u text to v's position and vice versa
            Swap(bivector_1_name_copy_redone, bivector_2_name_copy_redone),
            Transform(group_copy[-1], right_rotation_symbol),

            run_time=1,
        )

            
        # self.remove(bivector_1_name_copy_redone, bivector_2_name_copy_redone)

        self.wait(NOMINAL_WAIT_TIME)

        # group_copy = group.copy().shift(RIGHT * 4)
        # # self.play(Create(group_copy), run_time=1)
        # self.play(TransformFromCopy(group, group_copy), run_time=1)
        # self.wait(NOMINAL_WAIT_TIME)

        # # Rotate everything in the group by 180 degrees about z-axis
        # # group_copy.rotate(PI, axis=OUT)
        # for item in group_copy[:-1]:
        #     # item.rotate(PI, axis=OUT)
        #     self.play(item.animate.rotate(PI, axis=OUT), run_time=1)
        # self.wait(NOMINAL_WAIT_TIME)

        # # Create a copy of u and v text
        # bivector_1_name_copy = bivector_1_name.copy().shift(RIGHT * 4).set_color(RED)
        # bivector_2_name_copy = bivector_2_name.copy().shift(RIGHT * 4).set_color(BLUE)
        # self.play(Write(bivector_1_name_copy), Write(bivector_2_name_copy), run_time=1)
