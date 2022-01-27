import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 2000)
y = np.sin(x)

fig, ax = plt.subplots(1, 1)

ax.plot(x, y, ls="-", lw=2)

arrowprops = dict(arrowstyle="-|>", color="r")

ax.annotate("",(3*np.pi/2, np.sin(3*np.pi/2+0.05)),xytext=(np.pi/2, np.sin(np.pi/2)+0.05), color="r", arrowprops=arrowprops)	
																											# 省略文本内容只剩下箭头，箭头是正三角形的

ax.arrow(0.0, -0.4, np.pi/2, 1.2, head_width=0.05, head_length=0.1, fc='g', ec='y')			# 只绘制箭头，箭头不是正三角形的，黄边绿心的箭头

plt.xlim(0.0, 10.0)
plt.locator_params(axis='x', nbins=6)
plt.ylim(-1.5, 1.5)
plt.locator_params(axis='y', nbins=7)

plt.show()