"""
 *     author:  _Shinomiyaa_
 *     created: 17.04.2026 07:57:09
"""
import numpy as np

def confusion_matrix_norm(y_true, y_pred, num_classes=None, normalize='none'):
    """
    Compute confusion matrix with optional normalization.
    """
    # Write code here
    if num_classes is None:
        num_classes = max(max(y_true), max(y_pred)) + 1
    cm = np.zeros((num_classes, num_classes), dtype=int)
    for t, p in zip(y_true, y_pred):
        cm[t][p] += 1
    if normalize == 'true':
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
    elif normalize == 'pred':
        cm = cm.astype('float') / cm.sum(axis=0)[np.newaxis, :]
    elif normalize == 'all':
        cm = cm.astype('float') / cm.sum()
    else:
        cm = cm.astype('int')
    return cm
    pass