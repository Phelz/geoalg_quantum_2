from manim import *

vec_a_color = RED
vec_b_color = YELLOW
vec_c_color = BLUE


class Calculations(Scene):
    def construct(self):
        pass
        # self.mat_kwargs = {
        #     "v_buff": 0.6, 
        #     "left_bracket": "(", 
        #     "right_bracket": ")",
        #     "bracket_v_buff": 0.1
        # }

    def get_vector_matrix_from_num_vec(self, num_vec, dimension = 3, **mat_kwargs):
        if dimension == 3:
            mat = Matrix([[num_vec[0]], [num_vec[1]], [num_vec[2]]], **mat_kwargs)
        elif dimension == 2:
            mat = Matrix([[num_vec[0]], [num_vec[1]]], **mat_kwargs)

        return mat

    def group_vecs_with_symbol(self, mat_a, mat_b, type = "dot", color = WHITE):
        if type is "dot":
            mult = MathTex("\\cdot").set_color(color)
        elif type is "bullet":
            mult = MathTex("\\bullet").set_color(color)
        elif type is "cdot":
            mult = MathTex("\\cdot").set_color(color)
        else:
            mult = MathTex("\\times").set_color(color)

        group = VGroup(mat_a, mult, mat_b)
        group.arrange_submobjects(RIGHT)

        return group

    def get_dotproduct_path(self, vec_group, dimension = 3, color = LIGHT_BROWN, stroke_width = 5):
        path = VMobject()
        if dimension == 3:
            path.set_points_smoothly([
                vec_group[0][0][0].get_center(),     # x Kompenente vec1 und vec2
                vec_group[2][0][0].get_center(),
                vec_group[0][0][1].get_center(),     # y Kompenente vec1 und vec2
                vec_group[2][0][1].get_center(),
                vec_group[0][0][2].get_center(),     # z Kompenente vec1 und vec2
                vec_group[2][0][2].get_center(),
            ])
        elif dimension == 2:
            path.set_points_smoothly([
                vec_group[0][0][0].get_center(),     # x Kompenente vec1 und vec2
                vec_group[2][0][0].get_center(),
                vec_group[0][0][1].get_center(),     # y Kompenente vec1 und vec2
                vec_group[2][0][1].get_center(),
            ])

        path.set_color(color = color)
        path.set_stroke(width = stroke_width)

        return path

    def get_crossproduct_path_xyz(self, vec_group, color = ORANGE, stroke_width = 5):
        path_x, path_y, path_z = VMobject(), VMobject(), VMobject()

        # vec_group[0] --> erster Vektor, maths[1][1] Mal zeichen, maths[1][2] zweiter Vektor
        # vec_group[i][0] --> Vektoreinträge
        # vec_group[i][0][j] --> x,y,z Komponente

        path_x.set_points_smoothly([
            vec_group[0][0][1].get_center(),     # y Komponente vec1
            vec_group[2][0][2].get_center(),     # z Komponente vec2
            vec_group[0][0][2].get_center(),     # y Komponente vec1
            vec_group[2][0][1].get_center(),     # z Komponente vec2
        ])

        path_y.set_points_smoothly([
            vec_group[0][0][2].get_center(),     # z Komponente vec1
            vec_group[2][0][0].get_center(),     # x Komponente vec2
            vec_group[0][0][0].get_center(),     # x Komponente vec1
            vec_group[2][0][2].get_center(),     # z Komponente vec2
        ])

        path_z.set_points_smoothly([
            vec_group[0][0][0].get_center(),     # x Komponente vec1
            vec_group[2][0][1].get_center(),     # y Komponente vec2
            vec_group[0][0][1].get_center(),     # y Komponente vec1
            vec_group[2][0][0].get_center(),     # x Komponente vec2
        ])

        for path in path_x, path_y, path_z:
            path.set_color(color).set_stroke(width = stroke_width)

        return path_x, path_y, path_z

    def get_crossproduct_cut_lines(self, vec_group, color, line_buff = 0.1):
        line_buff = 0.1
        if color is None:
            color = LIGHT_BROWN

        lines = VGroup(*[
            Line(
                vec_group.get_left() + line_buff * LEFT, vec_group.get_right() + line_buff * RIGHT, 
                color = color, stroke_width = 5
            )
            for x in range(3)
        ])
        lines.arrange_submobjects(DOWN, buff = self.mat_kwargs.get("v_buff"))
        lines.move_to(vec_group)

        return lines

    def get_lines_for_comp_calc(self, vec_group, comp1, comp2, **kwargs):
        line1 = Line(
            start = vec_group[0][0][comp1].get_right(), 
            end = vec_group[2][0][comp2].get_left(),
            **kwargs
        )
        line2 = Line(
            start = vec_group[0][0][comp2].get_right(),
            end = vec_group[2][0][comp1].get_left(),
            **kwargs
        )

        lines = VGroup(line1, line2)

        return lines



class ProjectionScene(VectorScene):
    def constuct(self):
        pass

    def get_plane(self, **kwargs):
        self.plane = NumberPlane(**kwargs)
        self.plane.add_coordinates()
        self.origin = self.plane.c2p(0,0)

        return self.plane

    def get_vecs_from_nums(self, vec_a_num, vec_b_num):
        return VGroup(*[
            self.get_vector(vec_num, color = color)
            for vec_num, color in zip([vec_a_num, vec_b_num], [vec_a_color, vec_b_color])
        ])

    def get_parallelogramm_from_vecs(self, vec_a, vec_b, fill_opacity = 0.25):
        parallelo = VMobject()\
            .set_points_as_corners([
                vec_a.get_start(), vec_a.get_end(), vec_a.get_end() + vec_b.get_end(), vec_b.get_end(), vec_b.get_start()
            ])\
            .set_fill(color = vec_c_color, opacity = fill_opacity)\
            .set_stroke(color = BLUE, width = 2)

        return parallelo

    def get_projection_vec(self, num_vec_a, num_vec_b, **kwargs):
        cross_prod_value = np.dot(num_vec_a, num_vec_b)
        cross_prod_norm = cross_prod_value / np.linalg.norm(num_vec_a)**2

        start = self.origin
        end = self.plane.c2p(*[cross_prod_norm * x for x in num_vec_a])

        projection_vec = Arrow(start, end, buff = 0, **kwargs)

        return projection_vec

    def get_projection_line(self, num_vec_a, num_vec_b, **kwargs):
        pro_vec = self.get_projection_vec(num_vec_a, num_vec_b)

        line = Line(
            start = self.plane.c2p(*num_vec_b),
            end = pro_vec.get_end(),
            **kwargs
        )

        return line
    
    
# class Definition(Calculations):
#     def construct(self):
#         self.mat_kwargs = {
#             "v_buff": 0.6,
#             "left_bracket": "(",
#             "right_bracket": ")",
#             "bracket_v_buff": 0.1
#         }

#         self.cut_color = MAROON
#         self.com_color = ORANGE
#         self.path_color = LIGHT_BROWN

#         self.vec_a_num = [1, 2, -1]
#         self.vec_b_num = [3, 0,  2]


#         self.setup_scene()
#         self.crosspath_animation()
#         self.cross_vector_calculations()
#         self.cut_lines_for_calculations()
#         self.prepare_for_next_scene()


#     def setup_scene(self):
#         vec_a_num, vec_b_num = self.vec_a_num, self.vec_b_num
#         mat_a = Matrix([[vec_a_num[0]], [vec_a_num[1]], [vec_a_num[2]]], **self.mat_kwargs)
#         mat_b = Matrix([[vec_b_num[0]], [vec_b_num[1]], [vec_b_num[2]]], **self.mat_kwargs)

#         vec_group = self.group_vecs_with_symbol(mat_a, mat_b, type = "times", color = vec_c_color)
#         vec_group.move_to(np.array([3.12092922, 0, 0]))

