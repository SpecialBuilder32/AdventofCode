# Advent of Code 2020
# Day 14 Puzzle 1

# Performs bitmasking on a series of numbers
# NOTE i do not understand bitmasking, so this will be horribly manual and inefficient

import re
program = []
memory = {} # dicionary representative of a memory space

class instruction():
    # class to keep track of types of instructions
    def __init__(self, line):
        g = re.match(r'(m\w+)(?:\[(\d+)] |(\s))= (.+)$', line.rstrip('\n'))

        self.type = g.group(1)
        
        # depending on instruction, get certain info
        if self.type == 'mask':
            self.mask = g.group(4)
        
        elif self.type == 'mem':
            self.address = int(g.group(2))
            self.value = f"{int(g.group(4)):036b}" # use an f-string to pad leading zeros

    def apply_mask(self, mask):
        # applies the given string mask to the number specified.
        masked_value = list(self.value)
        for i in range(len(mask)): # for each character in mask
            if not mask[i] == 'X':
                masked_value[i] = mask[i]

        # print("".join(masked_value))
        return int("".join(masked_value), 2) # collapse list to string, and intrepet as binary


# input instructions
with open('Day 14/Input_14.txt', 'r') as input_file:
    for line in input_file:
        program.append(instruction(line))

# process instructions
for inct in program:
    # if mask instruction, update mask
    if inct.type == 'mask':
        mask = inct.mask

    # if memory instruction, apply mask and set memory location
    if inct.type == 'mem':
        memory[inct.address] = inct.apply_mask(mask)

# print(memory)

# print result
print("Sum of all values in Memory: ", sum(memory.values()))
