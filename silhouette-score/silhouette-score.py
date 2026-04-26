"""
 *     author:  _Shinomiyaa_
 *     created: 26.04.2026 07:31:58
"""
import numpy as np

def silhouette_score(X, labels):
    """
    Compute the mean Silhouette Score for given points and cluster labels.
    X: np.ndarray of shape (n_samples, n_features)
    labels: np.ndarray of shape (n_samples,)
    Returns: float
    """
    # Write code here
    n = X.shape[0]
    unique_labels = np.unique(labels)
    
    # Precompute distance matrix
    dist_matrix = np.linalg.norm(X[:, np.newaxis] - X[np.newaxis, :], axis=2)
    
    silhouettes = []
    
    for i in range(n):
        same_cluster = labels == labels[i]
        other_clusters = labels != labels[i]
        
        # a(i): mean intra-cluster distance
        if np.sum(same_cluster) > 1:
            a = np.mean(dist_matrix[i][same_cluster & (np.arange(n) != i)])
        else:
            a = 0
        
        # b(i): min mean distance to other clusters
        b = np.inf
        for label in unique_labels:
            if label == labels[i]:
                continue
            cluster_mask = labels == label
            if np.any(cluster_mask):
                dist = np.mean(dist_matrix[i][cluster_mask])
                b = min(b, dist)
        
        # silhouette score for point i
        if max(a, b) > 0:
            s = (b - a) / max(a, b)
        else:
            s = 0
        
        silhouettes.append(s)
    
    return np.mean(silhouettes)
    pass