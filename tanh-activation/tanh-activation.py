"""
 *     author:  Shinomiyaaa
 *     created: 08.03.2026 08:31:52
"""
import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x = np.array(x)
    return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))
    # return np.tanh(x) # 
    pass