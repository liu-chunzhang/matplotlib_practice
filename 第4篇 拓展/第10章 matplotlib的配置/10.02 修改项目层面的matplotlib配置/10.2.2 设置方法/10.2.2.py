import matplotlib.pyplot as plt
import numpy as np

# normal plot
plt.axes([0.1, 0.7, 0.3, 0.3], frameon=True, aspect="equal")
plt.xlim(0.0, 2.0)
plt.plot(np.arange(3), [0, 1, 0])
plt.cla()
plt.plot(np.arange(3), [0, 1, 0])

# no-plot
plt.axes([0.4, 0.4, 0.3, 0.3], frameon=True, aspect="equal")
plt.plot(2.0+np.arange(3), [0, 1, 0])

# no-axes
plt.axes([0.7, 0.1, 0.3, 0.3], frameon=True, aspect="equal")
plt.plot(4+np.arange(3), [0, 1, 0])
plt.axis("off")

plt.show()