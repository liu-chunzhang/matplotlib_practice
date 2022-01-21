import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.05, 10, 1000)
y = np.sin(x)
plt.plot(x, y, ls='-.', lw=2, c="c", label='plot figure')

plt.legend(loc="lower left")

plt.text(3.20, 0.14, r"$y=\sin(x)$", size=18, color="b")	# 使用了tex公式体后，weight好像没用了。

plt.xlim(0.00, 10)
plt.xticks(np.arange(0.0, 10.1, 2.0))
plt.ylim(-1.0, 1.0)
plt.yticks(np.arange(-1.0, 1.1, 0.5))

plt.show()