#         name = Tex("Kreuz","produkt")
#         name[0].set_color(vec_c_color)
#         name.move_to(np.array([3.12092922, 1.592528, 0]))

#         self.add(vec_group, name)
#         self.wait(2)

#         self.play(
#             AnimationGroup(
#                 vec_group.animate.move_to(np.array([-3.5, 0, 0])), 
#                 name.animate.move_to(np.array([-3.5, 1.592528, 0])), 
#                 lag_ratio = 0.15
#             ),
#             run_time = 3
#         )
#         self.wait()

#         self.vec_group, self.name = vec_group, name

#     def crosspath_animation(self):
#         equals1 = MathTex("=").next_to(self.vec_group, RIGHT)

#         path_cross1, path_cross2, path_cross3 = self.get_crossproduct_path_xyz(self.vec_group, color = self.path_color, stroke_width = 7)
#         cross_res = np.cross(self.vec_a_num, self.vec_b_num)
#         cross_vec = Matrix([[cross_res[0]], [cross_res[1]], [cross_res[2]]], **self.mat_kwargs)\
#             .next_to(equals1, RIGHT)


#         self.play(
#             Write(equals1), 
#             FadeIn(cross_vec[1:], lag_ratio = 0.1, shift = 0.5*UP),
#         )
#         self.wait() 

#         self.play(ShowPassingFlash(path_cross1, time_width = 0.5), rate_func = linear, run_time = 2)
#         self.play(
#             Write(cross_vec[0][0], run_time = 0.75)
#         )

#         self.play(ShowPassingFlash(path_cross2, time_width = 0.5), rate_func = linear, run_time = 2)
#         self.play(Write(cross_vec[0][1]), run_time = 0.75)


#         self.play(ShowPassingFlash(path_cross3, time_width = 0.5), rate_func = linear, run_time = 2)
#         self.play(Write(cross_vec[0][2]), run_time = 0.75)
#         self.wait()

#         self.equals1, self.cross_vec = equals1, cross_vec

#     def cross_vector_calculations(self):
#         x1, xm, x2 = MathTex("(", "2", "\\cdot", "2"),  MathTex("(", "-", ")"), MathTex("(", "-1", ")", "\\cdot", "0")
#         y1, ym, y2 = MathTex("-1", "\\cdot", "3"), MathTex("1", "-", "1"), MathTex("1", "\\cdot", "2")
#         z1, zm, z2 = MathTex("1", "\\cdot", "0"),  MathTex("1", "-", "1"), MathTex("2", "\\cdot", "3")

#         x1[0].set_color(BLACK)
#         for minus in xm, ym, zm:
#             minus[0::2].set_color(BLACK)

#         cross_calc = MobjectMatrix([[x1, xm, x2], [y1, ym, y2], [z1, zm, z2]], **self.mat_kwargs, element_alignment_corner=DOWN)
#         cross_calc.next_to(self.equals1, RIGHT)
#         cross_calc[1:].set_color(DARK_GREY)

#         equals2 = self.equals1.copy()\
#             .next_to(cross_calc, RIGHT)

#         self.equals2, self.cross_calc = equals2, cross_calc

#     def cut_lines_for_calculations(self):
#         path_cross1, path_cross2, path_cross3 = self.get_crossproduct_path_xyz(self.vec_group, color = self.path_color, stroke_width = 7)

#         # Name & Klammern dunkel machen, Lösungsvektor verschieben
#         self.play(
#             LaggedStartMap(
#                 FadeToColor, VGroup(self.name[1], self.vec_group[0][1:], self.vec_group[2][1:]), color = DARK_GREY,
#                 lag_ratio = 0.15
#             ), 
#             self.cross_vec.animate.next_to(self.equals2, RIGHT).set_color(DARK_GREY),
#             run_time = 2
#         )
#         self.wait()

#         # Linien für das Gleichungssystem & SurRects für CrossVector
#         cross_vec_rects = VGroup(*[
#             SurroundingRectangle(self.cross_vec[0][index], color = self.com_color) for index in range(len(self.cross_vec)) 
#         ])

#         lines = self.get_crossproduct_cut_lines(self.vec_group, color = self.cut_color)
#         text_comp = VGroup(*[
#             Tex(tex, "-", "Komponente").next_to(2*RIGHT + 3*UP, LEFT, aligned_edge=UR) 
#             for tex in ["$x$", "$y$", "$z$"]
#         ])

#         text_cut = VGroup(*[
#             Tex("Streiche ", tex, " Zeile") 
#             for tex in ["$1.$", "$2.$", "$3.$"]
#         ])
#         text_cut.move_to(3*LEFT + 2*DOWN)

#         text_mult = Tex("Multipliziere über ", "Kreuz")
#         text_mult.next_to(text_cut, RIGHT, buff = 1, aligned_edge=UP)
#         text_mult[1].set_color(vec_c_color)

#         for index in range(len(text_cut)):
#             text_cut[index][1:].set_color(self.cut_color)
#         for index in range(len(text_comp)):
#             text_comp[index][0].set_color(self.com_color)

#         cross_line1 = Line(UP + LEFT, DOWN + RIGHT, stroke_width = 2, color = vec_c_color)
#         cross_line2 = Line(DOWN + LEFT, UP + RIGHT, stroke_width = 2, color = vec_c_color)
#         cross_sign = VGroup(cross_line1, cross_line2)\
#             .match_height(self.vec_group[1])\
#             .move_to(self.vec_group[1])

#         lines_kwargs = {"stroke_width": 3, "buff": 0.1, "color": vec_c_color}
#         cross_lines_x = self.get_lines_for_comp_calc(self.vec_group, 1,2, **lines_kwargs)
#         cross_lines_y = self.get_lines_for_comp_calc(self.vec_group, 0,2, **lines_kwargs)
#         cross_lines_z = self.get_lines_for_comp_calc(self.vec_group, 0,1, **lines_kwargs)


#         self.play(
#             AnimationGroup(
#                 Write(text_comp[0]),
#                 Write(self.equals2), 
#                 FadeIn(self.cross_calc[1:], shift=0.5*UP, lag_ratio = 0.15),
#                 Create(cross_vec_rects[0]), 
#                 lag_ratio = 0.15
#             ), 
#             run_time = 2
#         )
#         self.wait()


#         # 1. Zeile streichen & Multipliziere über Kreuz
#         self.play(Write(text_cut[0]))
#         self.wait()

#         self.play(
#             LaggedStartMap(FadeToColor, VGroup(self.vec_group[0][0][0], self.vec_group[2][0][0]), color = DARK_GREY, lag_ratio = 0.1),
#             Create(lines[0]),
#             run_time = 2
#         )
#         self.wait()

#         self.play(Write(text_mult))
#         self.wait()


#         self.play(ReplacementTransform(cross_sign.copy(), cross_lines_x))
#         self.wait()

#         self.play(                                          # index  0 1 2 3  
#             AnimationGroup(                                 # !!!    ( 2 * 2 
#                 TransformFromCopy(self.vec_group[0][0][1], self.cross_calc[0][0][1]),
#                 TransformFromCopy(self.vec_group[2][0][2], self.cross_calc[0][0][3]),
#                 FadeIn(self.cross_calc[0][0][2]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.wait()
#         self.play(Write(self.cross_calc[0][1]))
#         self.play(                                          # index  0  1 2 3 4  
#             AnimationGroup(                                 # !!!    ( -1 ) * 0 
#                 TransformFromCopy(self.vec_group[0][0][2], self.cross_calc[0][2][1]),
#                 TransformFromCopy(self.vec_group[2][0][1], self.cross_calc[0][2][4]),
#                 FadeIn(self.cross_calc[0][2][3]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.play(LaggedStartMap(FadeIn, VGroup(self.cross_calc[0][2][0], self.cross_calc[0][2][2]), shift = 0.5*DOWN, lag_ratio = 0.1))
#         self.wait()

