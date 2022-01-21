import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
radii = 30*np.random.rand(barSlices)
width = 2*np.pi/barSlices
colors = np.array(["c", "m", "y", "b", "#C67171", "#C1CDCD", "#FFEC8B", "#A0522D", "red", "burlywood", "chartreuse", "green"])

fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

bars = ax.bar(theta, radii, width=width, color=colors, bottom=0.0)

plt.show()