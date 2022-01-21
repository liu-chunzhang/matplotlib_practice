import matplotlib.pyplot as plt
import numpy as np

font_style = dict(family="serif", color="navy", weight="black", size=12)
line_marker_style = dict(linestyle=":", linewidth=2, color="maroon", markersize=10)

fig = plt.figure()
ax = fig.add_subplot(111)

msNameList = ["'.'--point marker", "','--pixel marker", "'o'--circle marker", "'v'--triangle_down marker", "'^'--triangle_up marker", 
				"'<'--triangle_left marker", "'>'--triangle_right marker", "'1'--tri_down marker", "'2'--tri_up marker", "'3'--tri_left marker", 
				"'4'--tri_right marker", "'s'--square marker", "'p'--pentagon marker", "'*'--star marker", "'h'--hexagon1 marker", 
				"'H'--hexagon2 marker", "'+'--plus marker", "'x'--x marker", "'D'--diamond marker", "'d'--thin_diamond marker", "'|'--vline marker", 
				"'_'--hline marker"]

markerstyleList = ['.', ',', 'o', 'v', '^', '<', '>', '1', '2', '3', '4', 's', 'p', '*', 'h', 'H', '+', 'x', 'D', 'd', '|', '_']

x = np.arange(5, 11, 1)
y = np.linspace(1, 1, 6)

ax.text(4, 23, "marker styles", **font_style)

for i, ms in enumerate(markerstyleList):
	ax.text(-0.5, i+0.5, msNameList[i], **font_style)
	ax.plot(x, (i+0.5)*y, marker=ms, **line_marker_style)

ax.set_xlim(-1, 11)
ax.set_ylim(0, 24)

ax.margins(0.3)
ax.set_xticks([])
ax.set_yticks([])

plt.show()