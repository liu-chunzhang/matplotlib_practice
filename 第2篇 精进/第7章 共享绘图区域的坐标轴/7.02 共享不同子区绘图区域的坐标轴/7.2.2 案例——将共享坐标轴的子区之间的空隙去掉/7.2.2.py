import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 200)
y = np.cos(x)*np.sin(x)
y2 = np.exp(-x)*np.sin(x)
y3 = 3*np.sin(x)
y4 = np.power(x, 0.5)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, sharex="all")

fig.subplots_adjust(hspace=0)

ax1.plot(x, y, ls="-", lw=2)
ax1.set_yticks(np.arange(-0.6, 0.7, 0.3))
ax1.set_ylim(-0.7, 0.7)
ax1.set_xlim(0.0, 10.0)

ax2.plot(x, y2, ls="-", lw=2)
ax2.set_yticks(np.arange(-0.05, 0.36, 0.1))
ax2.set_ylim(-0.1, 0.4)

ax3.plot(x, y3, ls="-", lw=2)
ax3.set_yticks(np.arange(-3, 4, 1))
ax3.set_ylim(-3.5, 3.5)

ax4.plot(x, y4, ls="-", lw=2)
ax4.set_yticks(np.arange(0.0, 3.6, 0.5))
ax4.set_ylim(0.0, 4.0)

plt.show()