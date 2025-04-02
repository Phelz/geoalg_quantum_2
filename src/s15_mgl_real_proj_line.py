from manimlib import *
from src.definitions import *



class ProjectiveGeometry(Scene):
    def construct(self):
        
        # # # * Title
        # # # # * ______________________________________________________________________
        # title = Title(
        #     f'Projective Geometry', include_underline=False, 
        #     font_size=TITLE_FONTSIZE*1.5,)
        # title.to_corner(UL)
        # title.set_color(BLUE_D)
        # title.fix_in_frame()
        
        # self.play(
        #     Write(title),
        #     run_time=3,
        # )
        # self.wait(NOMINAL_WAIT_TIME)
        
        # * Construct a plane
        # * ______________________________________________________________________
        # plane = NumberPlane(
        #     x_range=[-1_000_000, 1_000_000, 500],
        #     y_range=[-1_000_000, 1_000_000, 500],
        #     # background_line_style={
        #         # "stroke_color": BLUE_D,
        #         # "stroke_width": 1,
        #         # "stroke_opacity": 0.4
        #     # }
        #     height=20_000,
        #     width=20_000,
        # )
        
        plane = NumberPlane(
            x_range=[-1_000, 1_000, 10],
            y_range=[-1_000, 1_000, 10],
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 0.,
                "stroke_opacity": 0.
            },
            faded_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.25
            },
            height=2_000,
            width=2_000,
        )
        
        self.play(
            ShowCreation(plane, rate_func=smooth),
            run_time=1,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        
        # * Drawing f(x) = x^2 + 1
        # * ______________________________________________________________________
        f = lambda x: x**2 + 2
        graph = plane.get_graph(
            f,
            color=YELLOW_C,
        )
        
        graph_label = plane.get_graph_label(
            graph,
            label='f(x) = x^2 + 1',
            x=10,
            # y_val=10,
        )
        
        self.play(
            ShowCreation(graph),
            Write(graph_label),
            run_time=5,
        )
        self.wait(NOMINAL_WAIT_TIME)
        

        
        # * Change the prespective to 3D
        # * ______________________________________________________________________
        self.play(
            self.camera.frame.animate.set_euler_angles(
                theta=0*DEGREES,
                phi=95*DEGREES,
            ).shift(OUT*3),
            run_time=10,
        )
        
        self.wait(NOMINAL_WAIT_TIME)
        # * Highlight the point at infinity
        # * ______________________________________________________________________

        pt_inf_label = Tex(
            "Point \ at", ' \ ', r'\infty',
            font_size=TITLE_FONTSIZE,
        ).set_color(BLUE_B)
        pt_inf_label.fix_in_frame()

        self.play(
            Write(pt_inf_label),
            run_time=2,
        )
        self.wait(NOMINAL_WAIT_TIME)