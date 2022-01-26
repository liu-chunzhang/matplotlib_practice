# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = np.arange(5)
y1 = [100, 68, 79, 91, 82]
y2 = [120, 75, 70, 78, 85]
std_err1 = [7, 2, 6, 10, 5]
std_err2 = [5, 1, 4, 8, 9]

error_attri = dict(elinewidth=2, ecolor="black", capsize=3)

bar_width = 0.4
tick_label = ["园区1", "园区2", "园区3", "园区4", "园区5"]

# create bar with errorbar
plt.bar(x, y1, bar_width, color="#87CEEB", align="center", edgecolor='k', yerr=std_err1, error_kw=error_attri, label="2010")
plt.bar(x+bar_width, y2, bar_width, color="#CD5C5C", align="center", edgecolor='k', yerr=std_err2, error_kw=error_attri, label="2013")

# set x,y_axis label
plt.xlabel("芒果种植区")
plt.ylabel("收割量")

# set xaxis tick_label
plt.xticks(x+bar_width/2, tick_label)
plt.ylim(0.0, 140.0)
plt.locator_params(axis='y', nbins=7)
plt.margins(x=0.15, y=0.10)

# set title of axes
plt.title("不同年份的芒果种植区的单次收割量")

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="gray", alpha=0.2)

plt.legend(loc="upper right")

plt.show()