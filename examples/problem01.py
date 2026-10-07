# 1a
model = {
    "x": {"a": ("y", 0), "b": ("z", 1)},
    "y": {"a": ("g", 4), "b": ("z", 0)},
    "z": {"a": ("g", 2), "b": ("y", 1)},
    "g": {"stop": ("g", 0)},
}
horizon = 3
state = "x"
greedy_path = [state]
greedy_reward = 0
for stage in range(horizon):
    action = None
    largest_reward = None
    for candidate_action in model[state]:
        candidate_reward = model[state][candidate_action][1]
        if largest_reward is None or candidate_reward > largest_reward:
            action = candidate_action
            largest_reward = candidate_reward
    successor, reward = model[state][action]
    greedy_reward += reward
    state = successor
    greedy_path.append(state)
print("Greedy:", " -> ".join(greedy_path), "reward =", greedy_reward)

# 1b
values = [{} for stage in range(horizon + 1)]
values[horizon] = {state: 0 for state in model}
optimal_actions = [{} for stage in range(horizon)]
for stage in range(horizon - 1, -1, -1):
    for state in model:
        candidates = {}
        for action in model[state]:
            successor, reward = model[state][action]
            candidates[action] = reward + values[stage + 1][successor]
        best_value = max(candidates.values())
        values[stage][state] = best_value
        optimal_actions[stage][state] = []
        for action, candidate in candidates.items():
            if candidate == best_value:
                optimal_actions[stage][state].append(action)
    print(f"V_{stage} = {values[stage]}")
print(f"V_3 = {values[3]}")

# 1c
for stage in range(horizon):
    print(f"Actions h={stage}: {optimal_actions[stage]}")
state = "x"
optimal_path = [state]
total_reward = 0
for stage in range(horizon):
    action = optimal_actions[stage][state][0]
    state, reward = model[state][action]
    total_reward += reward
    optimal_path.append(state)
print("Optimal:", " -> ".join(optimal_path), "reward =", total_reward)
