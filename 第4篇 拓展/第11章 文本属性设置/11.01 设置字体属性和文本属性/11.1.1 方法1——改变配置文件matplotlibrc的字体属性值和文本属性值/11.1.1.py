import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.bf"] = "bold"

plt.axes([0.1, 0.1, 0.8, 0.8], frameon=True, facecolor="y", aspect="equal")
plt.plot(2+np.arange(3), [0, 1, 0], ls=":", linewidth=8, dashes=[1, 1])
plt.title("Line Chart", font="serif")

# Add text in string 'FONT' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, 0.8, "FONT", weight="bold", color="blue")

plt.xlim(2.0, 4.0)
plt.xticks(weight="bold")
plt.locator_params(axis="x", tight=True, nbins=5)
plt.ylim(0.0, 1.0)
plt.yticks(weight="bold")

plt.show()