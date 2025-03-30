from manim import *
from reactive_manim import *
import manimforge as mf
mf.setup()



class OpeningQuote(Scene):
    def construct(self):
        
        ragged2e_template = TexTemplate()
        ragged2e_template.add_to_preamble(r"\usepackage{ragged2e}")
        words = Tex(r"``Mathematics is taken for granted in the physics curriculum—a body of \\ \
                        immutable truths to be assimilated and applied. The profound influence \\ \
                        of mathematics on our conceptions of the physical world is never analyzed. \\ \
                        The possibility that mathematical tools used today were invented to solve \\ \
                        problems in the past and might not be well suited for current problems \\ \
                        is never considered.''", 
                   tex_template=ragged2e_template, tex_environment="justify",
                   font_size = 40,
                   )
        
        words.to_edge(UP)
        author = Tex("-David Hestenes")
        author.set_color(BLUE_B)
        author.next_to(words, DOWN, buff = 0.5).to_edge(RIGHT)

        self.play(FadeIn(words))
        self.wait(1)
        self.play(Write(author, run_time = 3))
        self.wait()