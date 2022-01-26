import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 0.6, 10)
y = np.exp(x)

error = 0.05 + 0.15*x

lower_error = error
upper_error = 0.3*error
error_limit = [lower_error, upper_error]

plt.errorbar(x, y, yerr=error_limit, fmt=":o", ecolor="y", elinewidth=4, ms=5, mfc="c", mec='r')			# 带e的为误差棒参数，m的为标记参数

plt.xlim(0, 0.7)
plt.locator_params(axis='x', nbins=8)
plt.ylim(1.0, 1.9)
plt.locator_params(axis='y', nbins=5)

plt.show()