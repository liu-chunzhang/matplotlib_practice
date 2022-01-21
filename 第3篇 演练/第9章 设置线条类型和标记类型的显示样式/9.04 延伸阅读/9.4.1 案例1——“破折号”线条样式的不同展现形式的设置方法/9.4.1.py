import matplotlib.pyplot as plt
import numpy as np

font_style = dict(family="serif", weight="black", size=12)
line_marker_style1 = dict(linestyle="--", linewidth=2, color="maroon", markersize=10)
line_marker_style2 = dict(linestyle="--", linewidth=2, color="cornflowerblue", markersize=10)
line_marker_style3 = dict(linestyle="--", linewidth=2, color="turquoise", markersize=10)

fig = plt.figure()
ax = fig.add_subplot(111, facecolor="honeydew")

x = np.linspace(0, 2*np.pi, 500)
y = np.sin(x)*np.cos(x)

ax.plot(x, y, dashes=[10, 2], label="dashes=[10, 2]", **line_marker_style1)
ax.plot(x, y+0.2, dashes=[3, 1], label="dashes=[3, 1]", **line_marker_style2)
ax.plot(x, y+0.4, dashes=[2, 2, 8, 2], label="dashes=[2, 2, 8, 2]", **line_marker_style3)

ax.axis([0, 2*np.pi, -0.7, 1.2])

ax.legend(ncol=3, bbox_to_anchor=(0.00, 0.95, 1.0, 0.05), mode="expand", fancybox=True, shadow=True, prop=font_style)

plt.show()