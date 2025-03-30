from manim import *
from reactive_manim import *
import manimforge as mf
mf.setup()
import definitions as dfs



class GeometricProduct(VectorScene):

    def construct(self):
        
        # * ______________________________________________________________________
        self.next_section("Title", skip_animations=False)
        # * ______________________________________________________________________
        title = Text(
            f'The Geometric Product', color=BLUE_D,
            font_size=dfs.TITLE_FONTSIZE
        )
        title.to_edge(UP)
        
        # Geo product of u and v
        uterm = MathTex( "\\mathbf{u}" )
        vterm = MathTex( "\\mathbf{v}" )
        
        
        geo_prod_tex = MathTex(
            uterm, vterm, "=", uterm, "\\cdot", vterm, "+", uterm, "\\wedge", vterm,
            # "\\mathbf{u}  \\mathbf{v}  = \\mathbf{u} \\cdot \\mathbf{v} + \\mathbf{u} \\wedge \\mathbf{v}",
            color=WHITE, font_size=int(4 * dfs.TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *1.5)
        
        geo_prod_box = SurroundingRectangle(
            geo_prod_tex, buff=0.3, color=WHITE, corner_radius=0.005
        )
        
        self.play(Write(title), run_time=2)
        
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        self.play(
            Write(geo_prod_tex),
            Create(geo_prod_box),
            runtime=3
        )
        self.wait(dfs.PAUSE_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("Complex Numbers", skip_animations=False)
        # * ______________________________________________________________________
        
        z1 = MathTex("z_1", "=", "a" "+", "i", "b", 
            # tex_to_color_map={"i": BLUE_C},
            color=WHITE, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *3 + LEFT*1.75)
        z1[3].set_color(BLUE_C)         
        
        z2 = MathTex(
            # "z_2 = c - i b",
            "z_2", "=", "c", "-", "i", "d",
            # tex_to_color_map={"i": BLUE_C},
            color=WHITE, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *3 + RIGHT*1.75)
        z2[4].set_color(BLUE_C)
        
        self.play(
            Write(z1),
            runtime=3
        )
        
        self.wait(dfs.NOMINAL_WAIT_TIME)
        self.play(
            Write(z2),
            runtime=3
        )
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        z1_plus_z2 = MathTex(
            "z_1 + z_2", "=", "(a + c)", "+", "(b - d)", "i",
            # "z_1 + z_2 = (a + c) + (b - d) i",
            # tex_to_color_map={"i": BLUE_C},
            color=WHITE, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        ).to_edge(UP).shift(DOWN *4)
        z1_plus_z2[-1].set_color(BLUE_C)

        self.play(
            Write(z1_plus_z2),
            runtime=3
        )
        
        self.wait(dfs.PAUSE_WAIT_TIME)
        
        #  FadeOut all complex text
        self.play(
            FadeOut(z1),
            FadeOut(z2),
            FadeOut(z1_plus_z2),
            runtime=2
        )
        
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        self.play(
            FadeOut(title),
            FadeOut(geo_prod_box),
            runtime=1.5
        )
        
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Vector Setup", skip_animations=False)
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
            uterm, color=RED, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        ).next_to(u, DOWN)
        v_label = MathTex(
            vterm, color=BLUE, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        ).next_to(v, LEFT)
        
        self.play(
            Write(u_label),
            Write(v_label),
            runtime=2
        )
        
                
        # * ______________________________________________________________________
        self.next_section("Label Setup", skip_animations=False)
        # * ______________________________________________________________________
        
        
        left_rotation_symbol = MathTex(
            "\\circlearrowleft", color=WHITE, font_size=int(5 * dfs.TITLE_FONTSIZE / 3)
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

        self.wait(dfs.NOMINAL_WAIT_TIME)
        
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
        self.next_section("Parallelogram Setup", skip_animations=False)
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
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        
        # * ______________________________________________________________________
        self.next_section("Wedge Simplification", skip_animations=False)
        # * ______________________________________________________________________
        
        cross = Cross(geo_prod_tex[3] +  geo_prod_tex[4] + geo_prod_tex[5] ).scale(0.35)
        self.play(
            Write(cross),
            Indicate(geo_prod_tex[3], rate_func=there_and_back),
            Indicate(geo_prod_tex[4], rate_func=there_and_back),
            Indicate(geo_prod_tex[5], rate_func=there_and_back),
            run_time=3
        )
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
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
        
        self.wait(dfs.PAUSE_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("Zero Wedge", skip_animations=False)
        # * ______________________________________________________________________

        wedge_term = MathTex(geo_prod_tex[-3].copy(), geo_prod_tex[-2].copy(), geo_prod_tex[-1].copy(), 
             font_size=int(4 * dfs.TITLE_FONTSIZE / 3)
        ).to_corner(UR).shift(DOWN *0.75 + LEFT*2)
        
        self.play(
            TransformInStages.from_copy(geo_prod_tex, wedge_term, lag_ratio=0.5, run_time=2),
            runtime=2
        )
        
        self.wait(dfs.PAUSE_WAIT_TIME)
        
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
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        wedge_term.append("=")
        wedge_term.append("0")
        self.play(
            TransformInStages.progress(wedge_term, lag_ratio=0.5, run_time=2),
        )
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("Dot Simplification", skip_animations=False)
        # * ______________________________________________________________________

        e1_e1_tex = MathTex(e1_term, e1_term, "=", e1_term, "\\cdot", e1_term,
                            font_size=int(4 * dfs.TITLE_FONTSIZE / 3))
        e1_e1_tex.to_corner(UR).shift(DOWN * 2 + LEFT * 1)

        self.play(
            TransformMatchingTex(v_label.copy(), e1_e1_tex),
            runtime=3
        )
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        e1_e1_tex.append("=")
        e1_e1_tex.append("1")
        self.play(
            TransformInStages.progress(e1_e1_tex, lag_ratio=0.5, run_time=2),
        )
        # self.wait(dfs.NOMINAL_WAIT_TIME)
        wedge_term_center = wedge_term.get_center()
        e1_e1_tex.move_to(wedge_term_center)
        
        self.play(
            FadeOut(wedge_term),
            TransformInStages.progress(e1_e1_tex, lag_ratio=0.5, run_time=2),
        )
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        # Create a box around that final result
        box_dot_simple = SurroundingRectangle(
            e1_e1_tex, buff=0.3, color=WHITE, corner_radius=0.005
        )
        self.play(
            Create(box_dot_simple),
            run_time=2
        )
        self.wait(dfs.NOMINAL_WAIT_TIME)
        
        # * ______________________________________________________________________
        self.next_section("General Case", skip_animations=False)
        # * ______________________________________________________________________
        
        e_i = MathTex(
            "\\mathbf{e}_i", color=RED, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        )
        e_j = MathTex(
            "\\mathbf{e}_j", color=BLUE, font_size=int(3 * dfs.TITLE_FONTSIZE / 3)
        )
        
        general_case_wedge = MathTex(e_i, e_j, "=", e_i, "\\wedge", e_j,
            font_size=int(4 * dfs.TITLE_FONTSIZE / 3)
        ).move_to(geo_prod_tex.get_center())
        
        general_case_dot = MathTex(e_i, e_i, "=", e_i, "\\cdot", e_i, "=", "1",
            font_size=int(4 * dfs.TITLE_FONTSIZE / 3)
        ).move_to(box_dot_simple.get_center())
        
        self.play(
            TransformMatchingTex(e1_e1_tex, general_case_dot),
            TransformMatchingTex(geo_prod_tex, general_case_wedge),
            runtime=3
        )
        self.wait(dfs.PAUSE_WAIT_TIME)
        
        # Fade out everything
        self.play(
            [FadeOut(mob) for mob in self.mobjects]
        )
        
        
