import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', lw=2, c="c", label="plot figure", dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")			# 由于教材中的结果图遮挡了一部分曲线，所以选择放在左下方，下同

plt.xlim(0.0, 10)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.grid(linestyle=":", color="r")		# 绘制刻度线的网格线

plt.show()