#         self.play(ShowPassingFlash(path_cross1, time_width = 0.5), rate_func = linear, run_time = 2)
#         self.wait()

#         self.play(FocusOn(self.cross_vec[0][0]), run_time = 1)
#         self.play(FadeToColor(self.cross_vec[0][0], WHITE))
#         self.wait()

#         # FadeOut cross_lines, Streichlinie
#         self.play(
#             AnimationGroup(
#                 Uncreate(lines[0]),
#                 GrowFromPoint(cross_lines_x, point = self.vec_group[1].get_center(), rate_func = lambda t: smooth(1-t)),
#                 FadeToColor(VGroup(self.vec_group[0][0][0], self.vec_group[2][0][0]), WHITE, lag_ratio = 0.15),
#                 lag_ratio = 0.15
#             ), 
#             run_time = 2
#         )
#         self.wait()

#         # y-Komponente, 2 Zeile Streichen
#         self.play(
#             AnimationGroup(
#                 ReplacementTransform(text_comp[0], text_comp[1]), 
#                 ReplacementTransform(cross_vec_rects[0], cross_vec_rects[1]), 
#                 lag_ratio = 0.4
#             ), 
#             run_time = 2
#         )
#         self.wait()

#         self.play(Transform(text_cut[0], text_cut[1]))
#         self.wait()

#         # 2. Zeile Streichen 
#         self.play(
#             LaggedStartMap(FadeToColor, VGroup(self.vec_group[0][0][1], self.vec_group[2][0][1]), color = DARK_GREY, lag_ratio = 0.1),
#             Create(lines[1]),
#             run_time = 2
#         )
#         self.wait()

#         self.play(ReplacementTransform(cross_sign.copy(), cross_lines_y))
#         self.wait()

#         self.play(                                          # index   0 1 2 
#             AnimationGroup(                                 # !!!    -1 * 3 
#                 TransformFromCopy(self.vec_group[0][0][2], self.cross_calc[0][3][0]),
#                 TransformFromCopy(self.vec_group[2][0][0], self.cross_calc[0][3][2]),
#                 FadeIn(self.cross_calc[0][3][1]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.wait()
#         self.play(Write(self.cross_calc[0][4]))
#         self.play(                                                  # index  0 1 2 
#             AnimationGroup(                                         # !!!    1 * 2 
#                 TransformFromCopy(self.vec_group[0][0][0], self.cross_calc[0][5][0]),
#                 TransformFromCopy(self.vec_group[2][0][2], self.cross_calc[0][5][2]),
#                 FadeIn(self.cross_calc[0][5][1]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.wait()

#         self.play(ShowPassingFlash(path_cross2, time_width = 0.5), rate_func = linear, run_time = 2)
#         self.wait()

#         self.play(FocusOn(self.cross_vec[0][1]), run_time = 1)
#         self.play(FadeToColor(self.cross_vec[0][1], WHITE))
#         self.wait()


#         # FadeOut cross_lines, Streichlinie
#         self.play(
#             AnimationGroup(
#                 Uncreate(lines[1]),
#                 GrowFromPoint(cross_lines_y, point = self.vec_group[1].get_center(), rate_func = lambda t: smooth(1-t)),
#                 FadeToColor(VGroup(self.vec_group[0][0][1], self.vec_group[2][0][1]), WHITE, lag_ratio = 0.15),
#                 lag_ratio = 0.15
#             ), 
#             run_time = 2
#         )
#         self.wait()


#         # z-Komponente, 3 Zeile Streichen
#         self.play(
#             AnimationGroup(
#                 ReplacementTransform(text_comp[1], text_comp[2]), 
#                 ReplacementTransform(cross_vec_rects[1], cross_vec_rects[2]), 
#                 lag_ratio = 0.4
#             ), 
#             run_time = 2
#         )
#         self.wait()

#         self.play(ReplacementTransform(text_cut[0], text_cut[2]))
#         self.wait()

#         # 3. Zeile Streichen 
#         self.play(
#             LaggedStartMap(FadeToColor, VGroup(self.vec_group[0][0][2], self.vec_group[2][0][2]), color = DARK_GREY, lag_ratio = 0.1),
#             Create(lines[2]),
#             run_time = 2
#         )
#         self.wait()

#         self.play(ReplacementTransform(cross_sign.copy(), cross_lines_z))
#         self.wait()

#         self.play(                                          # index   0 1 2 
#             AnimationGroup(                                 # !!!     1 * 0 
#                 TransformFromCopy(self.vec_group[0][0][0], self.cross_calc[0][6][0]),
#                 TransformFromCopy(self.vec_group[2][0][1], self.cross_calc[0][6][2]),
#                 FadeIn(self.cross_calc[0][6][1]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.wait()
#         self.play(Write(self.cross_calc[0][7]))
#         self.play(                                                  # index  0 1 2 
#             AnimationGroup(                                         # !!!    2 * 3 
#                 TransformFromCopy(self.vec_group[0][0][1], self.cross_calc[0][8][0]),
#                 TransformFromCopy(self.vec_group[2][0][0], self.cross_calc[0][8][2]),
#                 FadeIn(self.cross_calc[0][8][1]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.wait()

#         self.play(ShowPassingFlash(path_cross3, time_width = 0.5), rate_func = linear, run_time = 2)
#         self.wait()

#         self.play(FocusOn(self.cross_vec[0][2]), run_time = 1)
#         self.play(FadeToColor(self.cross_vec[0][2], WHITE))
#         self.wait()

#         # FadeOut cross_lines, Streichlinie
#         self.play(
#             AnimationGroup(
#                 Uncreate(cross_vec_rects[2]),
#                 Uncreate(lines[2]),
#                 GrowFromPoint(cross_lines_z, point = self.vec_group[1].get_center(), rate_func = lambda t: smooth(1-t)),
#                 FadeToColor(VGroup(self.vec_group[0][0][2], self.vec_group[2][0][2]), WHITE, lag_ratio = 0.15),
#                 lag_ratio = 0.15
#             ), 
#             run_time = 2
#         )
#         self.wait(3)


#         self.text_mult, self.text_cut, self.text_comp = text_mult, text_cut, text_comp

#     def prepare_for_next_scene(self):
#         fadeout_group = VGroup(
#             self.text_comp[2], self.text_cut[2], self.text_mult,
#             self.equals1, self.cross_calc, self.equals2
#         )

#         self.play(
#             LaggedStartMap(
#                 FadeOut, 
#                 fadeout_group, 
#                 lag_ratio = 0.1
#             ), 
#             run_time = 2
#         )
#         self.wait(2)



# class OrthogonalProperty(Calculations):
#     def construct(self):
#         self.mat_kwargs = {
#             "v_buff": 0.6, 
#             "left_bracket": "(", 
#             "right_bracket": ")",
#             "bracket_v_buff": 0.1
#         }
#         self.dot_color = LIGHT_BROWN

#         self.vec_a_num = [1, 2, -1]
#         self.vec_b_num = [3, 0,  2]
#         self.vec_n_num = np.cross(self.vec_a_num, self.vec_b_num)

#         self.mat_a = self.get_vector_matrix_from_num_vec(self.vec_a_num, **self.mat_kwargs)
#         self.mat_b = self.get_vector_matrix_from_num_vec(self.vec_b_num, **self.mat_kwargs)
#         self.mat_n = self.get_vector_matrix_from_num_vec(self.vec_n_num, **self.mat_kwargs)

#         self.setup_from_old_scene()
#         self.dot_product_with_a()
#         self.dot_product_with_b()
#         self.text_for_ortho()


#     def setup_from_old_scene(self):
#         self.mat_n.move_to(np.array([5.5806598, 0, 0]))

#         cross_group = self.group_vecs_with_symbol(self.mat_a, self.mat_b, type = "\\times", color = vec_c_color)\
#             .move_to(np.array([-3.5, 0, 0]))
#         for element in cross_group[0], cross_group[2], self.mat_n:
#             element[1:].set_color(DARK_GREY)

