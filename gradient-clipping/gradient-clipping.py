"""
 *     author:  _Shinomiyaa_
 *     created: 12.04.2026 12:14:32
"""
import numpy as np

def clip_gradients(g, max_norm):
    """
    Clip gradients using global norm clipping.
    """
    # Write code here
    g = np.asarray(g)
    if max_norm <= 0: return g
    # l2_norm = np.sqrt(np.sum(g ** 2))
    l2_norm = np.linalg.norm(g)
    return g * (max_norm / l2_norm) if l2_norm > max_norm else g
    pass