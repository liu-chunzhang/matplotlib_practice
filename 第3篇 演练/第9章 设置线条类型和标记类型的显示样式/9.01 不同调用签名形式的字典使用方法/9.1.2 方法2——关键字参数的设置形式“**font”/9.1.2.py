import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)

font = {"family":"serif", "color":"navy", "weight":"black", "size":16}

x = np.linspace(0.0, 2*np.pi, 500)
y = np.cos(2*x)*np.sin(2*x)

ax.plot(x, y, color="k", ls="-", lw=2)

ax.set_title("keyword mode is '**font'", **font)
ax.text(1.5, 0.52, r"$y=\cos(2t)*\sin(2t)$", **font)
ax.set_xlabel("time (h)", **font)
ax.set_ylabel(r"$\Delta$height (cm)", **font)

ax.set_xlim(0.0, 2*np.pi)
ax.set_ylim(-0.6, 0.6)

plt.show()