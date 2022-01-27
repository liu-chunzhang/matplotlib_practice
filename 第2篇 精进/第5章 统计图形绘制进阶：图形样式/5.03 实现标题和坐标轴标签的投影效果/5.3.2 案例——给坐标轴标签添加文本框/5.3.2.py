import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig = plt.figure(figsize=(8, 8))
ax =fig.add_subplot(111)

box = dict(facecolor="#6959CD", pad=2, alpha=0.4)
ax.plot(x, y, c="b", ls="--", lw=2)

# set text contents
title = "$y=\sin({x})$"
xaxis_label = "$x\_axis$"
yaxis_label = "$y\_axis$"

ax.set_xlabel(xaxis_label, fontsize=18, bbox=box)
ax.set_ylabel(yaxis_label, fontsize=18, bbox=box)
ax.set_title(title, fontsize=23, va="bottom")

ax.yaxis.set_label_coords(-0.08, 0.5)	# axes coords
ax.xaxis.set_label_coords(1.0, -0.05)	# axes coords

ax.grid(ls="-.", lw=1, color="gray", alpha=0.3)

plt.xlim(0.5, 3.5)
plt.ylim(-1.0, 1.0)

plt.show()