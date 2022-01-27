import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1, figsize=(8, 4.8))	# 此即集成了fig和ax的定义语句

# set x,y-major_tick_locator
ax.xaxis.set_major_locator(MultipleLocator(1.0))	# 设置在x轴长为1时，设置主刻度
ax.yaxis.set_major_locator(MultipleLocator(1.0))	# 设置在y轴长为1时，设置主刻度

# set x,y-minor_tick_locator
ax.xaxis.set_minor_locator(AutoMinorLocator(4))		# 设置x轴的次刻度线为4道。
ax.yaxis.set_minor_locator(AutoMinorLocator(4))		# 设置y轴的次刻度线为4道。

# set x-minor_tick_formatter

def minor_tick(x, pos):		# n % n = 0; m % n = m(m<n)
	if not x % 1.0 :
		return ""
	return "%.2f" % x

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))	 # 此处类似于函数指针？

# change the appearance of ticks and tick labels
ax.tick_params(axis="x", which='major', length=10, width=2.0, colors="r")
ax.tick_params(axis="y", which='major', length=10, width=2.0, colors="r")
ax.tick_params(which='minor', length=5, width=1.0, labelsize=10, labelcolor='0.25')

# set x,y_axis_limit
ax.set_xlim(0, 4)
ax.set_ylim(0, 2)

# plot subplot
ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=10)			# pair 0
#ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=0)			# pair 1

# set grid
#ax.grid(linestyle="-", linewidth=0.5, color='r', zorder=0) 	# pair 0
#ax.grid(linestyle="-", linewidth=0.5, color='r', zorder=10)	# pair 1
ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=0)	# pair 2

plt.show()