#         cross_name = Tex("Kreuz", "produkt")\
#             .move_to(np.array([-3.5, 1.592528, 0]))
#         cross_name[0].set_color(vec_c_color)
#         cross_name[1].set_color(DARK_GREY)


#         self.add(cross_group, cross_name, self.mat_n)
#         self.wait()

#         cross_name.generate_target()
#         cross_name.target.move_to(4.5*LEFT + 2.5*UP)

#         cross_group.generate_target()
#         cross_group.target.next_to(cross_name.target, RIGHT, buff = 0.5)

#         cross_equals = MathTex("=")\
#             .set_color(DARK_GREY)\
#             .next_to(cross_group.target, RIGHT)

#         self.mat_n.generate_target()
#         self.mat_n.target.next_to(cross_equals, RIGHT)

#         self.play(
#             LaggedStartMap(MoveToTarget, VGroup(cross_name, cross_group, self.mat_n), path_arc = 1, lag_ratio = 0.15),
#             Write(cross_equals, rate_func = squish_rate_func(smooth, 0.66, 1)),
#             run_time = 3
#         )
#         self.wait()


#         self.cross_name, self.cross_group = cross_name, cross_group

#     def dot_product_with_a(self):
#         dot_name = Tex("Skalar", "produkt")\
#             .next_to(self.cross_name, DOWN, buff = 2, aligned_edge=RIGHT)
#         dot_name[0].set_color(self.dot_color)
#         dot_name[1].set_color(DARK_GREY)

#         self.play(Write(dot_name))
#         self.wait()

#         vec_a = self.mat_a.copy()
#         vec_n1 = self.mat_n.copy()

#         dot_group_a = self.dot_group_a = self.group_vecs_with_symbol(vec_a, vec_n1, type = "dot", color = self.dot_color)
#         dot_group_a.next_to(dot_name, RIGHT, buff = 0.5)

#         self.play(
#             Transform(self.mat_a.copy(), vec_a), 
#             Transform(self.mat_n.copy(), vec_n1, path_arc = -1), 
#             FadeIn(dot_group_a[1], shift = DOWN), 
#             run_time = 3
#         )
#         self.wait()

#         dot_equals1 = MathTex("=").set_color(DARK_GREY).next_to(dot_group_a, RIGHT)
#         self.play(Write(dot_equals1))
#         self.wait()

#         dot_path = self.get_dotproduct_path(dot_group_a)
#         self.play(ShowPassingFlash(dot_path, time_width = 0.25), rate_func = linear, run_time = 2)
#         self.wait()

#         # Aus beiden Vektoren --> Vektor fürs Skalarprodukt

#         x = MathTex("1", "\\cdot", "4")
#         y = MathTex("2", "\\cdot", "(", "-5", ")")
#         z = MathTex("-1", "\\cdot", "(", "-6", ")")
#         dot_vec = MobjectMatrix([[x], [y], [z]], **self.mat_kwargs, element_alignment_corner = DOWN)
#         dot_vec.next_to(dot_equals1, RIGHT)

#         self.play(
#             AnimationGroup(
#                 AnimationGroup(
#                     TransformFromCopy(dot_group_a[2][0][0], dot_vec[0][0][2]),
#                     FadeIn(dot_vec[0][0][1], shift = UP),
#                     TransformFromCopy(dot_group_a[0][0][0], dot_vec[0][0][0]),
#                     lag_ratio = 0.05
#                 ),
#                 AnimationGroup(
#                     TransformFromCopy(dot_group_a[2][0][1], dot_vec[0][1][3]),
#                     FadeIn(dot_vec[0][1][1], shift = UP),
#                     TransformFromCopy(dot_group_a[0][0][1], dot_vec[0][1][0]),
#                     FadeIn(dot_vec[0][1][2], shift = UP, rate_func = squish_rate_func(smooth, 0.5, 1)),
#                     FadeIn(dot_vec[0][1][4], shift = UP, rate_func = squish_rate_func(smooth, 0.5, 1)),
#                     lag_ratio = 0.05
#                 ),
#                 AnimationGroup(
#                     TransformFromCopy(dot_group_a[2][0][2], dot_vec[0][2][3]),
#                     FadeIn(dot_vec[0][2][1], shift = UP),
#                     TransformFromCopy(dot_group_a[0][0][2], dot_vec[0][2][0]),
#                     FadeIn(dot_vec[0][2][2], shift = UP, rate_func = squish_rate_func(smooth, 0.5, 1)),
#                     FadeIn(dot_vec[0][2][4], shift = UP, rate_func = squish_rate_func(smooth, 0.5, 1)),
#                     lag_ratio = 0.05
#                 ), 
#                 lag_ratio = 0.3
#             ), 
#             run_time = 3
#         )
#         self.wait()

#         # Vektor fürs Kreuzprodukt --> einzelne Komponenten 
#         dot_vec_num = [a*b for a,b in zip(self.vec_a_num, self.vec_n_num)]
#         dot_vec2 = self.get_vector_matrix_from_num_vec(dot_vec_num, **self.mat_kwargs, element_alignment_corner = DOWN)
#         dot_vec2.next_to(dot_equals1, RIGHT)
#         self.play(
#             AnimationGroup(
#                 *[
#                     ReplacementTransform(dot_vec[0][index], dot_vec2[0][index])
#                     for index in range(3)
#                 ], lag_ratio = 0.15
#             ),
#             run_time = 1
#         )
#         self.wait()

#         # Ergebnis als Summe
#         #                      0    1    2     3     4    5    6
#         dot_result1 = MathTex("4", "+", "(", "-10", ")", "+", "6")\
#             .next_to(dot_equals1, RIGHT)

#         self.play(
#             ReplacementTransform(dot_vec2[0][0], dot_result1[0]),
#             ReplacementTransform(dot_vec2[0][1], dot_result1[3]),
#             ReplacementTransform(dot_vec2[0][2], dot_result1[6]),
#             AnimationGroup(*[FadeIn(dot_result1[index], shift = 0.5*UP) for index in [1,2,4,5]], lag_ratio = 0.1), 
#             run_time = 1.5
#         )
#         self.wait()

#         self.dot_result = MathTex("0")\
#             .next_to(dot_equals1, RIGHT)
#         self.play(Transform(dot_result1, self.dot_result))
#         self.wait()

#     def dot_product_with_b(self):
#         vec_b = self.mat_b.copy()
#         vec_n2 = self.mat_n.copy()


#         dot_group_b = self.group_vecs_with_symbol(vec_b, vec_n2, type = "dot", color = self.dot_color)
#         dot_group_b.next_to(self.dot_group_a, DOWN, buff = 0.5, aligned_edge=RIGHT)

#         self.play(
#             Transform(self.mat_b.copy(), vec_b), 
#             Transform(self.mat_n.copy(), vec_n2, path_arc = -1), 
#             FadeIn(dot_group_b[1], shift = DOWN), 
#             run_time = 3
#         )
#         self.wait()

#         dot_equals2 = MathTex("=").set_color(DARK_GREY).next_to(dot_group_b, RIGHT)
#         self.play(Write(dot_equals2))
#         self.wait()

#         dot_path = self.get_dotproduct_path(dot_group_b)
#         self.play(ShowPassingFlash(dot_path, time_width = 0.25), rate_func = linear, run_time = 2)
#         self.wait()

#         self.dot_result2 = MathTex("0").next_to(dot_equals2, RIGHT)
#         self.play(Write(self.dot_result2))
#         self.wait(2)

#     def text_for_ortho(self):
#         texs = VGroup(*[
#             MathTex(tex).set_color(color).next_to(mob, UP, buff = 0)
#             for tex, color, mob in zip(
#                 ["\\vec{a}", "\\vec{b}", "\\vec{n}"], 
#                 [vec_a_color, vec_b_color, vec_c_color],
#                 [self.cross_group[0], self.cross_group[2], self.mat_n]
#             )
#         ])

