import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

font = {"family":"serif", "color":"navy", "weight":"black", "size":16, "math_fontfamily":"cm"}

x = np.linspace(0.0, 2*np.pi, 500)
y = np.cos(2*x)*np.sin(2*x)

ax.plot(x, y, color="k", ls="-", lw=2)

ax.set_xlim(0.0, 2*np.pi)
ax.locator_params(axis="x", nbins=7)
ax.set_xlabel(r"$\mathit{t} \mathrm{(h)}$", **font)				# 利用关键字设置形式**font
ax.set_ylim(-0.6, 0.6)
ax.locator_params(axis="y", nbins=7)
ax.set_ylabel(r"$\Delta\mathit{h} \mathrm{(cm)}$", **font)

ax.set_title("keyword mode is '**font'", **font)
ax.text(1.5, 0.52, r"$y=\cos(2t)\sin(2t)$", **font)

plt.show()