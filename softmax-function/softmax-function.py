"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 09:29:05
"""
import numpy as np

def softmax(x):
    """
    Compute the softmax of input x.
    Works for 1D or 2D NumPy arrays.
    For 2D, compute row-wise softmax.
    """
    # Write code here
    x = np.array(x)
    if x.ndim==1:
        x = x - np.max(x)
        return np.exp(x) / np.sum(np.exp(x))
    elif x.ndim == 2:
        x = x - np.max(x,axis=1,keepdims=1)
        return np.exp(x) / np.sum(np.exp(x),axis=1,keepdims=1)
    pass