import matplotlib.pyplot as plt

ax1 = plt.subplot(121)
ax1.set_xticks(range(0, 251, 50))
plt.grid(True, axis="x")

ax2 = plt.subplot(122)
ax2.set_xticks([])
plt.grid(True, axis="x")

plt.show()