# -*- coding:utf-8 -*-

import matplotlib as mpl

mpl.rcParams["font.sans-serif"]=["SimHei"]
mpl.rcParams["axes.unicode_minus"]=False

import matplotlib.pyplot as plt
import numpy as np

# set test scores
boxWeight = np.random.randint(0,10,100)
x = boxWeight

# plot histogram
bins = range(0, 11, 1)
plt.hist(x, bins=bins, histtype='bar', color='g', alpha=0.6, edgecolor='k', linewidth=1)

# set x,y_axis label
plt.xlabel("箱子重量(kg)")
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylabel("销售数量（个）")
plt.margins(0.0)

plt.show()