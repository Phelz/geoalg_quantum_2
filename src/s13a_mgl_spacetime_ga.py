
from manimlib import *
from src.definitions import *



class _13A_SGA(Scene):
    def construct(self):
        
        # * Symbols
        
        lbracket = "("; rbracket = ")"
        lbracket_set = r"\{"; rbracket_set = r"\}"
        
        plus = "+"; minus = "-"; equal = "="; dot = r"\cdot"
        space = r" \ "; comma = r","
        
        metric = r"\eta_{\alpha \beta}"
        metric_raised = r"\eta^{\alpha \beta}"
        metric_same_index = r"\eta_{\alpha \alpha}"
        metric_22 = r"\eta_{22}"
        metric_00 = r"\eta_{00}"
        
        
        gamma_alpha = r"\mathbf{\gamma_\alpha}"
        gamma_beta = r"\mathbf{\gamma_\beta}"
        
        gamma_0 = r"\mathbf{\gamma_0}"
        gamma_1 = r"\mathbf{\gamma_1}"
        gamma_2 = r"\mathbf{\gamma_2}"
        gamma_3 = r"\mathbf{\gamma_3}"
        
        gamma_beta_up = r"\mathbf{\gamma^\beta}"
        gamma_alpha_up = r"\mathbf{\gamma^\alpha}"
        
        gamma_2_up = r"\mathbf{\gamma^2}"
        gamma_0_up = r"\mathbf{\gamma^0}"
        
        
        delta_alpha_beta = r"\delta_{\alpha}^{\beta}"
        
        # color_dict = {
        #     gamma_alpha: RED,
        #     gamma_beta: BLUE,
        #     }
        
        
        # * Title
        title = Title(
            "Spacetime Geometric Algebra",
            stroke_color=BLUE,
            include_underline=True,
            match_underline_width_to_text=True,
            underline_style=dict(stroke_width=3, stroke_color=WHITE),
        ).to_corner(UL).set_color(BLUE)
        
        
        self.play(Write(title))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Metric signature
        metric_signature = Tex(
            metric, space, lbracket, 
            plus, comma, 
            space, minus, comma,
            space, minus, comma,
            space, minus, rbracket).to_edge(UP).shift(DOWN*1.25)
        
        self.play(Write(metric_signature))
        self.wait(PAUSE_WAIT_TIME)
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
        ).move_to(metric_signature.get_center() + DOWN*1 + RIGHT*0.5)
        
        self.play(Write(basis_set))
        self.wait(PAUSE_WAIT_TIME)
        
        # * Orthogonality: gamma_alpha gamma_beta = - gamma_beta gamma_alpha
        orthogonality = Tex(
            gamma_alpha, gamma_beta, 
            space, equal, space,
            minus, space,
            gamma_beta, gamma_alpha
        ).move_to(basis_set.get_center() + DOWN*1)
        

        # * Inner Product:
        inner_product = Tex(
            gamma_alpha, gamma_alpha, space, equal, space,
            gamma_alpha + space + dot + space + gamma_alpha, 
            space, equal, space, metric_same_index,
            isolate=[gamma_alpha + space + dot + space + gamma_alpha, metric_same_index],
        ).move_to(orthogonality.get_center() + DOWN*1)
        
        inner_text = Tex(
            r"\text{Inner Product:}"
        ).next_to(inner_product, LEFT).shift(LEFT*0.5)
        
        orth_text = Tex(
            r"\text{Orthogonality:}"
        ).move_to(inner_text.get_center() + UP*1)
        #.next_to(orthogonality, LEFT).shift(LEFT*0.5)

        self.play(Write(orthogonality))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(orth_text))
        self.wait(NOMINAL_WAIT_TIME)
        
        self.play(Write(inner_product))
        self.wait(NOMINAL_WAIT_TIME)
        self.play(Write(inner_text))
        self.wait(NOMINAL_WAIT_TIME)
        self.wait(NOMINAL_WAIT_TIME)

        # * Inner product example, use gamma_2
        inner_product_example = Tex(
            gamma_2 + space + dot + space + gamma_2, 
            space, equal, space, metric_22, space,
            equal, space, minus, "1",
            isolate=[gamma_2 + space + dot + space + gamma_2, metric_22, equal, minus],
        ).move_to(inner_product.get_center() + DOWN*1)
        
        self.play(
            TransformMatchingTex(
                inner_product.copy(),
                inner_product_example,
                key_map={
                    gamma_alpha + space + dot + space + gamma_alpha: gamma_2 + space + dot + space + gamma_2,
                    metric_same_index: metric_22,
                    equal: equal,
                    dot: dot,
                    gamma_alpha: "1"
                },
                run_time=2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        self.wait(NOMINAL_WAIT_TIME)
        # * Make space for duality, move everything to the left
        self.play(
            orthogonality.animate.shift(LEFT*1),
            inner_product.animate.shift(LEFT*1),
            inner_product_example.animate.shift(LEFT*1),
            orth_text.animate.shift(LEFT*1),
            inner_text.animate.shift(LEFT*1),
            basis_set.animate.shift(LEFT*1),
            metric_signature.animate.shift(LEFT*1),
        )
        line_separator = Line(
            ORIGIN + DOWN*2,
            ORIGIN + UP*2,
            color=WHITE,
        ).shift(RIGHT*2.5)
        
        self.play(
            ShowCreation(line_separator),
            run_time=1,
        )
        
        # * Remind the audience of the duality relation
        duality = Tex(
            gamma_alpha, space, dot, space, gamma_beta_up,
            space, equal, space, delta_alpha_beta,
            ).to_edge(RIGHT).shift(UP + LEFT*0.5).set_color(BLUE_B)
        
        duality_text = Tex(
            r"\text{Duality relation:}"
        ).set_color(BLUE_B)
        duality_text.next_to(duality, UP).shift(UP*0.25)
        
        
        box_duality = Polygon(
            duality.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            duality.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            duality.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            duality.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

            color=WHITE, fill_color=BLUE_A, fill_opacity=0.1
        ).set_color(BLUE_B)
        
        
        self.play(FadeIn(duality))
        self.play(Write(duality_text),
                  ShowCreation(box_duality))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Apply the duality relation to gamma_2
        duality_example = Tex(
            gamma_2, space, dot, space, gamma_2_up,
            space, equal, space, "1",
            ).move_to(duality.get_center() + DOWN*1.25)
        
        self.play(
            TransformMatchingTex(
                duality.copy(),
                duality_example,
                key_map={
                    gamma_alpha: gamma_2,
                    gamma_beta_up: gamma_2_up,
                    delta_alpha_beta: "1",
                    equal: equal,
                    dot: dot,
                },
                run_time=2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * FlashAround the duality example and the inner product example
        self.play(
            FlashAround(duality_example, buff=0.2),
            FlashAround(inner_product_example, buff=0.25),
            run_time=4,
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Transform the duality example according to the inner product
        
        
        duality_example_wrong = Tex(
            gamma_2, space, dot, space, gamma_2,
            space, equal, space, "1",
            ).move_to(duality_example.get_center() + DOWN*1.25)
        duality_example_wrong[3:5].set_color(RED)
        
        self.play(
            TransformMatchingTex(
                duality_example.copy(),
                duality_example_wrong,
                key_map={
                    gamma_2: gamma_2,
                    gamma_2_up: gamma_2,
                    "1": "1",
                    equal: equal,
                    dot: dot,
                },
                run_time=2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        # * Draw a cross aroung the wrong equation
        cross = Cross(duality_example_wrong, color=RED).set_opacity(0.75)
        self.play(ShowCreation(cross))
        self.wait(NOMINAL_WAIT_TIME)
        
        # * We would need to pick up a minus sign, so final formula is
        duality_final_formula = Tex(
            gamma_2, space, equal, space, minus, space, gamma_2_up,
            ).move_to(duality_example_wrong.get_center() + DOWN*1.25)
        
        duality_final_formula.set_color(BLUE_B)
        
        box_duality_final = Polygon(
            duality_final_formula.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            duality_final_formula.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            duality_final_formula.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            duality_final_formula.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

            color=WHITE, fill_color=BLUE_A, fill_opacity=0.1
        ).set_color(BLUE_B)
        self.play(
            Write(duality_final_formula),
            ShowCreation(box_duality_final),
            run_time=2,
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # * Clean up some space:
        # * 1. remove the basis set
        # * 2. Move orthogonality and inner product closer to the signature
        self.play(
            FadeOut(basis_set),
            
            orthogonality.animate.shift(UP*1),
            inner_product.animate.shift(UP*1),
            inner_product_example.animate.shift(UP*1),
            orth_text.animate.shift(UP*1),
            inner_text.animate.shift(UP*1),
        )
        
        
        # * Use gamma_0 as another example of the dot product
        inner_product_example_gamma_0 = Tex(
            gamma_0 + space + dot + space + gamma_0, 
            space, equal, space, metric_00, space,
            equal, space, "1",
            isolate=[gamma_0 + space + dot + space + gamma_0, metric_00],
        ).move_to(inner_product_example.get_center() + DOWN*1)
        
        self.play(
            TransformMatchingTex(
                inner_product_example.copy(),
                inner_product_example_gamma_0,
                key_map={
                    gamma_2 + space + dot + space + gamma_2: gamma_0 + space + dot + space + gamma_0,
                    metric_22: metric_00,
                    equal: equal,
                    dot: dot,
                    "1": "1",
                },
                run_time=2,
            )
        )
        self.wait(NOMINAL_WAIT_TIME)
        
        # * Clean up:
        # * 1. Remove orthogonality and inner product
        # * 2. move the examples up
        # * 3. Move the gamma_2 duality to the left
        self.play(
            FadeOut(orthogonality),
            FadeOut(inner_product),
            FadeOut(orth_text),
            FadeOut(inner_text),
            
            FadeOut(duality_example),
            FadeOut(duality_example_wrong),
            FadeOut(cross),
            
            inner_product_example.animate.shift(UP*1.75).to_edge(LEFT),
            inner_product_example_gamma_0.animate.shift(UP*1).to_edge(LEFT),
            
            duality_final_formula.animate.shift(UP*3.5 + LEFT*5),
            box_duality_final.animate.shift(UP*3.5 + LEFT*5),
            run_time=3
        )
        
        # * Show the duality relation for the gamma_0
        duality_example_gamma_0 = Tex(
            gamma_0, space, equal, space, gamma_0_up,
            ).move_to(duality_final_formula.get_center() + DOWN*1.75)
        duality_example_gamma_0.set_color(BLUE_B)
        
        box_duality_example_gamma_0 = Polygon(
            duality_example_gamma_0.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            duality_example_gamma_0.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            duality_example_gamma_0.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            duality_example_gamma_0.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

            color=WHITE, fill_color=BLUE_A, fill_opacity=0.1
        ).set_color(BLUE_B)
        
        self.play(
            TransformMatchingTex(
                duality_final_formula.copy(),
                duality_example_gamma_0,
                key_map={
                    gamma_2: gamma_0,
                    gamma_2_up: gamma_0_up,
                    equal: equal,
                },
                run_time=2,
            ),
        )
        self.play(
            ShowCreation(box_duality_example_gamma_0),
            run_time=2,
        )
        self.wait(PAUSE_WAIT_TIME)
        
        
        # * Finally, generalize the duality relation using the metric tensor
        lower_to_upper = Tex(
            gamma_alpha, space, equal, space,
            gamma_beta_up, space, metric)
        
        upper_to_lower = Tex(
            gamma_alpha_up, space, equal, space,
            gamma_beta, space, metric_raised)
        
        lower_to_upper.move_to(inner_product_example_gamma_0.get_center() + DOWN*1.75)
        upper_to_lower.move_to(lower_to_upper.get_center() + RIGHT*5)
        
        box_upper_to_lower = Polygon(
            upper_to_lower.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            upper_to_lower.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            upper_to_lower.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            upper_to_lower.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

            color=WHITE, fill_color=GREY, fill_opacity=0.1
        )
        
        box_lower_to_upper = Polygon(
            lower_to_upper.get_corner(UL) + 2.5*np.array([-0.1, 0.1, 0]),
            lower_to_upper.get_corner(UR) + 2.5*np.array([0.1, 0.1, 0]),
            lower_to_upper.get_corner(DR) + 2.5*np.array([0.1, -0.1, 0]),
            lower_to_upper.get_corner(DL) + 2.5*np.array([-0.1, -0.1, 0]),

            color=WHITE, fill_color=GREY, fill_opacity=0.1
        )
        
        self.play(
            Write(lower_to_upper),
            Write(upper_to_lower),
            run_time=2,
        )
        self.play(
            ShowCreation(box_lower_to_upper),
            ShowCreation(box_upper_to_lower),
            run_time=2,
        )
        self.wait(PAUSE_WAIT_TIME)
        
        # * Fade to black
        self.play(
            FadeOut(upper_to_lower),
            FadeOut(lower_to_upper),
            FadeOut(box_upper_to_lower),
            FadeOut(box_lower_to_upper),
            
            FadeOut(duality_example_gamma_0),
            FadeOut(box_duality_example_gamma_0),
            FadeOut(duality_final_formula),
            FadeOut(box_duality_final),
            
            FadeOut(line_separator),
            FadeOut(duality),
            FadeOut(box_duality),
            FadeOut(duality_text),
            
            FadeOut(inner_product_example),
            FadeOut(inner_product_example_gamma_0),
            
            FadeOut(metric_signature),
            FadeOut(title),
            
            run_time=2,
        )
            
        