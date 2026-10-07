# 8b
from common import Fraction, machine, backward_values, best_actions

working_switch = (Fraction(8) - Fraction(5)) / (Fraction("0.9") - Fraction("0.6"))
broken_switch = (Fraction(-2) - Fraction(-6)) / (Fraction(1) - Fraction("0.7"))
print("Stage 2 switches: W =", working_switch, ", B =", broken_switch)

# 8c
for salvage in (0, 10, 30):
    terminal = {"W": Fraction(salvage), "B": Fraction(0)}
    values, action_values = backward_values(machine, 3, terminal)
    print(f"lambda={salvage}, V_3={{'W': {salvage}, 'B': 0}}")
    for stage in (2, 1, 0):
        for state in machine:
            candidates = action_values[stage][state]
            print(f"h={stage}, {state}: Q={ {a: float(v) for a, v in candidates.items()} }, V={float(values[stage][state]):.2f}, best={best_actions(candidates)}")
    print("First action from W:", best_actions(action_values[0]["W"]))
