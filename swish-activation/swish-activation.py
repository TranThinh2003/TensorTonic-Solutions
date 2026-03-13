"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 08:16:03
"""
import numpy as np

def swish(x):
    """
    Implement Swish activation function.
    """
    # Write code here
    x = np.asarray(x)
    return x*(1/(1+np.exp(-x)))
    pass