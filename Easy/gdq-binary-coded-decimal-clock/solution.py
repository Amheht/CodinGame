# Solution written by Joseph Garcia
# Original Puzzle: https://www.codingame.com/training/easy/gdq---binary-coded-decimal-clock
import sys
import math

class BCD_Clock:
    def __init__(self):
        self.userTime = ''
        self.time = []
        self.bcd_dict = {
            0: '0000',
            1: '0001',
            2: '0010',
            3: '0011',
            4: '0100',
            5: '0101',
            6: '0110',
            7: '0111',
            8: '1000',
            9: '1001'}

    def set_time(self, userTime: str) -> None:
        self.userTime = userTime
        timeArr = userTime.split(':')
        self.time.append(int(timeArr[0]))
        self.time.append(int(timeArr[1][0]))
        self.time.append(int(timeArr[1][1]))
        self.time.append(int(timeArr[2][0]))
        self.time.append(int(timeArr[2][1]))
        self.time.append(int(timeArr[3][0]))

    def get_bcd_row(self, row, num): 
      return self.state_to_str(int(self.int_to_bcd(num)[row]))
      
    def state_to_str(self, state): 
      return ('_____','#####')[state]
      
    def int_to_bcd(self, num: int) -> str: 
      return self.bcd_dict[num]

    def display(self):
        for i in range(4):
            print(f"|{self.get_bcd_row(i, self.time[0])}|{self.get_bcd_row(i, self.time[1])}|{self.get_bcd_row(i, self.time[2])}|{self.get_bcd_row(i, self.time[3])}|{self.get_bcd_row(i, self.time[4])}|{self.get_bcd_row(i, self.time[5])}|")

_input = input()

clock = BCD_Clock()
clock.set_time(_input)
clock.display()
