import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.cos(x)
plt.plot(x, y, ls='-', lw=2, label='plot figure')	# 展现变量的趋势变化

plt.legend(loc="upper right")

# some extra configure					# 这些语句为保持图片拉伸时刻度的不变性而添加，之后文件同
plt.xlim(0.0, 10.0)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.show()
