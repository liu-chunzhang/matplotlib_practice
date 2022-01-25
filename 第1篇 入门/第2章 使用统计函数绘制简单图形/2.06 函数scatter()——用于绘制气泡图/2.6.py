import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

a = np.random.randn(100)
b = np.random.randn(100)

# colormap:RdYlBu
plt.scatter(a, b, s=np.power(10*a+20*b, 2), c=np.random.rand(100), cmap=mpl.cm.RdYlBu, marker="o", linewidth=1, edgecolor='k')
				# 用于绘制气泡图，借助于二维数据展示三维数据。cmap为选择的颜色映射表

plt.show()