# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["Fangsong"]
mpl.rcParams["axes.unicode_minus"] = False

time = np.arange(1, 11, 0.5)
machinePower = np.power(time, 2) + 0.7

plt.plot(time, machinePower, linestyle="-", linewidth=2, color="r")

plt.xlim(10, 1)
plt.xlabel("使用年限")
plt.xticks(np.arange(10.0, 0.9, -1.0))
plt.ylim(0, 120)
plt.ylabel("机器功率")
plt.yticks(np.arange(0.0, 120.1, 20.0))

plt.title("机器损耗曲线")

plt.grid(ls=":", lw=1, color="gray", alpha=0.5)

plt.show()