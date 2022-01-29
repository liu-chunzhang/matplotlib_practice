# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

mpl.rcParams["font.sans-serif"] = ["Lisu"]
mpl.rcParams["axes.unicode_minus"] = False
mpl.rcParams["mathtext.fontset"] = "cm"

x = np.arange(1, 13, 1)
y = np.array([12, 34, 22, 30, 18, 13, 15, 19, 24, 28, 23, 27])

fig, ax = plt.subplots(2, 2, figsize=(8, 5.6))

# subplot(221)
ax[0, 0].scatter(x, y*1.5, marker=r"$\clubsuit$", c="#fb8072", s=500, edgecolor='k')
ax[0, 0].locator_params(axis="x", tight=True, nbins=11)
ax[0, 0].set_xlim(0, 13)
ax[0, 0].set_xticks(x)
ax[0, 0].set_ylim(15, 55)
ax[0, 0].yaxis.set_major_locator(MultipleLocator(5.0))
ax[0, 0].set_title(r'显示样式 “$\clubsuit$” 的散点图')

# subplot(222)
ax[0, 1].scatter(x, y-2, marker=r"$\heartsuit$", s=500, edgecolor='k')
ax[0, 1].locator_params(axis="x", tight=True, nbins=11)
ax[0, 1].set_xlim(0, 13)
ax[0, 1].set_xticks(x)
ax[0, 1].set_ylim(5, 35)
ax[0, 1].yaxis.set_major_locator(MultipleLocator(5.0))
ax[0, 1].set_title(r'显示样式 “$\heartsuit$” 的散点图')

# subplot(223)
ax[1, 0].scatter(x, y*1.5, marker=r"$\diamondsuit$", s=500, edgecolor='k')
ax[1, 0].locator_params(axis="x", tight=True, nbins=11)
ax[1, 0].set_xlim(0, 13)
ax[1, 0].set_xticks(x)
ax[1, 0].set_ylim(15, 45)
ax[1, 0].yaxis.set_major_locator(MultipleLocator(5.0))
ax[1, 0].set_title(r'显示样式 “$\diamondsuit$” 的散点图')

# subplot(224)
ax[1, 1].scatter(x, y-9, marker=r"$\spadesuit$", c="#8dd3c7", s=500, edgecolor='k')
ax[1, 1].locator_params(axis="x", tight=True, nbins=11)
ax[1, 1].set_xlim(0, 13)
ax[1, 1].set_xticks(x)
ax[1, 1].set_ylim(0, 30)
ax[1, 1].yaxis.set_major_locator(MultipleLocator(5.0))
ax[1, 1].set_title(r'显示样式 “$\spadesuit$” 的散点图')

plt.suptitle("不同原始字符串作为标记类型的展示效果", fontsize=16, weight="black")

plt.subplots_adjust()

plt.show()