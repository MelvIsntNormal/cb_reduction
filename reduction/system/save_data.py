completed_levels = []


def level_complete(level):
    global completed_levels
    if level not in completed_levels:
        completed_levels.append(level)
