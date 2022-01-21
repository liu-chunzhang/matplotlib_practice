import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.0, 10, 40)
y = np.random.randn(40)

plt.plot(x, y, ls="-", lw=2, marker="o", ms=20, mfc="orange", alpha=0.6)

plt.grid(ls=":", color="gray", alpha=0.5)

plt.text(1, 2, "Matplotlib", fontsize=50, color="gray", alpha=0.5)

plt.xlim(0.0, 10.0)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-3.0, 3.0)
plt.locator_params(axis="y", nbins=8)

plt.show()