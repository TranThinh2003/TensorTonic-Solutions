"""
 *     author:  Shinomiyaaa
 *     created: 14.03.2026 11:41:53
"""
def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0) -> float:
    """
    Linear warmup (0→initial_lr) then linear decay (initial_lr→final_lr).
    Steps are 0-based; clamp at final_lr after total_steps.
    """

    if step >= total_steps:
        return final_lr

    # Warmup phase
    if warmup_steps > 0 and step < warmup_steps:
        return initial_lr * (step / warmup_steps)

    # Decay phase
    decay_steps = total_steps - warmup_steps
    decay_progress = (step - warmup_steps) / decay_steps

    lr = initial_lr - (initial_lr - final_lr) * decay_progress
    return lr