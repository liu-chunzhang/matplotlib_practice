import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["mathtext.fontset"] = "stix"
plt.rcParams["mathtext.bf"] = "bold"

# line properties in change
plt.rcParams["lines.linewidth"] = 8.0
plt.rcParams["lines.linestyle"] = "--"

# font properties in change
plt.rcParams["font.family"] = "serif"
#plt.rcParams["font.serif"] = "New Century Schoolbook"
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.variant"] = "small-caps"
plt.rcParams["font.weight"] = "black"
plt.rcParams["font.size"] = 12.0

# text properties in change
plt.rcParams["text.color"] = "blue"

plt.axes([0.1, 0.1, 0.8, 0.8], frameon=True, facecolor="y", aspect="equal")
plt.plot(2+np.arange(3), [0, 1, 0], dashes=[1, 1])
plt.title("Line Chart", weight="normal")

# Add text in string 'FONT' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, 0.8, "FONT")

plt.xlim(2.0, 4.0)
#plt.xticks(weight="bold")
plt.locator_params(axis="x", tight=True, nbins=5)
plt.ylim(0.0, 1.0)
#plt.yticks(weight="bold")

plt.show()