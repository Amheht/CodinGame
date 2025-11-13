# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/easy/moves-in-maze
from collections import deque

# Conversion table for 0-35
def move_char(n):
    return str(n) if n < 10 else chr(ord('A') + n - 10)

# Read input
w, h = map(int, input().split())
maze = [list(input()) for _ in range(h)]


class Solver:
    def __init__(self, width: int, height: int, maze: list[str]):
        self.width = width
        self.height = height
        self.maze = maze

        self.dist = [[None for _ in range(self.width)] for _ in range(self.height)]
        self.start = self.find_start()

        self.queue = deque()
        self.chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
      
    def solve(self):

        start_col, start_row = self.start
        self.dist[start_row][start_col] = 0
        self.queue.append((start_col, start_row))

        while self.queue:
            col, row = self.queue.popleft()
            for shift_col, shift_row in self.dirs:
                new_col = (col + shift_col) % self.width
                new_row = (row + shift_row) % self.height

                if self.maze[new_row][new_col] != '#' and self.dist[new_row][new_col] is None:
                    self.dist[new_row][new_col] = self.dist[row][col] + 1
                    self.queue.append((new_col, new_row))
                  
        for r in range(self.height):
            row = ""
            for c in range(self.width):
                if self.maze[r][c] == '#':
                    row += '#'
                elif self.dist[r][c] is None:
                    row += '.'
                else:
                    row += self.chars[self.dist[r][c]]
            print(row)

    def find_start(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.maze[row][col] == 'S':
                    return (col, row)

problem = Solver(w, h, maze)

problem.solve()
