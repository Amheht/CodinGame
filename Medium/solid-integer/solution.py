# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/ide/puzzle/solid-integer

def bijective_base_10(n):
    if n == 0: return "1"
    digits = []
    while n > 0:
        digit = n % 9
        if digit == 0: digit = 9
        digits.append(str(digit))
        n = (n - digit) // 9
    return ''.join(reversed(digits))

n = int(input())
result = bijective_base_10(n)
print(result)
