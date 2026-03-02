"""
 *     author:  Shinomiyaaa
 *     created: 02.03.2026 12:20:10
"""
import numpy as np

def linear_layer_forward(X, W, b):
    """
    Compute the forward pass of a linear (fully connected) layer.
    """
    batch_size = len(X)
    input_dim = len(X[0])
    output_dim = len(W[0])

    out = [[0 for _ in range(output_dim)] for _ in range(batch_size)]

    for i in range(batch_size):
        for j in range(output_dim):
            total = 0
            for k in range(input_dim):
                total += X[i][k] * W[k][j]
            total += b[j]
            out[i][j] = total

    return out
    
