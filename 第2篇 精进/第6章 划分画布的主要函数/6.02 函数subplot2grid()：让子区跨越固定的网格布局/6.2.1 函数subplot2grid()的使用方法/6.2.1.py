# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

# set subplot(23, 1, -2)
plt.subplot2grid((2, 3), (0, 0), colspan=2)
x = np.linspace(0.0, 4.0, 100)
y = np.random.randn(100)
plt.scatter(x, y, c="c")

plt.title("散点图")
plt.xlim(-1.0, 5.0)

# set subplot(233)
plt.subplot2grid((2, 3), (0, 2))
plt.title("空白绘图区域")

# set subplot(23, 4-6)
plt.subplot2grid((2, 3), (1, 0), colspan=3)
x = np.linspace(0.0, 4.0, 100)
y1 = np.sin(x)
plt.plot(x, y1, lw=2, ls="-")
plt.xlim(0.0, 3.0)
plt.grid(True, ls=":", c="r")
plt.title("折线图", loc="center")

# set figure title
plt.suptitle("subplot2grid()函数的实例展示", fontsize=25)

plt.show()