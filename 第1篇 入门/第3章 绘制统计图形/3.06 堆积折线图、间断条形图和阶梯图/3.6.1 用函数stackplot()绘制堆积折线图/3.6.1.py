import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = [0, 4, 3, 5, 6]
y1 = [1, 3, 4, 2, 7]
y2 = [3, 4, 1, 6, 5]

labels = ["BluePlanet", "BrownPlanet", "GreenPlanet"]
colors = ["#8da0cb", "#fc8d62", "#66c2a5"]

plt.stackplot(x, y, y1, y2, labels=labels, colors=colors, edgecolor='k')

plt.xlim(1.0, 5.0)
plt.ylim(0.0, 18.0)
plt.xticks(np.arange(1.0, 5.1, 0.5))
plt.yticks(np.arange(0.0, 18.1, 2.0))

plt.legend(loc="upper left")

plt.show()