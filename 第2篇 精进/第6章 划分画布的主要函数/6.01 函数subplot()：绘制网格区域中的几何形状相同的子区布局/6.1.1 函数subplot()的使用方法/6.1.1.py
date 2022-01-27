import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)
y1 = np.cos(x)

# set figure #1
plt.subplot(121)

plt.xlim(-8.0, 8.0)
plt.locator_params(axis='x', nbins=9)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)
plt.plot(x, y, ls=":")

# set figure #2
plt.subplot(122)

plt.xlim(-8.0, 8.0)
plt.locator_params(axis='x', nbins=9)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)
plt.plot(x, y1, ls=":")

plt.show()