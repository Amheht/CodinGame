# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/medium/shadows-of-the-knight-episode-1

# User inputs
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]

# Variable declaration
pos = {'x': x0, 'y': y0}
xmin = 0
xmax = w-1 
ymin = 0
ymax = h-1

# Game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
  
    if 'D' in bomb_dir: ymin = pos['y'] + 1
    elif 'U' in bomb_dir: ymax = pos['y'] - 1
    if 'L' in bomb_dir: xmax = pos['x'] - 1
    elif 'R' in bomb_dir: xmin = pos['x'] + 1

    pos['x'] = xmin + math.ceil((xmax  - xmin)/2)
    pos['y'] = ymin + math.ceil((ymax  - ymin)/2)

    # the location of the next window Batman should jump to.
    print(f"{pos['x']} {pos['y']}")
