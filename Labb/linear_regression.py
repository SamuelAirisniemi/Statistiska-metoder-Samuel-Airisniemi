import numpy as np

class LinearRegression:
    def __init__(self):
        self.b = None
        self.d = None
        self.n = None

    def fit(self, X, y):
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)

        self.n = X.shape[0]
        self.d = X.shape[1]

        X_design = np.column_stack((np.ones(self.n), X))

        XtX = X_design.T @ X_design
        Xty = X_design.T @ y

        self.b = np.linalg.inv(XtX) @ Xty

        return self.b

    def predict(self, X):
        X = np.array(X, dtype=float)
        n = X.shape[0]

        X_design = np.column_stack((np.ones(n), X))
        return X_design @ self.b

    def sse(self, X, y):
        y_hat = self.predict(X)
        return np.sum((y - y_hat) ** 2)

    def sample_variance(self, X, y):
        X = np.array(X, dtype=float)
        y = np.array(y, dtype=float)

        SSE = self.sse(X, y)
        return SSE / (self.n - self.d - 1)

    def standard_deviation(self, X, y):
        return np.sqrt(self.sample_variance(X, y))

    def rmse(self, X, y):
        SSE = self.sse(X, y)
        mse = SSE / self.n
        return np.sqrt(mse)
