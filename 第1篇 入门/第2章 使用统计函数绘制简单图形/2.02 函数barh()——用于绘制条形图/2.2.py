# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

# some simple data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# create bar
plt.barh(x, y, align="center", color='c', tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/", linewidth=1, edgecolor='k')

# set x,y_axis label
plt.xlabel("箱子重量(kg)")
plt.xlim(0.0, 9.0)
plt.xticks(np.arange(0.0, 9.1))
plt.ylabel("箱子编号")

plt.show()