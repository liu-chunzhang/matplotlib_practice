# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["Fangsong"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.random.randn(1000)

plt.boxplot(x, whiskerprops=dict(linestyle="--", dashes=[5, 5]), sym="+", vert=False)	# 使用whiskerprops调整箱线参数

plt.xlabel("随机数值")
plt.yticks([1], ["随机数生成器AlphaRM"], rotation=90, va='center')
plt.title("随机数生成器抗干扰能力的稳定性比较")

plt.grid(axis="x", ls=":", lw=1, color="gray", dashes=[2, 2], alpha=0.4)

plt.show()