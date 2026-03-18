"""
 *     author:  Shinomiyaaa
 *     created: 18.03.2026 10:47:18
"""
import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    # Write code here
    pmf = comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
    cdf = sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k + 1))
    return pmf, cdf
    pass