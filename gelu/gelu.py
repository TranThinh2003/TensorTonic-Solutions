"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 10:11:23
"""
import numpy as np
import math

def gelu(x):
    """
    Compute the Gaussian Error Linear Unit (exact version using erf).
    x: list or np.ndarray
    Return: np.ndarray of same shape (dtype=float)
    """
    # Write code here
    x = np.array(x,dtype=float)
    return 1/2 * x *(1+ np.vectorize(math.erf)(x/math.sqrt(2)))
    pass
