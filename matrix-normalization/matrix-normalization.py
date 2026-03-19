"""
 *     author:  Shinomiyaaa
 *     created: 20.03.2026 00:22:51
"""
import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    """
    Normalize a 2D matrix along specified axis using specified norm.
    """
    # Write code here
    try:
        if norm_type not in ('l1', 'l2', 'max', 'inf'): return None

        mat = np.array(matrix, dtype=float)
        if mat.size == 0 or mat.ndim == 0 or mat.ndim > 2: return None
        
        if norm_type == 'l2': norm = np.sqrt(np.sum(mat**2, axis=axis, keepdims=True))
        elif norm_type == 'l1': norm = np.sum(np.abs(mat), axis=axis, keepdims=True)
        elif norm_type in ('max', 'inf'): norm = np.max(np.abs(mat), axis=axis, keepdims=True)
            
        norm = np.where(norm == 0, 1.0, norm)
        return mat / norm
    except Exception: return None