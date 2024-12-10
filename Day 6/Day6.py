# Advent of Code 2024

# Start Time: 12:04 PM

# Pt 1 End Time: 1:09 PM (while watching movie)
# Pt 2 End Time:

# Total Time: 

# Part 1 - word-search central
import numpy as np
import time

with open("Day 6/Day6_Input.txt", "r") as f:
    room = []
    for line in f.readlines():
        room.append(list(line.strip()))
    room = np.array(room)
    orig_room = room.copy()
    
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
    def step_turtle(room, curr_loc, facing, facing_mark = False):
        # are we against a wall?
        ahead_loc = (curr_loc + facing).flatten()
        if within_room(ahead_loc) and room[tuple(ahead_loc)] in ("#", "O"):
            facing = (np.array([[0,1],[-1,0]])@facing.T).T
            return facing # don't advance if we just turned
        if facing_mark:
            if np.all(facing == (-1,0)):
                mark = "↑"
            elif np.all(facing == (0,1)):
                mark = "→"
            elif np.all(facing == (1,0)):
                mark = "↓"
            elif np.all(facing == (0,-1)):
                mark = "←"
        else:
            mark = "X"
        room[tuple(curr_loc.flatten())] = mark # mark current location
        curr_loc += facing
        return facing

    facing = step_turtle(room, curr_loc, facing)
    while within_room(curr_loc.flatten()): # we've left the map
        # have we looped?
        if np.all(facing == np.array([[-1,0]])) and np.all(curr_loc == start_loc):
            break

        # otherwise continue
        facing = step_turtle(room, curr_loc, facing)

    visited_locs = np.count_nonzero(room == "X")
    print(f"total squares visited by the gaurd: {visited_locs}")

# Part 2 - finding valid locations for new obstacles that cause a loop

    def pprint_room(room, loc):
        room[loc[0,0]-6:loc[0,0]+6,loc[0,1]-6:loc[0,1]+6]
        a = loc[0,0]-6 if loc[0,0]-6 > 0 else 0
        b = loc[0,1]-6 if loc[0,1]-6 > 0 else 0
        c = loc[0,0]+6
        d = loc[0,1]+6
        if c > (w:=room.shape[0]):
            a -= c-w
        if d > (h:=room.shape[1]):
            b -= d-h
        if loc[0,0]-6 < 0:
            c -= loc[0,0]-6
        if loc[0,1]-6 < 0:
            d -= loc[0,1]-6
        print("="*12)
        for row in room[a:c,b:d]:
            print("".join(row))

    # reset the room
    room = orig_room.copy()
    curr_loc = start_loc.copy()
    facing = np.array([[-1,0]])

    loop_counter = 0

    facing = step_turtle(room, curr_loc, facing, True)
    i = 0
    while within_room(curr_loc.flatten()):
        i+=1
        # have we looped?
        if np.all(facing == np.array([[-1,0]])) and np.all(curr_loc == start_loc):
            break

        # try placing a barrier ahead of us
        ahead_loc = (curr_loc + facing).flatten()
        branch_room = room.copy()
        if within_room(ahead_loc):
            if room[tuple(ahead_loc)] != ".": # either theres already a box, or we've visited the space already
                facing = step_turtle(room, curr_loc, facing, True)
                continue # to next primary loop
            branch_room[tuple(ahead_loc)] = "O"
        else:
            break #  we're reached the end of the main loop!
        branch_loc = curr_loc.copy()
        branch_facing = facing.copy()

        # try out the new room configuration
        branch_facing = step_turtle(branch_room, branch_loc, branch_facing, True)
        while within_room(branch_loc.flatten()): # we've left the map
            # have we looped?
            if (np.all(branch_facing == (-1,0)) and branch_room[tuple(branch_loc.flatten())] == "↑") or \
               (np.all(branch_facing == (0,1)) and branch_room[tuple(branch_loc.flatten())] == "→") or \
               (np.all(branch_facing == (1,0)) and branch_room[tuple(branch_loc.flatten())] == "↓") or \
               (np.all(branch_facing == (0,-1)) and branch_room[tuple(branch_loc.flatten())] == "←") or \
                (np.all(branch_loc == curr_loc) and np.all(branch_facing == facing)): # check for cases where the loop is so small our memory gets overwritten
                loop_counter += 1
                # np.savetxt("Day 6/DEBUG.txt", branch_room, fmt="%s", encoding="UTF-8")
                break

            # otherwise continue stepping the branch
            branch_facing = step_turtle(branch_room, branch_loc, branch_facing, True)
            # pprint_room(branch_room, branch_loc)

        # time.sleep(2)
        facing = step_turtle(room, curr_loc, facing, True)
        # pprint_room(room, curr_loc)
        print(f"loop number {i}/{visited_locs}")
    
    print(f"total possible loop-inducing obstacles: {loop_counter}")
    