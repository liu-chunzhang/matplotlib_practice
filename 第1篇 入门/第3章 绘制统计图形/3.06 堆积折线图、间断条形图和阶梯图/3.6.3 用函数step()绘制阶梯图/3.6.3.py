import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 10)
y = np.sin(x)

plt.step(x, y, color="#8dd3c7", where="post", lw=2)	# 绘制阶梯图

plt.xlim(0, 11)
plt.xticks(np.arange(1, 11, 1))
plt.ylim(-1.2, 1.2)
plt.yticks(np.arange(-1.0, 1.1, 0.5))

plt.show()