"""
 *     author:  Shinomiyaaa
 *     created: 11.03.2026 09:19:28
"""
import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.asarray(x)
    x = 1 / (1 + np.exp(-x))
    return x
    pass