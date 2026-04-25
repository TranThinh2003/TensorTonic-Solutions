"""
 *     author:  _Shinomiyaa_
 *     created: 25.04.2026 19:13:18
"""
def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    # Write code here
    # Compute discounted returns backward:
    if not rewards or not log_probs:
        return 0.0
    ans = [0] * len(rewards)
    G_t = 0
    for t in reversed(range(len(rewards))):
        G_t = rewards[t] + gamma * G_t
        ans[t] = G_t
    # Compute baseline (mean of returns):
    baseline = sum(ans) / len(ans)
    # Compute policy gradient loss:
    losses =[]
    for log_prob, G_t in zip(log_probs, ans):
        losses.append(-log_prob * (G_t - baseline))
    
    return sum(losses) / len(losses)
