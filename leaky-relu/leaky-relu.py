"""
 *     author:  Shinomiyaaa
 *     created: 11.03.2026 09:15:08
"""
import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x)
    x = np.array([i * alpha if i < 0 else i for i in x])
    return x
    pass