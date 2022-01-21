import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', lw=2, c='c', label='plot figure')

plt.legend(loc="lower right")

plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.xlim(0,10)
plt.ylim(-1, 1)

plt.show()