# Advent of Code 2024

# Start Time: 10:10 AM 

# Pt 1 End Time: 11:11 AM (while discussing Day 19 on MCC)
# Pt 2 End Time: 12:25 AM

# Total Time: 2hr 15min


## Part 1 - Searching a maze for the best places to "cheat" through a wall

import numpy as np
with open("Day 20/Day20_Input.txt", "r") as f:
    map = []
    for line in f.readlines():
        map.append(list(line.strip()))
    map = np.array(map)

start = np.argwhere(map=="S")[0]
end = np.argwhere(map=="E")[0]

# the maze only has one path, so run through it and record the time each space is reached
pos = start
moves = (
    np.array((0,1)),
    np.array((0,-1)),
    np.array((1,0)),
    np.array((-1,0)),
)
dist = 0
dist_map = np.full_like(map, -1, dtype=int)
while True:
    for move in moves:
        if map[*pos+move] in (".","E"): # the way forward
            dist_map[*pos] = dist
            map[*pos] = "X"
            pos += move
            dist += 1
            continue
    if np.all(pos == end):
        map[*pos] = "X"
        dist_map[*pos] = dist
        break

# now run through the map again, checking each possible "cheat"
num_good_cheats = 0
in_map = lambda pos: pos[0]>0 and pos[0]<map.shape[0] and pos[1]>0 and pos[1]<map.shape[1]
for step in range(dist):
    pos = np.argwhere(dist_map==step)[0]
    for move in moves:
        if map[*pos+move] == "#" and in_map(pos+2*move) and map[*pos+2*move] == "X": # a wall we could cheat through
            saved_time = dist_map[*pos+2*move] - dist_map[*pos] - 2 # taking the cheat takes 2 seconds
            if saved_time >= 100: # only count the good ones
                num_good_cheats += 1

print(f"There are {num_good_cheats} that save at least 100 steps")

## Part 2 - Turns out we can cheat for up to 20 steps, not just 2!
    # I think we can do this with some fun numpy grid stuffs

np.set_printoptions(threshold=np.inf, linewidth=np.inf)

# pad matrix edges so we can splice neatly
pad_dist_map = np.pad(dist_map, 19, constant_values=-1)

# form matrix for time to each space in a cheat
time_mtx = np.full((41,41), 0)
it = np.nditer(time_mtx, flags=["multi_index"])
cent = np.array([20,20])
for _ in it:
    time_mtx[it.multi_index] = np.linalg.norm(cent - it.multi_index, ord=1)
time_mtx[time_mtx>20] = dist+1 # any space further than 20 seconds, treat as if it would double the time to the end (since this is a diamond inside a square matrix)

# now run through the map again, this time checking how many cheats from the current space save enough time to be counted!
# cheats = {}
num_good_cheats = 0
for step in range(dist):
    pos = np.argwhere(dist_map==step)[0]
    dist_submap = pad_dist_map[pos[0]-1:pos[0]+40, pos[1]-1:pos[1]+40]
    saved_time_submap = dist_submap - time_mtx - dist_map[*pos]
    if 51 in saved_time_submap:
        print(saved_time_submap)
        print(step)
    for saved_time_pos in np.argwhere(saved_time_submap>=100):
        saved_time = saved_time_submap[*saved_time_pos]
        num_good_cheats += 1
        # cheats[saved_time] = cheats.setdefault(saved_time, 0) + 1

# print(dict(sorted(cheats.items())))
print(f"There are {num_good_cheats} long cheats that save at least 100 steps")