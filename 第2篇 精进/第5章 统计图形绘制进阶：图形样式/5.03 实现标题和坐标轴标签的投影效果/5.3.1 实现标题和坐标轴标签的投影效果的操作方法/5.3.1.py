import matplotlib.pyplot as plt
import matplotlib.patheffects as pes
import numpy as np

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fontsize = 23

# plot a sin(x) func
plt.plot(x, y, ls="--", lw=2)

# set text contents
title, xaxis_label, yaxis_label = "$y=\sin({x})$", "$x\_axis$", "$y\_axis$"

# get text instance
title_text_obj = plt.title(title, fontsize=fontsize, va="bottom", fontdict=dict(math_fontfamily="cm"))
xaxis_label_text_obj = plt.xlabel(xaxis_label, fontsize=fontsize-3, alpha=1.0, fontdict=dict(math_fontfamily="cm"))
yaxis_label_text_obj = plt.ylabel(yaxis_label, fontsize=fontsize-3, alpha=1.0, fontdict=dict(math_fontfamily="cm"))

# set shadow
title_text_obj.set_path_effects([pes.withSimplePatchShadow()])
pe = pes.withSimplePatchShadow(offset=(1, -1), shadow_rgbFace="r", alpha=0.3)	# 引入一个新类patheffects（路径效果）
xaxis_label_text_obj.set_path_effects([pe])
yaxis_label_text_obj.set_path_effects([pe])

plt.xlim(0.5, 3.5)
plt.locator_params(axis='x', nbins=7)
plt.ylim(-0.4, 1.0)
plt.locator_params(axis='y', nbins=8)

plt.show()