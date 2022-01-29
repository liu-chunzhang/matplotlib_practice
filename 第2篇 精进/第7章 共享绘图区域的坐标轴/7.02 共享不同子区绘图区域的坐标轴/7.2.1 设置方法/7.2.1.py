import matplotlib.pyplot as plt
import numpy as np

# create sample data

x1 = np.linspace(0, 2*np.pi, 400)
y1 = np.cos(x1**2)

x2 = np.linspace(0.01, 10, 100)
y2 = np.sin(x2)

x3 = np.random.rand(100)
y3 = np.linspace(0, 3, 100)

x4 = np.arange(0, 6, 0.5)
y4 = np.power(x4, 3)

# set (2, 2) subplots
#fig, ax = plt.subplots(2, 2, sharex="col")	# 控制共享坐标轴
#fig, ax = plt.subplots(2, 2, sharex="row")
#fig, ax = plt.subplots(2, 2, sharex="all")
fig, ax = plt.subplots(2, 2, sharex="none")

# set chart of each subplot

ax1 = ax[0, 0]
ax1.plot(x1, y1)
ax1.set_xlim(0.0, 7.0)
ax1.locator_params(axis='x', nbins=8)
ax1.set_ylim(-1.0, 1.0)
ax1.locator_params(axis='y', nbins=5)

ax2 = ax[0, 1]
ax2.plot(x2, y2)
ax2.set_xlim(0.0, 10.0)
ax2.locator_params(axis='x', nbins=6)
ax2.set_ylim(-1.0, 1.0)
ax2.locator_params(axis='y', nbins=5)

ax3 = ax[1, 0]
ax3.scatter(x3, y3)
ax3.set_xlim(-0.2, 1.2)
ax3.locator_params(axis='x', nbins=8)
ax3.set_ylim(-0.5, 3.5)
ax3.locator_params(axis='y', nbins=9)

ax4 = ax[1, 1]
ax4.scatter(x4, y4)
ax4.set_xlim(-1.0, 6.0)
ax4.locator_params(axis='x', nbins=8)
ax4.set_ylim(-50.0, 200.0)
ax4.locator_params(axis='y', nbins=6)

# Show figure and subplot(s)
plt.show()