import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

font = {"family":"monospace", "color":"maroon", "weight":"bold", "size":16, "math_fontfamily":"cm"}

x = np.linspace(0.0, 2*np.pi, 500)
y = np.cos(x)*np.sin(x)

ax.plot(x, y, color="k", ls="-", lw=2)

ax.set_title("keyword mode is 'fontdict=font'", fontdict=font)					# 调用关键字设置形式fontdict=font
ax.text(1.5, 0.4, r"$\Delta h=\cos(t)\sin(t)$", fontdict=font, fontsize=12)
ax.set_xlabel(r"$\mathit{t} \mathrm{(h)}$", fontdict=font)
ax.set_ylabel(r"$\Delta\mathit{h} \mathrm{(cm)}$", fontdict=font)

ax.set_xlim(0, 2*np.pi)
ax.locator_params(axis="x", nbins=7)
ax.set_ylim(-0.6, 0.6)
ax.locator_params(axis='y', nbins=7)

plt.show()