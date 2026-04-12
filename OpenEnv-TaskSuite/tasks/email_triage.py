def grader(action_history):
    correct_actions = sum(1 for a in action_history if a == "classify")
    total = len(action_history)
    return correct_actions / total if total > 0 else 0.0