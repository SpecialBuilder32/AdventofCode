# Advent of Code 2022

# Start Time: 1:30 AM
# Pt 1 End Time: 2:44 AM
    # Part 2 Start Time: 11:12 AM
# Pt 2 End Time: 11:26 AM
# Total Time: 1hr 25min

import re
import numpy as np # for nice 2d array manipulations in parsing
import copy

# parse input
with open('Day 5/Day5_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

    sep = lines.index('\n') # find where IC stops and instructions begin

    # parse out items in IC stacks  '[N] [C]    '
    num_stacks = len(lines[0])//4
    np_stacks = np.empty((sep-1, num_stacks), dtype=np.str_) # 2D array
    for i, line in enumerate(lines[:sep-1]):
        groups = re.findall(r'(?:\[(\w)\]|.{3})(?:.|\n)', line) # return all capture groups
        np_stacks[i,:] = groups

    # convert numpy to stacks vanilla lists
    IC_stacks = []
    for i in range(num_stacks):
        a = list(np.flip(np_stacks[:,i])) # vertical slice input space, and invert
        try:
            b = a[:a.index('')] # slice list before any empty entries
        except ValueError:
            b = a # no empty entry in lise
        IC_stacks.append(b)

    # parse instructions
    instructions = []
    for line in lines[sep+1:]:
        g = re.match(r'move (\w+) from (\w) to (\w)', line)
        instructions.append(tuple(map(int, g.groups())))


# Part 1 - Determine final configuration after running instruction
    # finally got done with parsing at 2:37 AM (1hr 07min)

stacks = copy.deepcopy(IC_stacks)
for num, orig, dest in instructions: # simulate instruction execution
    for _ in range(num): # do num moves
        stacks[dest-1].append( stacks[orig-1].pop() )

# get top box of each stack
sol1 = ""
for s in stacks:
    sol1 += s[-1]
print(f'The crates ontop of eaach stack after rearragement is {sol1}')  # actually simulating took only 7min after parsing

# Part 2 - Final configuration, but with moving multiple boxes at a time

stacks = copy.deepcopy(IC_stacks)
for num, orig, dest in instructions:
    stacks[dest-1].extend(stacks[orig-1][-num:])
    stacks[orig-1] = stacks[orig-1][:-num]

sol2 = ""
for s in stacks:
    sol2 += s[-1]
print(f'The crates ontop of each stack after multi-moving rearrangement is {sol2}')