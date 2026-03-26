"""
 *     author:  Shinomiyaaa
 *     created: 26.03.2026 23:15:05
"""
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    ans = []
    for p in points:
        min_dist = float('inf')
        assigned_centroid = None
        for i, centroid in enumerate(centroids):
            dist = sum((p - c) ** 2 for p, c in zip(p, centroid))
            if dist < min_dist:
                min_dist = dist
                assigned_centroid = i
        ans.append(assigned_centroid)
    return ans