import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

s = np.linspace(-0.5, 0.5, 1000)
x, y = np.meshgrid(s, s)
z = x**2 + y**2 + np.power(x**2+y**2, 2)

fig, ax = plt.subplots(1, 1)

# a ContourSet object returned by contour
cs = plt.contour(x, y, z, cmap=mpl.cm.hot)

# add label to contour
plt.clabel(cs, fmt="%3.2f")
plt.xticks(np.arange(-0.4, 0.5, 0.2))
plt.yticks(np.arange(-0.4, 0.5, 0.2))

# mappable is ContourSet object
plt.colorbar(cs)

plt.show()