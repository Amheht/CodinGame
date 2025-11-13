# Written by Joseph Garcia
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3


    def sign(self,p1,p2,p3):
        return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y)

    def isInside(self, p) -> bool:
        d1 = self.sign(p, self.p1, self.p2)
        d2 = self.sign(p, self.p2, self.p3)
        d3 = self.sign(p, self.p3, self.p1)

        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)

        return not (has_neg and has_pos)

hi, wi = [int(i) for i in input().split()]

# Set style
style = input()
if style == "expanded":
    style_gap = " "
else: style_gap = ""

# Build grid
grid = [["*"]*wi for _ in range(hi)]

how_many_triangles = int(input())
triangles = []
for i in range(how_many_triangles):
    x_1, y_1, x_2, y_2, x_3, y_3 = [int(j) for j in input().split()]
    triangles.append(Triangle(Point(x_1, y_1),Point(x_2, y_2),Point(x_3, y_3)))

for y in range(hi):
    for x in range(wi):
        for t, triangle in enumerate(triangles):
            if triangle.isInside(Point(x,y)):

                if grid[y][x] == "*":
                    grid[y][x] = " "
                else:
                    grid[y][x] = "*"

for line in grid:
    print(style_gap.join(char for char in line))