#         # ortho_a = MathTex("\\vec{a}", "\\cdot", "\\vec{n}", "=", "0").next_to(self.dot_result, RIGHT, buff = 1)
#         # ortho_b = MathTex("\\vec{b}", "\\cdot", "\\vec{n}", "=", "0").next_to(self.dot_result2, RIGHT, buff = 1)

#         # for eq in ortho_a, ortho_b:
#         #     eq.set_color_by_tex_to_color_map({
#         #         "\\vec{a}": vec_a_color, "\\cdot": self.dot_color, "\\vec{b}": vec_b_color, "\\vec{n}": vec_c_color
#         #     })

#         # self.add(texs, ortho_a, ortho_b)

#         brace = Brace(Line(self.dot_result.get_corner(UR), self.dot_result2.get_corner(DR)), RIGHT, color = DARK_GREY)
#         brace_text = Tex(
#             "Vektor ", "$\\vec{n}$", " steht \\\\", "senkrecht zum \\\\", 
#             "Vektor ", "$\\vec{a}$", " und \\\\", "zum Vektor ", "$\\vec{b}$"
#         )
#         brace_text.next_to(brace, RIGHT)
#         brace_text.set_color_by_tex_to_color_map({
#                 "\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color, "\\vec{n}": vec_c_color,
#             })

#         self.play(LaggedStartMap(FadeIn, texs, lag_ratio = 0.1))
#         self.play(Create(brace))
#         self.play(Write(brace_text))
#         self.wait()

#         arrow = Arrow(brace_text[1].get_top() + 0.75*UP, brace_text[1].get_top(), buff = 0.1, color = PINK)

#         text_nvec = Tex("Normalen", "vektor")
#         text_nvec[0].set_color(vec_c_color)
#         text_nvec[1].set_color(LIGHT_GREY)
#         text_nvec.next_to(arrow, UP)

#         self.play(Write(text_nvec))
#         self.play(GrowArrow(arrow), run_time = 1.5)
#         self.wait()

#         self.play(
#             Circumscribe(brace_text[6], color = PINK, fade_out = True, time_width = 0.5, run_time = 2),
#             FadeToColor(brace_text[6], PINK, run_time = 2),
#         )
#         self.wait()

#         text_perp = Tex("senkrecht")\
#             .set_color(vec_c_color)\
#             .next_to(text_nvec, UP, buff = 1)\
#             .shift(0.5*RIGHT)
#         arrow2 = Arrow(text_nvec[0].get_top(), text_perp[0].get_bottom(), buff = 0.1, color = PINK)
#         self.play(GrowArrow(arrow2))
#         self.play(Write(text_perp))
#         self.wait(3)



# class OrthogonalProperty3D(ThreeDScene):
#     def construct(self):
#         self.vec_a_num = [1, 2, -1]
#         self.vec_b_num = [3, 0,  2]
#         self.vec_n_num = np.cross(self.vec_a_num, self.vec_b_num)

#         axes = self.axes = ThreeDAxes()
#         axes.set_color(DARK_GREY)
#         self.set_camera_orientation(phi = 70*DEGREES, theta = 30*DEGREES)
#         self.origin = axes.coords_to_point(0,0,0)

#         self.cone_height, self.cone_radius = 0.5, 0.15
#         self.cone_kwargs = {"height": self.cone_height, "base_radius": self.cone_radius}

#         self.draw_axes()
#         self.draw_vecs()


#     def draw_axes(self):
#         labels_axes = VGroup(*[
#             MathTex(label).next_to(axis, direction = direction)
#             for label, axis, direction in zip(
#                 ["x", "y", "z"], 
#                 [self.axes.x_axis, self.axes.y_axis, self.axes.z_axis], 
#                 [RIGHT, UP, OUT]
#             )
#         ])

#         self.add_fixed_orientation_mobjects(*labels_axes)
#         self.add(self.axes)
#         self.wait(2)

#     def draw_vecs(self):
#         axes = self.axes
#         cone_kwargs = self.cone_kwargs

#         # vec_a = Arrow(start = self.origin, end = axes.coords_to_point(*self.vec_a_num), buff = 0, color = vec_a_color)
#         # vec_b = Arrow(start = self.origin, end = axes.coords_to_point(*self.vec_b_num), buff = 0, color = vec_b_color)
#         # vec_n = Arrow(start = self.origin, end = axes.coords_to_point(*self.vec_n_num), buff = 0, color = vec_c_color)

#         vec_a = Arrow3D(start = self.origin, end = axes.coords_to_point(*self.vec_a_num), **cone_kwargs, color = vec_a_color)
#         vec_b = Arrow3D(start = self.origin, end = axes.coords_to_point(*self.vec_b_num), **cone_kwargs, color = vec_b_color)
#         vec_n = Arrow3D(start = self.origin, end = axes.coords_to_point(*self.vec_n_num), **cone_kwargs, color = vec_c_color)

#         comp_a = self.get_component_lines(self.vec_a_num, line_class = Line, color = RED_E)
#         comp_b = self.get_component_lines(self.vec_b_num, line_class = Line, color = YELLOW_E)
#         comp_n = self.get_component_lines(self.vec_n_num, line_class = Line, color = BLUE_E)

#         # for comp, vec in zip([comp_a, comp_b, comp_n], [vec_a, vec_b, vec_n]):
#         #     self.play(Create(comp), lag_ratio = 0.15, run_time = 2)
#         #     self.play(Create(vec), run_time = 2)
#         #     self.wait(0.5)

#         self.play(
#             LaggedStartMap(Create, VGroup(comp_a, comp_b, comp_n), lag_ratio = 0.25), run_time = 2
#         )
#         self.play(
#             LaggedStartMap(Create, VGroup(vec_a, vec_b, vec_n), lag_ratio = 0.25), run_time = 2
#         )
#         self.wait()

#         self.move_camera(zoom = 0.75, run_time = 3)
#         self.wait()
#         self.play(
#             ApplyMethod(self.renderer.camera.zoom_tracker.set_value, 1, run_time = 3),
#             *[Uncreate(comp, lag_ratio = 0.1, run_time = 3) for comp in [comp_a, comp_b, comp_n]],
#         )
#         self.wait()

#         # Move Camera --> Orthogonalität zwischen Vektor b und n
#         self.move_camera(phi = 65.90516*DEGREES, theta = -116.56505*DEGREES, run_time = 3)
#         self.wait(2)

#         # Move Camera --> Orthogonalität zwischen Vektor a und n
#         self.move_camera(phi = 56.30993*DEGREES, theta = 0*DEGREES, run_time = 3)
#         self.wait(3)


#         self.move_camera(phi = 70*DEGREES, theta = 30*DEGREES, run_time = 3)
#         self.wait(3)




#     # functions
#     def get_component_lines(self, vec_num, line_class = DashedLine, color = BLUE, **kwargs):
#         axes = self.axes
#         x, y, z = vec_num[0], vec_num[1], vec_num[2]

#         x_component = line_class(axes.c2p(x, y, 0), axes.c2p(0, y, 0), color = color, **kwargs)
#         y_component = line_class(axes.c2p(x, y, 0), axes.c2p(x, 0, 0), color = color, **kwargs)
#         z_component = line_class(axes.c2p(x, y, 0), axes.c2p(x, y, z), color = color, **kwargs)

#         result = VGroup(x_component, y_component, z_component)

#         return result







# class OriginOfNormalVector(Calculations, MovingCameraScene):
#     def construct(self):
#         self.mat_kwargs = {
#             "v_buff": 0.6, 
#             "left_bracket": "(", 
#             "right_bracket": ")",
#             "bracket_v_buff": 0.1
#         }

#         self.word_property()
#         self.eq_property()
#         self.solution_vector()
#         self.proof_for_vector_a()
#         self.proof_for_vector_b()


#     def word_property(self):

