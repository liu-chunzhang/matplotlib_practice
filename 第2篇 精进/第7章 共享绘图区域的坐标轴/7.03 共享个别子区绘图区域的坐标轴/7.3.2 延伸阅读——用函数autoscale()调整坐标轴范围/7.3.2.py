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
fig, ax = plt.subplots(2, 2, figsize=(8, 5.6))

# set chart of each subplot
# subplot(221)
ax1 = plt.subplot(221)
ax1.plot(x1, y1)

ax1.set_xlim(0.0, 7.0)
ax1.locator_params(axis='x', nbins=8)
ax1.set_ylim(-1.0, 1.0)
ax1.locator_params(axis='y', nbins=5)

# subplot(222)
ax2 = plt.subplot(222)
ax2.plot(x2, y2)

ax2.set_xlim(0.0, 10.0)
ax2.locator_params(axis='x', nbins=6)
ax2.set_ylim(-1.0, 1.0)
ax2.locator_params(axis='y', nbins=5)

# subplot(223)
ax3 = plt.subplot(223)
ax3.scatter(x3, y3)
ax3.autoscale(enable=True, axis="both", tight=True)		# 进行坐标轴的自适应调整

# subplot(224)
ax4 = plt.subplot(224, sharex=ax1)
ax4.scatter(x4, y4)

ax4.set_xlim(-1.0, 7.0)
ax4.locator_params(axis='x', nbins=8)
ax4.set_ylim(-50.0, 200.0)
ax4.locator_params(axis='y', nbins=6)

plt.show()