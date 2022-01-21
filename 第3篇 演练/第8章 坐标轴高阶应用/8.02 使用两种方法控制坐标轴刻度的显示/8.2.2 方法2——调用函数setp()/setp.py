import matplotlib.pyplot as plt

line = plt.plot([1, 2, 3])
plt.setp(line, ls="--")
plt.show()