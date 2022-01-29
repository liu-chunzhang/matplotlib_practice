# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

mpl.rcParams["font.sans-serif"] = ["FangSong"]
mpl.rcParams["axes.unicode_minus"] = False
font_style = dict(fontsize=15, weight="black")

# First create sample data:
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)*np.cos(x)

# Create just a figure and only one subplot
fig, ax = plt.subplots(1, 1, subplot_kw=dict(facecolor="cornflowerblue"))	# 对全部子图生效！

ax.plot(x, y, "k--", lw=2)
ax.set_xlabel("时间（秒）", **font_style)		# 这里和教材效果图不一致！
ax.set_ylabel("振幅", **font_style)
ax.set_title("简单折线图", **font_style)

ax.set_xlim(0, 2*np.pi)
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.set_ylim(-0.65, 0.65)
ax.yaxis.set_major_locator(MultipleLocator(0.2))

ax.grid(ls=":", lw=1, color="gray", alpha=0.8)

# Show figure and subplot(s)
plt.show()