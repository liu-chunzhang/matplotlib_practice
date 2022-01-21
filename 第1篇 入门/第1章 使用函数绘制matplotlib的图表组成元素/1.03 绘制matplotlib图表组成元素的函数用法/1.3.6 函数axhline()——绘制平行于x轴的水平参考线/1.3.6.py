import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c='c', label="plot figure", dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")

plt.axhline(y=0.0, c="b", ls="--", lw=2)
plt.axvline(x=4.0, c='r', ls="--", lw=2)

plt.xlim(0.00,10.0)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-1.0,1.0)
plt.yticks(np.arange(-1.0, 1.1, 0.5))

plt.show()