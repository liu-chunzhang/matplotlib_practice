import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

radii = 30*np.random.rand(100)
theta = 2*np.pi*np.random.rand(100)
colors = np.random.rand(100)
size = 50*radii

ax = plt.subplot(111, polar=True)
ax.scatter(theta, radii, s=size, c=colors, cmap=mpl.cm.PuOr, marker="*")

plt.show()