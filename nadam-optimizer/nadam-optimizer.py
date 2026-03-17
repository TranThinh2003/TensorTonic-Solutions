"""
 *     author:  Shinomiyaaa
 *     created: 18.03.2026 00:07:46
"""
import numpy as np

def nadam_step(w, m, v, grad, lr=0.002, beta1=0.9, beta2=0.999, eps=1e-8):
    """
    Perform one Nadam update step.
    """
    # Write code here
    w = np.asarray(w)
    m = np.asarray(m)
    v = np.asarray(v)
    grad = np.asarray(grad)
    
    m = beta1 * m + (1 - beta1) * grad
    v = beta2 * v + (1 - beta2) * (grad ** 2)
    
    # Apply Nesterov look-ahead (No bias correction)
    m_nesterov = beta1 * m + (1 - beta1) * grad
    
    # Update weights
    w = w - lr * (m_nesterov / (np.sqrt(v) + eps))
    
    return w, m, v