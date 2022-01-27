import matplotlib.pyplot as plt
import numpy as np

radii = np.linspace(0, 1, 100)
theta = 2 * np.pi * radii

ax = plt.subplot(111, polar=True)

ax.plot(theta, radii, color="r", linestyle="-", linewidth=2)

ax.grid(ls="--")
ax.margins(0.0)

plt.show()