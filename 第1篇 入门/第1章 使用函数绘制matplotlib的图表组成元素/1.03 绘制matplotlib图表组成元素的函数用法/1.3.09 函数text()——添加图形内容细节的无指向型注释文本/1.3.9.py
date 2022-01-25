import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', dashes=[2, 1, 1, 1], lw=2, c="c", label='plot figure')

plt.legend(loc="lower left")

plt.text(3.20, 0.14, "y=sin(x)", size=18, color="b", fontdict={"family":"times"})	# 添加图形内容细节的无指向型注释文本

plt.xlim(0.0, 10)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.0, 1.0)
plt.locator_params(axis='y', nbins=5)

plt.show()