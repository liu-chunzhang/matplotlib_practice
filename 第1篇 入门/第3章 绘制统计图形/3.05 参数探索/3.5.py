# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]	# 使用中文字体
mpl.rcParams["axes.unicode_minus"] = False		# 允许使用负号

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# create bar
plt.bar(x, y, align="center", color='c', tick_label=["A", "B", "C", "D", "E"], hatch="///", edgecolor='k')

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")

plt.margins(y=0)
plt.locator_params(axis='y', nbins=5)

plt.show()