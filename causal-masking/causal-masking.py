"""
 *     author:  _Shinomiyaa_
 *     created: 30.03.2026 19:17:53
"""
import numpy as np

def apply_causal_mask(scores, mask_value=-1e9):
    """
    scores: np.ndarray with shape (..., T, T)
    mask_value: float used to mask future positions (e.g., -1e9)
    Return: masked scores (same shape, dtype=float)
    """
    # Write code here
    ans = np.copy(scores)
    for i in range(scores.shape[-2]):
        ans[..., i, i+1:] = mask_value
    return ans

    pass