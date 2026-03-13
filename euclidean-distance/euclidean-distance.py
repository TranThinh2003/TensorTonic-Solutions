"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 12:01:13
"""
import numpy as np
import math
def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    # Write code here
    x = np.asarray(x)
    y = np.asarray(y)
    return float(math.sqrt(np.sum((x-y)**2)))
    pass