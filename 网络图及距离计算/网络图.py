# encoding=utf-8

import networkx as nx
import matplotlib.pyplot as plt


g = nx.Graph()
g.add_nodes_from(['A', 'B', 'C', 'D','E', 'F'])
#
g.add_weighted_edges_from([('A','B',3.0),('A','D',5.0),('C', 'D',8.0),('D','E',12.0),('A', 'C',13.0),('A', 'E',188.0),('B','C',22.0),('B', 'D',34.0),('B', 'E',32.0),('C', 'E',38.0),('A','F',43.0),('B', 'F',45.0),('C', 'F',44.0),('D','F',55.0),('E', 'F',64.0)])



a = [1,1,1,1]

b = [1,2,1,1]
c = [111,111,1111,122,122,122,134,1234,12424,111,123,123,2,2,2]
#g.add_edges_from(zip(b,a))


colors = ['red', 'green', 'blue', 'yellow']
#g.add_edges_from(zip(b,c))
nx.draw(g,with_labels=True, node_size=600, node_color = 'white',pos = nx.spectral_layout(g))
plt.show()



# circular_layout：节点在一个圆环上均匀分布
# random_layout：节点随机分布
# shell_layout：节点在同心圆上分布
# spring_layout： 用Fruchterman-Reingold算法排列节点（这个算法我不了解，样子类似多中心放射状）
# spectral_layout：根据图的拉普拉斯特征向量排列节点？我也不是太明白
#最后两个靠谱


#
# import networkx as nx
# import matplotlib.pyplot as plt
#
# colors = ['red', 'green', 'blue', 'yellow']
# #有向图
# DG = nx.DiGraph()
# #一次性添加多节点，输入的格式为列表
# DG.add_nodes_from(['A', 'B', 'C', 'D'])
# #添加边，数据格式为列表
# DG.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('D','A')])
# #作图，设置节点名显示,节点大小，节点颜色
# nx.draw(DG,with_labels=True, node_size=900, node_color = colors)
# plt.show()