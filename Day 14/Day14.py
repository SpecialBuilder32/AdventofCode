# Advent of Code 2022

# Start Time: 5:44p (17th)
    # pause 6:41p - 7:39p
# Pt 1 End Time: 8:48p
# Pt 2 End Time: 9:33p
# Total Time: 2hr51min

# kinda-particle sim-thing today with sand. 

import numpy as np

with open('Day 14/Day14_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

# first we need the furthest away locations to initialize our grid from
min_x = 500 # this is where the sand falls in from
max_x = 500
max_y = 0
for line in lines:
    for coord_pair in line.strip().split(' -> '):
        x, y = map(int, coord_pair.split(','))
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

edge = 2
x_size = max_x - min_x + 2*edge # adds a buffer of 4 to the edge of the grid
y_size = max_y + 1 +1 # if sand hits this row its gotten to the edge :)
grid = np.full((y_size, x_size), fill_value=False, dtype=bool)
    # on our grid of booleans, an occupied space is a True

# printable version of grid
printing_chars = {True: '#', False: '.'}
def printable_grid(g):
    ret  = ''
    for row in g:
        str_row = ''.join(map(lambda a: printing_chars[a], row))
        ret += str_row+'\n'
    return ret

# loop through input again, this time filling in the walls into the grid
for line in lines:
    last_i_coord = (None, None)
    for coord_pair in line.strip().split(' -> '):
        coord = tuple(map(int, coord_pair.split(',')))

        # transform coord into indices
        i_coord = (coord[0]-min_x+edge, coord[1])

        if last_i_coord[0] is not None: # not the first coord in the line
            # find minimum coord for slicing
            ly = min(i_coord[1], last_i_coord[1])
            ry = max(i_coord[1], last_i_coord[1])
            lx = min(i_coord[0], last_i_coord[0])
            rx = max(i_coord[0], last_i_coord[0])

            grid[ly:ry+1, lx:rx+1] = True
        last_i_coord = i_coord
# print(printable_grid(grid))

# Pt 1 - Simulate falling sand
def simulate_sand(start_grid, stop_condition, inlet, printing=False):
    grid = start_grid.copy() #pylint: disable=redefined-outer-name
    fall_directions = [(1,0), (1,-1), (1,+1)] # priority of different motions
    stop_condition_met = False
    sand_inflow = np.array(inlet)
    units_of_sand = 0

    while not stop_condition_met:
        sand_particle = sand_inflow.copy()
        at_rest = False

        while not at_rest:
            for direc in fall_directions:
                if not grid[tuple(new_space := sand_particle+direc)]:
                    # if the direction is available
                    sand_particle = new_space # move the particle

                    if stop_condition(sand_particle): # we've reached the void!
                        stop_condition_met = True
                        at_rest = True
                        
                    break # skip checking more directions
                
            else: # if no motion was applied (ie break didn't execute)
                # particle is now at rest
                at_rest = True
                grid[tuple(sand_particle)] = True # space is now occupied
                units_of_sand += 1

                if grid[inlet]: # if the inlet is now blocked, end sim
                    stop_condition_met = True

        if printing:
            print(printable_grid(grid))
    return units_of_sand

sand_hit_void = lambda sand_particle: sand_particle[0] >= max_y
pt1 = simulate_sand(grid, sand_hit_void, (0, 500-min_x+edge))

print(f'{pt1} units of sand fell before falling into the void')

# Pt 2 - Now there isn't an endless void, now there's a floor.

# we may need more columns to account for the pyramid of sand that will be forming
needed_l_pad = max( y_size-(500-min_x), 0) 
needed_r_pad = max( y_size-(max_x-500), 0)
l_pad = np.full((y_size, needed_l_pad), False, dtype=bool)
r_pad = np.full((y_size, needed_r_pad), False, dtype=bool)

wider_grid = np.hstack((l_pad, grid, r_pad))
grid_with_floor = np.vstack((wider_grid, np.full(x_size+needed_l_pad+needed_r_pad, True, dtype=bool)))

# completion condition
room_full_of_sand = lambda a: None
    # no condition, let simulation run to completion

pt2 = simulate_sand(grid_with_floor, room_full_of_sand, (0, 500-min_x+edge+needed_l_pad))
print(f'{pt2} units of sand fell before filling the space entirely')