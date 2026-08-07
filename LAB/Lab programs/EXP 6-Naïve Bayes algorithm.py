import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split
data = np.array([
    [1, 55, 40, 0],
    [2, 60, 45, 0],
    [2, 65, 50, 0],
    [3, 68, 55, 0],
    [3, 72, 60, 1],
    [4, 75, 65, 1],
    [4, 78, 70, 1],
    [5, 80, 75, 1],
    [5, 85, 80, 1],
    [6, 88, 85, 1],
    [7, 90, 90, 1],
    [8, 95, 95, 1]
])
X = data[:, :3]
y = data[:, 3]
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.4,
    random_state=1,
    stratify=y
)
model = GaussianNB()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Actual    :", y_test)
print("Predicted :", y_pred)
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=[0, 1]))
print("\nAccuracy:",
      accuracy_score(y_test, y_pred) * 100, "%")