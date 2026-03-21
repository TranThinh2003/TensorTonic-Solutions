"""
 *     author:  Shinomiyaaa
 *     created: 21.03.2026 15:03:34
"""
def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    if not values: return []
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val: return [0] * len(values)
    w = (max_val - min_val) / num_bins
    arr = [int((v - min_val) / w) for v in values]
    return [i if i < num_bins - 1 else num_bins - 1 for i in arr]