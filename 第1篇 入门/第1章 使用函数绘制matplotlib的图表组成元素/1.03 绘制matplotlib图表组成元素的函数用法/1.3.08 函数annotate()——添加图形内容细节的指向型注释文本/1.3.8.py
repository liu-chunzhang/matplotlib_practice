import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c="c", label='plot figure', dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")

plt.annotate("maximum", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+1.0, 0.8), weight="bold", color="b",
				arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b") )	# 添加内容细节的指向型注释文本，更多细节见下册4.3.5节

plt.xlim(0.0, 10)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.show()