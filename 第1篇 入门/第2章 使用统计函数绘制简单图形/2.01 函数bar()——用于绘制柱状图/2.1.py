# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"]=["SimHei"]	# 使用中文字体
mpl.rcParams["axes.unicode_minus"]=False	# 允许使用负号

# some simple data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# create bar
plt.bar(x, y, align="center", color='c', tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/", linewidth=1, edgecolor='k')

# set x,y_axis label
plt.xlabel("箱子编号")
plt.ylabel("箱子重量(kg)")
plt.ylim(0.0, 9.0)
plt.yticks(np.arange(0.0, 9.1))

plt.show()