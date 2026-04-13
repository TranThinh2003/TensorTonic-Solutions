"""
 *     author:  _Shinomiyaa_
 *     created: 13.04.2026 19:05:44
"""
def expected_calibration_error(y_true, y_pred, n_bins):
    """
    Compute Expected Calibration Error.
    """
    # Write code here
    n = len(y_true)

    bin_correct = [0.0] * n_bins
    bin_conf = [0.0] * n_bins
    bin_count = [0] * n_bins

    for i in range(n):
        p = y_pred[i]
        y = y_true[i]

        bin_idx = int(p * n_bins)
        if bin_idx == n_bins: bin_idx -= 1

        bin_count[bin_idx] += 1
        bin_conf[bin_idx] += p
        bin_correct[bin_idx] += y
        
    ece = 0.0
    for i in range(n_bins):
        if bin_count[i] > 0:
            acc = bin_correct[i] / bin_count[i]
            conf = bin_conf[i] / bin_count[i]
            ece += (bin_count[i] / n) * abs(acc - conf)
    return float(ece)