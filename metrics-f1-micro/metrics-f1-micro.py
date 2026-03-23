"""
 *     author:  Shinomiyaaa
 *     created: 23.03.2026 09:02:18
"""
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    # Write code here
    tp = 0
    fp = 0
    fn = 0
    for i in range(len(y_true)):
        if y_true[i] == y_pred[i]:
            tp += 1
        else:
            fp += 1
            fn += 1
    return 2 * tp / (2 * tp + fp + fn) if (2 * tp + fp + fn) > 0 else 0.0
    pass
