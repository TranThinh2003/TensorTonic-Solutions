"""
 *     author:  _Shinomiyaa_
 *     created: 18.04.2026 23:58:48
"""
import numpy as np
def maxpool_forward(X, pool_size, stride):
    """
    Compute the forward pass of 2D max pooling.
    """
    # Write code here
    X = np.array(X) 

    if X.ndim == 2: X = X[np.newaxis, ..., np.newaxis] 
    
    N, H, W, C = X.shape
    
    out_h = (H - pool_size) // stride + 1
    out_w = (W - pool_size) // stride + 1
    out = np.zeros((N, out_h, out_w, C))
    
    for i in range(N):
        for h in range(out_h):
            for w in range(out_w):
                for c in range(C):
                    h_start = h * stride
                    w_start = w * stride
                    window = X[i,
                               h_start:h_start + pool_size,
                               w_start:w_start + pool_size,
                               c]
                    out[i, h, w, c] = np.max(window)
    return out[0, :, :, 0].tolist()