# 4a
from common import Fraction, machine, backward_values, best_actions

terminal = {"W": Fraction(0), "B": Fraction(0)}
cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]
values, action_values = backward_values(machine, 3, terminal, cautious)
for state in machine:
    for action, value in action_values[1][state].items():
        print(f"Qpi_1({state}, {action}) = {float(value):.2f}")

# 4b
improved = [stage_policy.copy() for stage_policy in cautious]
for state in machine:
    improved[1][state] = best_actions(action_values[1][state])[0]
improved_values, improved_q = backward_values(machine, 3, terminal, improved)
print("Improved policy:", improved)
print(f"Vprime_1: W={float(improved_values[1]['W']):.2f}, B={float(improved_values[1]['B']):.2f}")
improved[2]["W"] = "operate"
closed_values, closed_q = backward_values(machine, 3, terminal, improved)
print(f"After stage 2 change: W={float(closed_values[1]['W']):.2f}, B={float(closed_values[1]['B']):.2f}")
