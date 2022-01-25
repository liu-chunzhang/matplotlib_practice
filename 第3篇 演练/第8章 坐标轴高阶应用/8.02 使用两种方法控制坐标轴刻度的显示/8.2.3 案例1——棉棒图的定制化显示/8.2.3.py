import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.5, 2*np.pi, 20)
y = np.random.randn(20)

markerline, stemlines, baseline = plt.stem(x, y)

plt.setp(markerline, color="chartreuse", marker="D")
plt.setp(stemlines, ls="-.")
stemlines.set_linewidth(4)
baseline.set_linewidth(2)

plt.show()