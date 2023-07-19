import csv
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc
import pandas as pd
np.set_printoptions(threshold=np.inf)  # 设置print阈值为正无穷，不会省略输出内容

# 指定CSV文件路径
csv_file_1995 = '1995_32.csv'

#读取1995CSV文件
with open(csv_file_1995, 'r') as file_1995:
    reader = csv.reader(file_1995)
    data_1995 = [[float(value) if value else 0.0 for value in row] for row in reader]
#print(data_1995)
# 转换为NumPy数组
matrix_1995 = np.array(data_1995)
#print(matrix_1995)


# 创建无向图
G_1995 = nx.from_numpy_array(matrix_1995, create_using=nx.Graph)
#检验
adj_matrix = nx.to_numpy_array(G_1995)
print(adj_matrix)
# 指定CSV文件路径
csv_file = 'adjacency_matrix_1995.csv'

# 写入CSV文件
with open(csv_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(adj_matrix)

print("CSV文件已成功创建。")

# 绘制网络图
nx.draw(G_1995, with_labels=True, font_weight='bold')
plt.show()

# 计算权重接近中心性
weighted_closeness_centrality = nx.closeness_centrality(G_1995, distance='weight')

# 计算权重特征向量中心性
weighted_eigenvector_centrality = nx.eigenvector_centrality_numpy(G_1995, weight='weight')

# 计算权重度中心性
weighted_degree_centrality = dict(G_1995.degree(weight='weight'))

# 计算权重PageRank中心性
weighted_pagerank_centrality = nx.pagerank(G_1995, weight='weight')

# 将中心性指标保存到CSV文件
csv_file_path = '1995_centrality_scores.csv'
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Node', 'Weighted Closeness Centrality', 'Weighted Eigenvector Centrality', 'Weighted Degree Centrality', 'Weighted PageRank Centrality'])
    for node in G_1995.nodes:
        writer.writerow([node, weighted_closeness_centrality[node], weighted_eigenvector_centrality[node], weighted_degree_centrality[node], weighted_pagerank_centrality[node]])

# 计算聚类系数
clustering_coefficients = nx.clustering(G_1995)
# 创建 DataFrame
df_clustering = pd.DataFrame.from_dict(clustering_coefficients, orient='index', columns=['Clustering Coefficient'])
# 保存为 CSV 文件
df_clustering.to_csv("1995_clustering_coefficients.csv", index_label='Node')


#创建最小生成树
mst_1995 = nx.minimum_spanning_tree(G_1995)
# 绘制网络图
nx.draw(mst_1995, with_labels=True, font_weight='bold')
plt.show()

# 获取邻接矩阵
adj_matrix = nx.adjacency_matrix(mst_1995)

# 将邻接矩阵转换为 DataFrame
df = pd.DataFrame(adj_matrix.toarray())

# 保存为 CSV 文件
df.to_csv("1995_mst_adjacency_matrix.csv", index=False)

# 计算度数分布
degree_sequence = sorted([d for n, d in G_1995.degree()], reverse=True)
degree_count = {}
for degree in degree_sequence:
    if degree in degree_count:
        degree_count[degree] += 1
    else:
        degree_count[degree] = 1

# 绘制度数分布图
degrees, counts = zip(*degree_count.items())
plt.bar(degrees, counts)

# 设置图的标题和轴标签
plt.title("Degree Distribution of G_1995")
plt.xlabel("Degree")
plt.ylabel("Count")

# 保存图形为PNG文件
plt.savefig("1995_degree.png")

# 显示图形
plt.show()

