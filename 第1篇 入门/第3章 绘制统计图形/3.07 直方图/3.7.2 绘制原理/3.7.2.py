# -*- coding:utf-8 -*-

import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

import matplotlib.pyplot as plt
import numpy as np

# set test scores
scoresT = np.random.randint(0, 100, 100)

x = scoresT

# plot histogram
bins = range(0, 101, 10)

plt.hist(x, bins=bins, color="#377eb8", histtype="bar", rwidth=1.0, edgecolor='k')	# 绘制直方图，其中rwidth表示柱体相对宽度

# set x,y_axis label
plt.locator_params(axis='x', nbins=6)
plt.xlabel("测试成绩")
plt.locator_params(axis='y', nbins=10)
plt.ylabel("学生人数")
plt.margins(0, 0)

plt.show()