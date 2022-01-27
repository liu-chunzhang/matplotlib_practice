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

ax1.set_xlim(0, 7)
ax1.locator_params(axis='x', nbins=8)
ax1.set_ylim(-0.05, 0.35)
ax1.locator_params(axis='y', nbins=9)

ax1.set_title("折线图")
ax1.grid(ls=":", lw=1, color="gray", alpha=0.8)

# subplot(122)
ax2 = ax[1]
ax2.scatter(x, y, s=10, marker="o", facecolor='w', edgecolor='skyblue')	# 此处教材错误！因需要空心圆，所以不能用color，而应该分别设置facecolor和edgecolor！

ax2.set_xlim(-1, 7)
ax2.locator_params(axis='x', nbins=9)
ax2.set_title("散点图")

# Create a figure title
plt.suptitle("创建一张画布和两个子区的绘图模式", **font_style)

# Show figure and subplot(s)
plt.show()