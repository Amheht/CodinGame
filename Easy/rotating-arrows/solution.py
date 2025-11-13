# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/easy/rotating-arrows

# Constants & Declarations
ARROW_MAP = ["^", ">", "v", "<"]
rots = 0

# User inputs
w, h = [int(i) for i in input().split()]
y, x = [int(i) for i in input().split()]
lines = [input() for _ in range(h)]

i, j = x, y

# Matrix creation
mat = [["" for _ in range(w)] for _ in range(h)]
for row, line in enumerate(lines):
    for col, char in enumerate(line):
        mat[row][col] = char

while True:
    old_arrow = mat[i][j]
    new_arrow = ARROW_MAP[(ARROW_MAP.index(old_arrow) + 1) % 4]
    mat[i][j] = new_arrow

    rots += 1

    if new_arrow == '<' and j <= 0: break
    elif new_arrow == '^' and i <= 0: break
    elif new_arrow == '>' and i >= h: break
    elif new_arrow == 'v' and j >= w:break

    if new_arrow == "<": j -= 1
    elif new_arrow == "^": i -= 1
    elif new_arrow == ">": j += 1
    elif new_arrow == "v": i += 1

    if i == x and y == j: break

print(rots)
