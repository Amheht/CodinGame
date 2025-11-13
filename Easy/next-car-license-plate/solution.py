# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/easy/next-car-license-plate
class LP:
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, plate: str):

        self.left, self.center, self.right = plate.split('-')
        self.center = int(self.center)
        self.init_center = self.center
        self.carry = 0

    def render(self):
        print(f"{self.left}-{self.center}-{self.right}")
      
    def inc(self, amt):
        self.incCenter(amt)
        self.incRight()
        self.incLeft()
        self.render()

    def incCenter(self, amt):
        if amt == 0: return
        self.center = (self.center + amt) % 999
        if self.center == 0: 
            self.center = 999
            self.carry = (self.init_center + amt - 1) // 999
        else:
            self.carry = (self.init_center + amt) // 999
        self.center = str(self.center).zfill(3)

    def incRight(self):
        self.right, self.carry = self.incLetters(self.right, self.carry)

    def incLeft(self):
        self.left, self.carry = self.incLetters(self.left, self.carry)
      
    def incLetters(self, start, amt):
        if amt == 0: return start, 0
        init_left = LP.ALPHABET.index(start[0]) * 26
        init_right = LP.ALPHABET.index(start[1])
        initVal = init_left + init_right

        initVal += amt
        shiftLeft = (initVal // 26) % 26
        shiftRight = initVal % 26
        shiftVal = LP.ALPHABET[shiftLeft] + LP.ALPHABET[shiftRight]
        carry = initVal // (26 * 26)
        return shiftVal, carry

lp = LP(input())
lp.inc(int(input()))
