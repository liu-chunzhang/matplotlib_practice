import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 3, figsize=(8, 5.6))

# subplot(231)
colors = ["#8dd3c7", "#ffffb3", "#bebada"]

ax[0, 0].bar([1, 2, 3], [0.6, 0.2, 0.8], color=colors, width=0.5, hatch="///", align="center", edgecolor='k')	# 这里补加edgecolor='k'
ax[0, 0].errorbar([1, 2, 3], [0.6, 0.2, 0.8], yerr=0.1, capsize=0, ecolor="#377eb8", fmt="o:")

ax[0, 0].set_ylim(0, 1.0)
ax[0, 0].locator_params(axis='y', nbins=6)

# subplot(232)
ax[0, 1].errorbar([1, 2, 3], [20, 30, 36], xerr=2, ecolor="#4daf4a", elinewidth=2, fmt="s", label="ETN")
ax[0, 1].legend(loc=3, fancybox=True, shadow=True, fontsize=10, borderaxespad=0.4)	
																# fancybox为启动圆角箱形；borderaxespad为轴与图例之间的填充，以字体大小为单位，默认值为0.5

ax[0, 1].set_xlim(-2, 6)
ax[0, 1].locator_params(axis='x', nbins=9)
ax[0, 1].set_ylim(10, 40)
ax[0, 1].locator_params(axis='y', nbins=7)
ax[0, 1].grid(ls=":", lw=1, color="grey", alpha=0.5)

# subplot(233)
x3 = np.arange(1, 10, 0.5)
y3 = np.cos(x3)

ax[0, 2].stem(x3, y3, basefmt="r-", linefmt="b-.", markerfmt="bo", label="life signal")
ax[0, 2].legend(loc=2, fontsize=8, frameon=False, borderpad=0.0, borderaxespad=0.6)
ax[0, 2].set_xlim(0, 11)
ax[0, 2].locator_params(axis='x', nbins=6)
ax[0, 2].set_ylim(-1.1, 1.1)
ax[0, 2].locator_params(axis='y', nbins=5)

# subplot(234)
x4 = np.linspace(0, 2*np.pi, 500)
y4 = np.cos(x4)*np.exp(-x4)
x4_1 = np.linspace(0, 2*np.pi, 1000)
y4_1 = np.sin(2*x4_1)

line1, line2, = ax[1, 0].plot(x4, y4, "k--", x4_1, y4_1, "r-", lw=2)
ax[1, 0].legend((line1, line2), ("energy", "patience"), loc="upper center", fontsize=8, ncol=2, framealpha=0.3, mode="expand", 
					columnspacing=2, borderpad=0.1)

ax[1, 0].set_xlim(0, 2*np.pi)
ax[1, 0].locator_params(axis='x', nbins=7)
ax[1, 0].set_ylim(-2.0, 2.0)
ax[1, 0].locator_params(axis='y', nbins=9)

# subplot(235)
x5 = np.random.rand(100)
ax[1, 1].boxplot(x5, vert=False, showmeans=True, meanprops=dict(color="g"))

ax[1, 1].set_xlim(-1.1, 1.1)
ax[1, 1].locator_params(axis='x', nbins=5)
ax[1, 1].set_yticks([])
ax[1, 1].set_ylabel("Micro SD Card")
ax[1, 1].text(-1.0, 1.2, "net weight", fontsize=20, style="italic", weight="black", family="monospace")

# subplot(236)
mu = 0.0
sigma = 1.0

x6 = np.random.randn(10000)
n, bins, patches = ax[1, 2].hist(x6, bins=30, histtype="stepfilled", cumulative=True, density=True, color="cornflowerblue", label="Test")
																				# 从matplotlib3.0.2版以后，normed关键字由density代替！
y = (1 / (np.sqrt(2*np.pi) * sigma) * np.exp(-0.5 * (1 / sigma * (bins-mu))**2 ))
y = y.cumsum()
y /= y[-1]

ax[1, 2].plot(bins, y, "r--", linewidth=1.5, label="Theory")

ax[1, 2].set_xlim(-4, 4)
ax[1, 2].locator_params(axis='x', nbins=9)
ax[1, 2].set_ylim(0.0, 1.1)
ax[1, 2].locator_params(axis='y', nbins=6)

ax[1, 2].grid(ls=":", lw=1, color="grey", alpha=0.5)
ax[1, 2].legend(loc="upper left", fontsize=8, shadow=True, fancybox=True, framealpha=0.8)

# adjust subplots() layout
plt.subplots_adjust()	# 此函数可见6.3.2节末尾提及

plt.show()