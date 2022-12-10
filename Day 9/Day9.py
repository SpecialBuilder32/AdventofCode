# Advent of Code 2022

# Start Time: 1:28am
# Pt 1 End Time: 1:53am (24min)
# Pt 2 End Time: 
# Total Time: 

import numpy as np
import re

# NOTES:
    # np.clip
    # inf norm (cheybushev distance)

# Part 1 - Simple Rope Simulation-thingy

with open('Day 9/Day9_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines() # read in rops head instructions

H = np.array([0,0]) # rope head location
T = np.array([0,0]) # rope tail location

dir_map = {
    'L': np.array([-1,0]),
    'R': np.array([1,0]),
    'U': np.array([0,1]),
    'D': np.array([0,-1]),
}

visited_spaces = set()

for line in lines:
    dir_id, steps = re.match(r'([RLUD]) (\d+)', line).groups()
    steps = int(steps)
    dir_vec = dir_map[dir_id]

    for _ in range(steps): # take step number of iterations
        H += dir_vec # move head in direction

        HT_diff = H-T # vector between head and tail
        if np.linalg.norm(HT_diff, ord=np.inf) >= 2: # if head is far away to move tail
            tail_dir = np.clip(HT_diff, -1, 1) # cap motion of taildir
            T += tail_dir

        visited_spaces.add( tuple(T) )

# total visited spaces
print(f'Total spaces visited by the tail: {len(visited_spaces)}')
        