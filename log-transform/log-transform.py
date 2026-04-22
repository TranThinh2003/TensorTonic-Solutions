"""
 *     author:  _Shinomiyaa_
 *     created: 22.04.2026 11:49:39
"""
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    import math
    return [math.log1p(value) for value in values]