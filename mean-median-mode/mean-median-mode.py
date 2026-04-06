"""
 *     author:  _Shinomiyaa_
 *     created: 06.04.2026 07:35:52
"""
import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    # Write code here
    x = np.asarray(x)
    mean = np.mean(x)
    median = np.median(x)
    mode = Counter(x).most_common(1)[0][0]
    return mean, median, mode
    pass