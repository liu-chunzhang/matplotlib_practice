import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FuncFormatter

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)

# set x,y-major_tick_locator
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(1.0))

# set x,y-minor_tick_locator
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_minor_locator(AutoMinorLocator(4))

# set x-minor_tick_formatter

def minor_tick(x, pos):		# n % n = 0; m % n = m(m<n)
	if not x % 1.0 :
		return ""
	return "%.2f" % x

ax.xaxis.set_minor_formatter(FuncFormatter(minor_tick))

# change the appearance of ticks and tick labels
ax.tick_params("y", which='major', length=15, width=2.0, colors="r")
ax.tick_params(which='minor', length=5, width=1.0, labelsize=10, labelcolor='0.25')
ax.tick_params("x", which='major', length=15, width=2.0, colors="r")

# set x,y_axis_limit
ax.set_xlim(0,4)
ax.set_ylim(0,2)

# plot subplot
ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=10)	# pair 0
#ax.plot(x, y, c=(0.25, 0.25, 1.00), lw=2, zorder=0)	# pair 1

# set grid
ax.grid(linestyle="-", linewidth=0.5, color='r', zorder=0) 		# pair 0
#ax.grid(linestyle="-", linewidth=0.5, color='r', zorder=10)	# pair 1
#ax.grid(linestyle="--", linewidth=0.5, color='.25', zorder=0)	# pair 2

plt.show()

