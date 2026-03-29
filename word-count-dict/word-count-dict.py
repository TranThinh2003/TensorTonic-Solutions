"""
 *     author:  _Shinomiyaa_
 *     created: 30.03.2026 00:38:48
"""
def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    res = {}
    for i in sentences:
        for w in i:
            res[w] = res[w] + 1 if w in res else 1
    return res
    pass