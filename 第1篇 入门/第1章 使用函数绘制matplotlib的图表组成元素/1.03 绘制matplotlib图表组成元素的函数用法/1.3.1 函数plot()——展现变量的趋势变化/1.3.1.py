import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.cos(x)
plt.plot(x, y, ls='-', lw=2, label='plot figure')

plt.legend(loc="upper right")

# some extra configure
plt.xticks(np.arange(0.0, 11.0, 2.0))
plt.xlim(0.0, 10.0)
plt.yticks(np.arange(-1.0, 1.1, 0.5))
plt.ylim(-1.0, 1.0)

plt.show()