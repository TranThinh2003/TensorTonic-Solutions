"""
 *     author:  _Shinomiyaa_
 *     created: 05.04.2026 09:14:06
"""
import numpy as np
def ridge_regression(X, y, lam):
    """
    Compute ridge regression weights using the closed-form solution.
    """
    # Write code here
    X = np.asarray(X)
    y = np.asarray(y)
    n, d = X.shape
    I = np.eye(d)
    w = np.linalg.inv(X.T @ X + lam * I) @ X.T @ y
    return w