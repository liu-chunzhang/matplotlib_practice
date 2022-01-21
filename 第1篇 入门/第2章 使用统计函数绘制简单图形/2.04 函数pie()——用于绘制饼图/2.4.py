# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# some simple data
kinds = ("简易箱", "保温箱", "行李箱", "密封箱")
colors = ['#e41a1c', '#377eb8', '#4daf4a', '#984ea3']
soldNums = [0.05, 0.45, 0.15, 0.35]

# pie chart
plt.pie(soldNums, pctdistance=0.75, textprops=dict(color='k'), wedgeprops=dict(edgecolor='w'), 
			labels=kinds, autopct="%3.2f%%", startangle=60, colors=colors)

# set titie
plt.title("不同类型箱子的销售数量占比")

plt.show()