# Advent of Code 2024

# Start Time: 1:23 PM

# Pt 1 End Time: 3:04 PM (runtime ~10sec)
# Pt 2 End Time:

# Total Time: 


# Part 1 - Now we get to actually do A* maze-solving. 
import numpy as np
from dataclasses import dataclass, field
from copy import copy

maze = []
with open("Day 16/Day16_Input.txt", "r") as f:
    for line in f.readlines():
        maze.append(list(line.strip()))
maze = np.array(maze)

start = np.argwhere(maze=="S")[0]
goal = np.argwhere(maze=="E")[0]

Node = set[tuple[int,int], tuple[int,int]] # (pos, fac)
visited: set[Node] = set() # tracks nodes (pos, fac) we've been in already

# we're doing A* pathfinding, where rotation by 90 degrees is an expensive transition to a new node

PRINTABLE = False # disables path tracking, saving memory but preventing manual path audits
ROTS = (
    np.matrix('0 -1;  1 0'), # clockwise
    np.matrix('0  1; -1 0') # witershins
)
@dataclass
class Path:
    fac: np.array
    pos: np.array
    cost: int = 0
    neighbors: dict[Node, int] = field(default_factory=dict) # caches neighbors we've already found
    history: list[Node] = field(default_factory=list)

    def find_neighbors(self):
        self.neighbors = dict() # clear the dict and sever reference from copied path
        # space infront
        if maze[*self.pos+self.fac] != "#" and (node:=(tuple(self.pos+self.fac), tuple(self.fac))) not in visited:
            self.neighbors[node] = 1
        # rotating either direction
        fac = self.fac.reshape((2,1))
        for rot in ROTS:
            if (node:=(tuple(self.pos), tuple(nfac:=np.asarray(rot@fac).reshape(1,2)[0]))) not in visited \
                and maze[*self.pos+nfac] != "#": # turning won't make us face a wall

                self.neighbors[node] = 1000

    def print(self):
        if not PRINTABLE:
            return
        # prints path for being pretty's sake
        fac_dict = {
            (-1,0): "^", 
            (1,0): "v",
            (0,1): ">",
            (0,-1): "<"
        }
        print_maze = maze.copy()
        for pos, fac in self.history:
            print_maze[pos] = fac_dict[tuple(fac)]
        for row in print_maze:
            print("".join(row))

# starting node
init = Path(fac=np.array([0,1]), pos=start)
init.find_neighbors()
frontier = [init]
visited.add((tuple(start), (0,1)))

while True:
    # find cheapest neighbor to expand
    cheapest_cost = np.inf
    cheapest_node = None
    cheapest_path = None
    for path in frontier:
        for ngbh_node, trans_cost in path.neighbors.items():
            if ngbh_node in visited:
                continue # already been here, don't loop
            cost = path.cost + trans_cost + np.linalg.norm(goal-path.pos, ord=1) # taxicab distance to goal is our heuristic, which ignores corners
            if cost < cheapest_cost:
                cheapest_cost = cost
                cheapest_node = ngbh_node
                cheapest_path = path

    # expand the frontier on the chosen node
    if len(cheapest_path.neighbors) > 1: # this is a fork we may expand later
        new_path = copy(cheapest_path)
        new_path.pos, new_path.fac = map(np.array, cheapest_node) # transition to new node
        new_path.cost += cheapest_path.neighbors[cheapest_node]
        if PRINTABLE:
            new_path.history = new_path.history + [cheapest_node]
        new_path.find_neighbors()
        del cheapest_path.neighbors[cheapest_node]
        frontier.append(new_path)
    else: # just update the current path object
        cheapest_path.pos, cheapest_path.fac = map(np.array, cheapest_node) # transition to new node
        cheapest_path.cost += cheapest_path.neighbors[cheapest_node]
        if PRINTABLE:
            cheapest_path.history.append(cheapest_node)
        cheapest_path.find_neighbors()
    visited.add(cheapest_node)

    if cheapest_node[0] == tuple(goal):
        # we've reached the end!
        cheapest_path.print()
        print(f"The best path costs {cheapest_path.cost} to travel")
        break


