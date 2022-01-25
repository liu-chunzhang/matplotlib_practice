# -*- coding:utf-8 -*-

import matplotlib as mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

import matplotlib.pyplot as plt
import numpy as np

# some test scores
scoreT1 = np.random.randint(0, 100, 100)
scoreT2 = np.random.randint(0, 100, 100)

x = [scoreT1, scoreT2]
colors = ["#8dd3c7", "#bebada"]
labels = ["班级A", "班级B"]

# plot histograms
bins = range(0, 101, 10)

plt.hist(x, bins=bins, color=colors, histtype="stepfilled", rwidth=1.0, stacked=True, label=labels, edgecolor='k')	# 可以获得图3.14的效果
# plt.hist(x, bins=bins, color=colors, histtype="bar", rwidth=0.8, stacked=False, label=labels, edgecolor='k') # 可以获得图3.15的效果

# set x,y_axis label
plt.xlabel("测试成绩（分）")
plt.ylabel("学生人数")
plt.margins(0)

plt.title("不同班级的测试成绩的直方图")
plt.legend(loc="upper left")

plt.show()