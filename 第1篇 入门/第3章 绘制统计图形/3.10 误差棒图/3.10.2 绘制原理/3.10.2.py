import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 0.6, 10)
y = np.exp(x)

error = 0.05 + 0.15*x

lower_error = error
upper_error = 0.3*error
error_limit = [lower_error, upper_error]

plt.errorbar(x, y, yerr=error_limit, fmt=":o", ecolor="y", elinewidth=4, ms=5, mfc="c", mec='r', capthick=1, capsize=2)

plt.xlim(0, 0.7)
plt.xticks(np.arange(0.0, 0.7, 0.1))

plt.show()