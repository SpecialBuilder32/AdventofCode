# Advent of Code 2024

# Start Time: 2:44 PM - 3:16 PM
              # 5:16 PM - 5:46 PM

# Pt 1 End Time: 5:46 PM
# Pt 2 End Time: 5:52 PM

# Total Time: 66 min

# Part 1 - Pathfinding time boiiiis
import numpy as np

topo = []
with open("Day 10/Day10_Input.txt", "r") as f:
    for line in f.readlines():
        topo.append([(-1 if a == "." else a) for a in list(line.strip())])
    topo = np.array(topo, dtype=int)

trailheads = [tuple(row) for row in np.argwhere(topo==0)]
peaks = [tuple(row) for row in np.argwhere(topo==9)]
dest_scores = {a:set() for a in trailheads}
path_scores = {a:0 for a in trailheads}
horiz = [[head] for head in trailheads]

def topo_in_get(c: tuple[int,int]):
    x, y = c
    a, b = topo.shape
    if x < 0 or x >= a or y < 0 or y >= b:
        return None
    return topo[c]

# explore the paths - breath first to get all paths
    # although this checks every path to each peak, which is pretty inefficient :(. Hopefully not too slow
for height in range(1,10):
    new_horiz = []
    for path in horiz.copy(): # attempt to expand each path
        pos = path[-1]
        for adj_x, adj_y in [(1,0),(-1,0),(0,1),(0,-1)]:
            adj_c = (pos[0]+adj_x, pos[1]+adj_y)
            if topo_in_get(adj_c) == height:
                p = path.copy()
                p.append(adj_c)
                new_horiz.append(p)
    horiz = new_horiz

# add up the score for each trailhead
dest_score = 0
for path in horiz:
    dest_scores[path[0]].add(path[-1])
    path_scores[path[0]] += 1
for score_set in dest_scores.values():
    dest_score += len(score_set)
# print({a:len(b) for a,b in head_scores.items()})
print(f"trails score = {dest_score}")
print(f"distinct trails score = {sum(path_scores.values())}")

# Part 2 - completed inline, counting *all* paths which I already solved for in my existing method 🎉
