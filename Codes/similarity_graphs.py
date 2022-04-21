import pandas as pd
import numpy as p
import matplotlib.pyplot as plt
from sklearn.neighbors import kneighbors_graph, radius_neighbors_graph
import networkx as nx
df = pd.read_csv("C://Users//ARKAJYOTI//Desktop//IITK SEM 4//Statistical AI and Data Mining Techniques//Specral Clustering//SpectralClustering//Data//generate_GM.csv",
    header = None, sep=",")

print(df.describe())
# print(df.head())
# df.hist()
# plt.show()

# X = df.to_numpy()
# print(X)

# X = [[0], [3], [1]]
knn_graph = kneighbors_graph(df, 20, mode='connectivity', include_self=False)
knn_graph = knn_graph.toarray()
knn_graph
G = nx.to_networkx_graph(knn_graph)
nx.draw_random(G)
plt.savefig("./Figures/knn_graph.png")


epsilon_graph = radius_neighbors_graph(df, 0.1, mode='connectivity',
                           include_self=False)

epsilon_graph.toarray()
G = nx.to_networkx_graph(epsilon_graph)
nx.draw_random(G)
plt.savefig("./Figures/epsilon_graph.png")
