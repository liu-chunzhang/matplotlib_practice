import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', lw=2, c="c", label='plot figure', dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")			# 标示不同图形的文本标签图例

plt.xlim(0.0, 10)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.show()