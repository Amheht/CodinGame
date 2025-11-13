# Written by Joseph Garcia
import sys
import math

numbers = []
n = int(input())
numbers = [input() for i in range(n)]

def sum_sq_digits(number):
    total = 0
    number = str(number)
    for digit in number: total += int(digit)**2
    return str(total)

def is_happy(number):
    history = []
    while True:
        history.append(number)
        ssd = sum_sq_digits(number)
        if ssd == '1': return True
        elif ssd in history: return False
        number = ssd

for number in numbers:
    if is_happy(number): print(f'{number} :)')
    else: print(f'{number} :(')
