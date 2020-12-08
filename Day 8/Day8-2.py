# Advent of Code 2020
# Day 8 Puzzle 2

# Repairs a simple instruction script by finding the single corrupt instruction and changing it nop->jmp or jmp->nop

#       We know the broken instruction must be within the infinite loop somewhere, as there is only one broken, and fixing it stops the loop
#       So we can "brute force" our way through the looping instructions, trying to see what happens when that instruction gets changed.

#       This is easier than working backwards, which while maybe being more efficient, would require a map of which instructions could potentially jump to every other line

import re
import copy

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

def altered_code(code, i):
    # returns a copy of the code object but with the specified index flipped
    new_code = copy.deepcopy(code) # true deep copy of list, with cloned child Instruction objects
    if new_code[i].instruction == 'jmp':
        new_code[i].instruction = 'nop'
    elif new_code[i].instruction == 'nop':
        new_code[i].instruction = 'jmp'


    return new_code
    
# process code
def run_code(code, accumulator=0, line_idx=0, master_loop=True):

    while True: # run until break
        if line_idx >= len(code): # code got to end!
            return True, accumulator
            
        if master_loop: # call the function to see if flipping the instruction is worth it.
            success, a = run_code(altered_code(code, line_idx), accumulator=accumulator, line_idx=line_idx, master_loop=False)

            if success: # code exited! 
                return success, a # return final accumulator value
            # else continue to next instruction

        inst, val = code[line_idx].get()

        if inst == 'acc': # accumulator instruction
            accumulator += val
            line_idx += 1

        elif inst == 'jmp': # jump instruction
            line_idx += val

        elif inst == 'nop': # no operation
            line_idx += 1

        elif inst == 'Already Executed': # line already executed
            return False, accumulator # code looped, failure

s, success_accumulator = run_code(code)
print('Accumulator when code loops: ', success_accumulator)