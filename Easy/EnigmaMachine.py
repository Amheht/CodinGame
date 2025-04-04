import sys
import math

rotors = []
operation = input()
pseudo_random_number = int(input())
for i in range(3):
    rotors.append(input())
message = input()

# -- BEGIN SOLUTION --
class Enigma:
    ''' 
        Class designed to encode/decode strings of characters using an incremental value shift and
        variably ordered character sequences.

        Written By Amheht
    '''
    CHAR_SET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, operation, rotors, shift_value, messsage):

        self.operation = operation
        self.rotors = rotors
        self.shift_value = shift_value
        self.message = messsage

        if self.operation == 'ENCODE':
            self.Encode()
        else:
            self.Decode()

        print(self.message)
        
    def Decode(self) -> None:
        ''' Decodes the message. '''
        for rotor in reversed(self.rotors):
            self.message = self.remove_rotor(rotor)
        self.message = self.shift()

    def Encode(self) -> None:
        ''' Encodes the message. '''
        self.message = self.shift()
        for rotor in self.rotors:
            self.message = self.apply_rotor(rotor)

    def remove_rotor(self, rotor: str) -> str:
        ''' Uses a generator to translate a string from the rotor sequence to the standard sequence'''
        return ''.join(f"{Enigma.CHAR_SET[rotor.index(char)]}" for char in self.message)

    def apply_rotor(self, rotor: str) -> str:
        ''' Uses a generator to translate a string from the stnardard sequence to the rotor sequence'''
        return ''.join(f"{rotor[Enigma.CHAR_SET.index(char)]}" for char in self.message)

    def shift(self) -> None:
        ''' Returns a string that incrementally shifts each character using modular arithmetic.'''
        return ''.join(f"{chr((ord(self.message[index]) - 65 + ([-1,1][self.operation == 'ENCODE'] * (self.shift_value + index))) % 26  + 65)}" for index in range(len(self.message)) )     

main = Enigma(operation, rotors, pseudo_random_number, message)
