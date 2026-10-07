# 6c
from fractions import Fraction

horizon = 4
before_offer = [Fraction(0) for stage in range(horizon)]
thresholds = [Fraction(0) for stage in range(horizon)]
before_offer[horizon - 1] = Fraction(1, 2)
for stage in range(horizon - 2, -1, -1):
    continuation = before_offer[stage + 1]
    thresholds[stage] = continuation
    before_offer[stage] = (1 + continuation * continuation) / 2
for stage in range(horizon):
    print(f"h={stage}: threshold={float(thresholds[stage]):.9f}, W={before_offer[stage]} ({float(before_offer[stage]):.9f})")
gain = before_offer[0] - Fraction(1, 2)
print(f"Gain over accepting first offer: {gain} ({float(gain):.9f})")
