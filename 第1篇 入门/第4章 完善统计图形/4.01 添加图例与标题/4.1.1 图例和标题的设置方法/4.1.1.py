# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

plt.plot(x, y, label=r"$\sin(x)$")
plt.plot(x, y1, label=r"$\cos(x)$")

plt.xlim(-8.0, 8.0)
plt.locator_params(axis='x', nbins=9)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.legend(loc="lower left", prop=dict(math_fontfamily="stix"))

plt.title("正弦函数和余弦函数的折线图")

plt.show()