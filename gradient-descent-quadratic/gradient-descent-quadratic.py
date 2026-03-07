"""
 *     author:  Shinomiyaaa
 *     created: 07.03.2026 11:10:04
"""
def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # Write code here
    for i in range(steps):
        gradient = 2 * a * x0 + b
        x0 -= lr * gradient
    return x0
    pass
