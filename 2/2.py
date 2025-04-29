from manim import *
class A(Scene):
    def construct(self):
        c = Circle(fill_opacity=1)
        s= Square(color=YELLOW,fill_opacity=1)
        self.play(FadeIn(c))
        self.wait()
        self.play(ReplacementTransform(c,s))
        self.wait()
        self.play(FadeOut(s))
        self.wait()

# Scene:场景  

# Mobject:场景中的物体,如圆形、正方形等

# Animation: 作用于Mobject之上,用这些物体制作一些动画





