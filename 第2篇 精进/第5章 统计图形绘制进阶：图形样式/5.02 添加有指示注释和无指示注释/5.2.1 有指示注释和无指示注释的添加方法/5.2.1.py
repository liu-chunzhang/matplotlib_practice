import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# set subplot
ax.plot(x, y, c="b", ls="--", lw=2)

# Annotate the point xy with text with the "arrowstyle"
ax.annotate("maximum", xy=(np.pi/2, 1.0), xycoords="data", xytext=((np.pi/2)+0.15, 0.8), textcoords="data", weight="bold", color="r", size=15, 
				arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="r"))	# 有指示注解，此处额外添加了参数size=15,更多格式见下册第4章

# Annotate the whole points with text without the "arrowstyle"
# Add text to the axes
ax.text(2.8, 0.45, r"$y=\sin(x)$", fontsize=20, color="b", bbox=dict(facecolor='y', alpha=0.5), fontdict={"math_fontfamily":"cm"})

ax.set_xlim(0.5, 3.5)
ax.locator_params(axis='x', nbins=7)
ax.set_ylim(-0.4, 1.0)
ax.locator_params(axis='y', nbins=8)

plt.show()