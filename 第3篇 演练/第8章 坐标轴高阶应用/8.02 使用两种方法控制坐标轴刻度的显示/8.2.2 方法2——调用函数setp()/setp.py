import matplotlib.pyplot as plt

line, = plt.plot([1, 2, 3])		# 此处逗号不可不要，表明line是Line2D对象
plt.setp(line, ls="--")
plt.show()