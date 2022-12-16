# Advent of Code 2022

# Start Time: 1:03a (13th)
    # pause due to failure: 3:22am (13th)
    # 6:07p - 6:44p
    # 9:10p
# Pt 1 End Time: 11:05a (14th) - epiphany in the shower about what was wrong
# Pt 2 End Time: 
# Total Time

# pathfinding up a height map :tada:
    # looking for the shortest possible path

import time
import numpy as np
from string import ascii_lowercase

# parse input
with open('Day 12/Day12_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

    rows = len(lines)
    cols = len(lines[0].strip())
    heightmap = np.full((rows, cols), -1)
    height_lookup = {key: val for val, key in enumerate(ascii_lowercase)}

    for r, line in enumerate(lines):
        for c, char in enumerate(line.strip()):
            if char == 'S': # starting location
                start = (r,c)
                heightmap[r,c] = 0
            elif char == 'E':
                end = (r,c)
                heightmap[r,c] = 25
            else:
                heightmap[r,c] = height_lookup[char]

# Pt 1 - shortest path to the goal. 

    # Depth-first-search : Would be straightforward to implement, but we would need to exhaust the space to ensure optimality
        # also this graph definitely has loops
    # Breadth-first-search : Our graph is very large with lots of branching - so trying to do this in python isn't smart

    #... I guess A* really is the best approach I know how to do offhand. great... this'll be fun

# true transition cost = 1, all spaces equidistant on grid
# node heuristic = taxicab distance to destination, garunteed to be <= true cost of optimal path

def node_heuristic(start, end):
    # return 0 #- turns this into BFS
    disp = abs(start[0]-end[0]) + abs(start[1]-end[1])
    return disp - heightmap[start] # one-norm of distance. NOTE Using NP here slowed down a simple calc
        # adding height data here adds tendancy to go uphill, toward the goal. 
        # since we subtrack from an already underestimate, this is still admissable
        # in the timple 7x7 test case, this reaches the solution in a shorter number of iterations

def within_map(coords):
    return 0 <= coords[0] < rows and 0 <= coords[1] < cols

def display_map_conversion(checked_nodes, expand):
    chars = {True: '#', False: '.'}
    display = ""
    for i, row in enumerate(checked_nodes):
        for j, elem in enumerate(row):
            if (i,j) == expand[0]:
                display += 'X'
            else:
                display += chars[elem]
        display += '\n'
    display += '\r'
    return display

# do A*
    # since we don't need the actual path, just the length we can save on memory
frontier = [(start, 0)] # format: tuple(numpy coords, true cost from start)
checked_nodes = np.full((rows, cols), fill_value=False, dtype=bool)
checked_nodes_cost = np.full((rows, cols), fill_value=-1, dtype=int)

expandable_directions = (np.array((1,0)), np.array((-1,0)), np.array((0,1)), np.array((0,-1)))

peak_not_found = True
while peak_not_found:
    # identify lowest-cost-neighbor to expand
    min_idx = frontier.index(min(frontier, key=lambda a: node_heuristic(a[0], end)+a[1]))
    # frontier.sort(key=lambda a: node_heuristic(a[0], end)+a[1])
    expand = frontier.pop(min_idx) # expand the lowest-cost frontier member

    # check completion
    if np.array_equal(expand[0], end):
        print(f'The shortest possible path takes {expand[1]} steps')
        peak_not_found = False
        break

    for direc in expandable_directions:
        if within_map(neighbor := tuple(expand[0]+direc)) \
            and heightmap[neighbor]-1 <= heightmap[expand[0]]:

            # if the neighbor was already checked but from a higher cost path
            if checked_nodes[neighbor] and checked_nodes_cost[neighbor]>expand[1]+1:
                # reopen the node for evaluation
                frontier.append((neighbor, expand[1]+1))
                checked_nodes[neighbor] = False
                continue # skip the other checks

            # if neighbor is not already in the frontier
            if not checked_nodes[neighbor] and neighbor not in [a[0] for a in frontier]:
                # aadjacent square is a graph neighbor
                frontier.append((neighbor, expand[1]+1))
                continue

            # if neighbor is already in the frontier but under a higher cost
            if neighbor in (frontier_coords := [a[0] for a in frontier]) \
                and frontier[ (idx := frontier_coords.index(neighbor)) ][1] > expand[1]+1:
                # update cost of frontier member
                frontier[idx] = (neighbor, expand[1]+1)

    checked_nodes[expand[0]] = True # mark as explored
    checked_nodes_cost[expand[0]] = expand[1]

    # printing
    # print(display_map_conversion(checked_nodes, expand))
    # time.sleep(0.01)

    


            