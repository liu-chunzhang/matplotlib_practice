import matplotlib.pyplot as plt
import numpy as np

from calendar import day_name
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["ytick.color"] = "lightgreen"
plt.rcParams["xtick.color"] = "red"

fig = plt.figure()

ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

ax.spines["bottom"].set_position(("outward", 10))
ax.spines["left"].set_position(("outward", 10))
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

x = np.arange(1, 8, 1)
y = 2*x + 1

ax.scatter(x, y, c="orange", s=50, edgecolors="orange")

for tickline in ax.xaxis.get_ticklines():
	tickline.set_color("red")							# 同前，这句话没有实际用处。
	tickline.set_markersize(8)
	tickline.set_markeredgewidth(5)

for ticklabel in ax.get_xmajorticklabels():
	ticklabel.set_color("blue")
	ticklabel.set_fontsize(15)
	ticklabel.set_rotation(20)

ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))
plt.xticks(x, day_name[0:7], rotation=20)
ax.yaxis.set_ticks_position("left")
ax.xaxis.set_ticks_position("bottom")

for tickline in ax.yaxis.get_ticklines():
	tickline.set_color("lightgreen")					# 同前，这句话没有实际用处。
	tickline.set_markersize(20)
	tickline.set_markeredgewidth(5)

for ticklabel in ax.get_ymajorticklabels():
	ticklabel.set_color("green")
	ticklabel.set_fontsize(18)

ax.grid(ls=":", lw=1, color="gray", alpha=0.5)

plt.show()