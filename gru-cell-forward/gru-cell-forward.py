"""
 *     author:  Shinomiyaaa
 *     created: 09.03.2026 23:15:08
"""
import numpy as np

def _sigmoid(x):
    """Numerically stable sigmoid function"""
    return np.where(x >= 0, 1.0/(1.0+np.exp(-x)), np.exp(x)/(1.0+np.exp(x)))

def _as2d(a, feat):
    """Convert 1D array to 2D and track if conversion happened"""
    a = np.asarray(a, dtype=float)
    if a.ndim == 1:
        return a.reshape(1, feat), True
    return a, False

def gru_cell_forward(x, h_prev, params):
    """
    Implement the GRU forward pass for one time step.
    Supports shapes (D,) & (H,) or (N,D) & (N,H).
    """
    # Write code here
    Wz, Uz, bz = params["Wz"], params["Uz"], params["bz"]
    Wr, Ur, br = params["Wr"], params["Ur"], params["br"]
    Wh, Uh, bh = params["Wh"], params["Uh"], params["bh"]

    D = Wz.shape[0]
    H = Uz.shape[0]

    x, x1 = _as2d(x, D)
    h_prev, h1 = _as2d(h_prev, H)

    z = _sigmoid(x @ Wz + h_prev @ Uz + bz)
    r = _sigmoid(x @ Wr + h_prev @ Ur + br)
    
    h_tilde = np.tanh(x @ Wh + (r * h_prev) @ Uh + bh)
    
    h = (1 - z) * h_prev + z * h_tilde

    if x1 and h1:
        h = h.reshape(-1)

    return np.asarray(h, dtype=np.float32)
    pass