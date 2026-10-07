# 9a
from common import Fraction, machine

last_reward = {"W": Fraction(8), "B": Fraction(-2)}
for action in machine["W"]:
    reward, transitions = machine["W"][action]
    distribution = {}
    for successor, probability in transitions.items():
        total_reward = reward + last_reward[successor]
        distribution[total_reward] = probability
    mean = sum(total * probability for total, probability in distribution.items())
    variance = sum(probability * (total - mean) ** 2 for total, probability in distribution.items())
    print(f"{action}: distribution={ {int(g): float(p) for g, p in distribution.items()} }, mean={mean}, variance={variance}")

# 9b
for action in machine["W"]:
    reward, transitions = machine["W"][action]
    mean = sum(probability * (reward + last_reward[successor]) for successor, probability in transitions.items())
    within_variance = Fraction(0)
    between_variance = Fraction(0)
    for successor, probability in transitions.items():
        conditional_mean = reward + last_reward[successor]
        within_variance += probability * 0
        between_variance += probability * (conditional_mean - mean) ** 2
    print(f"Total variance: within={within_variance}, between={between_variance}, sum={within_variance + between_variance}")

# 9c
def expected_utility(stage, state, accumulated, utility):
    if stage == 3:
        return utility(accumulated)
    candidates = []
    for action in machine[state]:
        reward, transitions = machine[state][action]
        candidate = Fraction(0)
        for successor, probability in transitions.items():
            if probability > 0:
                candidate += probability * expected_utility(stage + 1, successor, accumulated + reward, utility)
        candidates.append(candidate)
    return max(candidates)

def identity_utility(total):
    return total

utility_value = expected_utility(0, "W", Fraction(0), identity_utility)
print(f"Expected utility with u(g)=g: {utility_value} ({float(utility_value):.2f})")
