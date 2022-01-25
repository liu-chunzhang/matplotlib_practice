# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]	# 使用中文字体
mpl.rcParams["axes.unicode_minus"] = False		# 不使用默认的Unicode minus模式来处理负号

# some simple data
x = [1, 2, 3, 4, 5]
y = [6, 10, 4, 5, 1]

# create bar
plt.bar(x, y, align="center", color='b', tick_label=["A", "B", "C", "D", "E"], alpha=0.6, linewidth=2, edgecolor='k')

# set x,y_axis label
plt.xlabel("测试难度")
plt.ylabel("试卷份数")
plt.margins(y=0)

# set yaxis grid
plt.grid(True, axis="y", ls=":", color="r", alpha=0.3)

plt.show()