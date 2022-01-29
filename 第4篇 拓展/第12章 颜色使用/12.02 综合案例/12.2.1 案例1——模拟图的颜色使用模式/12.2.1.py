import matplotlib.pyplot as plt
import numpy as np

rd = np.random.rand(10, 10)
plt.pcolor(rd, cmap="BuPu")						# 生成2维的模拟颜色图
plt.colorbar(ticks=np.arange(0, 1.0, 0.1))		# 添加颜色标尺并设置刻度标签

plt.show()