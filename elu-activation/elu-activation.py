"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 09:49:53
"""
import numpy as np
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    return [round(i if i > 0 else alpha * (np.exp(i) - 1),4) for i in x] 