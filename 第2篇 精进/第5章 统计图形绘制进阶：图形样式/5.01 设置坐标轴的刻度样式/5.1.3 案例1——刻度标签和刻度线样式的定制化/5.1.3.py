import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["ytick.color"] = 'lightgreen'

fig = plt.figure(facecolor=(1.0, 1.0, 0.9412))

ax = fig.add_axes([0.1, 0.4, 0.5, 0.5])

for ticklabel in ax.xaxis.get_ticklabels():
	ticklabel.set_color("slateblue")
	ticklabel.set_fontsize(18)
	ticklabel.set_rotation(30)

for tickline in ax.yaxis.get_ticklines():
	tickline.set_color("red")				# has no affect on plot()!
	tickline.set_markersize(20)
	tickline.set_markeredgewidth(2)

plt.show()