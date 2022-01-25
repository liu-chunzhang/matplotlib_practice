import matplotlib.pyplot as plt
import numpy as np

font = dict(family="serif", color="navy", weight="black", size=16)
color = "skyblue"
linewidth = 3

fig = plt.figure()
ax = fig.add_subplot(111)

linestyleList = ["-", "--", "-.", ":"]

x = np.arange(1, 11, 1)
y = np.linspace(1, 1, 10)

ax.text(4, 4.0, "line styles", **font)

for i, ls in enumerate(linestyleList):
	ax.text(0, i+0.5, f"'{ls}'", **font)
	ax.plot(x, (i+0.5) * y, linestyle=ls, color=color, linewidth=linewidth)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 4.5)

ax.margins(0.2)
ax.set_xticks([])
ax.set_yticks([])

plt.show()