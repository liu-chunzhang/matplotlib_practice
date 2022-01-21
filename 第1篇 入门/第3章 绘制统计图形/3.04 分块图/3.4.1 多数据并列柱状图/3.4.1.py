# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

# some simple data
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

bar_width = 0.35
tick_label = ["A", "B", "C", "D", "E"]

# create bar
plt.bar(x, y, bar_width, color='c', align="center", label="班级A", alpha=0.5, edgecolor='k')
plt.bar(x+bar_width, y1, bar_width, color='b', align="center", label="班级B", alpha=0.5, edgecolor='k')

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷分数")

# set xaxis ticks and ticklabels
plt.xticks(x+bar_width/2,tick_label)

plt.margins(y=0)
plt.locator_params(axis='y', nbins=5)
plt.legend(loc="upper right")

plt.show()