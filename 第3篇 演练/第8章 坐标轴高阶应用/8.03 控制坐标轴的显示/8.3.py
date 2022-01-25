import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.sin(x)

ax1 = plt.subplot(221)

ax1.spines["right"].set_color("none")
ax1.spines["top"].set_color("none")
ax1.set_xlim(-2*np.pi, 2*np.pi)
ax1.set_ylim(-1.0, 1.0)
plt.title(r"$a$")
plt.scatter(x, y, marker="+", color="b")

ax2 = plt.subplot(222)

ax2.spines["right"].set_color("none")
ax2.spines["top"].set_color("none")
ax2.xaxis.set_ticks_position("bottom")
ax2.set_xlim(-2*np.pi, 2*np.pi)
ax2.set_ylim(-1.0, 1.0)
plt.title(r"$b$")
plt.scatter(x, y, marker="+", color="g")

ax3 = plt.subplot(223)

ax3.spines["right"].set_color("none")
ax3.spines["top"].set_color("none")
ax3.yaxis.set_ticks_position("left")
ax3.set_xlim(-2*np.pi, 2*np.pi)
ax3.set_ylim(-1.0, 1.0)
plt.title(r"$c$")
plt.scatter(x, y, marker="+", color="b")

ax4 = plt.subplot(224)

ax4.spines["right"].set_color("none")
ax4.spines["top"].set_color("none")
ax4.xaxis.set_ticks_position("bottom")
ax4.yaxis.set_ticks_position("left")
ax4.set_xlim(-2*np.pi, 2*np.pi)
ax4.set_ylim(-1.0, 1.0)
plt.title(r"$d$")
plt.scatter(x, y, marker="+", color="b")

plt.show()