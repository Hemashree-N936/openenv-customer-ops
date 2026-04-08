def grade_performance(tickets):
    total = len(tickets)
    resolved = sum(1 for t in tickets if t.resolved)

    if total == 0:
        return 0.0

    score = resolved / total
    return round(score, 2)