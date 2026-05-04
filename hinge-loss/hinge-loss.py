"""
 *     author:  _Shinomiyaa_
 *     created: 04.05.2026 07:42:40
"""
import numpy as np

def hinge_loss(y_true, y_score, margin=1.0, reduction="mean") -> float:
    """
    y_true: 1D array of {-1,+1}
    y_score: 1D array of real scores, same shape as y_true
    reduction: "mean" or "sum"
    Return: float
    """
    # Write code here
    if reduction not in ("mean", "sum"): raise ValueError()
    y_true = np.asarray(y_true)
    y_score = np.asarray(y_score)
    if y_true.shape != y_score.shape: raise ValueError()
    loss = np.maximum(0, margin - y_true * y_score)
    return loss.mean() if reduction == "mean" else loss.sum()
    pass

