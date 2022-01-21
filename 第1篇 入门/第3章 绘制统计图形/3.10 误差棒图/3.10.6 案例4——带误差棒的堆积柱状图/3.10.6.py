# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = np.arange(5)
y1 = [1200, 2400, 1800, 2200, 1600]
y2 = [1050, 2100, 1300, 1600, 1340]
std_err1 = [150, 100, 180, 130, 80]
std_err2 = [120, 110, 170, 150, 120]

bar_width = 0.6
tick_label = ["家庭", "小说", "心理", "科技", "儿童"]
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
error_attri = dict(ecolor="black", elinewidth=2, capsize=0)

# create bar
plt.bar(x, y1, bar_width, color="#6495ED", align="center", edgecolor='k', yerr=std_err1, label="地区1", error_kw=error_attri)
plt.bar(x, y2, bar_width, bottom=y1, color="#FFA500", align="center", edgecolor='k', yerr=std_err2, label="地区2", error_kw=error_attri)

# set x,y_axis label
plt.xlabel("图书种类")
plt.ylabel("订购数量")

# set title
plt.title("大型图书展销会的不同图书种类的采购情况")

# set xaxis grid
plt.grid(True, axis="y", ls=":", color="gray", alpha=0.2)
plt.xticks(x, tick_label)
plt.yticks(np.arange(0, 5000.1, 1000))
plt.legend(loc=1)

plt.show()