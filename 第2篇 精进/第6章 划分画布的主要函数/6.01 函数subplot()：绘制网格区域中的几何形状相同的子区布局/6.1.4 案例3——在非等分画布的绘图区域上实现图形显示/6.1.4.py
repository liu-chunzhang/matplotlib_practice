import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()

x = np.linspace(0.0, 2*np.pi)
y = np.cos(x)*np.sin(x)

ax1 = fig.add_subplot(121)						# 绘制左边的子图
ax1.margins(0.03)
ax1.plot(x, y, ls="-", lw=2, color="b")
ax1.locator_params(axis='x', nbins=8)
ax1.set_yticks(np.arange(-0.4, 0.5, 0.2))

ax2 = fig.add_subplot(222)						# 绘制右上角子图
ax2.margins(0.7, 0.7)
ax2.plot(x, y, ls="-", lw=2, color="r")
ax2.locator_params(axis='x', nbins=8)
ax2.locator_params(axis='y', nbins=5)

ax3 = fig.add_subplot(224)						# 绘制右下角子图
ax3.margins(x=0.1, y=0.3)
ax3.plot(x, y, ls="-", lw=2, color="g")
ax3.locator_params(axis='x', nbins=9)
ax3.set_yticks(np.arange(-0.6, 0.7, 0.2))

plt.show()