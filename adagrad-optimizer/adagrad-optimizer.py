"""
 *     author:  _Shinomiyaa_
 *     created: 08.04.2026 07:55:42
"""
import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Write code here
    w = np.asarray(w,dtype=np.float64)
    g = np.asarray(g,dtype=np.float64)
    G = np.asarray(G,dtype=np.float64)
    G += g ** 2
    w -= lr * g / (np.sqrt(G + eps))
    return w, G
    pass