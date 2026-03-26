"""
 *     author:  Shinomiyaaa
 *     created: 26.03.2026 17:29:19
"""
import numpy as np

def relu(x: np.ndarray) -> np.ndarray:
    """ReLU activation: f(x) = max(0, x)"""
    # YOUR CODE HERE
    return np.maximum(0,x)
    pass