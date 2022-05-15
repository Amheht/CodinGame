import sys
import math

disk_count = int(input())
turn_count = int(input())


class TowersOfHanoi:
''' A class that generates the state of a Towers of Hanoi game for a given disk and turn count. '''

    def __init__(self, num_disks, num_turns = 0):
        self.num_disks = num_disks
        self.L = []
        self.M = []
        self.R = []
        self.direction = [-1,1][num_disks % 2 == 0]
        self.render_disk_max = (2 * num_disks) + 1
        self.state = ""
        self.turns = num_turns
        if num_turns:
          self.generate_state(turn_count)

    def generate_state(self, turn_count):
      ''' Generates a Towers of Hanoi game state based on the turn_count parameter.'''
        self.turns = turn_count
        for i in range(1, self.num_disks+1):
            position = self.get_pos(i, turn_count)
            if position == 0:
                self.L.append(i)
            elif position == 1:
                self.M.append(i)
            elif position == 2:
                self.R.append(i)

        # Fill in empty rows
        if len(self.L) < self.num_disks:
            self.L = ([0] * (self.num_disks - len(self.L))) + self.L
        if len(self.M) < self.num_disks:
            self.M = ([0] * (self.num_disks - len(self.M))) + self.M
        if len(self.R) < self.num_disks:
            self.R = ([0] * (self.num_disks - len(self.R))) + self.R

        self.render_state()
    def get_pos(self, disk_size, current_turn):
      
        ''' Returns the position of a disk in the game state give the disk size and the current turn.'''
        disk_direction = self.direction * [1,-1][disk_size % 2 == 0]
        moves = []
        start = 2 ** (disk_size - 1)
        current = start
        if start <= current_turn:
            moves.append(current)
            while current <= current_turn:
                current = current + (2 * start)
                if current <= current_turn:
                    moves.append(current)
        steps = len(moves)

        position = (steps * disk_direction) % 3
        return position


    def build_disk(self, disk_size, isEnd):
      ''' Returns a string that contains an ASCII generated image of the disk.'''
      
        disk = "#" * disk_size
        if disk_size == 1:
            disk = "|"
        pad = " " * int(((self.render_disk_max - disk_size)/2))
        if isEnd:
            return pad + disk
        return pad + disk + pad + " "

    def render_state(self):
      ''' Prints the current state of the game, as well as expected number of turns to 
          complete a new game with the given number of disks. '''
      
        for i in range(self.num_disks):
            L_disk = self.build_disk((2 * self.L[i]) + 1, 0)
            M_disk = self.build_disk((2 * self.M[i]) + 1, 0)
            R_disk = self.build_disk((2 * self.R[i]) + 1, 1)
            if i == self.num_disks - 1:
                self.state += L_disk + M_disk + R_disk
            else:
                self.state += L_disk + M_disk + R_disk + '\n'

        print(self.state)
        remaining_moves = (2**self.num_disks) - 1
        print(remaining_moves)

game = TowersOfHanoi(disk_count, turn_count)




