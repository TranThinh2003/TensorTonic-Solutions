"""
 *     author:  Shinomiyaaa
 *     created: 12.03.2026 10:26:48
"""
def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """
    n_features = len(points[0])
    
    # initialize sum and cnt
    sum = [[0.0] * n_features for _ in range(k)]
    cnt = [0] * k

    # accumulate sum
    for point, cluster in zip(points, assignments):
        cnt[cluster] += 1
        for i in range(n_features):
            sum[cluster][i] += point[i]
 
    centroids = []
    for i in range(k):
        if cnt[i] == 0:
            centroids.append([0.0] * n_features)  
        else:
            centroid = [s / cnt[i] for s in sum[i]]
            centroids.append(centroid)
    return centroids