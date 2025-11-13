# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/medium/stock-exchange-losses

class Loss:
    def __init__(self, peak: int, floor: int):
        self.peak = peak
        self.floor = floor

    def total(self) -> int:
        """Return the negative loss (floor - peak), or 0 if not a loss."""
        diff = self.floor - self.peak
        return diff if diff < 0 else 0

# Read input
n = int(input())
data = list(map(int, input().split()))

losses = []
peak = None
floor = None

for value in data:

    # First element initializes peak and floor
    if peak is None:
        peak = value
        floor = value
        continue

    # New rising peak → store previous loss window
    if value > peak:
        losses.append(Loss(peak, floor))
        peak = value
        floor = value
    else:
        # Lower price → extend floor
        if value < floor:
            floor = value

# In case the sequence never rises again, record the last window
if not losses:
    losses.append(Loss(peak, floor))

# Find the maximum (most negative) loss
max_loss = 0
for loss in losses:
    loss_value = loss.total()
    if loss_value < max_loss:
        max_loss = loss_value

print(max_loss)
