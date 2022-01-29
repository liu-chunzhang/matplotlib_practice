# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator			# 设置y的变动单位为1.0

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

fig = plt.figure(figsize=(8, 5.6))

# set subplot(23, 1-2)
ax = plt.subplot2grid((2, 3), (0, 0), colspan=2)		# 这里调用了面向对象的API，下面方便控制刻度标签的格式
x = np.linspace(0.0, 4.0, 100)
y = np.random.randn(100)
plt.scatter(x, y, c="c")

plt.title("散点图")
plt.xlim(-1.0, 5.0)
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))		# 可回顾5.1节

# set subplot(233)
ax2 = plt.subplot2grid((2, 3), (0, 2))
ax2.xaxis.set_major_locator(MultipleLocator(0.2))
ax2.yaxis.set_major_locator(MultipleLocator(0.2))
plt.title("空白绘图区域")

# set subplot(23, 4-6)
ax3 = plt.subplot2grid((2, 3), (1, 0), colspan=3)

x = np.linspace(0.0, 4.0, 100)
y1 = np.sin(x)

plt.plot(x, y1, lw=2, ls="-")

plt.xlim(0.0, 3.0)
ax3.xaxis.set_major_locator(MultipleLocator(0.5))
plt.ylim(-0.8, 1.0)
ax3.yaxis.set_major_locator(MultipleLocator(0.2))
plt.grid(ls=":", c="r")
plt.title("折线图", loc="center")

# set figure title
plt.suptitle("subplot2grid()函数的实例展示", fontsize=18)

plt.show()