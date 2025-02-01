from manim import *

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        # text=MathTex(r"&Let\ A \subset\mathbb{Z}^2\\&hA=\{a_1+\cdots+a_h\ |\ a_1,\cdots a_h\in A\}")   
        # self.add(index_labels(text[0]))
        # text[0][3:4].set_color(GREEN)
        # text[0][8:9].set_color(GREEN)
        # text[0][30:31].set_color(GREEN)
        # text[0][7:8].set_color(YELLOW)
        # text[0][19:20].set_color(YELLOW)
        # text[0][28:29].set_color(YELLOW)
        # self.add(text)
        
        text_size=36

        A=MathTex("A=\{ {{(2,1)}}, {{(-1,1)}}\}")
        A.shift(UP)
        tex1=MathTex("(2,1)")
        tex2=MathTex("(-1,1)")
        tex2.shift(2*RIGHT)
        texgroup=VGroup(tex1,tex2)
        # target_coord1 = A[0][3:8]  # Matches the "(2,1)" in A
        # target_coord2 = A[0][9:15]  # Matches the "(-1,1)" in A
        self.add(texgroup)
        self.wait()
        self.play(TransformMatchingTex(texgroup,A))

  
        self.wait()

   


