import matplotlib as mpl

# usage of package matplotlib
## method1 of setting attribution
mpl.rc("lines", linewidth=2, color='c', linestyle="--")		# 调用函数matplotlib.rc()

## method2 of setting atrribution
line = {"linewidth":2, "color":"c", "linestyle":"--"}
mpl.rc("lines", **line)