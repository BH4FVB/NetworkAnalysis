import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd
np.set_printoptions(threshold=np.inf)  # 设置print阈值为正无穷，不会省略输出内容

# 指定CSV文件路径
csv_file_2011 = '2011_31.csv'

#读取2011CSV文件
with open(csv_file_2011, 'r') as file_2011:
    reader = csv.reader(file_2011)
    data_2011 = [[float(value) if value else 0.0 for value in row] for row in reader]
#print(data_2011)
# 转换为NumPy数组
matrix_2011 = np.array(data_2011)
#print(matrix_2011)


# 创建无向图
G_2011 = nx.from_numpy_array(matrix_2011, create_using=nx.Graph)
#检验
adj_matrix = nx.to_numpy_array(G_2011)
print(adj_matrix)
# 指定CSV文件路径
csv_file = 'adjacency_matrix_2011.csv'

# 写入CSV文件
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(adj_matrix)

print("CSV文件已成功创建。")

# 绘制网络图
nx.draw(G_2011, with_labels=True, font_weight='bold')
plt.show()

# 计算权重接近中心性
weighted_closeness_centrality = nx.closeness_centrality(G_2011, distance='weight')

# 计算权重特征向量中心性
weighted_eigenvector_centrality = nx.eigenvector_centrality_numpy(G_2011, weight='weight')

# 计算权重度中心性
weighted_degree_centrality = dict(G_2011.degree(weight='weight'))

# 计算权重PageRank中心性
weighted_pagerank_centrality = nx.pagerank(G_2011, weight='weight')

# 将中心性指标保存到CSV文件
csv_file_path = '2011_centrality_scores.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Node', 'Weighted Closeness Centrality', 'Weighted Eigenvector Centrality', 'Weighted Degree Centrality', 'Weighted PageRank Centrality'])
    for node in G_2011.nodes:
        writer.writerow([node, weighted_closeness_centrality[node], weighted_eigenvector_centrality[node], weighted_degree_centrality[node], weighted_pagerank_centrality[node]])

#创建最小生成树
mst_2011 = nx.minimum_spanning_tree(G_2011)
# 绘制网络图
nx.draw(mst_2011, with_labels=True, font_weight='bold')
plt.show()

# 获取邻接矩阵
adj_matrix = nx.adjacency_matrix(mst_2011)

# 将邻接矩阵转换为 DataFrame
df = pd.DataFrame(adj_matrix.toarray())

# 保存为 CSV 文件
df.to_csv("2011_mst_adjacency_matrix.csv", index=False)
