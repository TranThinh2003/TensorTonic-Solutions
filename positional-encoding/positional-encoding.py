"""
 *     author:  _Shinomiyaa_
 *     created: 03.04.2026 18:15:19
"""
import numpy as np

def positional_encoding(seq_len, d_model, base=10000.0):
    """
    Return PE of shape (seq_len, d_model) using sin/cos formulation.
    Odd d_model -> last column is sin.
    """
    # Write code here
    pe = np.zeros((seq_len, d_model))

    pos = np.arange(seq_len)[:, np.newaxis]  

    for i in range(0, d_model, 2):
        div_term = base ** (i / d_model)
        pe[:, i] = np.sin(pos[:, 0] / div_term)

        if i + 1 < d_model:  
            pe[:, i + 1] = np.cos(pos[:, 0] / div_term)

    return pe
    pass