# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

from matplotlib.sankey import Sankey

mpl.rcParams["font.serif"] = ["Times New Roman"]
mpl.rcParams["axes.unicode_minus"] = False

flows = [0.2, 0.1, 0.4, 0.3, -0.6, -0.05, -0.15, -0.2]
labels = ["", "", "", "", "family", "trip", "education", "sport"]
orientations = [1, 1, 0, -1, 1, -1, 1, 0]

sankey = Sankey()

sankey.add(flows=flows, labels=labels, orientations=orientations, color="c", fc="lightgreen", patchlabel="Life Cost", alpha=0.7)

diagrams = sankey.finish()
diagrams[0].texts[4].set_color("r")
diagrams[0].texts[4].set_weight("bold")
diagrams[0].text.set_fontsize(20)
diagrams[0].text.set_fontweight("light")

plt.title("日常生活的成本开支的流量图", family="FangSong")

plt.show()