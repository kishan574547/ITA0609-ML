import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
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
X = data[:, 0].reshape(-1, 1)
y = data[:, 3]
linear = LinearRegression()
linear.fit(X, y)
linear_pred = linear.predict(X)
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
polynomial = LinearRegression()
polynomial.fit(X_poly, y)
poly_pred = polynomial.predict(X_poly)
linear_mse = mean_squared_error(y, linear_pred)
poly_mse = mean_squared_error(y, poly_pred)
print("Linear Regression MSE     :", linear_mse)
print("Polynomial Regression MSE :", poly_mse)
if poly_mse < linear_mse:
    print("\nPolynomial Regression performs better.")
else:
    print("\nLinear Regression performs better.")
plt.scatter(X, y, label="Actual Data")
plt.plot(
    X,
    linear_pred,
    label="Linear Regression"
)
order = np.argsort(X[:, 0])
plt.plot(
    X[order],
    poly_pred[order],
    label="Polynomial Regression"
)
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.title("Linear vs Polynomial Regression")
plt.legend()
plt.show()