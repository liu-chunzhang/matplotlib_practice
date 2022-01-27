import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', dashes=[2, 1, 1, 1], lw=2, c='c', label='plot figure')	# dashes控制显示间距：dashes=[2, 1, 1, 1]为折线组成单元为由2个数据点的线段，
																				# 1个数据点的间隔，1个数据点的线段和1个数据点的间隔组成的结构单元。可见9.4.1节

plt.legend(loc="lower right")

plt.xlabel("x-axis")	# 设置x轴的标签文本
plt.ylabel("y-axis")	# 设置y轴的标签文本

plt.xlim(0, 10)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1, 1)
plt.locator_params(axis='y', nbins=5)

plt.show()