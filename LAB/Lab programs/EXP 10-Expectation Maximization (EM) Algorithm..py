import numpy as np
from sklearn.mixture import GaussianMixture
data = np.array([
    [1, 55, 40, 42],
    [2, 60, 45, 48],
    [2, 65, 50, 52],
    [3, 68, 55, 58],
    [3, 72, 60, 62],
    [4, 75, 65, 68],
    [4, 78, 70, 72],
    [5, 80, 75, 76],
    [5, 85, 80, 82],
    [6, 88, 85, 87],
    [7, 90, 90, 92],
    [8, 95, 95, 96]
])
X = data[:, [0, 3]]
# Create Gaussian Mixture Model
model = GaussianMixture(
    n_components=2,
    random_state=0
)
model.fit(X)
clusters = model.predict(X)
probabilities = model.predict_proba(X)
print("Study Hours | Score | Cluster")
for i in range(len(X)):
    print(
        X[i, 0],
        "\t\t",
        X[i, 1],
        "\t",
        clusters[i]
    )
print("\nCluster Means:")
print(model.means_)
print("\nCluster Probabilities:")
print(np.round(probabilities, 2))