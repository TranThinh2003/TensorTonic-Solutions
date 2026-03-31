"""
 *     author:  _Shinomiyaa_
 *     created: 31.03.2026 14:30:36
"""
import numpy as np

def normalize_3d(v):
    """
    Normalize 3D vector(s) to unit length.
    """
    # Your code here
    v = np.asarray(v)
    # if(v.ndim == 1): v = v.reshape(1, -1)
    norms = np.linalg.norm(v, axis=-1, keepdims=True)

    norms[norms == 0] = 1
    return v / norms
    pass