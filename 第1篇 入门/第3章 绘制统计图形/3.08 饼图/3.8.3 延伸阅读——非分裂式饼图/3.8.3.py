# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

labels = ("A难度水平", "B难度水平", "C难度水平", "D难度水平")
students = [0.35, 0.15, 0.20, 0.30]

colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
explode = (0.1, 0.1, 0.1, 0.1)

# exploded pie chart
plt.pie(students, labels=labels, autopct="%3.1f%%", startangle=45, pctdistance=0.7, labeldistance=1.1, colors=colors)

plt.title("选择不同难度的测试试卷的学生占比")

plt.show()