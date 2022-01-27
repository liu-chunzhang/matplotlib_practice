import matplotlib.pyplot as plt
import numpy as np

from matplotlib.gridspec import GridSpec

fig = plt.figure()
gs = GridSpec(2, 2)

box = {"facecolor":"lightgreen", "pad":3, "alpha":0.2}

# subplot(2, 2, 1-2)
x1 = np.arange(0, 1e5, 500)
ax1 = fig.add_subplot(gs[0, :], facecolor="yellowgreen")
ax1.plot(x1, "k--", lw=2)
ax1.set_ylabel('YLabel0,0-1', bbox=box)
ax1.set_xlabel('XLabel0,0-1', bbox=box)
ax1.set_xlim(0, 200)
ax1.set_ylim(0, 1e5)
ax1.yaxis.set_label_coords(-0.1, 0.5)

# sunplot(2, 2, 3)
x2 = np.linspace(0, 1000, 10)
y2 = np.arange(1, 11, 1)
ax2 = fig.add_subplot(gs[1, 0], facecolor="cornflowerblue")
ax2.scatter(x2, y2, s=20, c="gray", marker="s", linewidths=2, edgecolor="k")
ax2.set_ylabel("YLabel10", bbox=box)
ax2.set_xlabel("XLabel10", bbox=box)
for ticklabel in ax2.get_xticklabels():
	ticklabel.set_rotation(45)
ax2.yaxis.set_label_coords(-0.15, 0.5)
ax2.xaxis.set_label_coords(0.5, -0.18)

# subplot(2, 2, 4)
x3 = np.linspace(0, 10, 100)
y3 = np.exp(-x3)
ax3 = fig.add_subplot(gs[1, 1])
ax3.errorbar(x3, y3, fmt="b-", yerr=0.6*y3, ecolor="lightsteelblue", elinewidth=2, capsize=0, errorevery=5)
ax3.set_ylabel("YLabel11", bbox=box)
ax3.set_xlabel("XLabel11", bbox=box)
ax3.xaxis.set_label_coords(0.5, -0.18)
ax3.set_ylim(-0.1, 1.1)
ax3.set_yticks(np.arange(0.1, 1, 0.1))

gs.tight_layout(fig)

plt.show()