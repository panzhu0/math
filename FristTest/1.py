from manim import *


# HelloWorld 继承 Scene 对象
class HelloWorld(Scene):
    def construct(self):
        # 创建Mobject
        text = Text('hello world')
        # 创建动画
        anim = Write(text)
        # 播放动画
        self.play(anim)
        self.wait(2)

# 运行:
































