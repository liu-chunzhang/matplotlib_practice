import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

a, b = np.random.randn(100), np.random.randn(100)
s = np.sqrt(np.power(a, 2) + np.power(b, 2)) * 100

plt.subplot(131)
# colormap:jet
plt.scatter(a, b, s, c=np.random.rand(100), cmap=mpl.cm.jet, marker="o", edgecolor='k', zorder=1)
plt.xlim(-2, 3)
plt.xticks(np.arange(-2.0, 3.1))
plt.ylim(-3, 4)
plt.yticks(np.arange(-3.0, 4.1))

plt.subplot(132)
plt.scatter(a, b, 50, marker="o", zorder=10)
plt.xlim(-2, 3)
plt.xticks(np.arange(-2.0, 3.1, 1))
plt.ylim(-3, 4)
plt.yticks(np.arange(-3.0, 4.1, 1))

plt.subplot(133)
# colormap:BuPu
plt.scatter(a, b, 50, c=np.random.rand(100), cmap=mpl.cm.BuPu, marker="+", zorder=100)
plt.xlim(-2, 3)
plt.xticks(np.arange(-2.0, 3.1, 1))
plt.ylim(-3, 4)
plt.yticks(np.arange(-3.0, 4.1, 1))

plt.show()