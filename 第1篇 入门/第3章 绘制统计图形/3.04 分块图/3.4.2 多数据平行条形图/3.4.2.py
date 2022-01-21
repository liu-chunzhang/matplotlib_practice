# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"]=["SimHei"]	# 使用中文字体
mpl.rcParams["axes.unicode_minus"]=False	# 允许使用负号

# some simple data
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

bar_width = 0.35
tick_label = ["A", "B", "C", "D", "E"]

# create horizontal bar
plt.barh(x, y, bar_width, color='c', align="center", label="班级A", alpha=0.5)
plt.barh(x+bar_width, y1, bar_width, color="b", align="center", label="班级B", alpha=0.5)

# set x,y_axis label
plt.xlabel("试卷份数")
plt.ylabel("测试难度")

plt.yticks(x+bar_width/2, tick_label)
plt.locator_params(axis='x', nbins=5)
plt.margins(x=0)

plt.legend()

plt.show()