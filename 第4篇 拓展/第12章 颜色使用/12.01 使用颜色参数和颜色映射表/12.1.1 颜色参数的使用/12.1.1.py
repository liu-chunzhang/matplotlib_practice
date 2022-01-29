import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
radii = 30*np.random.rand(barSlices)
width = 2*np.pi/barSlices
colors = np.array(["c", "m", "y", "b", "#C67171", "#C1CDCD", "#FFEC8B", "#A0522D", "red", "burlywood", "chartreuse", "green"])

fig = plt.figure()
ax = fig.add_subplot(polar=True)

bars = ax.bar(theta, radii, width=width, color=colors, bottom=0.0, edgecolor='k')
ax.set_rlim(0, 30)
ax.set_rticks(np.arange(0, 30.1, 5))

plt.show()