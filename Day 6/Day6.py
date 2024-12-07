# Advent of Code 2024

# Start Time: 12:04 PM

# Pt 1 End Time: 1:09 PM (while watching movie)
# Pt 2 End Time:

# Total Time: 

# Part 1 - word-search central
import numpy as np

with open("Day 6/Day6_Input.txt", "r") as f:
    room = []
    for line in f.readlines():
        room.append(list(line.strip()))
    room = np.array(room)
    
    start_loc = np.array(np.where(room=='^')).reshape((1,-1))
    curr_loc = start_loc.copy()
    facing = np.array([[-1,0]])
    
    # # helper method
    h, w = room.shape
    def within_room(coord) -> bool:
        x, y = coord
        if x < 0 or x >= h or y < 0 or y >= w:
            return False
        return True

    #run through turtle algorithm
    def step_turtle():
        global curr_loc, facing

        # are we against a wall?
        ahead_loc = (curr_loc + facing).flatten()
        if within_room(ahead_loc) and room[tuple(ahead_loc)] == "#":
            facing = (np.array([[0,1],[-1,0]])@facing.T).T
        room[tuple(curr_loc.flatten())] = "X" # mark current location
        curr_loc += facing

    step_turtle()
    while within_room(curr_loc.flatten()): # we've left the map
        # have we looped?
        if np.all(facing == np.array([[-1,0]])) and np.all(curr_loc == start_loc):
            break

        # otherwise continue
        step_turtle()

    visited_locs = np.count_nonzero(room == "X")
    print(f"total squares visited by the gaurd: {visited_locs}")

# Part 2 - finding valid locations for new obstacles that cause a loop
