import matplotlib.pyplot as plt
import numpy as np

rd = np.random.rand(10, 10)
plt.pcolor(rd, cmap="BuPu")
plt.colorbar()

plt.show()