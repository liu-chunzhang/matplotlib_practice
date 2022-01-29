# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

fig, ax1 = plt.subplots()
t = np.arange(0.05, 10.0, 0.01)
s1 = np.exp(t)
ax1.plot(t, s1, c="b", ls="-")

# set x-axis label
ax1.set_xlim(0.0, 10.0)
ax1.locator_params(axis='x', nbins=6)
ax1.set_xlabel("x坐标轴")

# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylim(0.0, 2.5e4)
ax1.locator_params(axis='y', nbins=6)
ax1.set_ylabel("以e为底的指数函数", color="b")
ax1.tick_params("y", colors="b")

# ax1 shares x-axis with ax2.
ax2 = ax1.twinx()				# 共享单一绘图区域的坐标轴

s2 = np.cos(t**2)
ax2.plot(t, s2, c="r", ls=":")

# Make the y-axis label, ticks and tick labels match the line color.
ax2.set_ylim(-1.0, 1.0)
ax2.locator_params(axis='y', nbins=5)
ax2.set_ylabel("余弦函数", color="r")
ax2.tick_params("y", colors="r")

plt.savefig("13.2.2.png")