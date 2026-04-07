"""
 *     author:  _Shinomiyaa_
 *     created: 07.04.2026 23:42:07
"""
def remove_stopwords(tokens, stopwords):
    """
    Returns: list[str] - tokens with stopwords removed (preserve order)
    """
    # Your code here
    return [token for token in tokens if token not in stopwords]
    pass