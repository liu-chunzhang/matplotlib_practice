import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

ax = plt.axes([0.1, 0.1, 0.8, 0.8], frameon=True, facecolor="y", aspect="equal")
plt.plot(2+np.arange(3), [0, 1, 0], ls="--", linewidth=8, dashes=[0.75, 0.75])
plt.title("Line Chart", font="serif", size=15, color='b')

# Add text in string 'FONT' to axis at location 'x', 'y', data
# coordinates
plt.text(2.25, 0.8, "FONT", color="blue", size=20, family="stix")

plt.xlim(2.0, 4.0)
xticks = plt.xticks(weight="bold", size=12, family="New Century Schoolbook", style="normal")
plt.locator_params(axis="x", nbins=5)
plt.ylim(0.0, 1.0)
plt.yticks(weight="bold", size=12, family="New Century Schoolbook", style="normal")
plt.locator_params(axis='y', nbins=6)

ax.spines["top"].set_color("b")
ax.spines["right"].set_color("b")
ax.spines["left"].set_color("b")
ax.spines["bottom"].set_color("b")

plt.show()