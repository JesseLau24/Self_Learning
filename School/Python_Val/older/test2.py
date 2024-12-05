import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# 输入数据
data = {
    'Visitor': ['A', 'B', 'C', 'D', 'E'],
    'Age': [34, 28, 31, 19, 24],
    'Number of visits per week': [2, 5, 3, 5, 4]
}

df = pd.DataFrame(data)

# 只提取数值列用于聚类
X = df[['Age', 'Number of visits per week']].values

# 计算距离矩阵并执行单链接层次聚类
linked = sch.linkage(X, method='average')

# 自定义绘图函数，在聚类图上标注距离
def plot_dendrogram_with_distances(linked, labels):
    plt.figure(figsize=(10, 6))
    dendro = sch.dendrogram(linked, labels=labels, distance_sort='ascending')
    
    # 获取坐标信息
    for i, d in enumerate(dendro['dcoord']):
        x = 0.5 * sum(dendro['icoord'][i][1:3])  # 水平坐标为中点
        y = d[1]  # 垂直坐标为分支高度
        plt.text(x, y, f'{y:.2f}', va='bottom', ha='center', fontsize=9, color='blue')  # 标注距离
    
    plt.title('Hierarchical Clustering Dendrogram (Average Linkage)')
    plt.xlabel('Visitor')
    plt.ylabel('Euclidean Distance')
    plt.show()

# 调用函数绘制并标注距离
plot_dendrogram_with_distances(linked, labels=df['Visitor'].values)
