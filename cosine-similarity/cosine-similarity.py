"""
 *     author:  Shinomiyaaa
 *     created: 19.03.2026 23:32:31
"""
import numpy as np

def cosine_similarity(a, b):
    """
    Compute cosine similarity between two 1D NumPy arrays.
    Returns: float in [-1, 1]
    """
    # Write code here
    if (np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0): return 0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    pass