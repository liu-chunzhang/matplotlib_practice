import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = [0, 4, 3, 5, 6]
y1 = [1, 3, 4, 2, 7]
y2 = [3, 4, 1, 6, 5]

labels = ["BluePlanet", "BrownPlanet", "GreenPlanet"]
colors = ["#8da0cb", "#fc8d62", "#66c2a5"]

plt.stackplot(x, y, y1, y2, labels=labels, colors=colors, edgecolor='k')	# 绘制堆积折线图

plt.xlim(1.0, 5.0)
plt.locator_params(axis='x', nbins=9)
plt.ylim(0.0, 18.0)
plt.locator_params(axis='y', nbins=10)

plt.legend(loc="upper left")

plt.show()