# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

ax = plt.subplot(111)

ax.plot(x, y, ls="-", lw=2, label=r"$\sin(x)$")
ax.plot(x, y1, ls="-", lw=2, label=r"$\cos(x)$")

# set xlimit
ax.set_xlim(-2*np.pi, 2*np.pi)
ax.set_ylim(-1.0, 1.0)
ax.locator_params(axis='y', nbins=5)

# set ticks
plt.xticks([-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], ["$-2\pi$", "$-3\pi/2$", "$-\pi$", "$-\pi/2$", 
				"$0$", "$\pi/2$", "$\pi$", "$3\pi/2$", "$2\pi$"])

ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

ax.spines["bottom"].set_position(("data", 0))
ax.spines["left"].set_position(("data", 0))

ax.xaxis.set_ticks_position("bottom")
ax.yaxis.set_ticks_position("left")

ax.legend(loc="lower left", prop={"math_fontfamily":"cm"})

plt.title(r"$\sin(x)$和$\cos(x)$函数", math_fontfamily="cm", y=1.05)

plt.show()