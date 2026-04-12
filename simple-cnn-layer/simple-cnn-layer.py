"""
 *     author:  _Shinomiyaa_
 *     created: 12.04.2026 13:15:58
"""
import numpy as np

def conv2d(x, W, b):
    """
    Simple 2D convolution layer forward pass.
    Valid padding, stride=1.
    """
    # Write code here
    N, C_in, H, W_in = x.shape
    C_out, _, kH, kW = W.shape
    
    H_out = H - kH + 1
    W_out = W_in - kW + 1
    out = np.zeros((N, C_out, H_out, W_out))
    
    for n in range(N):
        for c_out in range(C_out):
            for i in range(H_out):
                for j in range(W_out):
                    patch = x[n, :, i:i+kH, j:j+kW]   # (C_in, kH, kW)
                    out[n, c_out, i, j] = np.sum(patch * W[c_out]) + b[c_out]

    return out
    pass