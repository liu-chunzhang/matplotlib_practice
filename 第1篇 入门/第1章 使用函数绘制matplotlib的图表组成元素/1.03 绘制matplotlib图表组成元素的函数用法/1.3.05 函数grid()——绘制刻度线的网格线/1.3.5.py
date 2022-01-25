import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', lw=2, c="c", label="plot figure", dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")

plt.xlim(0.00, 10)
plt.yticks(np.arange(0.0, 10.1, 2))
plt.ylim(-1.0, 1.0)
plt.yticks(np.arange(-1.0, 1.1, 0.5))

plt.grid(linestyle=":", color="g")

plt.show()