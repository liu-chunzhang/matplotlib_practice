import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 2000)
y = np.sin(x)*np.cos(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y, ls="-", lw=2)

bbox = dict(boxstyle="round", fc="#7EC0EE", ec="#9B30FF")
arrowprops = dict(arrowstyle="-|>", connectionstyle="angle,angleA=0,angleB=90,rad=10", color="r")

ax.annotate("single point", (5, np.sin(5)*np.cos(5)),xytext=(3,np.sin(3)*np.cos(3)), fontsize=12, color="r", bbox=bbox, arrowprops=arrowprops)

ax.grid(ls=":", color="gray", alpha=0.6)

plt.xlim(0.0, 10.0)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-0.6, 0.6)
plt.locator_params(axis='y', nbins=8)

plt.show()