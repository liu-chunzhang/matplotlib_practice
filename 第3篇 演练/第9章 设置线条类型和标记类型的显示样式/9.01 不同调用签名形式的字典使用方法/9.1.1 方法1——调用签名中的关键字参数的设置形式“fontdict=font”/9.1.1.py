import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

font = {"family":"monospace", "color":"maroon", "weight":"bold", "size":16}

x = np.linspace(0.0, 2*np.pi, 500)
y = np.cos(x)*np.sin(x)

ax.plot(x, y, color="k", ls="-", lw=2)

ax.set_title("keyword mode is 'fontdict=font'", fontdict=font)
ax.text(1.5, 0.4, r"$\Delta h=\cos(t)\sin(t)$", fontdict=font)
ax.set_xlabel("time (h)", fontdict=font)
ax.set_ylabel(r"$\Delta$height (cm)", fontdict=font)

ax.set_xlim(0, 2*np.pi)

ax.set_ylim(-0.6, 0.6)

plt.show()