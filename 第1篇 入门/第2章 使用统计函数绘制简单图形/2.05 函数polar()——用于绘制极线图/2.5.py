import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)	# endpoint表示不包括终点值，对此见附录B3.2
r = 30 * np.random.rand(barSlices)

plt.polar(theta, r, color='chartreuse', linewidth=2, marker="*", mfc="r", ms=10)	# 用于绘制极线图
plt.margins(0)																		# 取消极轴多余空白
plt.grid(ls="-", dashes=[2, 2])

plt.show()