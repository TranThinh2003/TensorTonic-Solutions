"""
 *     author:  _Shinomiyaa_
 *     created: 01.04.2026 11:33:07
"""
import math

def ndcg(relevance_scores, k):
    """
    Compute NDCG@k.
    """
    # Write code here
    dcg = 0.0
    for i in range(min(k, len(relevance_scores))):
        dcg += (2 ** relevance_scores[i] - 1) / math.log2(i + 2)
    ideal_relevance_scores = sorted(relevance_scores, reverse=True)

    idcg = 0.0
    for i in range(min(k, len(ideal_relevance_scores))):
        idcg += (2 ** ideal_relevance_scores[i] - 1) / math.log2(i + 2)
    return dcg / idcg if idcg > 0 else 0.0
    pass