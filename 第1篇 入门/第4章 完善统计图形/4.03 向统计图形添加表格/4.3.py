# -*- coding:utf-8 -*-

import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams["font.sans-serif"] = ["SimHei"]
mpl.rcParams["axes.unicode_minus"] = False

labels = ("A难度水平", "B难度水平", "C难度水平", "D难度水平")

students = [0.35, 0.15, 0.20, 0.30]

explode = (0.1, 0.1, 0.1, 0.1)

colors = ["#377eb8", "#e41a1c", "#4daf4a", "#984ea3"]

# exploded pie chart
plt.pie(students, explode=explode, labels=labels, autopct="%1.1f%%", startangle=45, shadow=True, colors=colors)

plt.title("选择不同难度的测试试卷的学生占比")

# add table to pie figure
colLabels = ["A难度水平", "B难度水平", "C难度水平", "D难度水平"]
rowLabels = ["学生选择试卷人数"]
studentValues = [[350,150,200,300]]
colColors = ["#377eb8", "#e41a1c", "#4daf4a", "#984ea3"]

plt.table(cellText=studentValues, cellLoc="center", colWidths=[0.25]*4, colLabels=colLabels, colColours=colColors,
			 rowLabels=rowLabels, rowLoc="center", loc="bottom")
plt.show()