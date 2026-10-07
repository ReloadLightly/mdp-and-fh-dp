# 7b
from common import Fraction, machine, backward_values, best_actions

augmented = {}
for state in ("W0", "W1", "B"):
    if state == "B":
        original_state = "B"
    else:
        original_state = "W"
    augmented[state] = {}
    for action in machine[original_state]:
        reward, transitions = machine[original_state][action]
        working_probability = transitions["W"]
        if state == "W1" and action == "operate":
            working_probability = Fraction("0.3")
        if action == "operate":
            working_successor = "W1"
        else:
            working_successor = "W0"
        augmented[state][action] = (reward, {working_successor: working_probability, "B": 1 - working_probability})

# 7c
terminal = {state: Fraction(0) for state in augmented}
values, action_values = backward_values(augmented, 3, terminal)
for stage in (2, 1, 0):
    for state in augmented:
        candidates = action_values[stage][state]
        print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")
print(f"Optimal V0(W,0) = {float(values[0]['W0']):.2f}")

# 7d
operate_repair = [{"W0": "operate", "W1": "operate", "B": "repair"} for stage in range(3)]
policy_values, policy_q = backward_values(augmented, 3, terminal, operate_repair)
for stage in (2, 1, 0):
    print(f"Policy V_{stage} = { {s: float(v) for s, v in policy_values[stage].items()} }")
loss = values[0]["W0"] - policy_values[0]["W0"]
print(f"Operate/repair loss from (W,0) = {float(loss):.2f}")
