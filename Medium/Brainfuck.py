from enum import Enum, auto

class CMD_TYPE(Enum):
    POINTER = auto()
    REGISTER = auto()
    BRACKET = auto()
    OUTPUT = auto()
    INPUT = auto()

    @classmethod
    def get(cls, val):
        if val in ['<','>']:
            return cls.POINTER
        elif val in ['+','-']:
            return cls.REGISTER
        elif val in ['[',']']:
            return cls.BRACKET
        elif val == '.':
            return cls.OUTPUT
        elif val == ',':
            return cls.INPUT     

c = None
l, s, n = [int(i) for i in input().split()]

program = []
inputs = []

for _ in range(l):
    r = input()
    program.append(r)
for _ in range(n):
    c = int(input())
    inputs.append(c)


class PyFuck:
    ''' 
        PyFuck: A Python Implementation of Brainfuck. 
        Written by: Amheht
    '''
    def __init__(self, s, program, inputs):
        self.registers =  [0] * s
        self.num_registers = s
        self.ptr = 0
        self.output = ''

        self.error = False
        self.program = program
        self.inputs = inputs

        self.loops = []
        self.code = ''
        self.idx = 0

        self._sanitize_code()
        self._bracket_mapping()

    def ptr_operation(self, cmd) -> None:
        ''' Increments or decrements the ptr value by 1. '''     
        if cmd == '<':
            self.ptr += -1
        else: self.ptr += 1

        self.chk_ptr()

    def chk_ptr(self) -> None:
        ''' Checks if the program's pointer is a valid value. ''' 
        if self.ptr < 0 or self.ptr > self.num_registers - 1:
            self.error = True
            print("POINTER OUT OF BOUNDS")

    def register_operation(self, cmd) -> None:
        ''' Increments or decrements the register indexed at the pointer by 1. '''
        if cmd == '-':
            self.registers[self.ptr] += -1
        else: self.registers[self.ptr] += 1

        if self.registers[self.ptr] < 0 or self.registers[self.ptr] > 255:
            self.error = True
            print("INCORRECT VALUE")

    def input_operation(self):
        ''' Writes input to pointed register. '''
        self.registers[self.ptr] = self.inputs.pop(0)

    def output_operation(self):
        ''' Writes characters to the output string. '''
        self.output += chr(self.registers[self.ptr])

    def _sanitize_code(self) -> None:
        ''' Removes invalid characters from the instance's code.'''
        allowed = '-+<>[].,'
        chars_i_want = set(allowed)
        for line in self.program:
            self.code += ''.join(c for c in line if c in chars_i_want)

    def _bracket_mapping(self):
        ''' Maps all bracket to the corresponding loop. '''
        starts = []
        for idx in range(len(self.code)):
            if self.code[idx] == '[':
                starts.append(idx)
            elif self.code[idx] == ']':
                self.loops.append((starts.pop(), idx))

        if len(starts) != 0:
            self.error = True
            print("SYNTAX ERROR")

    def _find_end(self, val) -> int:
        ''' Returns the bracket loop from the given start index. '''
        for loop in self.loops:
            if val == loop[0]:
                return loop[1]

        self.error = True
        print("SYNTAX ERROR")
        return -1

    def _find_begin(self, val) -> int:
        ''' Returns the bracket loop from the given stop index. '''
        for loop in self.loops:
            if val == loop[1]:
                return loop[0]
    
        print("SYNTAX ERROR")
        self.error = True
        return -1

    def bracket_operation(self):
        ''' Bracket logic applied at the given index. '''
        cmd = self.code[self.idx]
        if cmd == '[':
            if self.registers[self.ptr] == 0:
                self.idx = self._find_end(self.idx)
        else:
            if self.registers[self.ptr] != 0:
                self.idx = self._find_begin(self.idx)
             
    def run(self):
        ''' Executed the loaded Brainfuck program. '''
        while self.idx < len(self.code):
            cmd = self.code[self.idx]

            cmd_type = CMD_TYPE.get(cmd)
            
            if cmd_type == CMD_TYPE.POINTER:
                self.ptr_operation(cmd)
            elif cmd_type == CMD_TYPE.REGISTER:
                self.register_operation(cmd)
            elif cmd_type == CMD_TYPE.BRACKET:
                self.bracket_operation()
            elif cmd_type == CMD_TYPE.OUTPUT:
                self.output_operation()
            elif cmd_type == CMD_TYPE.INPUT:
                self.input_operation()
            if self.error:
                break
            self.idx += 1
          
        if not self.error:
            print(self.output)

main = PyFuck(s, program, inputs)
main.run()
