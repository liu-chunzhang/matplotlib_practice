import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
r = 30 * np.random.rand(barSlices)

plt.polar(theta, r, color='chartreuse', linewidth=2, marker="*", mfc="r", ms=10)
plt.margins(0)
plt.grid(ls="-", dashes=[2, 2])

plt.show()