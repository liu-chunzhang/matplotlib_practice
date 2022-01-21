import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.random.rand(1000)

plt.scatter(x, y, label="scatter figure")

plt.legend(loc="upper right")

plt.xlim(-2.0, 12.0)
plt.xticks(np.arange(-2.0, 12.1, 2.0))
plt.ylim(-0.2, 1.2)
plt.yticks(np.arange(-0.2, 1.3, 0.2))

plt.show()