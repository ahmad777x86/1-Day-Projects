from manim import *

class Test(Scene):
    def construct(self):
        
        circle = Circle(color=RED, radius=2)
        square = Square(color=BLUE, side_length=4)
        text = Text("Hello World")

        self.play(Write(text))
        self.play(Create(circle))

        self.wait(1)

        self.play(Create(square))