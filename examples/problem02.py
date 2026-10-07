# 2c
from common import Fraction, machine, backward_values

cautious = [{"W": "maintain", "B": "repair"} for stage in range(3)]
terminal = {"W": Fraction(0), "B": Fraction(0)}
values, action_values = backward_values(machine, 3, terminal, cautious)
for stage in (2, 1, 0):
    print(f"Vpi_{stage}: W={float(values[stage]['W']):.2f}, B={float(values[stage]['B']):.2f}")

# 2d
enumerated_value = Fraction(0)
for middle_state, first_probability in machine["W"]["maintain"][1].items():
    last_action = cautious[2][middle_state]
    last_reward, last_transitions = machine[middle_state][last_action]
    for end_state, second_probability in last_transitions.items():
        probability = first_probability * second_probability
        total_reward = Fraction(5) + last_reward
        enumerated_value += probability * total_reward
        print(f"W -> {middle_state} -> {end_state}: p={float(probability):.2f}, reward={total_reward}")
print(f"Enumeration Vpi_1(W) = {float(enumerated_value):.2f}")
