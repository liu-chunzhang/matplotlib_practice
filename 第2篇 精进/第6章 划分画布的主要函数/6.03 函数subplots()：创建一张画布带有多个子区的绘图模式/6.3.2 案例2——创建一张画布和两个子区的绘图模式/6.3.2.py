# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

font_style = dict(fontsize=18, weight="black")

# First create sample data
x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)*np.exp(-x)

# Create just a figure and only one subplot
fig, ax = plt.subplots(1, 2, sharey=True)

# subplot(121)
ax1 = ax[0]
ax1.plot(x, y, "k--", lw=2)
ax1.set_title("折线图")
ax1.grid(ls=":", lw=1, color="gray", alpha=0.8)
ax1.set_xlim(0, 7)
ax1.set_ylim(-0.05, 0.35)

# subplot(122)
ax2 = ax[1]
ax2.scatter(x, y, s=10, c="skyblue", marker="o")
ax2.set_title("散点图")

# Create a figure title
plt.suptitle("创建一张画布和两个子区的绘图模式", **font_style)

# Show figure and subplot(s)
plt.show()