import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

# normal plot
ax = plt.axes([0.1, 0.7, 0.3, 0.3], frameon=True, facecolor='y', aspect="equal")	
ax.xaxis.set_major_locator(MultipleLocator(0.5))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
plt.plot(np.arange(3), [0, 1, 0], dashes=[1, 1])

# no-plot
ax2 = plt.axes([0.35, 0.4, 0.3, 0.3], frameon=True, facecolor='y', aspect="equal")
plt.plot(2.0+np.arange(3), [0, 1, 0], dashes=[1, 1])
ax2.xaxis.set_major_locator(MultipleLocator(0.5))
ax2.yaxis.set_major_locator(MultipleLocator(0.2))

# no-axes
ax3 = plt.axes([0.6, 0.1, 0.3, 0.3], frameon=True, facecolor='y', aspect="equal")
plt.plot(4+np.arange(3), [0, 1, 0], dashes=[1, 1])
ax3.xaxis.set_major_locator(MultipleLocator(0.5))
ax3.yaxis.set_major_locator(MultipleLocator(0.2))
plt.axis("off")

plt.show()