import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# 输入数据
data = {
    'Visitor': ['A', 'B', 'C', 'D', 'E'],
    'Age': [33, 26, 21, 47, 38],
    'Number of visits per week': [2, 3, 5, 2, 4]
}

df = pd.DataFrame(data)

# 只提取数值列用于聚类
X = df[['Age', 'Number of visits per week']].values

# 计算距离矩阵并执行单链接层次聚类
linked = sch.linkage(X, method='average')

# 绘制层次聚类树状图
plt.figure(figsize=(10, 6))
sch.dendrogram(linked, labels=df['Visitor'].values, distance_sort='ascending')
plt.title('Hierarchical Clustering Dendrogram (average Linkage)')
plt.xlabel('Visitor')
plt.ylabel('Euclidean Distance')
plt.show()
