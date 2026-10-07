# 5a
def inventory_step(level, action):
    if action == "sell":
        if level > 0:
            return level - 1, 2
        return 0, 0
    if level < 3:
        return level + 1, 0
    return 3, 5

# 5abc
values = {level: 0 for level in range(4)}
for remaining in range(1, 4):
    next_values = {}
    for level in range(4):
        candidates = {}
        for action in ("sell", "stock"):
            successor, reward = inventory_step(level, action)
            candidates[action] = reward + values[successor]
        next_values[level] = max(candidates.values())
        actions = []
        for action, candidate in candidates.items():
            if candidate == next_values[level]:
                actions.append(action)
        print(f"n={remaining}, l={level}: candidates={candidates}, best={actions}")
    values = next_values
    print(f"F_{remaining} = {values}")
