# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1

class Node:
    def __init__(self,row:int = -1, col:int = -1):
        self.row = row
        self.col = col

    def is_neighbor(self, target) -> bool:
        if isinstance(target, Node):
            if self.row == target.row:
                return self.col <  target.col
            elif self.col == target.col:
                return self.row < target.row
        return False

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.row == other.row and self.col == other.col
        return False

    def __str__(self):
        return f'{self.row} {self.col}'

class GameSpace:

    def __init__(self, height: int, width: int):
        self.height = height
        self.width = width

        self.nodes = []

    def add_node(self, row: int, col: int):
        new_node = Node(row,col)
        self.nodes.append(new_node)

    def find_closest(self, node: Node):
        right_min = self.width
        down_min = self.height
        right_neighbor = Node()
        down_neighbor = Node()

        for target in self.nodes:
            # Check down
            if node != target:
                if node.is_neighbor(target):

                    if node.row == target.row and abs(node.col - target.col) < down_min:
                        down_neighbor = target
                        down_min = abs(node.col - target.col)

                    if node.col == target.col and abs(node.row - target.row) < right_min:
                        right_neighbor = target
                        right_min = abs(node.row - target.row)
                        
        return right_neighbor, down_neighbor

    def solve(self):
        for node in self.nodes:
            right, down = self.find_closest(node)
            print(f'{node} {right} {down}')
          
# Don't let the machines win. You are humanity's last hope...
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

game = GameSpace(height, width)
x = y = 0
for i in range(height):
    line = input()  # width characters, each either 0 or .
    for x, char in enumerate(line):
        if char == '.': continue
        game.add_node(x,y)
    y += 1

game.solve()
