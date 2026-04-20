"""
 *     author:  _Shinomiyaa_
 *     created: 20.04.2026 08:17:49
"""
import numpy as np

def bag_of_words_vector(tokens, vocab):
    """
    Returns: np.ndarray of shape (len(vocab),), dtype=int
    """
    # Your code here
    vec = np.zeros(len(vocab), dtype=int)
    for i, word in enumerate(vocab):
        vec[i] = tokens.count(word)
    return vec