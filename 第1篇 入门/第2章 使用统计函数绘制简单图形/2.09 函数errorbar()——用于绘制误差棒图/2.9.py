import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.1, 0.6, 6)
y = np.exp(x)

plt.errorbar(x, y, fmt="bo:", yerr=0.2, xerr=0.02, capsize=3)

plt.xlim(0, 0.7)

plt.show()