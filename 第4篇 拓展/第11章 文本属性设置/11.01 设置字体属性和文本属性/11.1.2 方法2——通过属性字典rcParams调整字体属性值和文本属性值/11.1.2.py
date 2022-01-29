import matplotlib.pyplot as plt
import numpy as np

# line properties in change
plt.rcParams["lines.linewidth"] = 8.0
plt.rcParams["lines.linestyle"] = "--"

# font properties in change
plt.rcParams["font.family"] = "serif"
plt.rcParams["font.serif"] = "New Century Schoolbook"
plt.rcParams["font.style"] = "normal"
plt.rcParams["font.variant"] = "small-caps"
plt.rcParams["font.weight"] = "black"
plt.rcParams["font.size"] = 12.0

# text properties in change
plt.rcParams["text.color"] = "blue"

ax = plt.axes([0.1, 0.1, 0.8, 0.8], frameon=True, facecolor="y", aspect="equal")
plt.plot(2+np.arange(3), [0, 1, 0], dashes=[0.75, 0.75])
plt.title("Line Chart", weight="normal")

# Add text in string 'FONT' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, 0.8, "FONT", weight="black")

plt.xlim(2.0, 4.0)
plt.xticks(weight="bold", size=12)
plt.locator_params(axis="x", nbins=5)
plt.ylim(0.0, 1.0)
plt.yticks(weight="bold", size=12)
plt.locator_params(axis="y", nbins=6)

ax.spines["top"].set_color("b")
ax.spines["right"].set_color("b")
ax.spines["left"].set_color("b")
ax.spines["bottom"].set_color("b")

plt.show()