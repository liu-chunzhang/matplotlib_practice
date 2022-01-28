import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

ax = plt.subplot()

x = np.linspace(0.5, 2*np.pi, 20)
y = np.random.randn(20)

markerline, stemlines, baseline = ax.stem(x, y)

ax.set_xlim(0.0, 7.0)
ax.xaxis.set_major_locator(MultipleLocator(1.0))
ax.yaxis.set_major_locator(MultipleLocator(0.5))

plt.setp(markerline, mfc="chartreuse", mec="steelblue", linewidth=1, marker="D")
plt.setp(stemlines, ls="-.", color='steelblue')
plt.setp(baseline, color='r', linewidth=2)

plt.show()