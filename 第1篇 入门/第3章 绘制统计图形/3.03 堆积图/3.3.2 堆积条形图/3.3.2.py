# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]	# 使用中文字体
mpl.rcParams["axes.unicode_minus"] = False		# 允许使用负号

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]

# create horizontal bar
plt.barh(x, y, align="center", color='#66c2a5', tick_label=["A", "B", "C", "D", "E"], label="班级A", edgecolor='k')
plt.barh(x, y1, align="center", left=y, color="#8da0cb", label="班级B", edgecolor='k')	# 输出堆积条形图

# set x,y_axis label
plt.ylabel("测试难度")
plt.locator_params(axis='x', nbins=10)
plt.xlabel("试卷份数")

plt.margins(x=0)
plt.legend(loc="upper right")

plt.show()