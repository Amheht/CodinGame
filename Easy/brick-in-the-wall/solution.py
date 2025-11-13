# Written by Joseph Garcia

# Acceleration due to gravity
g = 10

# Distance to lift brick in meters for L-th row.
def getDist(L: int) -> float: return  (L-1) * 6.5 / 100

def getWork(d: float, mass: float) -> float: return d * g * mass

# num of bricks in a row (also max)
x = int(input())

# num of bricks
n = int(input())

# integer weights of the bricks
weights = [int(w) for w in input().split()]

# sort weights
weights.sort()
total_work = 0

bricks_in_row = 0
row = 1
while weights:
    total_work += getWork(getDist(row), weights.pop(-1))
    bricks_in_row += 1
    if bricks_in_row >= x:
        bricks_in_row = 0
        row +=1
      
print(f"{total_work:.3f}")

