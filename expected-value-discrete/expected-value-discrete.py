"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 11:27:47
"""
import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    x = np.asarray(x)
    p = np.asarray(p)
    if (x.shape != p.shape or not np.isclose(p.sum(),1)): raise ValueError
    return np.sum(x*p);
    pass
