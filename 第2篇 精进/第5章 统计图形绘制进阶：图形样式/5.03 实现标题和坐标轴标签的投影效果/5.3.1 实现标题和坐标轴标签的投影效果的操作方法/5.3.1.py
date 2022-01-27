import matplotlib.pyplot as plt
import matplotlib.patheffects as pes
import numpy as np

x = np.linspace(0.5, 3.5, 100)
y = np.sin(x)

fontsize = 23

# plot a sin(x) func
plt.plot(x, y, ls="--", lw=2)

# set text contents
title = "$y=\sin({x})$"
xaxis_label = "$x\_axis$"
yaxis_label = "$y\_axis$"

# get text instance
title_text_obj = plt.title(title, fontsize=fontsize, va="bottom")
xaxis_label_text_obj = plt.xlabel(xaxis_label, fontsize=fontsize-3, alpha=1.0)
yaxis_label_text_obj = plt.ylabel(yaxis_label, fontsize=fontsize-3, alpha=1.0)

# set shadow
title_text_obj.set_path_effects([pes.withSimplePatchShadow()])
pe = pes.withSimplePatchShadow(offset=(1, -1), shadow_rgbFace="r", alpha=0.3)
xaxis_label_text_obj.set_path_effects([pe])
yaxis_label_text_obj.set_path_effects([pe])

plt.xlim(0.5, 3.5)
plt.ylim(-1.0, 1.0)

plt.show()