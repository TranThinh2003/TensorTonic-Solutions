"""
 *     author:  _Shinomiyaa_
 *     created: 19.04.2026 23:42:08
"""
import numpy as np

def matrix_inverse(A):
    """
    Returns: A_inv of shape (n, n) such that A @ A_inv ≈ I
    """
    # Write code here
    A = np.asarray(A)
    try:
        return np.linalg.inv(A)
    except np.linalg.LinAlgError:
        return None
    pass
