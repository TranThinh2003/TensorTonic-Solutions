"""
 *     author:  _Shinomiyaa_
 *     created: 23.04.2026 08:13:51
"""
import numpy as np

def global_avg_pool(x):
    """
    Compute global average pooling over spatial dims.
    Supports (C,H,W) => (C,) and (N,C,H,W) => (N,C).
    """
    # Write code here
    if x.ndim == 3:
        # (C,H,W) => (C,)
        return np.mean(x, axis=(1,2))
    elif x.ndim == 4:
        # (N,C,H,W) => (N,C)
        return np.mean(x, axis=(2,3))
    raise ValueError()
    pass