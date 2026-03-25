"""
 *     author:  Shinomiyaaa
 *     created: 25.03.2026 10:34:34
"""
import numpy as np

def angle_between_3d(v, w):
    """
    Compute the angle (in radians) between two 3D vectors.
    """
    # Your code here
    cos = np.dot(v, w) / (np.linalg.norm(v) * np.linalg.norm(w))
    theta = np.arccos(cos)
    return theta
    pass