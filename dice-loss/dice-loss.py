"""
 *     author:  _Shinomiyaa_
 *     created: 06.04.2026 07:29:46
"""
import numpy as np

def dice_loss(p, y, eps=1e-8):
    """
    Compute Dice Loss for segmentation.
    """
    # Write code here
    p = np.asarray(p)
    y = np.asarray(y)
    dice = (2 * np.sum(p*y) + eps) / (np.sum(p) + np.sum(y) + eps)
    dice_l = 1 - dice
    return dice_l
    pass