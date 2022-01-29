import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 2.1, 0.1)
y = np.power(x, 3)
y1 = np.power(x, 2)
y2 = np.power(x, 1)

plt.plot(x, y, ls="-", lw=2, label=r"$x^{3}$")
plt.plot(x, y1, ls="-", lw=2, label=r"$x^{2}$")
plt.plot(x, y2, ls="-", lw=2, label=r"$x^{1}$")

plt.locator_params(axis='x', nbins=5)
plt.locator_params(axis='y', nbins=9)
plt.margins(x=0, y=0)

plt.legend(loc="upper left", bbox_to_anchor=(0.05, 0.95), ncol=3, title="power function", shadow=True, fancybox=True)	# fancybox是线框圆角处理参数

plt.show()