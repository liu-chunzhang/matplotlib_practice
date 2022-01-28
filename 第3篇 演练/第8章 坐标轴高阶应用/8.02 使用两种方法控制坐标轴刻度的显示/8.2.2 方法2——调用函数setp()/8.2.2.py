import matplotlib.pyplot as plt

plt.rcParams["grid.linestyle"] = ":"

ax1 = plt.subplot(221)
ax1.set_xlim(0.0, 1.0)
ax1.set_ylim(0.0, 1.0)
ax1.locator_params(nbins=6)
plt.setp(ax1.get_xticklabels(), visible=True)
plt.setp(ax1.get_xticklines(), visible=True)
plt.grid(True, axis="x", ls=":")

ax2 = plt.subplot(222)
ax2.set_xlim(0.0, 1.0)
ax2.set_ylim(0.0, 1.0)
ax2.locator_params(nbins=6)
plt.setp(ax2.get_xticklabels(), visible=True)
plt.setp(ax2.get_xticklines(), visible=False)

plt.grid(True, axis="x")

ax3 = plt.subplot(223)
ax3.set_xlim(0.0, 1.0)
ax3.set_ylim(0.0, 1.0)
ax3.locator_params(nbins=6)
plt.setp(ax3.get_xticklabels(), visible=False)
plt.setp(ax3.get_xticklines(), visible=True)
plt.grid(True, axis="x")

ax4 = plt.subplot(224)
ax4.set_xlim(0.0, 1.0)
ax4.set_ylim(0.0, 1.0)
ax4.locator_params(nbins=6)
plt.setp(ax4.get_xticklabels(), visible=False)
plt.setp(ax4.get_xticklines(), visible=False)
plt.grid(True, axis="x")

plt.show()