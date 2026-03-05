"""
 *     author:  Shinomiyaaa
 *     created: 06.03.2026 00:24:28
"""
import numpy as np

def dropout(x, p=0.5, rng=None):
    """
    Apply dropout to input x with probability p.
    Return (output, dropout_pattern).
    """
    # Write code here
    x = np.asarray(x)
    if rng is None: rng = np.random
    # keep probability
    prob = 1 - p
    scale = 1.0 / prob
    
    # generate dropout mask (1 = keep, 0 = drop)
    mask = (rng.random(x.shape) < prob).astype(x.dtype)
    dropout_pattern = mask * scale
    
    ans = x * dropout_pattern 
    return ans, dropout_pattern
    pass