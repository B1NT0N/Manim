from manim import *

class Squid(Scene):
    def construct(self):
        big_square = Square(side_length=1000).set_fill(WHITE, opacity=1.0)
    
        triangle = Triangle().scale(1.3)
        circle = Circle(radius = 1).next_to(triangle, LEFT+0.5*LEFT)
        square = Square(side_length=2).next_to(triangle, RIGHT+1.5*RIGHT)

        circle.set_stroke(color=WHITE, width=20)
        square.set_stroke(color=WHITE, width=20)
        triangle.set_stroke(color=WHITE, width=20)
        
        self.play(Create(triangle), Create(square), Create(circle))
        self.wait(0.2)
        
        self.play(FadeToColor(square, color="#e21c80"), FadeToColor(circle, color="#e21c80"), FadeToColor(triangle, color="#e21c80"))
        
        self.wait(1)
        
        
        