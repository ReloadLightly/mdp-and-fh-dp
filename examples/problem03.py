# 3b
from common import Fraction, machine, backward_values, best_actions

terminal = {"W": Fraction(0), "B": Fraction(0)}
values, action_values = backward_values(machine, 3, terminal)
for stage in (2, 1, 0):
    for state in machine:
        candidates = action_values[stage][state]
        print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")

# 3c
print("Optimal first action:", best_actions(action_values[0]["W"]))

# 3d
cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]
cautious_values, cautious_q = backward_values(machine, 3, terminal, cautious)
for state in machine:
    loss = values[1][state] - cautious_values[1][state]
    print(f"Loss at h=1, {state}: {float(loss):.2f}")

# 3e
markov_count = 2 ** (1 + 2 + 2)
history_count = 0
for first_action in machine["W"]:
    for working_action in machine["W"]:
        for broken_action in machine["B"]:
            reachable_histories = 0
            for middle_state in machine:
                if middle_state == "W":
                    action = working_action
                else:
                    action = broken_action
                reward, transitions = machine[middle_state][action]
                for successor, probability in transitions.items():
                    if probability > 0:
                        reachable_histories += 1
            history_count += 2 ** reachable_histories
print("Behavioral Markov policies:", markov_count)
print("Behavioral history policies:", history_count)
