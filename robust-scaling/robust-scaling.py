"""
 *     author:  Shinomiyaaa
 *     created: 21.03.2026 14:25:09
"""
def robust_scaling(values):
    """
    Scale values using median and interquartile range.
    """
    # Write code here
    if not values: return []
    
    def get_median(nums):
        n = len(nums)
        if n == 0: return 0
        return nums[n // 2] if n % 2 != 0 else (nums[n // 2 - 1] + nums[n // 2]) / 2.0

    nums = sorted(values)
    n = len(nums)

    median = get_median(nums)
    lower_half = nums[:n // 2]
    upper_half = nums[(n + 1) // 2:]

    Q1 = get_median(lower_half) if lower_half else median
    Q3 = get_median(upper_half) if upper_half else median
    IQR = Q3 - Q1

    if IQR == 0: return [float(i - median) for i in values]
    return [float(i - median) / IQR for i in values]