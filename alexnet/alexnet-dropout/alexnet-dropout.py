"""
 *     author:  Shinomiyaaa
 *     created: 26.03.2026 17:36:39
"""
import numpy as np

def dropout(x: np.ndarray, p: float = 0.5, training: bool = True) -> np.ndarray:
    """Apply dropout to input."""
    # YOUR CODE HERE
    if training:
        mask = np.random.rand(*x.shape) > p
        return x * mask / (1 - p)
    else:
        return x
    pass