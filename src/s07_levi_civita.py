from manim import *
from reactive_manim import *
import manimforge as mf
mf.setup()
import definitions as dfs
        

class LeviCevita(Scene):

    def construct(self):

        # * ______________________________________________________________________
        self.next_section("Title", skip_animations=False)
        # * ______________________________________________________________________
        title = Text(
            f'The Levi-Civita Tensor', color=BLUE_D,
            font_size=dfs.TITLE_FONTSIZE
        )
        title.to_edge(UP)
        
        self.play(Write(title), run_time=2)
        self.wait(dfs.NOMINAL_WAIT_TIME)
        # * ______________________________________________________________________
        self.next_section("OG Definition", skip_animations=False)
        # * ______________________________________________________________________

        levi_cevita = MathTex(
            "\\epsilon_{ijk} = \\begin{cases} 1 & \\text{if } (i,j,k) \\text{ is an even permutation of } (1,2,3), \\\\ -1 & \\text{if } (i,j,k) \\text{ is an odd permutation of } (1,2,3), \\\\ 0 & \\text{otherwise.} \\end{cases}"
        )

        self.play(Write(levi_cevita, run_time=3))
        self.wait()
        # Make it smaller and move it up a bit
        self.play(levi_cevita.animate.scale(0.9).shift(UP))

        # Provide examples
        
        
        lc_ex_text = MathTex("\\epsilon_{123} = \\ 1").shift(DOWN*1.5).scale(2)
        lc_ex_text[0][3].set_color(YELLOW)  # Color the "3"

        self.play(Write(lc_ex_text), run_time=1)
        self.wait(dfs.NOMINAL_WAIT_TIME)

        # Animate the example by switching the 2 and the 3
        lc_ex_anti = MathTex("\\epsilon_{132} = -1").shift(DOWN*1.5).scale(2)
        lc_ex_anti[0][2].set_color(YELLOW)  # Color the "3"
        self.play(TransformMatchingTex(lc_ex_text, lc_ex_anti), run_time=1)
        self.wait(dfs.NOMINAL_WAIT_TIME)

        lc_ex_cyc = MathTex("\\epsilon_{312} = 1").shift(DOWN*1.5).scale(2)
        lc_ex_cyc[0][1].set_color(YELLOW)  # Color the "3"
        self.play(TransformMatchingTex(lc_ex_anti, lc_ex_cyc), run_time=1)
        self.wait(dfs.NOMINAL_WAIT_TIME)


        # Fade out everything
        self.play(FadeOut(levi_cevita), FadeOut(lc_ex_cyc), FadeOut(lc_ex_anti))

        # * ______________________________________________________________________
        self.next_section("A Geometric-Tensor Attempt", skip_animations=False)
        # * ______________________________________________________________________


        # Visualize the tensor as 3d grid of numbers, with no tips
        grid = ThreeDAxes( 
            x_range=[-3, 3],
            y_range=[-3, 3],
            z_range=[-3, 3],
            x_length=6,
            y_length=6,
            z_length=6,
            axis_config={"include_numbers": False, "include_tip": False},
        )
        # Set the axes to be invisible
        grid.set_stroke(width=0)
        # hide the axes tips

        # hide the axes

        # self.play(Create(grid), run_time=2)
        self.wait(1)

        # Create the 3d grid of numbers
        grid_numbers_eps = VGroup()
        grid_numbers_actual = VGroup()


        # tensor = ThreeDVMobject()
        # self.play(Create(tensor), run_time=2)
        prism = Prism(dimensions=[3, 3, 3], fill_opacity=0.1, stroke_width=.1, stroke_color=WHITE, fill_color=WHITE)
        self.play(Create(prism), run_time=2)

        self.wait(1)
        self.play( Rotate(prism, angle=-PI/8, axis=LEFT),
                   Rotate(grid, angle=-PI/8, axis=LEFT),
                  run_time=1)
        
        self.play( Rotate(prism, angle=-PI/6, axis=UP),
                   Rotate(grid, angle=-PI/6, axis=UP),
                  run_time=1)

        self.wait(1)

        for i in range(3):
            for j in range(3):
                for k in range(3):
                    grid_numbers_eps.add(MathTex(f"\\epsilon_{{{i+1}{j+1}{k+1}}}").move_to(grid.coords_to_point(i-1, j-1, k-1)))

        grid_numbers_eps.set_opacity(0.5)
        self.play(Write(grid_numbers_eps), run_time=3)
        self.wait(1)
        self.play(FadeOut(grid_numbers_eps), run_time=1)


        # Now turn those into the actual numbers
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    if (i, j, k) == (0, 1, 2) or (i, j, k) == (1, 2, 0) or (i, j, k) == (2, 0, 1):
                        grid_numbers_actual.add(MathTex("1").move_to(grid.coords_to_point(i-1, j-1, k-1)))
                    elif (i, j, k) == (0, 2, 1) or (i, j, k) == (2, 1, 0) or (i, j, k) == (1, 0, 2):
                        grid_numbers_actual.add(MathTex("-1").move_to(grid.coords_to_point(i-1, j-1, k-1),))
                    else:
                        grid_numbers_actual.add(MathTex("0").move_to(grid.coords_to_point(i-1, j-1, k-1)))

        grid_numbers_actual.set_opacity(0.5)

        self.play(Write(grid_numbers_actual), run_time=3)
        # set the opacity of the grid numbers to 0

        # Rotate the prism, grid and numbers
        self.play( Rotate(prism, angle=PI/4, axis=UP),
                   Rotate(grid, angle=PI/4, axis=UP),
                   Rotate(grid_numbers_actual, angle=PI/4, axis=UP),
                  run_time=5)
        
        self.play( Rotate(prism, angle=-PI/4, axis=UP),
            Rotate(grid, angle=-PI/4, axis=UP),
            Rotate(grid_numbers_actual, angle=-PI/4, axis=UP),
            run_time=5)

        
        
        
        
        
        
        
        
        