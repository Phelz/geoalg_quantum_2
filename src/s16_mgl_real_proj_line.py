from manimlib import *
from src.definitions import *



class _16_RealProjectiveLine(Scene):
    def construct(self):
        
        # * Title
        # * ______________________________________________________________________
        title = Title(
            f'Real Projective Line', include_underline=False, 
            font_size=TITLE_FONTSIZE*1.5,)
        title.to_corner(UL)
        title.set_color(BLUE)
        # title.fix_in_frame()
        
        title.z_index = 10
            
        
        
        self.play(
            Write(title),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Construct a plane
        # * ______________________________________________________________________

        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-7, 7, 1],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 0.5,
                "stroke_opacity": 0.75
            },
            faded_line_style={
                "stroke_color": BLUE_B,
                "stroke_width": 0.5,
                "stroke_opacity": 0.5
            },
            height=16,
            width=16,
        )
        
        
        bg_rect_title = BackgroundRectangle(
            title,
            color=BLACK,
            buff=0.3,)
        bg_rect_title.z_index = 9
        
        
        self.play(
            ShowCreation(plane),
            ShowCreation(bg_rect_title),
            run_time=2,
        )
        
        # * Signify the artist by a dot at the ORIGIN
        # * ______________________________________________________________________
        
        
        artist_dot = Dot(
            ORIGIN,
            color=YELLOW,
            radius=0.1,
        )
        artist_dot.set_fill(YELLOW, opacity=0.5)
        artist_dot.set_stroke(YELLOW, width=2)
        
        
        artist_tex = TexText(
            "Artist",
            font_size=TITLE_FONTSIZE*1,
        ).set_color(YELLOW_C)
        artist_tex.next_to(
            artist_dot,
            DOWN,
            buff=0.1,
        ).shift(DOWN * 0.25 + RIGHT*0.1 )
        
        
        self.play(
            Flash(ORIGIN, color=YELLOW),
            Write(artist_tex),
            run_time=1,
        )
        
        self.play(
            ShowCreation(artist_dot),
            run_time=1,
        )
        
        # * Draw the line that is the Easel for the artist
        # * ______________________________________________________________________
        
        line_graph = Line(
            start=plane.c2p(-10, 1),
            end=plane.c2p(10, 1),
            color=YELLOW_C,
            stroke_width=4,
        )
        
        line_graph_label = TexText(
            "Easel",
            font_size=TITLE_FONTSIZE * 1,
        ).set_color(YELLOW_C)
        line_graph_label.next_to(
            line_graph, UP, buff=0.2
        ).to_edge(RIGHT)
        
        self.play(
            ShowCreation(line_graph),
            Write(line_graph_label),
            run_time=2,
        )
        
        #         line_graph = plane.get_graph(
        #     lambda y: 1,
        #     color=YELLOW_C,
        #     # x_range=[-5, 5],
        # )
        
        # line_graph_label = plane.get_graph_label(
        #     line_graph,
        #     label='Easel',
        #     x=10,
        #     # y_val=10,
        # )
        
        # self.play(
        #     ShowCreation(line_graph),
        #     Write(line_graph_label),
        #     run_time=3,
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        
        # * Draw some points for the artist to draw
        # * ______________________________________________________________________
        dot_x_pos = np.array([-4, -2, 0, 2, 4])
        dot_y_pos = np.ones(len(dot_x_pos)) * 2
        
        dots = VGroup()
        for x, y in zip(dot_x_pos, dot_y_pos):
            dot = Dot(
                plane.c2p(x, y),
                color=BLUE_B,
                radius=0.1,
            )
            dot.set_fill(BLUE_B, opacity=0.5)
            dot.set_stroke(BLUE_B, width=2)
            dots.add(dot)
        self.play(
            LaggedStartMap(
                ShowCreation,
                dots,
                lag_ratio=0.5,
                run_time=3,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # # * Draw lines connecting the dots to the ORIGIN
        # # * ______________________________________________________________________
        lines = VGroup()
        for dot in dots:
            line = Line(
                start=ORIGIN,
                end=dot.get_center(),
                color=BLUE_B,
                stroke_width=2,
            )
            lines.add(line)
        self.play(
            LaggedStartMap(
                ShowCreation,
                lines,
                lag_ratio=0.5,
                run_time=3,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Create Dots at the intersection of the lines and the easel
        # * ______________________________________________________________________
        
        intersection_pts = VGroup()
        
        for line in lines:
            intersection = line_intersection((line_graph.get_start(), line_graph.get_end()), (line.get_start(), line.get_end()))
            intersection_pt = Dot(
                intersection,
                color=RED_B,
                radius=0.125,
            )
            
            intersection_pt.set_fill(RED_B, opacity=0.5)
            intersection_pt.set_stroke(RED_B, width=2)
            intersection_pts.add(intersection_pt)
        
        self.play(
            LaggedStartMap(
                FadeIn,
                intersection_pts,
                lag_ratio=0.5,
                run_time=3,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Instead of Artist, we have a Special Camera, and instead of the Easel we have a screen
        # * ______________________________________________________________________
        screen_tex = TexText(
            "Screen",
            font_size=TITLE_FONTSIZE*1,
        ).set_color(YELLOW_C)
        
        special_camera_tex = TexText(
            "Special Camera",
            font_size=TITLE_FONTSIZE*1,
        ).set_color(YELLOW_C)
        special_camera_tex.move_to(
            artist_tex.get_center(),
            aligned_edge=DOWN,
        ).shift(DOWN * 0.25)
        screen_tex.move_to(
            line_graph_label.get_center(),
            aligned_edge=DOWN,
        ).shift(DOWN * 0.25)
        
        self.play(
            ReplacementTransform(artist_tex, special_camera_tex),
            ReplacementTransform(line_graph_label, screen_tex),
            run_time=3,
        )
        
        self.play(
            special_camera_tex.animate.move_to(ORIGIN + DOWN*0.5)
        )
        
        # * Special Camera Mechanics
        # * ______________________________________________________________________
        
        # *1. Points between the camera and the easel are projected to the screen
        
        # Draw points on the lines between the camera and the easel at y=0.5
        
        pts_at_y_0_5 = VGroup()
        arrows_to_easel = VGroup()
        
        for line, intersection_dot in zip(lines, intersection_pts):
            pt = line.point_from_proportion(0.25)
            pt = Dot(
                pt,
                color=BLUE_B,
                radius=0.1,
            )
            pt.set_fill(BLUE_B, opacity=0.5)
            pt.set_stroke(BLUE_B, width=2)
            pts_at_y_0_5.add(pt)
            
            arrow = Arrow(
                start=pt.get_center(),
                end=intersection_dot.get_center(),
                color=RED_B,
                stroke_width=2,
            )
            arrows_to_easel.add(arrow)
            
        self.play(
            LaggedStartMap(
                FadeIn,
                pts_at_y_0_5,
                lag_ratio=0.5,
                run_time=3,
            ),
            
            LaggedStartMap(
                GrowArrow,
                arrows_to_easel,
                lag_ratio=0.5,
                run_time=3,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)        
        
        # Fade out the Special Camera tex'
        self.play(
            FadeOut(special_camera_tex),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # *2. Behind the Camera
        
        # Extend the lines to the back of the camera
        dots_x_pos_behind = dot_x_pos * -1
        dots_y_pos_behind = np.ones(len(dot_x_pos)) * -2
        
        dots_behind = VGroup()
        lines_behind = VGroup()
        arrow_from_behind = VGroup()
        
        easel_behind = Line(
            start=plane.c2p(-10, -1),
            end=plane.c2p(10, -1),
            color=YELLOW_C,
            stroke_width=4,
        ).set_opacity(0)
        
        for x, y in zip(dots_x_pos_behind, dots_y_pos_behind):
            dot = Dot(
                plane.c2p(x, y),
                color=BLUE_B,
                radius=0.1,
            )
            dot.set_fill(BLUE_B, opacity=0.5)
            dot.set_stroke(BLUE_B, width=2)
            dots_behind.add(dot)
            
            line = Line(
                start=ORIGIN,
                end=dot.get_center(),
                color=BLUE_B,
                stroke_width=2,
            )
            lines_behind.add(line)
            
            intersection_behind = line_intersection((easel_behind.get_start(), easel_behind.get_end()), (line.get_start(), line.get_end()))
            
            arrow = Arrow(
                start=dot.get_center(),
                end=intersection_behind,
                color=RED_B,
                stroke_width=2,
            )
            
            arrow_from_behind.add(arrow)
                
            
        self.play(
            LaggedStartMap(
                ShowCreation,
                dots_behind,
                lag_ratio=0.5,
                run_time=2,
            ),
            LaggedStartMap(
                ShowCreation,
                lines_behind,
                lag_ratio=0.5,
                run_time=2,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.play(
            LaggedStartMap(
                GrowArrow,
                arrow_from_behind,
                lag_ratio=0.5,
                run_time=3,
            ),
            # Indicate the dots of intersection
            # *[Indicate(dot, scale_factor=2, color=RED) for dot in intersection_pts],
            LaggedStartMap(
                Indicate,
                intersection_pts,
                lag_ratio=0.7,
                scale_factor=2,
                color=RED,
                run_time=3,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Temporarily set the opacity of all lines and dots to 0.2 at once
        self.play(
            *[
            item.animate.set_opacity(0.2)
            for group in [lines_behind, dots_behind, intersection_pts, arrow_from_behind, arrows_to_easel, dots, lines, pts_at_y_0_5]
            for item in group
            ],
            *[FadeOut(item) for item in [arrow_from_behind, arrows_to_easel]],
            
            run_time=1,
        )
        
        # Focus the last arrow
        self.play(
            *[item.animate.set_opacity(1) for item in [lines_behind[-1], dots_behind[-1], intersection_pts[-1], dots[-1], lines[-1], pts_at_y_0_5[-1]]],
            FadeOut(screen_tex),
            run_time=1,
            
        )

        self.wait(NOMINAL_WAIT_TIME)
        
        # * Describe the last dot
        # Get the coords of the dots
        last_dot = dots[-1]
        dot_y_0_5 = pts_at_y_0_5[-1]
        
        last_dot_coords_point = plane.p2c(last_dot.get_center())
        dot_y_0_5_coords_point = plane.p2c(dot_y_0_5.get_center())

        
        space = " \ "
        # Write out the coords of the dot_y_0_5 on screen in (x, y) format
        ldot_tex_lbra, ldot_coord_1, comma, ldot_coord_2, ldot_tex_lket = ldot_label = VGroup(
            Text("("),
            DecimalNumber(last_dot_coords_point[0], num_decimal_places=1,
                          text_config={
                              'font': 'Comic Sans MS',
                          }
                          ),
            Tex(",  "),
            DecimalNumber(last_dot_coords_point[1], num_decimal_places=1),
            Text(")"),
        )
        ldot_label.arrange(RIGHT, buff=0.1)
        ldot_label.set_color(BLUE_B).move_to(
            last_dot.get_center(),
            aligned_edge=DOWN,
        ).shift(UP * 0.5 + RIGHT*1.25)
        
        # Copy
        
        last_dot_copy = last_dot.copy().set_opacity(0.5)
        last_dot_copy.move_to(last_dot.get_center())
        
        last_dot_coords_copy = plane.p2c(last_dot_copy.get_center())
        
        ldot_tex_lbra_copy, ldot_coord_1_copy, comma_copy, ldot_coord_2_copy, ldot_tex_lket_copy = ldot_label_copy = VGroup(
            Text("("),
            DecimalNumber(last_dot_coords_copy[0], num_decimal_places=1),
            Tex(", "),
            DecimalNumber(last_dot_coords_copy[1], num_decimal_places=1),
            Text(")"),
        )
        ldot_label_copy.arrange(RIGHT, buff=0.1)
        ldot_label_copy.set_color(BLUE_B).move_to(
            last_dot.get_center(),
            aligned_edge=DOWN,
        ).shift(DOWN * 0.75 + RIGHT*1.25)
        
        self.play(
            Write(ldot_label),
            run_time=2,
        )
        
        self.play(
            TransformFromCopy(ldot_label, ldot_label_copy),
            run_time=1,
        )
        

        ldot_label_copy.add_updater(lambda m: m.move_to(last_dot_copy.get_center(), aligned_edge=DOWN).shift(DOWN * 0.75 + RIGHT*1.25))
        
        def get_x_coord():
            return plane.p2c(last_dot_copy.get_center())[0]
        def get_y_coord():
            return plane.p2c(last_dot_copy.get_center())[1]
        
        f_always(ldot_coord_1_copy.set_value, get_x_coord)
        f_always(ldot_coord_2_copy.set_value, get_y_coord)
        
        lambda_tex = Tex(
            r"\lambda",
            font_size=TITLE_FONTSIZE*1.2,
        ).set_color(YELLOW_C).next_to(ldot_label, LEFT, buff=0.1)
        
        
        self.play(
            Write(lambda_tex),
            last_dot_copy.animate.move_to(
                intersection_pts[-1].get_center(),
            ),
            run_time=2,
        )
        
        # * LAMBDA Scaling
        # * ______________________________________________________________________
        
        self.play(
            FlashAround(lambda_tex, color=YELLOW_C, buff=0.2),
            run_time=3,
        )
        
        one_half = Tex(
            r"\frac{1}{2}",
            font_size=TITLE_FONTSIZE*1.2,
        ).set_color(YELLOW_C).move_to(
            lambda_tex.get_center(),
        )
        self.play(
            ReplacementTransform(lambda_tex, one_half),
            run_time=3,
        )
        
        
        # Repeat the same procedure for the last_dot_behind
        # Write out the coords of the dot_y_0_5 on screen in (x, y) format
        last_dot_behind = dots_behind[-1]
        last_dot_behind_coords_point = plane.p2c(last_dot_behind.get_center())
        
        lambda_decimal_descriptor, ldot_behind_tex_lbra, ldot_behind_coord_1, comma, ldot_behind_coord_2, ldot_behind_tex_lket = ldot_behind_label = VGroup(
            DecimalNumber(-0.5, num_decimal_places=1),
            Text("("),
            DecimalNumber(last_dot_behind_coords_point[0], num_decimal_places=1),
            Tex(",  "),
            DecimalNumber(last_dot_behind_coords_point[1], num_decimal_places=1),
            Text(")"),
        )
        ldot_behind_label.arrange(RIGHT, buff=0.1)
        ldot_behind_label.set_color(BLUE_B).move_to(
            last_dot_behind.get_center(),
            aligned_edge=DOWN,
        ).shift(UP * 0.75 + LEFT*0.8)
        ldot_behind_label[0].set_color(YELLOW_C)
        
        self.play(
            Write(ldot_behind_label),
            run_time=2,
        )
        self.wait(2)
        
        ldot_behind_copy = last_dot_behind.copy().set_opacity(0.5)
        ldot_behind_copy.move_to(last_dot_behind.get_center())
        

        ldot_behind_label.add_updater(lambda m: m.move_to(ldot_behind_copy.get_center(), aligned_edge=DOWN).shift(UP * 0.75 + LEFT*0.8))
        
        def get_x_coord_behind():
            return plane.p2c(ldot_behind_copy.get_center())[0]
        def get_y_coord_behind():
            return plane.p2c(ldot_behind_copy.get_center())[1]

        def get_lambda_decimal():
            x_ldot_behind = plane.p2c(ldot_behind_copy.get_center())[0]
            x_intersection = plane.p2c(intersection_pts[-1].get_center())[0]
            ratio = x_intersection / x_ldot_behind
            return ratio
        lambda_decimal_descriptor.add_updater(lambda m: m.set_value(get_lambda_decimal()))    
        
        
        f_always(ldot_behind_coord_1.set_value, get_x_coord_behind)
        f_always(ldot_behind_coord_2.set_value, get_y_coord_behind) 
        
        
        self.play(
            ldot_behind_copy.animate.move_to(
            lines_behind[-1].point_from_proportion(0.5),
            ),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            ldot_behind_copy.animate.move_to(
            lines_behind[-1].point_from_proportion(0.25),
            ),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # *3. Extend the lines
        # * ______________________________________________________________________
        
        # Extend the y=2x line
        start = np.array([8, 4])
        end = - start 
        new_line = Line(
            start=start,
            end=end,
            color=BLUE_B,
            stroke_width=4,
        )
        self.play(
            FadeOut(lines_behind[-1]),
            FadeOut(lines[-1]),
            FadeIn(new_line),
            run_time=3,
        )
        # Fadeout all other lines and dots completely
        self.play(
            *[
            item.animate.set_opacity(0)
            for group in [lines_behind[:-1], dots_behind[:-1], intersection_pts[:-1], dots[:-1], lines[:-1], pts_at_y_0_5[:-1]]
            for item in group
            ],
            run_time=1,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # *4. Describe the line
        # * ______________________________________________________________________
        y = "y"
        equal = "="
        m = "m"
        x = "x"
        plus = "+"
        b = "b"
        
        
        line_equation = Tex(
            y, space, equal, space, m, x, space, plus, space, b,
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(BLUE_B).to_edge(RIGHT).shift(DOWN*2 + LEFT*2)

        bg_rect_tex = BackgroundRectangle(
            line_equation,
            color=BLACK,
            buff=0.6)
        
        
        self.play(
            ShowCreation(bg_rect_tex),
            Write(line_equation),
            run_time=2,
        )
        # Cross out the b term
        cross_b = Cross(
            line_equation[-1],
            stroke_width=4,
            color=RED,
        )
        self.play(
            ShowCreation(cross_b),
            run_time=1,
        )
        self.wait(1)
        
        line_equation_iteration_1 = Tex(
            y, space, equal, space, m, x,
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(BLUE_B).move_to(
            line_equation.get_center(),
            )
            
        # line_equation_iteration_1.z_index = 10
        # .to_edge(RIGHT).shift(DOWN*0.5 + LEFT*2.5)
        
        self.play(
            TransformMatchingTex(line_equation, line_equation_iteration_1),
            FadeOut(cross_b),
            run_time=2,
        )
        self.wait(1)
            
        line_equation_iteration_2 = Tex(
            r"\frac{y}{x}", space, equal, space, m,
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(BLUE_B).move_to(
            line_equation_iteration_1.get_center(),
            )
            #.shift(DOWN*0.75)
        #.to_edge(RIGHT).shift(DOWN*1 + LEFT*2.25)
        
        # line_equation_iteration_2.z_index = 10
        
        self.play(
            TransformMatchingTex(line_equation_iteration_1, line_equation_iteration_2),
            run_time=2,
        )
        self.wait(1)      
        
        # Scale by lambda
        line_equation_iteration_3 = Tex(
            r"\frac{ \lambda  y}{ \lambda  x}", space, equal, space, m,
            font_size=TITLE_FONTSIZE*1.5,
            isolate=[r"\lambda"]
            ).set_color(BLUE_B).move_to(
            line_equation_iteration_2.get_center(),
            )
            # .shift(DOWN*0.75)
        
        
        #.to_edge(RIGHT).shift(DOWN*1 + LEFT*2.25)  
        line_equation_iteration_3.set_color_by_tex(r"\lambda", YELLOW_C)
        
        self.play(
            ReplacementTransform(line_equation_iteration_2, line_equation_iteration_3),
            run_time=2,
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        
        
        line_equation_iteration_4 = Tex(
            r"\frac{y}{x}", space, equal, space, m,
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(BLUE_B).move_to(
            line_equation_iteration_3.get_center(),
            )
            # .shift(DOWN*0.75)
        
        line_equation_iteration_4.set_color_by_tex("m", YELLOW_C)
        self.play(
            TransformMatchingTex(line_equation_iteration_3, line_equation_iteration_4),
            # Also FadeOut the decimal descriptor and the lambda_tex
            FadeOut(lambda_decimal_descriptor),
            FadeOut(one_half),
            run_time=2,
        )
        self.play(
            Indicate(line_equation_iteration_4[-1], scale_factor=2, color=YELLOW_C),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.wait(NOMINAL_WAIT_TIME)
        
        # # ! NOT NEEDED        
        # # # Now set the m = 2
        # # line_equation_iteration_5 = Tex(
        # #     r"\frac{y}{x}", space, equal, space, "2",
        # #     font_size=TITLE_FONTSIZE*1.5,
        # #     ).set_color(BLUE_B).move_to(
        # #     line_equation_iteration_4.get_center(),
        # #     )
        # #     # .shift(DOWN*0.75)
        # # line_equation_iteration_5.set_color_by_tex("2", YELLOW_C)
        # # self.play(
        # #     TransformMatchingTex(line_equation_iteration_4, line_equation_iteration_5),
        # #     run_time=3,
        # # )
        # # self.wait(NOMINAL_WAIT_TIME)
        
        # # # Indicate the intersection point and bring it to the front, making it bigger as well
        # # self.play(
        # #     Indicate(intersection_pts[-1], scale_factor=2, color=RED),
        # #     run_time=3,
        # # )
        
        # # self.wait(NOMINAL_WAIT_TIME)
        
        # * Clean up 
        # * ______________________________________________________________________
        
        self.play(
            *[FadeOut(obj) for obj in [
            # line_equation_iteration_5,
            bg_rect_tex,
            ldot_label,
            ldot_label_copy,
            *ldot_behind_label[1:],
            dot_y_0_5,
            ldot_behind_copy,
            last_dot_copy,
            dots[-1],
            dots_behind[-1],
            # Equation
            line_equation_iteration_4,
            
            ]],
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Rotation scene
        # * ______________________________________________________________________
        
        # Attach the intersection point to where the line meets the easel
        
        # Shift the new_line up by one unit
        def get_intersection():
            intersection = line_intersection((line_graph.get_start(), line_graph.get_end()), (new_line.get_start(), new_line.get_end()))
            return intersection

        
        intersection_pts[-1].add_updater(lambda m: m.move_to(get_intersection()))
        
        # Rotate the new line
        self.play(
            line_graph.animate.shift(UP*1.05),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)



        # Draw a dot at a specific proportion of the line
        dot_at_2_1 = Dot(
            new_line.point_from_proportion(0.3825),
            color=BLUE_C,
            radius=0.1,
        )
        dot_at_2_1.set_fill(BLUE_A, opacity=1)
        
        self.play(
            ShowCreation(dot_at_2_1),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Add a trace to the path of the dot
        trace = TracedPath(
            dot_at_2_1.get_center,
            stroke_width=4,
            stroke_color=BLUE_A,
            # stroke_opacity=0.5,
        )
        self.add(trace)
        
        trail = TracingTail(
            intersection_pts[-1].get_center,
            stroke_width=4,
            stroke_color=RED,
            stroke_opacity=0.75,
            # time_traced=5,
        )
        # trail.z_index = 10
        self.add(trail)
        
        # Make sure the intersection point is always facing the camera
        
        # * START ROTATION
        self.play(
            Rotate(
                new_line,
                angle=PI/2,
                about_point=ORIGIN,
                run_time=3,
            ),
            Rotate(
                dot_at_2_1,
                angle=PI/2,
                about_point=ORIGIN,
                axis=OUT,
                run_time=3,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * BIG SCENE ROTATION
        self.play(
            Rotate(
                new_line,
                angle=PI/4,
                about_point=ORIGIN,
            ),
            Rotate(
                dot_at_2_1,
                angle=PI/4,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=5
        )
        self.wait(NOMINAL_WAIT_TIME)
        
                
        self.play(
            Rotate(
                new_line,
                angle=PI/4,
                about_point=ORIGIN,
            ),
            Rotate(
                dot_at_2_1,
                angle=PI/4,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=9
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Label the point at infinity
        infinity_tex_right = Tex(
            "Point", space, "at", space, r"\infty", r"\rightarrow", 
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(BLUE_B).to_edge(RIGHT).shift(UP*1.5)
        infinity_tex_left = Tex(
          r"\leftarrow", "Point", space, "at", space, r"\infty",
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(BLUE_B).to_edge(LEFT).shift(UP*1.5)
        
        
        self.play(
            Write(infinity_tex_right),
            Write(infinity_tex_left),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # ! No need 
        self.play(
            Rotate(
                new_line,
                angle=-PI/4,
                about_point=ORIGIN,
            ),
            Rotate(
                dot_at_2_1,
                angle=-PI/4,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Calculate the angle to rotate the line to y=0
        current_angle = np.arctan2(new_line.get_end()[1] - new_line.get_start()[1], 
                       new_line.get_end()[0] - new_line.get_start()[0])
        target_angle = 0  # For y=0, the line should be horizontal
        rotation_angle = target_angle - current_angle

        # Rotate the line to y=0
        self.play(
            Rotate(
            new_line,
            angle=rotation_angle,
            about_point=ORIGIN,
            ),
            Rotate(
            dot_at_2_1,
            angle=rotation_angle,
            about_point=ORIGIN,
            axis=OUT,
            ),
            run_time=3
        )
        
        # Make a copy of new_line and make it yellow and a bit thicker
        new_line_copy = new_line.copy().set_color(YELLOW_C).set_stroke(width=6)
        
        # Label the new line
        new_line_label = Tex(
            y, space, equal, space, "0",
            font_size=TITLE_FONTSIZE*1.5,
            ).set_color(YELLOW_C).to_edge(RIGHT).shift(DOWN*0.5 + LEFT*0.5)
        
        self.play(
            ShowCreation(new_line_copy),
            Write(new_line_label),
            infinity_tex_left.animate.set_color(YELLOW_C),
            infinity_tex_right.animate.set_color(YELLOW_C),
            run_time=3,
        )
        self.wait(PAUSE_WAIT_TIME*1.5)
        
        # * DOUBLE ANGLE 
        # * ______________________________________________________________________
        self.play(
            Rotate(
                new_line,
                angle=PI/2,
                about_point=ORIGIN,
            ),
            Rotate(
                dot_at_2_1,
                angle=PI/2,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            Rotate(
                new_line,
                angle=PI/2,
                about_point=ORIGIN,
            ),
            Rotate(
                dot_at_2_1,
                angle=PI/2,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=3
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(
            Rotate(
                new_line,
                angle=PI,
                about_point=ORIGIN,
            ),
            Rotate(
                dot_at_2_1,
                angle=PI,
                about_point=ORIGIN,
                axis=OUT,
            ),
            run_time=10
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # !! NOT NEEDED -- this is my pause
        self.play(
            Rotate(
                new_line,
                angle=2*PI,
                about_point=ORIGIN,
                lag_ratio=0.5,
            ),
            Rotate(
                dot_at_2_1,
                angle=2*PI,
                about_point=ORIGIN,
                axis=OUT,
                lag_ratio=0.5,
            ),
            run_time=30
        )
        self.wait(PAUSE_WAIT_TIME)
        
        
        # * Final Scene, Transforming the circle into a sphere and the lines into planes
        # * ______________________________________________________________________
        # Fade out the infinity labels
        self.play(
            FadeOut(infinity_tex_right),
            FadeOut(infinity_tex_left),
            FadeOut(title),
            FadeOut(new_line_label),
            FadeOut(bg_rect_title),
            FadeOut(plane),
            run_time=3,
        )
        # Create a circle aroung the traced path, so basically a circle with radius=2 about the origin
        circle = Circle(
            radius=2.1,
            color=BLUE_B,
            stroke_width=4,
            stroke_color=BLUE_B,
            fill_opacity=0.5,
            fill_color=BLUE_B,
            
        )
        self.play(
            ShowCreation(circle),
            run_time=3,
        )
        
        # Draw a 3D axes now
        axes = ThreeDAxes(
            x_range=[-10, 10, 1],
            y_range=[-10, 10, 1],
            z_range=[-10, 10, 1],

        )
        self.play(
            ShowCreation(axes),
            run_time=3,
        )
        
        # Now add a tracing path to the circle and rotate by 360 to make it a sphere

        circles = VGroup()
        for i in range(8):  # Create 12 copies for a full rotation
            new_circle = circle.copy().rotate(
            angle=(i * 360*DEGREES/16),  # Rotate by 30 degrees each step
            about_point=ORIGIN,
            axis=UP,
            )
            new_circle.set_opacity(0.25)  # Set opacity for better visualization
            # Set stroke with BLUE_D color
            new_circle.set_stroke(width=7, color=BLUE_D)
            circles.add(new_circle)
            

        # Do a similar thing with the lines
        inf_lines = VGroup()
        for i in range(8):
            l = new_line.copy().rotate(
            angle=(i * 360*DEGREES/16),  # Rotate by 30 degrees each step
            about_point=ORIGIN,
            axis=UP,
            )
            l.set_color(YELLOW_C)
            l.set_opacity(0.25)
            l.set_stroke(width=2)
            inf_lines.add(l)
            
        easel_lines = VGroup()
        for i in range(8):
            l = line_graph.copy().rotate(
            angle=(i * 360*DEGREES/16),  # Rotate by 30 degrees each step
            about_point=ORIGIN,
            axis=UP,
            )
            l.set_color(YELLOW_C)
            l.set_opacity(0.5)
            l.set_stroke(width=2)
            easel_lines.add(l)

        self.play(
            LaggedStartMap(
                ShowCreation,
                circles,
                lag_ratio=0.5,
                run_time=10,
            ),
            LaggedStartMap(
                ShowCreation,
                easel_lines,
                lag_ratio=0.5,
                run_time=10,
            ),
            LaggedStartMap(
                ShowCreation,
                inf_lines,
                lag_ratio=0.5,
                run_time=10,
            ),
            self.camera.frame.animate.set_euler_angles(
                theta=70*DEGREES,
                phi=50*DEGREES,
            ),
            FadeOut(circle),
            
            run_time=10,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # Fade out the lines and put a rectangle in their place  
        
        rectangle_inf_lines = Square3D(
            side_length=20,
            u_range=[-0.5, 0.5],
            v_range=[-0.5, 0.5],
            color=YELLOW_C,
        ).set_opacity(0.1)
        
        rectangle_easel_lines = Square3D(
            side_length=20,
            u_range=[-0.5, 0.5],
            v_range=[-0.5, 0.5],
            color=YELLOW_C,
        ).set_opacity(0.1)
        rectangle_easel_lines.move_to(
            new_line.get_center(),
        )
        rectangle_easel_lines.rotate(
            angle=PI/2,
            # about_point=ORIGIN,
            axis=RIGHT,
        )

        # Move its center to the center of the line_graph
        rectangle_inf_lines.move_to(
            line_graph.get_center(),
        )
        rectangle_inf_lines.rotate(
            angle=PI/2,
            # about_point=ORIGIN,
            axis=RIGHT,
        )
        
        sphere = Sphere(
            radius=2.1,
            color=BLUE_B,
        ).set_opacity(0.75) 
        # sphere_mesh = SurfaceMesh(
        #     sphere,
        #     color=BLUE_D,)
        
        self.play(
            FadeOut(easel_lines),
            FadeOut(inf_lines),
            FadeOut(circles),
            ShowCreation(sphere),
            
            run_time=3,
        )

        self.play(
            ShowCreation(rectangle_inf_lines),
            run_time=1,
        )
        
     
        self.play(
            ShowCreation(rectangle_easel_lines),
            run_time=1,
        )
        

        # * New title to the left
        new_title = Title(
            "Real Projective Plane",
            font_size=TITLE_FONTSIZE*1.25,
            match_underline_width_to_text=True,
        ).set_color(BLUE_D).to_edge(LEFT)
        new_title.fix_in_frame()
        
        self.play(
            Write(new_title),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Now our points are (x, 1, z) 
        
        new_points_tex = Tex(
            r"\mathbb{P}", r"\mathbb{R}^2", ":", space,
            r"\left(x, \  y, \ z\right)")
            # r"\left (" + "x,"+ space+ "y,"+ space+ "z"+ "\right)")
        new_points_tex.move_to(
            new_title.get_center(),
        ).shift(DOWN)
        new_points_tex.fix_in_frame()
        
        
        self.play(
            Write(new_points_tex),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)

        new_points_tex_scaled = Tex(
            r"\mathbb{P}", r"\mathbb{R}^2", ":", space,
            r"\frac{1}{y}", space,
            # r"\left(" + "x,"+ space+ "y,"+ space+ "z"+ "\right)")
            r"\left( x, \ y, \ z\right)")
        
        new_points_tex_scaled.move_to(
            new_points_tex.get_center(),
        )
        new_points_tex_scaled.fix_in_frame()

        self.play(
            TransformMatchingTex(new_points_tex, new_points_tex_scaled),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        new_points_tex_final = Tex(
            r"\mathbb{P}", r"\mathbb{R}^2", ":", space,
            r"\left ( \frac{x}{y}, \ 1, \ \frac{z}{y}\right )")
            # "\left(" + space+
            # r"\frac{x}{y}," + space+
            # r"1" + space+
            # r"\frac{z}{y}" + space+
            # "\right)")

        new_points_tex_final.move_to(
            new_points_tex_scaled.get_center(),
        )
        new_points_tex_final.fix_in_frame()
        self.play(
            TransformMatchingTex(new_points_tex_scaled, new_points_tex_final),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Indicate that only x and z are our free parameters now, and color them yellow
        self.play(
            Indicate(new_points_tex_final[-4:-1], scale_factor=1.2, color=YELLOW_C),
            Indicate(new_points_tex_final[-10:-7], scale_factor=1.2, color=YELLOW_C),
            run_time=1.5,
        )
        self.play(
            new_points_tex_final[-4:-1].animate.set_color(YELLOW_C),
            new_points_tex_final[-10:-7].animate.set_color(YELLOW_C),
            run_time=1.5,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Correspondence between CP1 and PR2
        # * ______________________________________________________________________
        w_correspondence_with_xy_zy = Tex(
            "u", space, equal, r"\frac{w}{v}", space, r"\Longleftrightarrow ", space,
            
            r"\left ( \frac{x}{y}, \ 1, \ \frac{z}{y}\right )", space,)
            # r"\left {" + r"\frac{x}{y}," + space + r"1," + space + r"\frac{z}{y}"+ r"\right }")
            # r"\left {" + r"\frac{x}{y}," + space + r"\frac{z}{y}"+ r"\right } ")
        w_correspondence_with_xy_zy.move_to(
            new_points_tex_final.get_center(),
        ).shift(DOWN*1.25)
        w_correspondence_with_xy_zy.fix_in_frame()

        self.play(
            Write(w_correspondence_with_xy_zy),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)        
        
        correspondence_tex = Tex(
            r"\mathbb{P}", r"\mathbb{C}^1", r"\Longleftrightarrow ", r"\mathbb{P}", r"\mathbb{R}^2",
            font_size=TITLE_FONTSIZE*1.5,
        ).move_to(w_correspondence_with_xy_zy.get_center()).shift(DOWN*1.25 + LEFT*0.25)
        correspondence_tex.fix_in_frame()
        
        self.play(
            Write(correspondence_tex),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        bbox_result =Polygon(
            correspondence_tex.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            correspondence_tex.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            correspondence_tex.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            correspondence_tex.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

        )
        bbox_result.fix_in_frame()
        self.play(
            ShowCreation(bbox_result),
            run_time=2,
        )
        self.wait(PAUSE_WAIT_TIME*2)

        

