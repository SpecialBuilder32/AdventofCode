# Advent of Code 2024

# Start Time: 9:30 AM

# Pt 1 End Time: 10:22 AM ... pathfinding algorithms break my brain too much
# Pt 2 End Time: 10:56 - hell yea binary search!

# Total Time: 1hr 26min

# Part 1 - More Pathfinding!

import numpy as np

in_bytes = []
with open("Day 18/Day18_Input.txt", "r") as f:
    for line in f.readlines():
        in_bytes.append(tuple(map(int, line.strip().split(","))))

map_size = (71,71)
map = np.full(map_size, ".")
for in_byte in in_bytes[:1024]: # simulate first 1024 bytes falling
    map[in_byte] = "#"

# print(map.T)

# do pathfinding, easier than the maze problem!
def do_pathfinding():
    start = (0,0)
    goal = (70,70)
    paths = {(0,0): 0}
    visited = {(0,0)}
    goal_vec = lambda pos: (goal[0]-pos[0], goal[1]-pos[1])
    outside_map = lambda pos: pos[0]<0 or pos[0]>=map_size[0] or pos[1]<0 or pos[1]>=map_size[1]

    while len(paths) > 0:
        horiz = []
        for head, length in paths.copy().items():
            keep = False
            for dir in ((0,1),(0,-1),(1,0),(-1,0)):
                if not outside_map(pos:=(head[0]+dir[0], head[1]+dir[1])) and map[pos] != "#" and pos not in visited:
                    horiz.append((head, pos, length + 1))
                    keep = True
            if not keep: # no more to neighbors
                del paths[head]
        if not horiz:
            return # no valid horizons to check - no solution

        to_expand = min(horiz, key=lambda t: t[2]+np.linalg.norm(goal_vec(t[1])))
        paths[to_expand[1]] = to_expand[2]
        visited.add(to_expand[1])

        if to_expand[1] == goal:
            return to_expand
        
res = do_pathfinding()
print(f"Found path with length {res[2]}")

## Part 2 - What is the first byte that will seal off any possible path!
    # we can just run the pathfinding on a loop until no path is found - no need to figure out the actual path

map_backup = map.copy()
# binary search for first byte that prevents valid paths
bisect_window = (len(in_bytes)-1024)
mid = bisect_window//2

while bisect_window >= 1:
    map = map_backup.copy()
    for in_byte in in_bytes[1024:mid+1024]:
        map[in_byte] = "#"

    if not do_pathfinding():
        # there is no valid path!
        mid -= bisect_window//2
        bisect_window/=2
    else:
        mid += bisect_window//2
        bisect_window/=2
    mid = int(mid)

print(f"byte falling at time {mid+1024}, position {in_bytes[mid+1024]} seals off the path!")