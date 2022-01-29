import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1, figsize=(8, 8))

box = dict(facecolor="#6959CD", pad=2, alpha=0.4)

ax.plot(x, y, c="b", ls="--", lw=2)

# set text contents
title, xaxis_label, yaxis_label = "$y=\sin({x})$", "$x\_axis$", "$y\_axis$"

ax.set_xlabel(xaxis_label, fontsize=18, bbox=box, fontdict={"math_fontfamily":"cm"})
ax.set_ylabel(yaxis_label, fontsize=18, bbox=box,  fontdict={"math_fontfamily":"cm"})
ax.set_title(title, fontsize=23, va="bottom", fontdict={"math_fontfamily":"cm"})

ax.yaxis.set_label_coords(-0.08, 0.5)	# axes coords
ax.xaxis.set_label_coords(1.0, -0.05)	# axes coords

ax.grid(ls="-.", lw=1, color="gray", alpha=0.3)

plt.xlim(0.5, 3.5)
plt.locator_params(axis='x', nbins=7)
plt.ylim(-0.4, 1.0)
plt.locator_params(axis='y', nbins=8)

plt.show()