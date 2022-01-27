import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

# set subplot(211)
plt.subplot(211)
plt.xlim(-2*np.pi, 2*np.pi)
plt.locator_params(axis='x', nbins=7)	# 除非特别地想控制标签，对于图像形状和性质十分明确，个人以为用locator_params更好
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

# plot figure
plt.plot(x, y)

# setsubplot(212)
plt.subplot(212)

# set xlimit
plt.xlim(-2*np.pi, 2*np.pi)

plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

# set ticks
plt.xticks([-2*np.pi, -3*np.pi/2, -np.pi, -np.pi/2, 0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi], [r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$", r"$-\pi/2$", 
				r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])

# plot figure
plt.plot(x, y)

plt.show()