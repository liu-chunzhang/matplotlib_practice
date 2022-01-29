import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import MultipleLocator

# ColorBrewer Diverging: RdYlBu
hexHtml = ["#d73027", "#f46d43", "#fdae61", "#frr090", "#ffffbf", "#e0f3f8", "#abd9e9", "#74add1", "#4575b4"]
sample = 10000

fig, ax = plt.subplots(1, 1, figsize=(8, 5.6))

for j in range(len(hexHtml)):
	y = np.random.normal(0, 0.1, size=sample).cumsum()
	x = np.arange(sample)
	ax.scatter(x, y, label=f"{j}", cmap=hexHtml[j], ls="-", linewidth=0.2, marker=".")	# 此处可以用f表达式

ax.set_xlim(-2000, 12000)
ax.locator_params(axis='x', nbins=7)
ax.yaxis.set_major_locator(MultipleLocator(5))
ax.legend(loc=1)

plt.show()