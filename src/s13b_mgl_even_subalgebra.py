from manimlib import *
from src.definitions import *


class _13B_EvenSubalgebra(Scene):
    def construct(self):
        
        # * Symbols
        
        lbracket = "("; rbracket = ")"
        lbracket_set = r"\{"; rbracket_set = r"\}"
        
        plus = "+"; minus = "-"; equal = "="; dot = r"\cdot"
        space = r" \ "; comma = r","
        
        def_symb = r"\equiv"
        
        gamma_0 = r"\mathbf{\gamma_0}"
        gamma_1 = r"\mathbf{\gamma_1}"
        gamma_2 = r"\mathbf{\gamma_2}"
        gamma_3 = r"\mathbf{\gamma_3}"
        
        gamma_i = r"\mathbf{\gamma_i}"
        gamma_j = r"\mathbf{\gamma_j}"
        
        sigma_1 = r"\mathbf{\sigma_1}"
        sigma_2 = r"\mathbf{\sigma_2}"
        sigma_3 = r"\mathbf{\sigma_3}"

        sigma_i = r"\mathbf{\sigma_i}"      

        
        # * Title
        title = Title(
            "The Even Subalgebra",
            stroke_color=BLUE_D,
            include_underline=True,
            match_underline_width_to_text=True,
            underline_style=dict(stroke_width=3, stroke_color=WHITE),
        ).to_corner(UL).set_color(BLUE_D)
        
        
        self.play(Write(title))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Basisc vectors set
        basis_set = Tex(
            lbracket_set,
            gamma_0, comma,
            space,
            gamma_1, comma,
            space,
            gamma_2, comma,
            space,
            gamma_3, rbracket_set
        ).move_to(title.get_center() + DOWN*1.25).to_edge(LEFT)
        
        self.play(Write(basis_set))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Bivector generators, the set gamma_i gamma_0 and gamma_i gamma_j
        sigma_set = Tex(
            lbracket_set,
            gamma_i, gamma_0, 
            rbracket_set)
        sigma_set.move_to(basis_set.get_center()).shift(RIGHT*5)
        
        other_set = Tex(
            lbracket_set,
            gamma_i, gamma_j, 
            rbracket_set)
        other_set.move_to(sigma_set.get_center()).shift(RIGHT*3)
        
        self.play(Write(sigma_set))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(other_set))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Focusing on the sigma set, Indicate and add sigma_i
        
        sigma_i_tex = Tex(
            sigma_i, space, def_symb, space, space
        ).next_to(sigma_set, LEFT, aligned_edge=DOWN)
        
        self.play(FadeIn(sigma_i_tex))
        self.play(
            Indicate(sigma_set, scale_factor=1.2),
            Indicate(sigma_i_tex, scale_factor=1.2),
            run_time=3,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Generating Scalars: Unitarity
        
        # sigma_i_squared = Tex(
        #     lbracket, sigma_i, ")^2"
        