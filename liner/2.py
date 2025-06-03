from matplotlib import pyplot as plt
import numpy as np

# 随机出现一些点
# 设置全局字体为支持中文的字体（如SimHei、Microsoft YaHei等）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 黑体
plt.rcParams['axes.unicode_minus'] = False    # 解决负号显示问题

points = np.random.rand(10,2)
x = points[:,0]
y = points[:,1]
plt.title("随机出现的10个二维点")
plt.plot(x,y,".")
plt.show()