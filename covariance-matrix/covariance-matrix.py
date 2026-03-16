"""
 *     author:  Shinomiyaaa
 *     created: 16.03.2026 23:20:10
"""
import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    try: X = np.asarray(X)
    except Exception: return None

    if X.ndim != 2: return None
    n_samples = X.shape[0]
    if n_samples < 2: return None
    if X.ndim != 2: return None
    mean_x = np.mean(X, axis=0)
    centered_X = X - mean_x
    cov_matrix = np.dot(centered_X.T, centered_X) / (X.shape[0] - 1)
    return cov_matrix
    pass