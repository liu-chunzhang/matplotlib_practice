import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

# viewing family options
families = ["serif", "sans-serif", "fantasy", "monospace"]

ax.text(-1, 1, "family", fontsize=18, horizontalalignment='center')

pi = np.arange(0.9, 0.0, -0.1)

for i, family in enumerate(families):
	ax.text(-1, pi[i], family, family=family, horizontalalignment='center')

# viewing size options
sizes = ["xx-small", "x-small", "small", "medium", "large", "x-large", "xx-large"]

ax.text(-0.5, 1, "size", fontsize=18, horizontalalignment='center')

for i, size in enumerate(sizes):
	ax.text(-0.5, pi[i], size, size=size, horizontalalignment='center')

# viewing style options
styles = ["normal", "italic", "oblique"]

ax.text(0.0, 1.0, "style", fontsize=18, horizontalalignment='center')

for i, style in enumerate(styles):
	ax.text(0.0, pi[i], style, family="sans-serif", style=style, horizontalalignment='center')

# viewing variant options
variants = ["normal", "small-caps"]

ax.text(0.5, 1.0, "variant", fontsize=18, horizontalalignment='center')

for i, variant in enumerate(variants):
	ax.text(0.5, pi[i], variant, family="serif", variant=variant, horizontalalignment='center')

# viewing weight options
variants = ["light", "normal", "semibold", "bold", "black"]

ax.text(1.0, 1.0, "weight", fontsize=18, horizontalalignment='center')

for i, weight in enumerate(variants):
	ax.text(1.0, pi[i], weight, weight=weight, family="serif", horizontalalignment='center')	# 此处有可能因为缺少字体粗体而无法显示出区别！

#ax.text()

ax.axis([-1.5, 1.5, 0.1, 1.1])
ax.set_xticks([])
ax.set_yticks([])

plt.show()