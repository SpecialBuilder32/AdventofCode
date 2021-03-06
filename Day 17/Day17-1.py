# Advent of Code 2020
# Day 17 Puzzle 1

# Runs through a 3D version of Conway's Game of Life

import numpy as np # for easier nested arrays
num_cycles = 6 # number of cycles to run through before stopping

# input starting state
with open('Day 17/Input_17.txt', 'r') as input_file:
    initial_state = []
    for line in input_file:
        initial_state.append(list(line.rstrip('\n')))
    initial_width = len(initial_state)

# insert initial_state into a 3D space with enough space around
space = np.full_like([], 0, dtype=int, shape=[initial_width+2*num_cycles]*3) # correctly sized space

for i in range(num_cycles, num_cycles+initial_width):
    for j in range(num_cycles, num_cycles+initial_width):
        space[num_cycles+1,i,j] = int(initial_state[i-num_cycles][j-num_cycles] == '#')

# function to process single cell
def next_state(x, y, z):
    # determines the next state for the cube at specified coordinates
    active_neighbors = 0
    for i in range(x-1,x+2): # for the surrounding cubes
        for j in range(y-1,y+2):
            for k in range(z-1,z+2):
                if not (i,j,k) == (x,y,z): # excluding the center cell
                    try: # in case cube is outside valid space
                        active_neighbors += space[i,j,k]
                    except:
                        pass # nothing to catch

    if space[x,y,z] and active_neighbors in (2,3): # if active, and enough neighbors to remain so
        return 1
    elif not space[x,y,z] and active_neighbors == 3: # if inacive and enough neighbors to activate
        return 1
    else: # otherwise the cell dies
        return 0

# process cube space
for current_cycle in range(num_cycles): # for each cycle
    new_space = space.copy()

    for x in range(len(space)):
        for y in range(len(space[x])):
            for z in range(len(space[x,y])):
                new_space[x,y,z] = next_state(x,y,z)

    space = new_space

# results
print("Total Active Spaces: ", sum(sum(sum(space))))