# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]	# 使用中文字体
mpl.rcParams["axes.unicode_minus"] = False		# 不使用默认处理负号的方式

# some simple data
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [3, 1, 4, 5, 8, 9, 7, 2]

# create bar
plt.bar(x, y, align="center", color='c', tick_label=["q", "a", "c", "e", "r", "j", "b", "p"], hatch="/", linewidth=1, edgecolor='k')
																																# 用于绘制柱状图

# set x,y_axis label
plt.xlabel("箱子编号")
plt.ylim(0.0, 9.0)
plt.locator_params(axis='y', nbins=10)
plt.ylabel("箱子重量(kg)")

plt.show()