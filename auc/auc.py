"""
 *     author:  Shinomiyaaa
 *     created: 03.03.2026 23:15:36
"""
import numpy as np

def auc(fpr, tpr):
    """
    Compute AUC (Area Under ROC Curve) using trapezoidal rule.
    """
    # Write code here
    auc_value = 0
    for i in range(len(fpr) - 1):
        area = (fpr[i+1] - fpr[i]) * (tpr[i] + tpr[i+1]) / 2
        auc_value += area
    return auc_value

    pass