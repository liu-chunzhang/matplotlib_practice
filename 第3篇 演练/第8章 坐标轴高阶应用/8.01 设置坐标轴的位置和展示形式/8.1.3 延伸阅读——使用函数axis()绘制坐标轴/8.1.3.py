import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["axes.xmargin"] = 0.0
plt.rcParams["axes.ymargin"] = 0.0

plt.axis([3, 7, -0.5, 3])
plt.plot(4+np.arange(3), [0, 1, 0], color="blue", linewidth=4, linestyle="-")

plt.show()