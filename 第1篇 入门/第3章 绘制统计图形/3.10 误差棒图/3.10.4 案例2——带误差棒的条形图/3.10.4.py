# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["LiSu"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
x = np.arange(5)
y = [1200, 2400, 1800, 2200, 1600]
std_err = [150, 100, 180, 130, 80]

bar_width = 0.6
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

# create horizontal bar
plt.barh(x, y, bar_width, color=colors, align="center", xerr=std_err, error_kw=dict(capthick=0.5, capsize=3), 
			tick_label=["家庭", "小说", "心理", "科技", "儿童"], edgecolor='k')

# set x,y_axis label
plt.xlim(0, 2600)
plt.locator_params(axis='x', nbins=6)
plt.xlabel("订购数量")
plt.ylabel("图书种类")

# set title
plt.title("大型图书展销会的不同图书种类的采购情况")

# set xaxis grid
plt.grid(True, axis="x", ls=":", color="gray", alpha=0.2)

plt.show()