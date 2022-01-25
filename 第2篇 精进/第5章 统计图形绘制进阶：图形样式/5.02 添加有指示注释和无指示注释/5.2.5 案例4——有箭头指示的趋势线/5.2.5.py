import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 2000)
y = np.sin(x)

fig = plt.figure()
ax = fig.add_subplot(111)

ax.plot(x, y, ls="-", lw=2)

ax.set_ylim(-1.5, 1.5)

arrowprops = dict(arrowstyle="-|>", color="r")

ax.annotate("",(3*np.pi/2, np.sin(3*np.pi/2+0.05)),xytext=(np.pi/2, np.sin(np.pi/2)+0.05), color="r", arrowprops=arrowprops)

ax.arrow(0.0, -0.4, np.pi/2, 1.2, head_width=0.05, head_length=0.1, fc='g', ec='g')

plt.xlim(0, 10)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-1.5, 1.5)
plt.locator_params(axis='y', nbins=8)

plt.show()