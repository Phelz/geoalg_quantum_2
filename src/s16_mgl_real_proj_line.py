from manimlib import *
from src.definitions import *



class RealProjectiveLine(Scene):
    def construct(self):
        
        # * Title
        # * ______________________________________________________________________
        title = Title(
            f'Real Projective Line', include_underline=False, 
            font_size=TITLE_FONTSIZE*1.5,)
        title.to_corner(UL)
        title.set_color(BLUE_D)
        title.fix_in_frame()
        
        self.play(
            Write(title),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Construct a plane
        # * ______________________________________________________________________

        plane = NumberPlane(
            x_range=[-7, 7, 1],
            y_range=[-5, 5, 1],
            # background_line_style={
            #     "stroke_color": BLUE_D,
            #     "stroke_width": 1,
            #     "stroke_opacity": 1
            # },
            # faded_line_style={
            #     # "stroke_color": BLUE_D,
            #     "stroke_width": 0.5,
            #     "stroke_opacity": 1
            # },
            height=15,
            width=15,
        )
        
        self.play(
            ShowCreation(plane),
            run_time=2,
        )
        
        # * Signify the artist by a dot at the origin
        # * ______________________________________________________________________
        origin = plane.c2p(0, 0)
        
        
        artist_dot = Dot(
            origin,
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
            Flash(origin, color=YELLOW),
            Write(artist_tex),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        self.play(
            ShowCreation(artist_dot),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Draw the line that is the Easel for the artist
        # * ______________________________________________________________________
        
        line_graph = Line(
            start=plane.c2p(-7, 1),
            end=plane.c2p(7, 1),
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
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
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
        dot_y_pos = np.ones(len(dot_x_pos)) * 1.75
        
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
        
        # # * Draw lines connecting the dots to the origin
        # # * ______________________________________________________________________
        lines = VGroup()
        for dot in dots:
            line = Line(
                start=origin,
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
                radius=0.1,
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
        dots_y_pos_behind = np.ones(len(dot_x_pos)) * -1.75
        
        dots_behind = VGroup()
        lines_behind = VGroup()
        arrow_from_behind = VGroup()
        
        easel_behind = Line(
            start=plane.c2p(-7, -1),
            end=plane.c2p(7, -1),
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
                start=origin,
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
                run_time=3,
            ),
            LaggedStartMap(
                ShowCreation,
                lines_behind,
                lag_ratio=0.5,
                run_time=3,
            ),
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.play(
            LaggedStartMap(
                GrowArrow,
                arrow_from_behind,
                lag_ratio=0.5,
                run_time=7,
            ),
            # Indicate the dots of intersection
            # *[Indicate(dot, scale_factor=2, color=RED) for dot in intersection_pts],
            LaggedStartMap(
                Indicate,
                intersection_pts,
                lag_ratio=0.7,
                scale_factor=2,
                color=RED,
                run_time=7,
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
        last_dot_behind = dots_behind[-1]
        
        last_dot_coords_point = plane.p2c(last_dot.get_center())
        dot_y_0_5_coords_point = plane.p2c(dot_y_0_5.get_center())
        last_dot_behind_coords_point = plane.p2c(last_dot_behind.get_center())
        
        space = " \ "
        # Write out the coords of the dot_y_0_5 on screen in (x, y) format
        ldot_tex_lbra, ldot_coord_1, comma, ldot_coord_2, ldot_tex_lket = ldot_label = VGroup(
            Text("("),
            DecimalNumber(last_dot_coords_point[0], num_decimal_places=2,
                          text_config={
                              'font': 'Comic Sans MS',
                          }
                          ),
            TexText(",  "),
            DecimalNumber(last_dot_coords_point[1], num_decimal_places=2),
            Text(")"),
        )
        ldot_label.arrange(RIGHT, buff=0.1)
        ldot_label.set_color(BLUE_B).move_to(
            last_dot.get_center(),
            aligned_edge=DOWN,
        ).shift(UP * 0.5 + RIGHT*1.25)
        
        # Copy
        ldot_tex_lbra_copy, ldot_coord_1_copy, comma_copy, ldot_coord_2_copy, ldot_tex_lket_copy = ldot_label_copy = VGroup(
            Text("("),
            DecimalNumber(last_dot_coords_point[0], num_decimal_places=2),
            Text(", "),
            DecimalNumber(last_dot_coords_point[1], num_decimal_places=2),
            Text(")"),
        )
        ldot_label_copy.arrange(RIGHT, buff=0.1)
        ldot_label_copy.set_color(BLUE_B).move_to(
            last_dot.get_center(),
            aligned_edge=DOWN,
        ).shift(DOWN * 0.5 + RIGHT*1.25)
        
        self.play(
            Write(ldot_label),
            run_time=2,
        )
        
        self.play(
            TransformFromCopy(ldot_label, ldot_label_copy),
            run_time=1,
        )
        
        
        

        # last_dot_coords_tex = Tex(
        #     f"({last_dot_coords_point[0]:.2f}, {last_dot_coords_point[1]:.2f})",
        #     font_size=TITLE_FONTSIZE*1,
        # ).set_color(BLUE_B)
        # last_dot_coords_tex.move_to(
        #     last_dot.get_center(),
        #     aligned_edge=DOWN,
        # ).shift(UP * 0.5 + RIGHT*1.25)
        
        # # Make a copy of the tex down below
        # last_dot_coords_tex_copy = last_dot_coords_tex.copy().move_to(
        #     last_dot.get_center(),
        #     aligned_edge=DOWN,
        # ).shift(DOWN * 0.5 + RIGHT*1.25)
        
        # self.play(
        #     Write(last_dot_coords_tex),
        #     run_time=3,
        # )
        # self.play(
        #     TransformFromCopy(last_dot_coords_tex, last_dot_coords_tex_copy),
        #     run_time=1,
            
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        
        # # * Now, add updaters that move this last dot to the intersection point, updating the numbers in the tex
        # last_dot_copy = last_dot.copy().set_opacity(0.5)
        # last_dot_copy.move_to(last_dot.get_center())
        
        # last_dot_copy_coords = plane.p2c(last_dot_copy.get_center())
        
        # last_dot_coords_tex_copy.add_updater(lambda m: m.move_to(last_dot_copy.get_center(), aligned_edge=DOWN).shift(DOWN * 0.5 + RIGHT*1.25))
        
        # last_dot_coords_tex_copy.make_number_changeable()
                                             

        
        # # Now move the last dot to the intersection point
        # self.play(
        #     last_dot_copy.animate.move_to(intersection_pts[-1].get_center()),
        #     run_time=3,
        # )
        

        
        # # Get the coords of the dots
        # last_dot = dots[-1]
        # dot_y_0_5 = pts_at_y_0_5[-1]
        # last_dot_behind = dots_behind[-1]
        
        # last_dot_coords_point = plane.p2c(last_dot.get_center())
        # dot_y_0_5_coords_point = plane.p2c(dot_y_0_5.get_center())
        # last_dot_behind_coords_point = plane.p2c(last_dot_behind.get_center())
        
        # # Write out the coords of the dot_y_0_5 on screen in (x, y) format
        # last_dot_coords_tex = Tex(
        #     f"({last_dot_coords_point[0]:.2f}, {last_dot_coords_point[1]:.2f})",
        #     font_size=TITLE_FONTSIZE*1,
        # ).set_color(BLUE_B)
        # last_dot_coords_tex.move_to(
        #     last_dot.get_center(),
        #     aligned_edge=DOWN,
        # ).shift(UP * 0.5 + RIGHT*1.25)
        
        # self.play(
        #     Write(last_dot_coords_tex),
        #     run_time=3,
        # )