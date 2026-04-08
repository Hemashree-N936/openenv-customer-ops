def calculate_reward(ticket, action, step_count):
    reward = 0.0

    if action.action_type == "respond":
        reward += 0.2

        # Priority bonus
        if ticket.priority == "high":
            reward += 0.3

        # Tone quality
        msg = (action.message or "").lower()
        if "sorry" in msg or "apologize" in msg:
            reward += 0.2

        # Speed bonus
        reward += max(0, 0.3 - 0.05 * step_count)

        ticket.resolved = True

    # Penalty for ignoring high priority
    if ticket.priority == "high" and not ticket.resolved:
        reward -= 0.4

    return max(min(reward, 1.0), -1.0)