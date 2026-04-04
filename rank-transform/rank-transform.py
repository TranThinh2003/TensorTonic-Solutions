"""
 *     author:  _Shinomiyaa_
 *     created: 04.04.2026 08:07:54
"""
def rank_transform(values):
    """
    Replace each value with its average rank.
    """
    # Write code here
    n = len(values)
    arr = sorted((val, idx) for idx, val in enumerate(values))
    ranks = [0] * n
    i = 0
    
    while i < n:
        j = i
        while j < n and arr[j][0] == arr[i][0]:
            j += 1
        avg_rank = (i + j + 1) / 2
        for k in range(i, j):
            ranks[arr[k][1]] = avg_rank
        i = j
    return ranks