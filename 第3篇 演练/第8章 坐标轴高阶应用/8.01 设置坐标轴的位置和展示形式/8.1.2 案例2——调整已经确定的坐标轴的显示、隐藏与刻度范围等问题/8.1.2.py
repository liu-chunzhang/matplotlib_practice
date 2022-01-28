import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["axes.xmargin"] = 0.0
plt.rcParams["axes.ymargin"] = 0.0

# set #1 plot
plt.axes([0.05, 0.7, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal", yticks=(np.arange(0.0, 2.0, 0.2)))
plt.plot(np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle="--")
#plt.ylim(0.0, 1.5)		# 由于下一句的作用，这一句无法体现效果！
plt.axis("image")		# 使画面紧凑

# set #2 plot
plt.axes([0.3, 0.4, 0.3, 0.3], frameon=True, facecolor="y", aspect="equal", yticks=(np.arange(0.0, 2.0, 0.2)))
plt.plot(2+np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle="-")
plt.ylim(0, 15)
plt.axis([2.1, 3.9, 0.5, 1.9])	# plt.axis是在已有的坐标轴内调整显示范围！不同于plt.axes


# set #3 plot
plt.axes([0.55, 0.1, 0.3, 0.3], frameon=False, facecolor="y", aspect="equal", yticks=(np.arange(0.0, 2.0, 0.2)))
plt.plot(4+np.arange(3), [0, 1, 0], color="blue", linewidth=2, linestyle=":")
plt.ylim(0.0, 1.5)
plt.axis("off")

plt.show()