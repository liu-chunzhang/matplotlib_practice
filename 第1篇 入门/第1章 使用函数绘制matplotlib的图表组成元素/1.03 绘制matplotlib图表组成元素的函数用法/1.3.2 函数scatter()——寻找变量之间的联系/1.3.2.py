import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)

plt.scatter(x, y, c='b', label="scatter figure")	# 寻找变量之间的关系

plt.legend(loc="upper right")

plt.xlim(-2.0, 12.0)
plt.locator_params(axis='x', nbins=7)
plt.ylim(-0.2, 1.2)
plt.locator_params(axis='y', nbins=8)

plt.show()
