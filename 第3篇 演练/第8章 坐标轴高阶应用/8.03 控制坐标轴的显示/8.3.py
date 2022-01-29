import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)

ax1 = plt.subplot(221)

plt.scatter(x, y, s=8, marker="+", color="b")

ax1.set_xlim(-2*np.pi, 2*np.pi)
ax1.xaxis.set_major_locator(MultipleLocator(2.0))
ax1.set_ylim(-1.0, 1.0)
ax1.locator_params(axis='y', nbins=5)

plt.title(r"$(a)$", fontsize=10, math_fontfamily="cm", y=-0.25)		# 此处需要设置fontsize,math_fontfamily和y

ax1.spines["right"].set_color("none")
ax1.spines["top"].set_color("none")

ax2 = plt.subplot(222)

plt.scatter(x, y, s=8, marker="+", color="g")

ax2.set_xlim(-2*np.pi, 2*np.pi)
ax2.xaxis.set_ticks_position("bottom")
ax2.xaxis.set_major_locator(MultipleLocator(2.0))
ax2.set_ylim(-1.0, 1.0)
ax2.locator_params(axis='y', nbins=5)

plt.title(r"$(b)$", fontsize=10, math_fontfamily="cm", y=-0.25)

ax2.spines["right"].set_color("none")
ax2.spines["top"].set_color("none")

ax3 = plt.subplot(223)

plt.scatter(x, y, s=8, marker="+", color="b")

ax3.set_xlim(-2*np.pi, 2*np.pi)
ax3.xaxis.set_major_locator(MultipleLocator(2.0))
ax3.set_ylim(-1.0, 1.0)
ax3.locator_params(axis='y', nbins=5)
ax3.yaxis.set_ticks_position("left")

ax3.spines["right"].set_color("none")
ax3.spines["top"].set_color("none")

plt.title(r"$(c)$", fontsize=10, math_fontfamily="cm", y=-0.25)

ax4 = plt.subplot(224)

plt.scatter(x, y, s=8, marker="+", color="b")

ax4.set_xlim(-2*np.pi, 2*np.pi)
ax4.xaxis.set_ticks_position("bottom")
ax4.xaxis.set_major_locator(MultipleLocator(2.0))
ax4.set_ylim(-1.0, 1.0)
ax4.locator_params(axis='y', nbins=5)
ax4.yaxis.set_ticks_position("left")

ax4.spines["right"].set_color("none")
ax4.spines["top"].set_color("none")

plt.title(r"$(d)$", fontsize=10, math_fontfamily="cm", y=-0.25)

plt.subplots_adjust(hspace=0.3)		# 为调整子图之下图注的显示添加这一句

plt.show()