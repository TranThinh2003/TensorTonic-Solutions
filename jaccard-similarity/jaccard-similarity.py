"""
 *     author:  _Shinomiyaa_
 *     created: 15.04.2026 07:26:52
"""
def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    # Write code here
    set_a = set(set_a)
    set_b = set(set_b)
    union = set_a.union(set_b)
    intersection = set_a.intersection(set_b)
    if not union: return 0.0  # Avoid division by zero
    return len(intersection) / len(union)
    