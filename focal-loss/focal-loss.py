"""
 *     author:  Shinomiyaaa
 *     created: 24.03.2026 12:04:06
"""
import numpy as np

def focal_loss(p, y, gamma=2.0):
    """
    Compute Focal Loss for binary classification.
    """
    # Write code here
    loss = 0.0
    eps = 1e-9  

    for i in range(len(p)):
        pi = np.clip(p[i], eps, 1 - eps)

        if y[i] == 1: loss += - (1 - pi) ** gamma * np.log(pi)
        
        else: loss += - pi ** gamma * np.log(1 - pi)
    return loss / len(p)  