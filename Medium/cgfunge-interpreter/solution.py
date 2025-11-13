# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/ide/puzzle/cgfunge-interpreter

class CGF:
    """
    Interpreter for the CGF 2D esoteric language.
    """

    def __init__(self, program: list[str]) -> None:
        self.program = program
        self.stack: list[object] = []

        self.is_string = False
        self.is_alive = True

        self.row = 0
        self.col = 0
        self.result = ""

        # Instruction groups
        self.ARITHMETIC = "+-*"
        self.END = "E"
        self.SKIP = "S"
        self.POP = "P"
        self.MOVE = "><^v"
        self.SWITCH = "X"
        self.DUPLICATE = "D"
        self.STACK_LOGIC = "_|"
        self.OUTPUT = "IC"

        # Direction vectors corresponding to MOVE in order: >, <, ^, v
        self.SHIFT = [
            (0, 1),   # '>'
            (0, -1),  # '<'
            (-1, 0),  # '^'
            (1, 0),   # 'v'
        ]
        self.direction = [0, 1]  # start moving right

        self.run()

    def run(self) -> None:
        while self.is_alive:
            ch = self.ptr()

            if self.is_string:
                # String mode: push characters until next '"'
                if ch == '"':
                    self.is_string = False
                elif ch.isdigit():
                    # In string mode, digits are pushed as their ASCII codes
                    self.stack.append(ord(ch))
                else:
                    self.stack.append(ch)

            else:
                # Normal (non-string) mode: interpret instructions
                if ch == '"':
                    self.is_string = True

                elif ch.isnumeric():
                    # Single-digit integer literal
                    self.stack.append(int(ch))

                elif ch in self.ARITHMETIC:
                    # Arithmetic on the top two stack items
                    y = str(self.stack.pop())
                    x = str(self.stack.pop())
                    self.stack.append(eval(x + ch + y))

                elif ch in self.SWITCH:
                    # Swap the top two values
                    second = self.stack.pop()
                    first = self.stack.pop()
                    self.stack.append(second)
                    self.stack.append(first)

                elif ch in self.POP:
                    self.stack.pop()

                elif ch in self.DUPLICATE:
                    self.stack.append(self.stack[-1])

                elif ch in self.MOVE:
                    # Change direction
                    self.direction = list(self.SHIFT[self.MOVE.index(ch)])

                elif ch in self.STACK_LOGIC:
                    # Conditional direction change based on top of stack
                    value = self.stack.pop()
                    cond = bool(value)
                    if ch == "|":
                        # True = up, False = down
                        self.direction = [-1, 0] if cond else [1, 0]
                    else:  # '_'
                        # True = left, False = right
                        self.direction = [0, -1] if cond else [0, 1]

                elif ch in self.OUTPUT:
                    # Output integer or character
                    if ch == "I":
                        self.result += str(self.stack.pop())
                    else:  # 'C'
                        if isinstance(self.stack[-1], int):
                            self.result += chr(self.stack.pop())
                        else:
                            self.result += str(self.stack.pop())

                elif ch in self.SKIP:
                    # Skip one extra cell in the current direction
                    self.row += self.direction[0]
                    self.col += self.direction[1]

                elif ch in self.END:
                    # Halt execution
                    self.is_alive = False
                    break

            # Always move one step in the current direction after executing
            self.row += self.direction[0]
            self.col += self.direction[1]

        print(self.result)

    def ptr(self) -> str:
        """Return the character at the current instruction pointer."""
        return self.program[self.row][self.col]


n = int(input())
program = [input() for _ in range(n)]
CGF(program)
