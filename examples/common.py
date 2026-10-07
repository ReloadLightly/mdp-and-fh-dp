# 2a: exact machine data
from fractions import Fraction

machine = {
    "W": {
        "operate": (Fraction(8), {"W": Fraction("0.6"), "B": Fraction("0.4")}),
        "maintain": (Fraction(5), {"W": Fraction("0.9"), "B": Fraction("0.1")}),
    },
    "B": {
        "repair": (Fraction(-2), {"W": Fraction("0.7"), "B": Fraction("0.3")}),
        "replace": (Fraction(-6), {"W": Fraction(1), "B": Fraction(0)}),
    },
}

# 2c: policy evaluation or optimization by backward recursion
def backward_values(model, horizon, terminal, policy=None):
    values = [{} for stage in range(horizon + 1)]
    action_values = [{} for stage in range(horizon)]
    values[horizon] = terminal.copy()
    for stage in range(horizon - 1, -1, -1):
        for state in model:
            candidates = {}
            for action in model[state]:
                reward, transitions = model[state][action]
                candidate = reward
                for successor, probability in transitions.items():
                    candidate += probability * values[stage + 1][successor]
                candidates[action] = candidate
            action_values[stage][state] = candidates
            if policy is None:
                values[stage][state] = max(candidates.values())
            else:
                selected_action = policy[stage][state]
                values[stage][state] = candidates[selected_action]
    return values, action_values

# 3b: retain all ties
def best_actions(candidates):
    best_value = max(candidates.values())
    actions = []
    for action, value in candidates.items():
        if value == best_value:
            actions.append(action)
    return actions
