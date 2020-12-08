# Advent of Code 2020
# Day 8, Puzzle 1

# Runs through some simple script-instructions to find a variable's value when the code starts to loop again

import re

class Instruction():
    def __init__(self, instruction):
        grouped_instruction = re.match(r'(.{3}) (.\d+)$', instruction )
        self.instruction = grouped_instruction.group(1)
        self.value = int(grouped_instruction.group(2))
        self.executed = False
    
    def get(self):
        if not self.executed:
            self.executed = True
            return self.instruction, self.value
        else:
            return 'Already Executed', 0 # already executed

code = [] # empty list to hold instructions

# input data
with open('Day 8/Input_8.txt', 'r') as input_file:
    for line in input_file:
        code.append(Instruction(line.rstrip('\n')))

# process code
accumulator = 0
line_idx = 0

while True: # run until break
    inst, val = code[line_idx].get()

    if inst == 'acc': # accumulator instruction
        accumulator += val
        line_idx += 1

    elif inst == 'jmp': # jump instruction
        line_idx += val

    elif inst == 'nop': # no operation
        line_idx += 1

    elif inst == 'Already Executed': # line already executed
        break # exit while loop

print('Accumulator when code loops: ', accumulator)
