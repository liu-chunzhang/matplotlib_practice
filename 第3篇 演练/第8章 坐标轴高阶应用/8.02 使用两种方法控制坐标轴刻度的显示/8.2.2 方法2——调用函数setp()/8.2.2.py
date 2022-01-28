import matplotlib.pyplot as plt

plt.rcParams["grid.linestyle"] = ":"

ax1 = plt.subplot(221)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.setp(ax1.get_xticklines(), visible=True)
plt.grid(True, axis="x", ls=":")

ax2 = plt.subplot(222)
plt.setp(ax2.get_xticklabels(), visible=True)
plt.setp(ax2.get_xticklines(), visible=False)

plt.grid(True, axis="x")

ax3 = plt.subplot(223)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklines(), visible=True)
plt.grid(True, axis="x")

ax4 = plt.subplot(224)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_xticklines(), visible=False)
plt.grid(True, axis="x")

plt.show()