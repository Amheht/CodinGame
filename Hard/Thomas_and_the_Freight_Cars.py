# CodingGame - Thomas and the Freight Cars
# Difficulty - Hard
# Solution by Joseph Garcia

from functools import lru_cache

@lru_cache(maxsize=None)
def dp(index: int, front: int, back: int) -> int:
    if index == len(carts):
        return 0

    curr = carts[index]
    best = dp(index + 1, front, back)  # skip current cart

    # Try inserting cart at front.
    if front == -1 or curr > front:
        best = max(best, 1 + dp(index + 1, curr, back if back != -1 else curr))

    # Try inserting cart at back.
    if back == -1 or curr < back:
        best = max(best, 1 + dp(index + 1, front if front != -1 else curr, curr))

    return best

# ---- Start input from test ---- #
n = int(input())
carts = list(map(int, input().split()))
# ----  End input from test  ---- #


# Normalize front/back with -1 = no value yet
result = dp(0, -1, -1)
print(result)
