import matplotlib.pyplot as plt
import numpy as np

radii = np.linspace(0, 1, 100)
theta = 2*np.pi*radii

ax = plt.subplot(111, polar=True)	# 绘制极线图

ax.plot(theta, radii, color="r", linestyle="-", linewidth=2)
ax.margins(0.0)

ax.grid(ls="--")

plt.show()