import scipy.misc
import matplotlib as mpl
import matplotlib.pyplot as plt

ascent = scipy.misc.ascent()

# display an image on the axes
plt.imshow(ascent, cmap=mpl.cm.gray)

# add colorbar to a plot
plt.colorbar(ticks=range(0, 241, 30))

# show the plot
plt.show()