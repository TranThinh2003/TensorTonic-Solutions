"""
 *     author:  Shinomiyaaa
 *     created: 23.03.2026 00:04:22
"""
import numpy as np

def mc_policy_evaluation(episodes, gamma, n_states):
    """
    Returns: V (NumPy array of shape (n_states,))
    """
    # Write code here
    V = np.zeros(n_states)
    sum = np.zeros(n_states)
    cnt = np.zeros(n_states)

    for episode in episodes:
        states = [step[0] for step in episode]
        rewards = [step[1] for step in episode]

        G = 0
        returns = np.zeros(len(episode))
        for t in reversed(range(len(episode))):
            G = rewards[t] + gamma * G
            returns[t] = G

        visited = set()
        for t in range(len(episode)):
            s = states[t]
            if s not in visited:
                visited.add(s)
                sum[s] += returns[t]
                cnt[s] += 1
                V[s] = sum[s] / cnt[s]
    return V
    pass