#         eq1 = MathTex("\\vec{a}", "\\cdot", "\\vec{n}", "=", "0").to_corner(UL)
#         eq2 = MathTex("\\vec{b}", "\\cdot", "\\vec{n}", "=", "0").next_to(eq1, DOWN, aligned_edge = RIGHT)

#         for eq in eq1, eq2:
#             eq.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color, "\\times": GREEN , "\\vec{n}": vec_c_color})

#         eqs = VGroup(eq1, eq2)
#         eqs.save_state()

#         text = Tex("Der ", "Normalenvektor", " ist sowohl zu Vektor ", "$\\vec{a}$\\\\", " als auch zu Vektor ", "$\\vec{b}$", " senkrecht orientiert.")
#         text.set_color(LIGHT_GREY)
#         text.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color, "Normalenvektor": vec_c_color})
#         text.next_to(eqs, RIGHT, buff = 1)

#         # Gleichungen centern
#         eqs.center().scale(2)

#         self.play(AnimationGroup(*[
#             FadeIn(eq, shift = direction) for eq, direction in zip([eq1, eq2], [LEFT, RIGHT])
#         ], lag_ratio = 0.1))
#         self.wait()

#         self.play(
#             Restore(eqs, path_arc = -2, run_time = 3), 
#             Write(text, run_time = 1.5)
#         )
#         self.wait()


#         self.eqs = eqs
#         self.text = text

#     def eq_property(self):

#         ax, ay, az = MathTex("a_1"), MathTex("a_2"), MathTex("a_3")
#         bx, by, bz = MathTex("b_1"), MathTex("b_2"), MathTex("b_3")
#         nx, ny, nz = MathTex("n_1"), MathTex("n_2"), MathTex("n_3")
#         for element in ax, ay, az, bx, by, bz, nx, ny, nz:
#             element.set_color_by_tex_to_color_map({"a": vec_a_color, "b": vec_b_color, "n": vec_c_color})

#         mat_a = MobjectMatrix([[ax], [ay], [az]], **self.mat_kwargs)
#         mat_b = MobjectMatrix([[bx], [by], [bz]], **self.mat_kwargs)
#         mat_n = MobjectMatrix([[nx], [ny], [nz]], **self.mat_kwargs)
#         mat_n2 = mat_n.copy()

#         for mat in mat_a, mat_b, mat_n, mat_n2:
#             mat[1:].set_color(DARK_GREY)

#         eq1_mat = self.group_vecs_with_symbol(mat_a, mat_n, type="cdot")
#         eq2_mat = self.group_vecs_with_symbol(mat_b, mat_n2, type="cdot").next_to(eq1_mat, DOWN, aligned_edge=RIGHT)

#         equals_zero_a = MathTex("=", "0")
#         equals_zero_a[0].set_color(DARK_GREY)
#         equals_zero_a.next_to(eq1_mat, RIGHT)
#         equals_zero_b = equals_zero_a.copy().next_to(eq2_mat, RIGHT)

#         self.play(
#             LaggedStartMap(Create, VGroup(eq1_mat, eq2_mat, equals_zero_a, equals_zero_b), lag_ratio = 0.1), 
#             run_time = 2
#         )
#         self.wait()

#         # Skalarprodukte nach links, 
#         for eq in eq1_mat, eq2_mat:
#             eq.generate_target()
#             eq.target.to_edge(LEFT)

#         #               0     1        2       3     4     5        6       7     8     9       10       11
#         dot1 = MathTex("=", "a_1", "\\cdot", "n_1", "+", "a_2", "\\cdot", "n_2", "+", "a_3", "\\cdot", "n_3")
#         dot2 = MathTex("=", "b_1", "\\cdot", "n_1", "+", "b_2", "\\cdot", "n_2", "+", "b_3", "\\cdot", "n_3")

#         for dot, eq_mat in zip([dot1, dot2], [eq1_mat, eq2_mat]):
#             dot[0].set_color(DARK_GREY)
#             dot.next_to(eq_mat.target, RIGHT)
#             dot.set_color_by_tex_to_color_map({"a": vec_a_color, "b": vec_b_color, "n": vec_c_color})

#         self.play(
#             MoveToTarget(eq1_mat), 
#             MoveToTarget(eq2_mat),
#             equals_zero_a.animate.next_to(dot1, RIGHT),
#             equals_zero_b.animate.next_to(dot2, RIGHT),
#             run_time = 2
#         )
#         self.wait()

#         self.play(
#             ShowIncreasingSubsets(dot1), ShowIncreasingSubsets(dot2), 
#             run_time = 2
#         )
#         self.wait()


#         # Surrounding Rectangles
#         sur_rects1 = VGroup(*[SurroundingRectangle(dot1[index], color = LIGHT_BROWN) for index in [3,7,11]])
#         sur_rects2 = VGroup(*[SurroundingRectangle(dot2[index], color = LIGHT_BROWN) for index in [3,7,11]])

#         self.play(Create(sur_rects1, lag_ratio = 0.15), run_time = 2)
#         self.wait()

#         self.play(
#             Uncreate(sur_rects1, lag_ratio = 0.15), 
#             Create(sur_rects2, lag_ratio = 0.15), 
#             run_time = 2
#         )
#         self.wait()
#         self.play(FadeOut(sur_rects2))
#         self.wait()


#         # Ausfaden und verschieben --> in der Mitt Platz machen
#         self.play(
#             VGroup(eq1_mat, dot1, equals_zero_a).animate.to_edge(UP), 
#             VGroup(eq2_mat, dot2, equals_zero_b).animate.to_edge(DOWN), 
#             FadeOut(VGroup(*self.eqs, self.text), shift = 2*UP),
#             run_time = 2
#         )
#         self.wait()

#         self.mat_a, self.mat_b = mat_a, mat_b
#         self.equals_zero_a, self.equals_zero_b = equals_zero_a, equals_zero_b
#         self.eq1_mat, self.eq2_mat = eq1_mat, eq2_mat
#         self.dot1, self.dot2 = dot1, dot2

#     def solution_vector(self):
#         mat_a, mat_b = self.mat_a.copy(), self.mat_b.copy()
#         cross = self.group_vecs_with_symbol(mat_a, mat_b, type = "times", color = vec_c_color)\
#             .shift(3*LEFT)
#         equals = MathTex("=").next_to(cross, RIGHT)

#         nx_comp = MathTex("a_2", "\\cdot", "b_3", "-", "a_3", "\\cdot", "b_2")
#         ny_comp = MathTex("a_3", "\\cdot", "b_1", "-", "a_1", "\\cdot", "b_3")
#         nz_comp = MathTex("a_1", "\\cdot", "b_2", "-", "a_2", "\\cdot", "b_1")

#         for coord in nx_comp, ny_comp, nz_comp:
#             coord.set_color_by_tex_to_color_map({"a": vec_a_color, "b": vec_b_color})

#         mat_cross_calc = MobjectMatrix([[nx_comp], [ny_comp], [nz_comp]], **self.mat_kwargs)
#         mat_cross_calc[1:].set_color(DARK_GREY)
#         mat_cross_calc.next_to(equals, RIGHT)


#         self.play(
#             AnimationGroup(
#                 TransformFromCopy(self.mat_a, mat_a), 
#                 Write(cross[1]),
#                 TransformFromCopy(self.mat_b, mat_b),
#                 Write(equals),
#                 lag_ratio = 0.15
#             ), 
#             run_time = 2
#         )
#         self.wait()


#         path_x, path_y, path_z = self.get_crossproduct_path_xyz(cross, color = vec_c_color, stroke_width = 7)
#         paths = VGroup(path_x, path_y, path_z)
#         cut_lines = self.get_crossproduct_cut_lines(cross, color = WHITE, line_buff = 0.1)

