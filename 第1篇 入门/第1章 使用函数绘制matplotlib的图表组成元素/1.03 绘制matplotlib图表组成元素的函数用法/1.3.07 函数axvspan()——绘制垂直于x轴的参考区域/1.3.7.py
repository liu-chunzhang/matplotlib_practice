import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c="c", label='plot figure', dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")

plt.axvspan(xmin=4.0, xmax=6.0, facecolor="y", alpha=0.3)	# 绘制垂直于x轴的参考区域
plt.axhspan(ymin=0.0, ymax=0.5, facecolor="y", alpha=0.3)	# 绘制垂直于y轴的参考区域

plt.xlim(0.0, 10)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.show()