import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
import numpy as np


# 作用是内嵌画图，省略掉plt.show()这一步，直接显示图像 可以将matplotlib的图表直接嵌入到Notebook
# 之中，或者使用指定的界面库显示图表，它有一个参数指定matplotlib图表的显示方式。inline表示将图表嵌入到Notebook中
# 魔法命令都以%或者%%开头，以%开头的成为行命令，%%开头的称为单元命令。行命令只对命令所在的行有效，而
# 单元命令则必须出现在单元的第一行，对整个单元的代码进行处理。


def read_csv(path):
    data = pd.read_csv(path, header=None)
    data = np.array(data)
    return data


edges = read_csv('C:/Users/86131/Desktop/1.csv')  # 这里是数据集的位置
plt.rcParams['figure.figsize'] = (30, 30)
print(edges)

g = nx.DiGraph()  # 定义有向图，无向图是nx.Graph()
g.add_weighted_edges_from(edges)
weights = g.edges.data("weight")
# 生成节点位置序列
pos = nx.random_layout(g)
plt.rcParams['figure.figsize'] = (30, 30)
weights = nx.get_edge_attributes(g, "weight")
nx.draw_networkx(g, pos, node_size=5000)
nx.draw_networkx_edge_labels(g, pos, edge_labels=weights)
plt.axis('off')
plt.show()

pos = nx.shell_layout(g)
print(pos)

labels = {}
for node in g.nodes():
    labels[node] = node

plt.rcParams['figure.figsize'] = (30, 30)  # 设置画布大小
pos = {10: ([1, 4]),
       11: ([5, 5]), 12: ([5, -0.5]),
       60: ([-0.7, -0.5]), 63: ([4, -0.5]),
       30: ([-0.1, -0.5]), 23: ([-0.6, -0.7]),
       24: ([-0.4, -0.5]), 41: ([-0.6, -0.4]),
       43: ([-0.5, -0.2]), 21: ([-7, -0.4]),
       61: ([0.5, -0.6]), 64: ([0.4, -0.2]),
       40: ([0.2, -0.93087375]), 42: ([0.49999991, -0.86602545]),
       71: ([0.62349004, -0.78183132]), 20: ([0.73305202, -0.68017262]),
       22: ([0.82623881, -0.56331998]), 33: ([0.90096885, -0.43388376]),
       51: ([0.95557278, -0.29475528]), 32: ([0.98883086, -0.149042]),
       34: ([1.00000000e+00, 1.74845553e-07]), 62: ([0.9888308, 0.14904234]),
       85: ([0.95557278, 0.29475516]), 35: ([0.90096891, 0.43388364]),
       75: ([0.82623863, 0.56332028]), 31: ([0.73305178, 0.68017286]),
       73: ([0.62348974, 0.7818315]), 72: ([0.49999961, 0.86602563]),
       86: ([0.36534116, 0.93087369]), 36: ([0.22252069, 0.97492796]),
       47: ([0.07473042, 0.99720377]), 81: ([-0.07473014, 0.99720377]),
       87: ([-0.22252135, 0.97492784]), 49: ([-0.36534089, 0.93087381]),
       65: ([-0.50000018, 0.86602527]), 45: ([-0.62348956, 0.78183168]),
       70: ([-0.7330519, 0.68017268]), 74: ([-0.82623899, 0.56331974]),
       53: ([-0.90096879, 0.43388388]), 55: ([-0.95557284, 0.29475495]),
       46: ([-0.98883075, 0.14904262])}
nx.draw_networkx_nodes(g, pos, node_size=5000)  # 画节点
nx.draw_networkx_edges(g, pos, )  # 画边
nx.draw_networkx_labels(g, pos=pos, labels=labels, font_size=20)
# nx.draw_networkx_labels(g,pos,labels=labels)       # 画标签
nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, font_size=20)
plt.axis('off')  # 去掉坐标刻度
plt.show()