#         for number in range(len(cut_lines)):
#             self.play(
#                 AnimationGroup(
#                     Create(cut_lines[number]), 
#                     ShowPassingFlash(paths[number]),
#                     Write(mat_cross_calc[0][number]), 
#                     lag_ratio = 0.25
#                 ), 
#                 run_time = 2.5
#             )
#             self.play(Uncreate(cut_lines[number]))
#             self.wait()
#         self.play(Write(mat_cross_calc[1:]))
#         self.wait()


#         self.mat_cross_calc = mat_cross_calc

#     def proof_for_vector_a(self):
#         part1 = self.dot1[:4]
#         part1.generate_target()
#         part1.target.shift(2.4*UP)

#         part2 = self.dot1[4:8]
#         part2.generate_target()
#         part2.target.next_to(part1.target, DOWN, buff = 0.8, aligned_edge=LEFT)

#         part3 = self.dot1[8:]
#         part3.generate_target()
#         part3.target.next_to(part2.target, DOWN, buff = 0.8, aligned_edge=LEFT)

#         # 
#         self.play(
#             self.camera.frame.animate.shift(2.4*UP), 
#             VGroup(self.eq1_mat).animate.shift(2.4*UP),
#             MoveToTarget(part1),
#             MoveToTarget(part2, path_arc = -1), 
#             MoveToTarget(part3, path_arc = -2), 
#             FadeOut(self.equals_zero_a),
#             run_time = 2
#         )
#         self.wait()


#         # transform components from cross vector into dot product
#         insert1 = MathTex("(", "a_2", "\\cdot", "b_3", "-", "a_3", "\\cdot", "b_2", ")")
#         insert2 = MathTex("(", "a_3", "\\cdot", "b_1", "-", "a_1", "\\cdot", "b_3", ")")
#         insert3 = MathTex("(", "a_1", "\\cdot", "b_2", "-", "a_2", "\\cdot", "b_1", ")")

#         for eq, target in zip([insert1, insert2, insert3], [part1[2], part2[2], part3[2]]):
#             eq.set_color_by_tex_to_color_map({"a": vec_a_color, "b": vec_b_color})
#             eq.next_to(target, RIGHT)

#         self.play(
#             AnimationGroup(
#                 *[FadeOut(part[-1], shift = 0.5*UP) for part in [part1, part2, part3]],
#                 *[FadeIn(VGroup(eq[0], eq[-1]), shift = 0.5*UP) for eq in [insert1, insert2, insert3]], 
#                 lag_ratio = 0.1
#             ), 
#             run_time = 1.5
#         )
#         self.play(
#             AnimationGroup(
#                 TransformFromCopy(self.mat_cross_calc[0][0], insert1[1:-1]),
#                 TransformFromCopy(self.mat_cross_calc[0][1], insert2[1:-1]),
#                 TransformFromCopy(self.mat_cross_calc[0][2], insert3[1:-1]),
#                 lag_ratio = 0.25
#             ),
#             run_time = 3
#         )
#         self.wait()

#         # Terms cancel each other out
#         front_rects = VGroup(*[SurroundingRectangle(self.dot1[index], color = vec_c_color) for index in [1, 5, 9]])
#         front_rects1 = front_rects[1].copy()

#         inner_rects = VGroup()
#         for part in insert1, insert2, insert3:
#             sur_rect_front = SurroundingRectangle(part[1:4], color = vec_c_color)
#             sur_rect_back = SurroundingRectangle(part[5:8], color = vec_c_color) 
#             inner_rects.add(sur_rect_front, sur_rect_back)

#         # a1 * a2 * b3
#         self.play(*[Create(rect, run_time = 2) for rect in [front_rects[0], inner_rects[0]]])
#         self.wait()
#         self.play(*[Create(rect, run_time = 2) for rect in [front_rects[1], inner_rects[3]]])
#         self.wait()

#         self.play(
#             ReplacementTransform(inner_rects[0], inner_rects[1]),
#             insert1[1:4].animate.fade(darkness = 0.75),
#             insert2[5:8].animate.fade(darkness = 0.75),
#             Uncreate(front_rects[1]),
#             Uncreate(inner_rects[3]),
#             run_time = 3
#         )
#         self.wait()

#         # a1 * a3 * b2
#         self.play(*[Create(rect, run_time = 2) for rect in [front_rects[2], inner_rects[4]]])
#         self.wait()

#         self.play(
#             ReplacementTransform(inner_rects[4], inner_rects[5]),
#             *[Uncreate(rect) for rect in [front_rects[0], inner_rects[1]]],
#             insert3[1:4].animate.fade(darkness = 0.75),
#             insert1[5:8].animate.fade(darkness = 0.75),
#             run_time = 3
#         )
#         self.wait()

#         # a2 * a3 * b1
#         self.play(*[Create(rect, run_time = 2) for rect in [front_rects1, inner_rects[2]]])
#         self.wait()


#         self.play(
#             *[Uncreate(rect) for rect in [front_rects1, front_rects[2], inner_rects[2], inner_rects[5]]],
#             insert2[1:4].animate.fade(darkness = 0.75),
#             insert3[5:8].animate.fade(darkness = 0.75),
#             run_time = 3
#         )
#         self.wait()

#         self.equals_zero_a.next_to(insert3, RIGHT)
#         self.play(FadeIn(self.equals_zero_a))
#         self.wait()

#     def proof_for_vector_b(self):
#         self.play(
#             self.camera.frame.animate.shift(5*DOWN), 
#             run_time = 5
#         )
#         self.wait(3)



