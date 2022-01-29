import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c='c', label="plot figure", dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")

plt.axhline(y=0.0, c="b", ls="--", lw=2)	# 绘制平行于x轴的水平参考线
plt.axvline(x=4.0, c='r', ls="--", lw=2)	# 绘制垂直于x轴的水平参考线

plt.xlim(0.0, 10.0)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.show()