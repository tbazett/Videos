from manim import Scene, Circle

class Arrowsuck(Scene):
    def construct(self):
        circle1=Circle(radius=1, fill_opacity =1, fill_color=RED)
        circle2=Circle(radius=1, fill_opacity =1, fill_color=RED)
        circle1.shift(2*LEFT)
        circle2.shift(2*RIGHT)
        arrow=Arrow(2*LEFT, 2*RIGHT)
        arrow.z_index=-1
        arrow.submobjects[-1].z_index = -1
        self.add(circle1, circle2)
        self.add(arrow)