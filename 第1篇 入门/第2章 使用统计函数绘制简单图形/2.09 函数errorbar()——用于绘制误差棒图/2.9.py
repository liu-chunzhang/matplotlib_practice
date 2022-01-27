import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 0.6, 6)
y = np.exp(x)

plt.errorbar(x, y, fmt="bo:", yerr=0.2, xerr=0.02, capsize=3)	# 用于绘制误差棒图，参数capsize表明棒的外延线的长度

plt.xlim(0, 0.7)
plt.locator_params(axis='x', nbins=8)
plt.ylim(0.8, 2.2)
plt.locator_params(axis='y', nbins=8)

plt.show()