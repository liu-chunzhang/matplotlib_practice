import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MultipleLocator

x = np.linspace(0.0, 10.0, 200)
y = np.cos(x)*np.sin(x)
y2 = np.exp(-x)*np.sin(x)
y3 = 3*np.sin(x)
y4 = np.power(x, 0.5)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex="all")

fig.subplots_adjust(hspace=0)					# 去掉不同子区间的空白间隔

# subplot(411)
ax1.plot(x, y, ls="-", lw=2)

ax1.set_xlim(0.0, 10.0)
ax1.xaxis.set_major_locator(MultipleLocator(2.0))
ax1.set_ylim(-0.7, 0.7)
ax1.yaxis.set_major_locator(MultipleLocator(0.2))

# subplot(412)
ax2.plot(x, y2, ls="-", lw=2)

ax2.set_ylim(-0.1, 0.4)
ax2.set_yticks(np.arange(-0.05, 0.36, 0.1))		# 此处设置MultipleLocator不能控制刻度从0.05开始

# subplot(413)
ax3.plot(x, y3, ls="-", lw=2)

ax3.set_ylim(-3.5, 3.5)
ax3.yaxis.set_major_locator(MultipleLocator(1.0))

# subplot(414)
ax4.plot(x, y4, ls="-", lw=2)

ax4.set_ylim(0.0, 4.0)
ax4.set_yticks(np.arange(0.0, 4.0, 0.5))

plt.show()