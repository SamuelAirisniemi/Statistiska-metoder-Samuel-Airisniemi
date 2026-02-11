import numpy as np
from scipy.stats import f, t

class LinearRegression:
    def __init__(self, confidence_level = 0.95):
        self.b = None
        self.d = None
        self.n = None
        self.confidence_level = confidence_level
        self.X1 = None
        self.y = None
        self.y_hat = None
        self.residuals = None
        self.SSE = None
        self.Syy = None
        self.SSR = None
        self.sigma2 = None
        self.std_dev = None
        self.XtX_inv = None
        self.C = None
        self.standard_errors = None
        self.t_values = None
        self.p_values = None
        self.F_value = None
        self.F_p_value = None
        self.feature_names = None
    
    #One-hot encodes categorical columns and returns encoded matrix + feature names
    def one_hot_encode(self, X, categorical_cols, feature_names = None, drop_first = True):
        X = np.array(X, dtype = object)
        numeric_cols = [i for i in range(X.shape[1]) if i not in categorical_cols]
        X_numeric = X[:, numeric_cols].astype(float)
        new_features = []
        new_features_names = []
        new_features.append(X_numeric)
        
        if feature_names is not None:
            for idx in numeric_cols:
                new_features_names.append(feature_names[idx])
        else:
            for idx in numeric_cols:
                new_features_names.append(f"X{idx}")

        for col in categorical_cols:
            categories = np.unique(X[:, col])
            if drop_first:
                categories = categories[1:]
            for cat in categories:
                dummy = (X[:, col] == cat).astype(float).reshape(-1, 1)
                new_features.append(dummy)
                if feature_names is not None:
                    new_features_names.append(f"{feature_names[col]}_{cat}")
                else:
                    new_features_names.append(f"X{col}_{cat}")

        X_encoded = np.hstack(new_features)
        return X_encoded, new_features_names
    
    #Fits the linear regression model using OLS: b = (X^T X)^(-1) X^T y
    def fit(self, X, y, feature_names = None):
        X = np.array(X, dtype = float)
        y = np.array(y, dtype = float)

        self.n = X.shape[0]
        self.d = X.shape[1]
        self.X1 = np.column_stack((np.ones(self.n), X))
        self.y = y

        if feature_names is None:
            self.feature_names = ["Intercept"] + [f"X{i}" for i in range(self.d)]
        else:
            self.feature_names = ["Intercept"] + list(feature_names)
        
        XtX = self.X1.T @ self.X1
        Xty = self.X1.T @ y

        self.XtX_inv = np.linalg.inv(XtX)
        self.b = self.XtX_inv @ Xty
        self.y_hat = self.X1 @ self.b
        self.residuals = self.y - self.y_hat
        self.SSE = np.sum(self.residuals ** 2)
        self.Syy = np.sum((self.y - np.mean(self.y)) ** 2)
        self.SSR = self.Syy - self.SSE
        self.sigma2 = self.SSE / (self.n - self.d - 1)
        self.std_dev = np.sqrt(self.sigma2)
        self.C = self.XtX_inv * self.sigma2
        self.standard_errors = np.sqrt(np.diag(self.C))
        self.t_values = self.b / self.standard_errors
        df = self.n - self.d - 1
        self.p_values = 2 * t.sf(np.abs(self.t_values), df)
        self.F_value = (self.SSR / self.d) / self.sigma2
        self.F_p_value = f.sf(self.F_value, self.d, df)
        return self.b
    
    #Predicts new values using the fitted regression model
    def predict(self, X):
        X = np.array(X, dtype = float)
        n = X.shape[0]

        X1 = np.column_stack((np.ones(n), X))
        return X1 @ self.b
    
    #Computes SSE for the model or for new data
    def sse(self, X = None, y = None):
        if X is None and y is None:
            return self.SSE
        y = np.array(y, dtype = float)
        y_hat = self.predict(X)
        return np.sum((y - y_hat) ** 2)
    
    #Computes the unbiased sample variance: sigma^2 = SSE / (n - d - 1)
    def sample_variance(self, X = None, y = None):
        if X is None and y is None:
            return self.sigma2
        SSE = self.sse(X, y)
        return SSE / (self.n - self.d - 1)
    
    #Computes the standard deviation of the residuals
    def standard_deviation(self, X = None, y = None):
        return np.sqrt(self.sample_variance(X, y))
    
    #Computes RMSE for the model or new data
    def rmse(self, X = None, y = None):
        if X is None and y is None:
            mse = self.SSE / self.n
            return np.sqrt(mse)
        SSE = self.sse(X, y)
        mse = SSE / self.n
        return np.sqrt(mse)
    
    #Computes R^2. The coefficient of determination
    def r2(self):
        return 1 - (self.SSE / self.Syy)
    
    #Returns F-statistics and p-value for overall regression significance 
    def regression_significance(self):
        return self.F_value, self.F_p_value
    
    #Returns t-values and p-values for individual parameter significance tests
    def t_test(self):
        return self.t_values, self.p_values
    
    #Computes confidence intervals for all regression coefficients
    def confidence_intervals(self, confidence_level = None):
        if confidence_level is None:
            confidence_level = self.confidence_level

        alpha = 1 - confidence_level
        df = self.n - self.d - 1
        t_crit = t.ppf(1 - alpha / 2, df)

        intervals = []
        for i in range(len(self.b)):
            lower = self.b[i] - t_crit * self.standard_errors[i]
            upper = self.b[i] + t_crit * self.standard_errors[i]
            intervals.append((lower, upper))
        return intervals
    
    #Computes Pearson correlation matrix between all columns in X
    def pearson_matrix(self, X):
        X = np.array(X, dtype=float)
        return np.corrcoef(X, rowvar=False)

    #Prints a full statistical summary of the fitted regression model
    def summary(self):
        print("\nLinear Regression Summary")
        print(f"n (samples): {self.n}")
        print(f"d (features): {self.d}")

        print("Coefficients:")
        for i, name in enumerate(self.feature_names):
            print(f"{name:25s} {self.b[i]:12.6f}")
        
        print(f"SSE: {self.SSE:.6f}")
        print(f"Sample variance (sigma^2): {self.sigma2:.6f}")
        print(f"Standard deviation: {self.std_dev:.6f}")
        print(f"RMSE: {self.rmse():.6f}")
        print(f"R^2: {self.r2():.6f}")

        print("t-test results (individual significance):")
        print(f"{'Feature':25s} {'beta':>12s} {'std_err':>12s} {'t':>12s} {'p-value':>12s}")

        for i, name in enumerate(self.feature_names):
            print(f"{name:25s} {self.b[i]:12.6f} {self.standard_errors[i]:12.6f} "
                  f"{self.t_values[i]:12.6f} {self.p_values[i]:12.6f}")
        
        F_val, F_p = self.regression_significance()
        print("Regression significance (F-test):")
        print(f"F = {F_val:.6f}")
        print(f"p-value = {F_p:.6f}")

        ci = self.confidence_intervals()
        print(f"{int(self.confidence_level*100)}% confidence intervals:")
        for i, name in enumerate(self.feature_names):
            print(f"{name:25s}: [{ci[i][0]:.6f}, {ci[i][1]:.6f}]")