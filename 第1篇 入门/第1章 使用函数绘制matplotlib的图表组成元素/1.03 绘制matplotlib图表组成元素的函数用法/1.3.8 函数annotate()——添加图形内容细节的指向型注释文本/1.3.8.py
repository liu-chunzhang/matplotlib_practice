import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)

plt.plot(x, y, ls='-.', lw=2, c="c", label='plot figure', dashes=[2, 1, 1, 1])

plt.legend(loc="lower left")

plt.annotate("maximum", xy=(np.pi/2, 1.0), xytext=((np.pi/2)+1.0, 0.8), weight="bold", color="b",
				arrowprops=dict(arrowstyle="->", connectionstyle="arc3", color="b") )

plt.xlim(0.00, 10)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-1.0, 1.0)
plt.yticks(np.arange(-1.0, 1.1, 0.5))

plt.show()