class TwoOrthogonalVectors(ThreeDScene):
    def construct(self):
        self.vec_a_num = [2/3, -1/3, 2/3]
        self.vec_b_num = [2/3,  2/3, -1/3]
        self.vec_n_num = np.cross(self.vec_a_num, self.vec_b_num)

        axis_length = self.axis_length = 7.5
        axis_min = self.axis_min = -1.5
        axis_max = self.axis_max = 1.5
        axes = self.axes = ThreeDAxes(
            x_range = [axis_min, axis_max, 1], y_range = [axis_min, axis_max, 1], z_range = [axis_min, axis_max, 1], 
            x_length = axis_length, y_length = axis_length, z_length = axis_length, 
            axis_config = {"color": DARK_GREY},
        )
        self.origin = axes.c2p(0,0,0)
        self.set_camera_orientation(phi = 70*DEGREES, theta = 30*DEGREES)

        self.acr_rate = 0.1

        self.setup_scene()
        self.draw_plane()
        self.show_second_vector()



    def setup_scene(self):
        axes, origin = self.axes, self.origin

        self.vec_a = Arrow3D(origin, axes.c2p(*self.vec_a_num), color = RED)
        self.vec_b = Arrow3D(origin, axes.c2p(*self.vec_b_num), color = BLUE)
        self.vec_n = Arrow3D(origin, axes.c2p(*self.vec_n_num), color = YELLOW)

        self.play(Create(self.axes), run_time = 2)
        self.begin_ambient_camera_rotation(rate = self.acr_rate)
        self.wait()

        self.play(*[Create(mob, run_time = 2) for mob in [self.vec_a, self.vec_b]])
        self.wait(3)

    def draw_plane(self):
        lines_kwags = {"stroke_width": 2, "color": GREY, "stroke_opacity": 0.2}
        lines_a = VGroup(*[
            Line(
                start = self.axes.c2p(*[-1.5*comp_a + s*comp_b for comp_a, comp_b in zip(self.vec_a_num, self.vec_b_num)]), 
                end  =  self.axes.c2p(*[+1.5*comp_a + s*comp_b for comp_a, comp_b in zip(self.vec_a_num, self.vec_b_num)]), 
                **lines_kwags
            )
            for s in np.linspace(-1.5,1.5,7)
        ])

        lines_b = VGroup(*[
            Line(
                start = self.axes.c2p(*[r*comp_a - 1.5*comp_b for comp_a, comp_b in zip(self.vec_a_num, self.vec_b_num)]), 
                end  =  self.axes.c2p(*[r*comp_a + 1.5*comp_b for comp_a, comp_b in zip(self.vec_a_num, self.vec_b_num)]), 
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
        big_rect.set_fill(color = BLUE_E, opacity = 0.3)
        big_rect.set_stroke(width = 0.5, color = GREY)


        self.play(Create(big_rect), Create(lines_a), Create(lines_b), run_time = 3)
        self.wait()

        self.play(Create(self.vec_n), run_time = 2)
        self.wait(3)

    def show_second_vector(self):
        self.stop_ambient_camera_rotation()
        self.move_camera(phi = 70*DEGREES, theta = 20*DEGREES, run_time = 3)
        self.wait()

        self.move_camera(phi = 70*DEGREES, theta = -15*DEGREES, run_time = 3)
        self.wait()

        vec_n2_num = np.cross(self.vec_b_num, self.vec_a_num)
        self.vec_n2 = Arrow3D(self.origin, self.axes.c2p(*vec_n2_num), color = vec_c_color)

        self.play(Create(self.vec_n2), run_time = 2)
        self.wait(3)


        self.begin_ambient_camera_rotation(rate = 0.1)
        self.wait(25)



# class OverlayTwoOrthoVectors(Scene):
#     def construct(self):
#         self.correct_cross_vector()
#         self.opposite_cross_vector()
#         self.right_hand_rule()


#     def correct_cross_vector(self):
#         plane = Tex("Ebene, die von ", "$\\vec{a}$", "\\\\und ", "$\\vec{b}$", " aufgespannt\\\\", "wird")\
#             .next_to(2.5*RIGHT + 1.5*DOWN, RIGHT)

#         arc = CurvedArrow(start_point = plane[0].get_left() + 0.2*LEFT, end_point = 1.5*RIGHT + 2*DOWN, color = DARK_BLUE)
        
#         eq = MathTex("\\vec{n}", "=", "\\vec{a}", "\\times", "\\vec{b}")\
#             .next_to(2*RIGHT + 2*UP, RIGHT)

#         norm_vec = Tex("Normalenvektor")\
#             .set_color(vec_c_color)\
#             .next_to(eq, UP, aligned_edge = LEFT)

#         for mob in plane, eq:
#             mob.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color, "\\vec{n}": vec_c_color})


#         self.play(Write(eq), run_time = 1.5)
#         self.wait()

#         self.play(FadeIn(norm_vec, shift = 3*LEFT), run_time = 2)
#         self.wait()

#         self.play(Write(plane), run_time = 1.5)
#         self.play(Create(arc))
#         self.wait()


#         self.play(
#             FadeOut(arc, rate_func = squish_rate_func(smooth, 0, 0.5)),
#             VGroup(eq, norm_vec).animate.shift(0.5*LEFT + 0.5*UP),
#             plane.animate(rate_func = squish_rate_func(smooth, 0, 0.6)).scale_about_point(0.75, plane.get_corner(UR)),
#             run_time = 3
#         )
#         self.wait()

#         self.plane, self.eq, self.norm_vec = plane, eq, norm_vec

#     def opposite_cross_vector(self):
#         wrong_cross = MathTex("\\vec{a}", "\\times", "\\vec{b}")
#         right_cross = MathTex("\\vec{b}", "\\times", "\\vec{a}")
#         anti_commut = MathTex("\\vec{a}", "\\times", "\\vec{b}", "=", "-", "\\vec{b}", "\\times", "\\vec{a}")\

#         for cross in wrong_cross, right_cross, anti_commut:
#             cross.next_to(1.5*LEFT + 2*DOWN, LEFT)
#             cross.set_color_by_tex_to_color_map({"\\vec{a}": vec_a_color, "\\vec{b}": vec_b_color, "-": vec_c_color})

#         self.play(Write(wrong_cross), run_time = 1.5)
#         self.wait()

#         question_mark = Tex("?")
#         exclamation_mark = Tex("!")
#         for mark in question_mark, exclamation_mark:
#             mark.scale(2)
#             mark.set_color(GREEN)
#             mark.set_fill(color = GREY, opacity = 0.25)
#             mark.set_stroke(width = 1.5)
#             mark.next_to(wrong_cross, LEFT, buff = 0.75)

#         self.play(DrawBorderThenFill(question_mark))
#         self.wait()

#         self.play(
#             ReplacementTransform(question_mark, exclamation_mark, rate_func = squish_rate_func(smooth, 0.4, 1)),
#             ClockwiseTransform(wrong_cross[0], right_cross[2]),
#             ClockwiseTransform(wrong_cross[2], right_cross[0]),
#             run_time = 2
#         )
#         self.wait()


#         anti_commut.to_edge(LEFT).shift(4.25*UP)
#         arrow = Arrow(ORIGIN, UP, buff = 0, color = vec_c_color).next_to(anti_commut[4], DOWN)
#         text_anti = Tex("Anti", "-", "Kommutativ").next_to(arrow, DOWN)
#         text_anti[0].set_color(vec_c_color)

#         self.play(
#             ShrinkToCenter(exclamation_mark),
#             Write(anti_commut),
#             run_time = 1.5
#         )
#         self.wait()

#         self.play(GrowArrow(arrow))
#         self.play(Write(text_anti))
#         self.wait(3)


#         fadeout_group = VGroup(wrong_cross, text_anti, arrow, anti_commut, self.plane, self.eq, self.norm_vec)
#         self.play(
#             AnimationGroup(
#                 *[
#                     FadeOut(mob, shift = 3*direction) for mob, direction in zip(
#                         fadeout_group, [LEFT, LEFT, LEFT, LEFT, RIGHT, RIGHT, RIGHT]
#                     )
#                 ], lag_ratio = 0.1
#             ), 
#             run_time = 3
#         )
#         self.wait()

#     def right_hand_rule(self):
#         svg = SVGMobject("Right_Hand_Rule_Winding")\
#             .scale(1.5)\
#             .shift(5*RIGHT)

#         for part in svg[0], svg[12:14]:
#             part.set_fill(color = "#E5C489", opacity = 1)
#             part.set_stroke(color=DARK_GREY, width = 2)

#         for part in svg[1:12], svg[14:]:
#             part.set_fill(opacity = 0)
#             part.set_stroke(color = DARK_GREY, width = 2)

#         svg.rotate(angle = -25*DEGREES, axis = OUT)

#         self.play(DrawBorderThenFill(svg))
#         self.wait()

#         text = Tex("Rechte","-","Hand","-","Regel")
#         text.next_to(svg, UP, buff = 1, aligned_edge=RIGHT)
#         self.play(Write(text))
#         self.wait()

#         arrowa = Arrow(ORIGIN, 2*LEFT + 1.6*UP, buff = 0, color = vec_a_color)
#         arrowb = Arrow(ORIGIN, 2*LEFT + 0.1*UP, buff = 0, color = vec_b_color)
#         arrowc = Arrow(ORIGIN, 2*UP + RIGHT, buff = 0, color = vec_c_color)


#         arcs_hand = Arc(
#             radius = 1.5, start_angle = arrowa.get_angle(), angle = angle_between_vectors([2,1.6,0], [2, 0.1, 0]), color = GREEN,

#         ).add_tip()

#         for arrow in arrowa, arrowb:
#             arrow.shift(5*RIGHT)
#             self.play(GrowArrow(arrow), run_time = 2)
#             self.wait()

#         for mob in arcs_hand, arrowc:
#             mob.shift(5*RIGHT)

#         self.play(Create(arcs_hand), run_time = 3)
#         self.wait()

#         self.play(GrowArrow(arrowc), run_time = 3)
#         self.wait()

#         self.play(
#             AnimationGroup(
#                 *[GrowFromPoint(mob, point = arrowa.get_start(), rate_func = lambda t: smooth(1-t)) for mob in [svg, arrowc, arrowb, arrowa, arcs_hand, text]], 
#                 lag_ratio = 0.1
#             ),
#             run_time = 1.5
#         )
#         self.wait()

