# Advent of Code 2022

# Start Time: 2:06p (23rd)
    # pause 3:07p - 4:17p
    # pause 5:14p - 6:15p
# Pt 1 End: 6:34p
    # pause 6:57p - 9:27p
    # pause 12:45a - ? (mostly compute)
# Pt 2 End: 
# Total Time: 

# this is maybe the most complicated problem so far. It is an optimization problem and a 
    # pathfinding problem all wrapped into one...
    
# Goal, what is the maximum amount of steam that could be released in 30 moves
    # Of all the valves, only like 12 release any steam, so the branching number is 
    # quite low and so exhausting the solution tree is feasible. If every valve released
    # steam, then that would be very difficult and we'd have to resort to non-exact solutions
    # to approximate the maximum.

from itertools import permutations
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



# Pt 2 - Now we train an.. uh elephant.. to help me open valves. There are two agents in this navigation
@dataclass
class PartnerPath():
    agents: tuple

# this is a different algorithm, so I'm not going to refactor the previous code into this 
    # solution, even though it will be somewhat similar
paths = [PartnerPath((
            Path((START,), 0, 0),
            Path((START,), 0, 0)
        ))]
completed_paths = []
MAX_TIME = 26 # it took 4 minutes to teach the elephant

# we're going to asyncronously make decisions about which valve each agent will proceed to next
    # the agent with the least time spent doing things always makes the next branching decision,
    # but cannot target the space that the other agent is already moving to open

# additionally, I need some upper-bound on solutions to be able to throw out bad solutions early
    # rather than compute them all to completion (too much space complexity)
    # a good upper bound on a solution's steam would be if all the closed valves were opened right now.
    # if another path has an actual steam value higher than that, theres no way this is the optima
completed_paths = []
highest_steam = 0
while len(paths) > 0:
    new_paths = []
    for path in paths:
        # figure out which agent needs to make a decision
        decision_maker = sorted(path.agents, key=lambda e: e.spent_time)
            # 0th element is the agent - with shortest time spent
        decision_makers = 1
        if decision_maker[0].spent_time == decision_maker[1].spent_time:
            decision_makers = 2

        # compute distances from elephant and human
        distances = [None,] *2
        for i, agent in enumerate(decision_maker):
            distances[i] = ( compute_distances(agent.valve_sequence[-1], graph) )

        # list of valves visited (or being moved to) by both human and elephant
        partner_selected_valves = (*decision_maker[0].valve_sequence, *decision_maker[1].valve_sequence)
        remaining_valves = [v for v in usable_valves.values() if v.name not in partner_selected_valves]

        # early throw-out of path. If max steam is already lower than another paths steam
        upper_limit_remaining_steam = 0
        remaining_time = MAX_TIME - decision_maker[0].spent_time
        for valve in remaining_valves:
            upper_limit_remaining_steam += remaining_time*valve.flowrate
        ideal_max_steam = upper_limit_remaining_steam + path.agents[0].steam + path.agents[1].steam

        if ideal_max_steam < highest_steam: # even if we opened all the remaining valves now, we can't beat the current best
            continue # skip to expanding the next path

        # generate possible branch paths from this point, applied to the decision maker(s)
        no_valves_left = True
        for option in permutations(remaining_valves, r=decision_makers):
                # permutations ensures all posibilities when both are decision makers
            no_valves_left = False
            # generate new path with this possibility
            no_reachable_valves = False
            generated_path = list(decision_maker)
            for i, target_valve in enumerate(option): # for each decision maker
                # can we get there in time
                time_to_reach = distances[i][target_valve.name]
                time_open = MAX_TIME - time_to_reach - OPENING_TIME - decision_maker[i].spent_time
                if time_open <= 0: # no we can't open it in time
                    no_reachable_valves = True
                    break # don't bother to check the other decison maker, if one exists
                
                # set next destination to path
                generated_path[i] = Path(
                    valve_sequence=(*decision_maker[i].valve_sequence, target_valve.name), 
                    steam=decision_maker[i].steam + time_open*target_valve.flowrate,
                    spent_time=decision_maker[i].spent_time + time_to_reach + OPENING_TIME
                )

            if no_reachable_valves:# we can't open any more valves
                completed_paths.append(PartnerPath(tuple(decision_maker)))
            else:
                new_paths.append(PartnerPath(tuple(generated_path)))
                # update the running highest steam
                if (new_highest:=generated_path[0].steam + generated_path[1].steam) > highest_steam:
                    highest_steam = new_highest

        if no_valves_left: # no valves are left to look at
            completed_paths.append(PartnerPath(tuple(decision_maker)))
    paths = new_paths
    print(len(completed_paths))
        
# locate optimal path
optimal_partner_path = max(completed_paths, key=lambda e: e.agents[0].steam + e.agents[1].steam)
optimal_partner_steam = optimal_partner_path.agents[0].steam + optimal_partner_path.agents[1].steam

print(f'\nOptimal elephant-employing route releases {optimal_partner_steam} steam, following the route \n\t{optimal_partner_path.agents[0].valve_sequence}, {optimal_partner_path.agents[1].valve_sequence}')
# even with the early-quit on paths it still took over an hour to compute
    # solution : 2999 steam - Yes the elephant is worth it