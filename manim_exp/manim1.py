from manim import *

class Test(Scene):
    def construct(self):
        
        a = Axes(x_range=[-1,10],y_range=[-1,10])
        graph = a.plot(lambda n : n*n)
        g = a.plot(lambda x: 2*x)
        self.add(graph,a,g)
