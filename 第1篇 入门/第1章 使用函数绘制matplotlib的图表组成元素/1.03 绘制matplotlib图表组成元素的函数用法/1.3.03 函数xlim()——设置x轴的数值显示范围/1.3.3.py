import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)

plt.scatter(x, y, label="scatter figure")

plt.legend(loc="upper right")

plt.xlim(0.05, 10)						# 控制x轴的数值显示范围
plt.locator_params(axis='x', nbins=6)
plt.ylim(0, 1)							# 控制y轴的数值显示范围
plt.locator_params(axis='y', nbins=6)

plt.show()