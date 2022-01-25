# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

# create bar
plt.bar(x, y, align="center", color='#66c2a5', tick_label=["A", "B", "C", "D", "E"], label="班级A", edgecolor='k')
plt.bar(x, y1, align="center", bottom=y, color="#8da0cb", label="班级B", edgecolor="k")	# 有层次地显示两个y的和

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷分数")
plt.locator_params(axis="x", nbins=10)

plt.margins(y=0)
plt.legend(loc="upper right")

plt.show()