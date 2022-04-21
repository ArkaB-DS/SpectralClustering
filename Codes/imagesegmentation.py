# Spectral clustering for image segmentation

# import necesssary libraries
import numpy as np
import matplotlib.pyplot as plt

from sklearn.feature_extraction import image
from sklearn.cluster import spectral_clustering

x, y = np.indices((100, 100))

c1 = (37, 28)
c2 = (45, 52)
c3 = (63, 56)
c4 = (26, 68)

r1, r2, r3, r4 = 15, 12, 13, 14

C1 = (x - c1[0]) ** 2 + (y - c1[1]) ** 2 < r1 ** 2
C2 = (x - c2[0]) ** 2 + (y - c2[1]) ** 2 < r2 ** 2
C3 = (x - c3[0]) ** 2 + (y - c3[1]) ** 2 < r3 ** 2
C4 = (x - c4[0]) ** 2 + (y - c4[1]) ** 2 < r4 ** 2


img = C1 + C2 + C3 + C4


mask = img.astype(bool)

img = img.astype(float)
img += 1 + 0.3 * np.random.randn(*img.shape)

graph = image.img_to_graph(img, mask=mask)

graph.data = np.exp(-graph.data / graph.data.std())

# Force the solver to be arpack, since amg is numerically
# unstable on this example
labels = spectral_clustering(graph, n_clusters=4, eigen_solver="arpack")
label_im = np.full(mask.shape, -1.0)
label_im[mask] = labels


plt.matshow(img)
plt.matshow(label_im)

plt.show()
