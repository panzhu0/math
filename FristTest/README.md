### 安装
pip install manim

### 编码
```python
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
```

### 使用
```bash
manim -p 1.py HelloWorld
```

### Scene
四个常用方法:  add remove play  wait

### Animation
作用于Moject类上,
FadeIn FadeOout ReplacementTransform

### Moject

### 命令
manim xxx.py TRY -p
-p 预览
TRY 指定Scene
