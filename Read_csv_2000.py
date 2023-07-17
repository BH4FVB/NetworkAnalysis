import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(threshold=np.inf)  # 设置print阈值为正无穷，不会省略输出内容

# 指定CSV文件路径
#csv_file_1995 = '1995_io95a294_94.CSV'
csv_file_2000 = '2000_kihon_seisan_32.csv'
#csv_file_2005 = '2005_io05a302_34.CSV'
# csv_file_2011 = '2011_kihon_seisan_190 - 2.CSV'
# csv_file_2015 = '2015_kihon_seisan_37.CSV'

#读取1995CSV文件
# with open(csv_file_1995, 'r') as file_1995:
#     reader = csv.reader(file_1995)
#     data_1995 = [[float(value) if value else 0.0 for value in row] for row in reader]
#读取2005CSV文件
with open(csv_file_2000, 'r') as file_2000:
    reader = csv.reader(file_2000)
    data_2000 = [[float(value) if value else 0.0 for value in row] for row in reader]

# #读取2011CSV文件
# with open(csv_file_2011, 'r') as file_2011:
#    reader = csv.reader(file_2011)
#    data_2011 = [[float(value) if value else 0.0 for value in row] for row in reader]
#
# # 读取2015CSV文件
# with open(csv_file_2015, 'r') as file_2015:
#     reader = csv.reader(file_2015)
#     data_2015 = [[float(value) if value else 0.0 for value in row] for row in reader]

# 转换为NumPy数组
# matrix_1995 = np.array(data_1995)
matrix_2000 = np.array(data_2000)
#matrix_2005 = np.array(data_2005)
# matrix_2011 = np.array(data_2011)
# matrix_2015 = np.array(data_2015)
# #检验
# print(data_1995)
# print(matrix_1995)
#
# print(data_2005)
# print(matrix_2005)
#
# print(data_2011)
# print(matrix_2011)

# print(data_2015)
# print(matrix_2015)

# 创建图
# G_1995 = nx.from_numpy_array(matrix_1995, create_using=nx.DiGraph)
G_2000 = nx.from_numpy_array(matrix_2000, create_using=nx.DiGraph)
#G_2005 = nx.from_numpy_array(matrix_2005, create_using=nx.DiGraph)
# G_2011 = nx.from_numpy_array(matrix_2011, create_using=nx.DiGraph)
# G_2015 = nx.from_numpy_array(matrix_2015, create_using=nx.DiGraph)
#检验
# adj_matrix = nx.to_numpy_array(G_1995)
# print(adj_matrix)
#
# adj_matrix = nx.to_numpy_array(G_2005)
# print(adj_matrix)
#
# adj_matrix = nx.to_numpy_array(G_2011)
# print(adj_matrix)

# adj_matrix = nx.to_numpy_array(G_2015)
# print(adj_matrix)

# 绘制网络图
# nx.draw(G_1995, with_labels=True, font_weight='bold')
nx.draw(G_2000, with_labels=True, font_weight='bold')
#nx.draw(G_2005, with_labels=True, font_weight='bold')
# nx.draw(G_2011, with_labels=True, font_weight='bold')
# nx.draw(G_2015, with_labels=True, font_weight='bold')
plt.show()

# 计算加权中心性指标
weighted_degree_centrality = dict()
for node in G_2000.nodes():
    weighted_degree = sum(G_2000[node][neighbor]['weight'] for neighbor in G_2000.neighbors(node))
    weighted_degree_centrality[node] = weighted_degree

# 将加权中心性指标写入CSV文件
with open('2000_weighted_centrality_metrics.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['节点名称', '加权度中心性'])

    for node, centrality in weighted_degree_centrality.items():
        writer.writerow([node, centrality])

print("CSV文件已成功创建。")