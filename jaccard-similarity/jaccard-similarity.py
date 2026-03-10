"""
 *     author:  Shinomiyaaa
 *     created: 10.03.2026 12:04:42
"""
import numpy as np
def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    set_a = set(set_a)
    set_b = set(set_b)
    # Write code here
    intersection = set_a.intersection(set_b)
    union = set_a.union(set_b)
    if not union: return 0.0  # Avoid division by zero
    return len(intersection) / len(union)