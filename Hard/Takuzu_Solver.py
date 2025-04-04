

# ---- Start input from test ---- #
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
n = int(input())
data = [[char for char in input()] for _ in range(n)]
# ---- End input from test ---- #

class Board:

    def __init__(self, dim: int = 0):
        """Initialize a square board of given dimension with all cells empty ('.')."""
        self.dim = dim
        self.data = self._build_grid()

    def build(self, dim: int = 4) -> None:
        """Reinitialize the board to a new dimension."""
        self.dim = dim
        self.data = self._build_grid()

    def _build_grid(self) -> list:
        """Create and return a blank grid with '.' in all cells."""
        return [['.' for _ in range(self.dim)] for _ in range(self.dim)]

    def get_row(self, r) -> list:
        """Return the specified row."""
        return self.data[r]

    def get_col(self, c) -> list:
        """Return the specified column."""
        return [self.data[r][c] for r in range(self.dim)]

    def chk_cnt(self, idx: int, _type: str = 'ROW') -> bool:
        """Check that each row or column has equal number of 0s and 1s or can potentially be balanced."""
        data = self.get_row(idx) if _type == 'ROW' else self.get_col(idx)

        # Count elements.
        dots = data.count('.')
        zeros  = data.count('0')
        ones = data.count('1')

        # Verify counts.
        return ones == zeros if dots == 0 else abs(zeros - ones) <= dots

    def chk_seq(self, idx:int, _type: str = 'ROW') -> bool:
        """Ensure no three identical digits appear consecutively in a row or column."""
        data = self.get_row(idx) if _type == 'ROW' else self.get_col(idx)

        # Check 3 of the same entries in a row, excluding blanks.
        for i in range(2, self.dim):
            if (data[i] == data[i-1] == data[i-2]) and data[i] != '.':
                return False
        return True

    def chk_unq(self) -> bool:
        """Check for uniqueness among fully filled rows and columns."""

        # Get data and convert it to a tuple; ignore cols/rows that have empty squares.
        rows = [tuple(self.get_row(i)) for i in range(self.dim) if not '.' in self.get_row(i)]
        cols = [tuple(self.get_col(i)) for i in range(self.dim) if not '.' in self.get_col(i)]

        # Get counts of cols/rows.
        num_cols = len(cols)
        num_rows = len(rows)
        
        # Turn into set and compare sizes to check for duplicates.
        return len(set(rows)) == len(rows) and len(set(cols)) == len(cols)

    def is_valid(self) -> bool:
        """Validate the entire board against count, sequence, and uniqueness rules."""
        for i in range(self.dim):

            # 1. Check if the rows/cols are balanced.
            if not self.chk_cnt(i, 'ROW'): return False
            if not self.chk_cnt(i, 'COL'): return False

            # 2. Check for adjacent character count.
            if not self.chk_seq(i, 'ROW'): return False
            if not self.chk_seq(i, 'COL'): return False

        # 3. Check for uniqueness amongst each col and then each row and return result..
        return self.chk_unq()
           

    def render(self) -> None:
        """Print the current board to stdout."""
        for row in self.data:
            print(''.join(row))

    def move(self, row: int, col: int, val: str) -> None:
        """Set the cell at (row, col) to val ('0' or '1')."""
        self.data[row][col] = val


    def load(self, data) -> None:
        """Load an existing data grid into the board."""
        # Set dim and data.
        self.dim = len(data)
        self.data = [[data[r][c] for c in range(self.dim)] for r in range(self.dim)]

    def copy(self):
        """Create and return a deep copy of the current board."""
        board_copy = Board()
        board_copy.load(self.data)
        return board_copy

    def get_moves(self) -> list:
        """Return a list of indices with available/valid moves."""

        test = self.copy()
        test.balance()
        test.pairs()
        test.gaps()
        if test.is_valid():
            self.balance()
            self.pairs()
            self.gaps()

        return [[r, c] for r in range(self.dim) for c in range(self.dim) if self.data[r][c] == '.']


    def balance(self) -> None:
        """Balances the number of 0s and 1s in each rows and columns."""
        # Handles rows.
        for i in range(self.dim):
            row = self.get_row(i)

            if row.count('.') == 1:
                j = row.index('.')
                ones  = row.count('1')
                zeros = row.count('0')
                self.data[i][j] = '0' if ones > zeros else '1'
                # Count elements.

        # Handles cols.
        for j in range(self.dim):
            col = self.get_col(j)
            if col.count('.') == 1:
                i = col.index('.')
                ones = col.count('1')
                zeros = col.count('0')
                self.data[i][j] = '0' if ones > zeros else '1'

    def gaps(self) -> None:
        """Fills same digit gaps (like 1.1) with the opposite value (101)."""
        for i in range(self.dim):
            for j in range(1, self.dim-1):
                if (self.data[i][j-1] == self.data[i][j+1]) and (self.data[i][j-1] != '.') and (self.data[i][j] == '.'):
                    self.data[i][j] = self._opposite(self.data[i][j-1])
                if (self.data[j-1][i] == self.data[j+1][i]) and (self.data[j-1][i] != '.') and (self.data[j][i] == '.'):
                    self.data[j][i] = self._opposite(self.data[j-1][i])



    def pairs(self) -> None:
        """If two adjacent digits are the same, fill the neighbor(s) with the opposite value."""
        for i in range(self.dim):
            for j in range(self.dim-1):
                if self.data[i][j] == self.data[i][j+1] and self.data[i][j] != '.': 
                    if j>0:
                           self.data[i][j-1] = self._opposite(self.data[i][j]) 

                    if j < self.dim-2:
                        if self.data[i][j+2] == '.':
                            self.data[i][j+2] = self._opposite(self.data[i][j+1])

                if self.data[j][i] == self.data[j+1][i] and self.data[j][i] != '.': 
                    if j>0:
                        if self.data[j-1][i] == '.':
                            self.data[j-1][i] = self._opposite(self.data[j][i])
                    if j < self.dim-2:
                        if self.data[j+2][i] == '.':
                            self.data[j+2][i] = self._opposite(self.data[j+1][i])


    def _opposite(self, value: str) -> str:
        """Return the opposite binary digit as a string."""
        return '1' if value == '0' else '0'

def solve(board) -> bool:
    """Recursively solve the puzzle using constraint propagation and backtracking."""
    moves = board.get_moves()
    if not moves:
        board.render()
        return True

    r, c = moves.pop()
    for val in ['0','1']:
        b0 = board.copy()
        b0.move(r, c, val)
        if b0.is_valid():
            if solve(b0):
                return True
    return False

board = Board()
board.load(data)
solve(board)
