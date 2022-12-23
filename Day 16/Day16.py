# Advent of Code 2022

# Start Time: 2:06p (23rd)
    # pause 3:07p - 4:17p
    # pause 5:14p - 6:15p
# Pt 1 End: 6:34p
# Pt 2 End:
# Total Time: 

# this is maybe the most complicated problem so far. It is an optimization problem and a 
    # pathfinding problem all wrapped into one...
    
# Goal, what is the maximum amount of steam that could be released in 30 moves
    # Of all the valves, only like 12 release any steam, so the branching number is 
    # quite low and so exhausting the solution tree is feasible. If every valve released
    # steam, then that would be very difficult and we'd have to resort to non-exact solutions
    # to approximate the maximum.

import re
from dataclasses import dataclass
from math import factorial
#pylint: disable=redefined-outer-name


# storage for graph data
@dataclass
class Valve():
    name: str
    flowrate: int
    neighbors: tuple

# Read in graph
with open('Day 16/Day16_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

graph = dict()
for line in lines:
    m = re.match(r'Valve (\w{2}) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
    name = m.group(1)
    flowrate = int(m.group(2))
    neighbors = tuple(m.group(3).split(', '))
    graph.update({name: Valve(name, flowrate, neighbors)})

# we will need to find the distances between two arbitrary nodes
    # likely the best way to do that is by BFS from the start node and just recording the shortest
    # distance to each other node in the graph at once. It'll save compute and we need multiple
    # distances all at once
def compute_distances(start_node, graph) -> dict:
    # computes distances to all nodes on graph from specified start node, formatted as a dict
    ret_distances = {start_node: 0}
    explored_set = [start_node]
    d = 1
    n = graph[start_node].neighbors
    
    while len(explored_set) < len(graph):
        explored_set.extend(n) # record nodes we've already recorded distance to
        ret_distances.update({k:d for k in n}) # record neighbors at the current distance

        new_n = set()
        for node in n:
            # unexplored nodes are in the next to reach
            new_n.update([a for a in graph[node].neighbors if a not in explored_set])
        n = tuple(new_n)
        d += 1
    return ret_distances

# We're going to use the un-stuck valves as our decision points to reduce branching. 
usable_valves = {k:v for k,v in graph.items() if v.flowrate != 0}
print(f'There are {len(usable_valves)} usable valves, so a max of {factorial(len(usable_valves))} paths to compute')

# Now we step-through and generate all the paths between the usable-valves in a sort-of-bfs expansion
START = 'AA'
MAX_TIME = 30 # paths end at 30 minutes of time
OPENING_TIME = 1 # time it takes to open a valve

@dataclass
class Path():
    valve_sequence: tuple
    steam: int
    spent_time: int = 0

# Loop through the paths expanding the possibilities
paths = [Path((START,), 0, 0)]
completed_paths = []
cond = True
while len(paths) > 0:
    new_paths = []
    for path in paths:
        # expand paths
        no_reachable_valves = True
        distances = compute_distances(path.valve_sequence[-1], graph)
        for valve in [v for v in usable_valves.values() if v.name not in path.valve_sequence]: # for any unvisited valves
            time_to_reach = distances[valve.name]
            time_open = MAX_TIME - time_to_reach - OPENING_TIME - path.spent_time

            # if it won't take too long to get there
            if (post_time:=path.spent_time + time_to_reach + OPENING_TIME) < MAX_TIME:
                new_paths.append(Path(
                    valve_sequence=(*path.valve_sequence, valve.name,),
                    steam = path.steam + time_open*valve.flowrate,
                    spent_time = post_time)
                    )
                no_reachable_valves = False

        if no_reachable_valves: # store the path as finalized. 
            completed_paths.append(path)

    paths = new_paths # replace old paths with new ones
print(f'Computed {len(completed_paths)} possible paths')

# locate the path with the most steam
optimal_path = max(completed_paths, key=lambda e: e.steam)
print(f'The optimal path {optimal_path.valve_sequence} releases {optimal_path.steam} steam in 30 mins')