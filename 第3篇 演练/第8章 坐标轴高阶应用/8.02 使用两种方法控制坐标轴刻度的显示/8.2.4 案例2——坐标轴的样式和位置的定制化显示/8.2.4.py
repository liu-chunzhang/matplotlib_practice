import matplotlib.pyplot as plt
import numpy as np

from calendar import day_name
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["xtick.color"] = "blue"
plt.rcParams["ytick.color"] = "lightgreen"

fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

ax.spines["bottom"].set_position(("outward", 10))
ax.spines["left"].set_position(("outward", 10))
ax.spines["top"].set_color("none")
ax.spines["right"].set_color("none")

x = np.arange(1, 8, 1)
y = 2*x + 1

ax.scatter(x, y, c="orange", s=30, edgecolors="orange")

for tickline in ax.xaxis.get_ticklines():				# 同前，tickline.set_color("blue")没有实际用处，故删去
	tickline.set_markersize(6)
	tickline.set_markeredgewidth(5)

for ticklabel in ax.get_xmajorticklabels():
	ticklabel.set_color("slateblue")
	ticklabel.set_fontsize(15)
	ticklabel.set_rotation(20)

ax.xaxis.set_ticks_position("bottom")
plt.xticks(x, day_name[0:7], rotation=20)
ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%1.1f$"))
ax.yaxis.set_ticks_position("left")

for tickline in ax.yaxis.get_ticklines():				# 同前，tickline.set_color("lightgreen")没有实际用处，故删去
	tickline.set_markersize(6)
	tickline.set_markeredgewidth(5)

for ticklabel in ax.get_ymajorticklabels():
	ticklabel.set_color("green")
	ticklabel.set_fontsize(15)
	ticklabel.set_math_fontfamily("cm")

ax.set_ylim(2.0, 16.0)

ax.grid(ls=":", lw=1, color="gray", alpha=0.5)

plt.show()