"""
 *     author:  _Shinomiyaa_
 *     created: 16.04.2026 10:21:16
"""
import numpy as np

def _entropy(y):
    """
    Helper: Compute Shannon entropy (base 2) for labels y.
    """
    y = np.asarray(y)
    if y.size == 0:
        return 0.0
    vals, counts = np.unique(y, return_counts=True)
    p = counts / counts.sum()
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum()) if p.size else 0.0

def information_gain(y, split_mask):
    """
    Compute Information Gain of a binary split on labels y.
    Use the _entropy() helper above.
    """
    # Write code here
    IG = _entropy(y) - (split_mask.sum() * _entropy(y[split_mask]) + (1 - split_mask).sum() * _entropy(y[~split_mask])) / len(y)
    return float(IG)
    pass
