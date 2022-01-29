import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

barSlices = 12

theta = np.linspace(0.0, 2*np.pi, barSlices, endpoint=False)
radii = 30*np.random.rand(barSlices)
width = np.pi/4*np.random.rand(barSlices)

fig = plt.figure()
ax = fig.add_subplot(polar=True)

bars = ax.bar(theta, radii, width=width, bottom=0.0, edgecolor='k')

for r, bar in zip(radii, bars):
	bar.set_facecolor(mpl.cm.Accent(r/30))
	bar.set_alpha(r/30)

ax.set_rlim(0, 30)
ax.set_rticks(np.arange(0, 30.1, 5))
plt.grid(ls="-", dashes=[2, 2])

plt.show()