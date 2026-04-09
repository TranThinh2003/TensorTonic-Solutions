"""
 *     author:  _Shinomiyaa_
 *     created: 09.04.2026 08:52:24
"""
import numpy as np

def leaky_relu(x, alpha=0.01):
    """
    Vectorized Leaky ReLU implementation.
    """
    # Write code here
    x = np.asarray(x,dtype=np.float64)
    x = np.array([i if i >=0 else alpha * i for i in x])
    return x
    pass