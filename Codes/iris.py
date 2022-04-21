
import numpy as np  
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import SpectralClustering
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
from sklearn import metrics
from sklearn.metrics.pairwise import euclidean_distances
from scipy.sparse import csgraph
from numpy import linalg as LA

df = pd.read_csv("./Data/iris.csv")
print(df.shape)

X = df.copy()
X = X.drop('species', axis=1)
print(X.describe())

similarity_matrix = euclidean_distances(X)
print(similarity_matrix.shape)

L_sym = csgraph.laplacian(similarity_matrix, normed=True)

eigenvalues, eigenvectors = LA.eig(L_sym)
eigenvalues.sort()

plt.scatter(range(1,11),eigenvalues[:10])
plt. savefig("./Figures/iris.png", dpi=100)


sc = SpectralClustering(n_clusters = 3)
sc.fit(X)

Cd = X.copy()
Cd = pd.DataFrame(Cd)
Cd.loc[:,'Cluster'] = sc.labels_ # append labels to points

frames = [df['species'], Cd['Cluster']]
result = pd.concat(frames, axis = 1)

for cnum in range(3):

    OC = pd.DataFrame(result[result['Cluster'] == cnum].groupby('species').size())
    OC.columns=['Size']
    
    pred = OC.index[OC['Size'] == OC['Size'].max()].tolist()
    pred[0]

    rowIndex = result.index[result['Cluster'] == cnum]
    result.loc[rowIndex, 'predlabel'] = pred[0]
    
    print(cnum, pred[0])

true = (df['species'] == result['predlabel']).sum()
Acc = round(true/df.shape[0],3)
print('Accuracy ', Acc)


