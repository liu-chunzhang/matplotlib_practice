import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["axes.xmargin"] = 0.0
plt.rcParams["axes.ymargin"] = 0.0

yticks = np.arange(0.0, 1.1, 0.2)

# set #1 plot
xticks1 = np.arange(0.0, 2.1, 0.5)

plt.axes([0.05, 0.7, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal", xticks=xticks1, yticks=yticks)		# 可以在这里设置xticks和yticks
plt.plot([0, 1, 2], [0, 1, 0], color="blue", linewidth=2, linestyle="--")

# set #2 plot
xticks2 = np.arange(2.0, 4.1, 0.5)

plt.axes([0.3, 0.4, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal", xticks=xticks2, yticks=yticks)
plt.plot([2, 3, 4], [0, 1, 0], color="blue", linewidth=2, linestyle="--")

# set #2 plot
xticks3 = np.arange(4.0, 6.1, 0.5)

plt.axes([0.55, 0.1, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal", xticks=xticks3, yticks=yticks)
plt.plot([4, 5, 6], [0, 1, 0], color="blue", linewidth=2, linestyle=":")

plt.show()