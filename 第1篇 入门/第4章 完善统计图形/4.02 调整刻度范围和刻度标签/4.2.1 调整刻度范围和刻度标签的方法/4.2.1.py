# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 200)
y = np.sin(x)

# set subplot(211)
plt.subplot(211)
plt.xlim(-2*np.pi, 2*np.pi)
plt.xticks(np.arange(-6.0, 6.1, 2.0))
plt.ylim(-1.0, 1.0)
plt.yticks(np.arange(-1.0, 1.1, 0.5))

# plot figure
plt.plot(x,y)

# setsubplot(212)
plt.subplot(212)

# set xlimit
plt.xlim(-2*np.pi, 2*np.pi)
plt.ylim(-1.0, 1.0)

# set ticks
plt.xticks([-2*np.pi, -3*np.pi/2, -1*np.pi, -1*np.pi/2, 0, (np.pi)/2, np.pi, 3*np.pi/2, 2*np.pi], 
			[r"$-2\pi$", r"$-3\pi/2$", r"$-\pi$", r"$-\pi/2$", r"$0$", r"$\pi/2$", r"$\pi$", r"$3\pi/2$", r"$2\pi$"])
plt.yticks(np.arange(-1.0, 1.1, 0.5))

plt.plot(x, y)

plt.show()