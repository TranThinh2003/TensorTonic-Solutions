import math
"""
 *     author:  _Shinomiyaa_
 *     created: 04.04.2026 07:15:17
"""
def perplexity(prob_distributions, actual_tokens):
    """
    Compute the perplexity of a token sequence given predicted distributions.
    """
    # Write code here
    log_prob_sum = 0.0
    
    for probs, token in zip(prob_distributions, actual_tokens):
        if token >= len(probs):
            return float('inf')
        log_prob_sum += math.log(probs[token])
    return math.exp(-log_prob_sum / len(actual_tokens))