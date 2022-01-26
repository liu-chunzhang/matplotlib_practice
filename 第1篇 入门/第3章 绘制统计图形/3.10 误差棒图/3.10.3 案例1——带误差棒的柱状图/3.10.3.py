# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = np.arange(5)
y = [100, 68, 79, 91, 82]
std_err = [7, 2, 6, 10, 5]

error_attri = dict(elinewidth=2, ecolor="black", capsize=3)

# create bar with errorbar
plt.bar(x, y, color="c", width=0.6, align="center", edgecolor='k', yerr=std_err, error_kw=error_attri, 
			tick_label=["园区1", "园区2", "园区3", "园区4", "园区5"])

# set x,y_axis label
plt.xlabel("芒果种植区")
plt.locator_params(axis='y', nbins=7)
plt.ylabel("收割量")

# set title of axes
plt.title("不同芒果种植区的单次收割量")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="gray", alpha=0.2)

plt.show()