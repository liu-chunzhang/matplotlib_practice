import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

a = np.random.randn(100)
b = np.random.randn(100)

exponent = 2

plt.subplot(131)
# colormap:jet
plt.scatter(a, b, np.sqrt(np.power(a, exponent) + np.power(b, exponent)) * 100, c=np.random.rand(100), cmap=mpl.cm.jet, marker="o", zorder=1)
plt.xlim(-2, 3)
plt.xticks(range(-2, 4, 1))
plt.ylim(-3, 4)
plt.yticks(range(-3, 5, 1))

plt.subplot(132)
plt.scatter(a, b, 50, marker="o", zorder=10)
plt.xlim(-2, 3)
plt.xticks(range(-2, 4, 1))
plt.ylim(-3, 4)
plt.yticks(range(-3, 5, 1))

plt.subplot(133)
# colormap:BuPu
plt.scatter(a, b, 50, c=np.random.rand(100), cmap=mpl.cm.BuPu, marker="+", zorder=100)
plt.xlim(-2, 3)
plt.xticks(range(-2, 4, 1))
plt.ylim(-3, 4)
plt.yticks(range(-3, 5, 1))

plt.show()