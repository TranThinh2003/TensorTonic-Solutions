"""
 *     author:  _Shinomiyaa_
 *     created: 28.03.2026 12:17:13
"""
import numpy as np

def rnn_step_forward(x_t, h_prev, Wx, Wh, b):
    """
    Returns: h_t of shape (H,)
    """
    # Write code here
    pre_act = np.dot(x_t, Wx) + np.dot(h_prev, Wh) + b
    return np.tanh(pre_act)
    pass