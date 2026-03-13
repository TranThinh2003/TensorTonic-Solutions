"""
 *     author:  Shinomiyaaa
 *     created: 13.03.2026 09:43:50
"""
import numpy as np

def selu(x, lam=1.0507009873554804934193349852946, alpha=1.6732632423543772848170429916717):
    """
    Apply SELU activation element-wise.
    Returns a list of floats rounded to 4 decimal places.
    """
    # Write code here
    return [round(i * lam if i > 0 else alpha * lam * (np.exp(i) - 1),4) for i in x]
    pass
