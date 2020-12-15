# Advent of Code 2020
# Day 14 Puzzle 2

# Performs bitmasking on a series of numbers and their addresses

import re
program = []
memory = {} # dicionary representative of a memory

class instruction():
    # class to keep track of types of instructions
    def __init__(self, line):
        g = re.match(r'(m\w+)(?:\[(\d+)] |(\s))= (.+)$', line.rstrip('\n'))

        self.type = g.group(1)
        
        # depending on instruction, get certain info
        if self.type == 'mask':
            self.mask = g.group(4)
        
        elif self.type == 'mem':
            self.address = f"{int(g.group(2)):036b}"
            self.value = f"{int(g.group(4)):036b}" # use an f-string to pad leading zeros

    def apply_mask(self, mask):
        # applies the given string mask to the address.
        masked_value = list(self.address)
        for i in range(len(mask)): # for each character in mask
            if not mask[i] == '0': # if its not a zero, copy mask to result
                masked_value[i] = mask[i]

        # calculate floating bits
        num_floaters = masked_value.count('X')
        addresses = []
        for bin_insert in range(2**num_floaters-1, -1, -1):
            bin_insert = list(bin(bin_insert)[2:]) # cut off label and turn into list

            while len(bin_insert)<num_floaters: # add leading zeros
                bin_insert.insert(0, '0')

            # stick bin_inset into values of X in masked value ie ['1', '1', '0']
            j = 0
            address = masked_value.copy()
            for i in range(len(address)):
                if address[i] == 'X':
                    address[i] = bin_insert[j]
                    j += 1

            # add address to list as a decimal
            addresses.append(int("".join(address), 2))
        return addresses


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
        for location in inct.apply_mask(mask):
            memory[location] = int(inct.value, 2)
            
# print result
print("Sum of all values in Memory: ", sum(memory.values()))
