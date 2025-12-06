# Advent of Code 2024

# Start Time: 8:43 PM - 10:20 PM (while watching Polar Express :P)
            # 11:07 PM

# Pt 1 End Time: 
# Pt 2 End Time: 

# Total Time:


## Part 1 - Robots pushing buttons for rbutton pushing robots 
import numpy as np
from operator import lt, gt
with open("Day 21/Day21_Input.txt", "r") as f:
    codes = []
    for line in f.readlines():
        codes.append(line.strip())

NUMPAD = np.array([
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
])
DIRPAD = np.array([
    [None, "^", "A"],
    ["<", "v", ">"]
])
DIRS = {
    ">": (1, lt, np.array([0, 1])), # pos element to check, operator to check against, displacement to apply
    "^": (0, gt, np.array([-1, 0])),
    "v": (0, lt, np.array([1, 0])),
    "<": (1, gt, np.array([0, -1]))
} # in order of presedence to ensure an optimal length

# determine sequence of moves to put the desired code into the numpad
def seq_for_keypad(code: str, keypad):
    pos = np.argwhere(keypad=="A")[0]
    seq = ""
    for char in code:
        goal = np.argwhere(keypad==char)[0]
        # navigate to the right button
        while np.any(goal != pos):
            for dir_chr, (elm, op, dir_vec) in DIRS.items(): # in optimal order
                if op(pos[elm], goal[elm]):
                    seq += dir_chr
                    pos += dir_vec
                    break # start dir list from the top
        seq += "A" # press that number
    return seq

# assign helpers for each pad layout
from functools import partial
numpad = partial(seq_for_keypad, keypad=NUMPAD)
dirpad = partial(seq_for_keypad, keypad=DIRPAD)

# find chain sequence of button presses to enter the given codes
tol = 0
for code in [codes[4]]:
    a = numpad(code)
    print(a)
    a = dirpad(a)
    print(a)
    seq = dirpad(a)
    # seq = dirpad(dirpad(numpad(code)))
    print(seq)
    complexity = len(seq) * int(code[0:-1])
    tol += complexity

print(f"total complexity for the desired codes is {tol}")