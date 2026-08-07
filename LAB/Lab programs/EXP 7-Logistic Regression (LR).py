import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Dataset: Study Hours, Attendance, Assignments, Pass
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

# Features and target
X = data[:, :3]
y = data[:, 3]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.4,
    random_state=1,
    stratify=y
)

# Create Logistic Regression model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Results
print("Actual    :", y_test)
print("Predicted :", y_pred)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nAccuracy:",
      accuracy_score(y_test, y_pred) * 100, "%")