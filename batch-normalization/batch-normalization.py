"""
 *     author:  Shinomiyaaa
 *     created: 27.03.2026 09:33:55
"""
import numpy as np

def batch_norm_forward(x, gamma, beta, eps=1e-5):
    """
    Forward-only BatchNorm for (N,D) or (N,C,H,W).
    """
    # Write code here
    x = np.array(x)
    gamma = np.array(gamma)
    beta = np.array(beta)
    if x.ndim == 2:
        mean = np.mean(x,axis=0,keepdims=True)
        var = np.var(x,axis=0,keepdims=True)
    elif x.ndim == 4:
        mean = np.mean(x,axis=(0,2,3),keepdims=True)
        var = np.var(x,axis=(0,2,3),keepdims=True)
        
        if gamma.ndim == 1: gamma = gamma.reshape(1,-1,1,1)
        if beta.ndim == 1: beta = beta.reshape(1,-1,1,1)
    
    x_hat = (x - mean) / np.sqrt(var + eps)
    return gamma * x_hat + beta
    pass