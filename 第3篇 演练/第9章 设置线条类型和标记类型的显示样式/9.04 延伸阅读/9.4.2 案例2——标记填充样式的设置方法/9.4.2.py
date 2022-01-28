import matplotlib.pyplot as plt
import numpy as np

font_style = dict(family="sans-serif", color="saddlebrown", weight="semibold", size=16)
line_marker_style = dict(linestyle=":", linewidth=2, color="cornflowerblue", markerfacecoloralt="lightgrey", marker="o", markersize=18)

fig, ax = plt.subplots()

fillstyleList = ["full", "left", "right", "bottom", "top", "none"]

x = np.arange(3, 11, 1)
y = np.linspace(1, 1, 8)

ax.text(4, 6.5, "fill styles", **font_style)

for i, fs in enumerate(fillstyleList):
	ax.text(0, i+0.4, f"'{fs}'", **font_style)
	ax.plot(x, (i+0.5)*y, fillstyle=fs, **line_marker_style, mec='k')

ax.set_xlim(-1.0, 11.0)
ax.set_ylim(0.0, 7.0)

ax.margins(0.3)
ax.set_xticks([])
ax.set_yticks([])

plt.show()