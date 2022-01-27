import matplotlib.pyplot as plt
import numpy as np

from calendar import day_name
from matplotlib.ticker import FormatStrFormatter

plt.rcParams["font.sans-serif"] = ["SimHei"]

fig = plt.figure()
ax = fig.add_axes([0.2, 0.2, 0.7, 0.7])

x = np.arange(1, 8)
y = 2*x

ax.plot(x, y, ls="-", lw=2, color="orange", marker="o", ms=20, mfc="c", mec="b")

# RMB ticklabel
ax.yaxis.set_major_formatter(FormatStrFormatter(r"$\yen%.1f$"))	# 设置货币刻度标签
# dayName ticklabel
plt.xticks(x, day_name[0:7], rotation=20)						# 设置时间序列刻度标签

ax.set_xlim(0, 8)
ax.set_ylim(0, 18)

plt.show()