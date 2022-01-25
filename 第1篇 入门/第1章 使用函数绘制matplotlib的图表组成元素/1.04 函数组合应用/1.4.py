import matplotlib.pyplot as plt
import numpy as np

from matplotlib import cm as cm

# define data
x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)
y1 = np.random.randn(100)

# scatter figure
plt.scatter(x, y1, c='0.25', label='scatter figure')

# plot figure
plt.plot(x, y, ls='--', lw=2, label='plot figure')

# some clean up(removing chartjunk)
# turn the top spine and the right spine off
for spine in plt.gca().spines:					# python基础语法里，循环对象是字典时默认调用其key()函数。
	if spine == "top" or spine == "right" :
		plt.gca().spines[spine].set_color("none")

# turn bottom tick for x-axis on
plt.gca().xaxis.set_ticks_position("bottom")
# set tick_line position of bottom

# turn left ticks for y-axis on
plt.gca().yaxis.set_ticks_position("left")
# set tick_line position of left

# set x,yaxis limit
plt.xlim(0.0, 4.0)
plt.xticks(np.arange(0.0, 4.1, 0.5))
plt.ylim(-3.0, 3.0)
plt.yticks(np.arange(-3.0, 3.1))

# set axes labels
plt.ylabel("y_axis")
plt.xlabel("x_axis")

# set x,yaxis grid
plt.grid(True, ls=":", color="r")

# add a horizontal line across the axis
plt.axhline(y=0.0, c="r", ls="--", lw=2)

# add a vertical span across the axis
plt.axvspan(xmin=1.0, xmax=2.0, facecolor='y', alpha=0.3)

# set annotating info
plt.annotate("maximum",
	xy=(np.pi/2, 1.0), 
	xytext=((np.pi/2 + 0.15),1.5), 
	weight="bold", 
	color="r", 
	arrowprops=dict(arrowstyle="->", 
		connectionstyle="arc3", 
		color="r")
	)

plt.annotate("spine",
	xy=(0.75, -3),
	xytext=(0.35,-2.25),
	weight="bold",
	color="b",
	arrowprops=dict(arrowstyle="->", 
		connectionstyle="arc3",
		color="b")
	)

plt.annotate("",
	xy=(0.0, -2.78),
	xytext=(0.4,-2.32),
	arrowprops=dict(arrowstyle="->", 
		connectionstyle="arc3",
		color="b")
	)

plt.annotate("",
	xy=(3.5, -2.98),
	xytext=(3.6, -2.70),
	arrowprops=dict(arrowstyle="->", 
		connectionstyle="arc3",
		color="b")
	)

# set text info
plt.text(3.6, -2.70, "'|' is tickline", weight="bold", color="b")
plt.text(3.6, -2.95, "3.5 is ticklabel", weight="bold", color="b")

# set title
plt.title("structure of matplotlib")

# set legend
plt.legend(loc="upper right")

plt.show()