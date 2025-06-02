import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']  # 或者 'Microsoft YaHei', 'KaiTi', 'FangSong'
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

# 创建图形和坐标轴
fig, ax = plt.subplots(figsize=(8, 8))

# 设置坐标轴范围
ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

# 设置 X 和 Y 轴的标签（只显示 "First Roll" 和 "Second Roll"）
ax.set_xticks([0.5, 1.5, 2.5, 3.5])  # 网格中心位置
ax.set_xticklabels(["1", "2", "3", "4"])  # 骰子点数
ax.set_yticks([0.5, 1.5, 2.5, 3.5])  # 网格中心位置
ax.set_yticklabels(["1", "2", "3", "4"])  # 骰子点数

# 添加 X 和 Y 轴的说明
ax.set_xlabel("X = First Roll", fontsize=12, labelpad=10)
ax.set_ylabel("Y = Second Roll", fontsize=12, labelpad=10)

# 绘制网格线
for x in range(5):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=2)
for y in range(5):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=2)

# # 添加网格标签
# for i in range(4):
#     for j in range(4):
#         ax.text(i + 0.5, j + 0.5, f'({i+1},{j+1})', 
#                 ha='center', va='center', fontsize=12)

# 添加标题
plt.title('SAMPLE SPACE', fontsize=16, pad=20)

# 示例：标记一个随机事件（例如选中(2,3)格子）
selected_cell = (1, 2)  # 注意Python是0-based索引
ax.add_patch(plt.Rectangle(selected_cell, 1, 1, color='red', alpha=0.3))

selected_cell = (2, 1)  # 注意Python是0-based索引
ax.add_patch(plt.Rectangle(selected_cell, 1, 1, color='red', alpha=0.3))

selected_cell = (0, 0)  # 注意Python是0-based索引
ax.add_patch(plt.Rectangle(selected_cell, 1, 1, color='red', alpha=0.3))


# 计算并显示概率
total_cells = 16
probability = 1 / total_cells
# plt.figtext(0.5, 0.05, 
#             f'古典概型概率计算: 每个格子被选中的概率 = 1/{total_cells} = {probability:.3f}',
#             ha='center', fontsize=12)

plt.tight_layout()
plt.show()