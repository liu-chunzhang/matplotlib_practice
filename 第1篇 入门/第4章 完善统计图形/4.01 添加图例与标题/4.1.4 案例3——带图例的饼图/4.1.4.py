# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

elements = ["面粉", "砂糖", "奶油", "草莓酱", "坚果"]

weight = [40, 15, 20, 10, 15]

colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]

wedges, texts, autotexts = plt.pie(weight, autopct="%3.1f%%", wedgeprops=dict(edgecolor='c'), colors=colors) 
																								# 原教材代码中textprops因为参量labels没有输入而无作用

plt.legend(wedges, elements, fontsize=12, title="配料表", loc="center left", bbox_to_anchor=(0.91, 0, 0.3, 1))

plt.setp(autotexts, size=12, color='w', weight="light")
#plt.setp(texts, size=12)	# 这一句没有用处，因为在绘制饼图时根本没有传入任何文字标签（即没有给labels赋值）！

plt.title("不同果酱面包配料比例表")

plt.show()