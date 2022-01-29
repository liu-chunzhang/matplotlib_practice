import matplotlib.pyplot as plt
import numpy as np

ax = plt.axes([0.1, 0.1, 0.8, 0.8], frameon=True, facecolor="y", aspect="equal")
# line properties in change
plt.plot(2+np.arange(3), [0, 1, 0], linewidth=8.0, linestyle="--", dashes=[0.75, 0.75])
plt.title("Line Chart", color='red', family="New Century Schoolbook", style="normal", variant="small-caps", weight="black", size=18)

# Add text in string 'FONT' to axis at location 'x', 'y', data coordinates
# font properties and text properties in change
plt.text(2.25, 0.8, "FONT", weight="bold", color="blue", fontdict={"family": "New Century Schoolbook", "style":"normal", 
			"variant":"small-caps", "weight":"black", "size":28})

plt.xlim(2.0, 4.0)
plt.locator_params(axis="x", nbins=5)
plt.xticks(weight="bold")

plt.ylim(0.0, 1.0)
plt.locator_params(axis="y", nbins=6)
plt.yticks(weight="bold")

ax.spines["top"].set_color("b")
ax.spines["right"].set_color("b")
ax.spines["left"].set_color("b")
ax.spines["bottom"].set_color("b")

plt.show()