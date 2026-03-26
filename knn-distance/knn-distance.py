"""
 *     author:  Shinomiyaaa
 *     created: 26.03.2026 13:24:02
"""
import numpy as np

def knn_distance(X_train, X_test, k):
    """
    Compute pairwise distances and return k nearest neighbor indices.
    """
    # Write code here
    X_train = np.array(X_train)
    X_test = np.array(X_test)
    if X_train.ndim == 1: X_train = X_train.reshape(-1,1)
    if X_test.ndim == 1: X_test = X_test.reshape(-1,1)
    distance = np.sqrt(((X_test[:,np.newaxis,:] - X_train[np.newaxis,:,:]) ** 2).sum(axis=2))
    actual_k = min(k,X_train.shape[0])
    knn_indices = np.argsort(distance, axis=1)[:,:actual_k]
    res = np.full((X_test.shape[0],k),-1,dtype=int)
    res[:,:actual_k] = knn_indices
    return res
    pass
