# Advent of Code 2020
# Day 12 Puzzle 1

# Keeps track of movement instructions of a boat and determines the final manhattan distance from the start

import re
import numpy as np

# ship variables
pos = 0+0j # North is complex (y), east is real (x)
facing = 1+0j # complex vector coresponding to facing direction

actions = []

class action():
    def __init__(self, raw_text):
        re_text = re.match(r'(\w)(\d+)$', raw_text)
        self.action = re_text.group(1)
        self.value = int(re_text.group(2))

# input directions
with open('Day 12/Input_12.txt', 'r') as input_file:
    for line in input_file:
        actions.append(action(line))

# process directions
for step in actions:
    if step.action == 'N': # move cardinal directions
        pos += 1j*step.value
    elif step.action == 'S':
        pos += -1j*step.value
    elif step.action == 'E':
        pos += step.value
    elif step.action == 'W':
        pos += -step.value
    elif step.action == 'F': # move in facing direction
        pos += step.value*facing
    elif step.action == 'R':
        facing *= np.exp(1j*-step.value*np.pi/180) # rotate facing vector by speficied degrees
    elif step.action == 'L':
        facing *= np.exp(1j*step.value*np.pi/180)

# print manhattan distance (complex + real)
print("Ships Manhattan Distance: ", abs(pos.real)+abs(pos.imag))

