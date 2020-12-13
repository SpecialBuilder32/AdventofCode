# Advent of Code 2020
# Day 12 Puzzle 2

# Keeps track of movement instructions of a waypoint and boat and determines the final manhattan distance from the start

import re
import numpy as np

# waypoint variables
wp_pos = 10+1j # complex positioin vector of waypoint relative to the ship. real=east, imag=north
ship_pos = 0+0j # absolute position of ship in water

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
    if step.action == 'N': # move waypoint cardinal directions
        wp_pos += 1j*step.value
    elif step.action == 'S':
        wp_pos += -1j*step.value
    elif step.action == 'E':
        wp_pos += step.value
    elif step.action == 'W':
        wp_pos += -step.value

    elif step.action == 'F': # move to waypoint x num of times
        ship_pos += step.value*wp_pos

    elif step.action == 'R': # rotate waypoint around ship
        wp_pos *= np.exp(1j*-step.value*np.pi/180) 
    elif step.action == 'L':
        wp_pos *= np.exp(1j*step.value*np.pi/180)

    # print("waypoint: ", wp_pos, "ship:", ship_pos)

# print manhattan distance (complex + real)
print("Ships Manhattan Distance: ", round(abs(ship_pos.real)+abs(ship_pos.imag),0))

