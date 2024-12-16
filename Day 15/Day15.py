# Advent of Code 2024

# Start Time: 10:47 AM

# Pt 1 End Time: 11:34 AM
# Pt 2 End Time: 12:18 PM

# Total Time: 47min + 44min


## Part 1 - Box pushing grid
import numpy as np

with open("Day 15/Day15_Input.txt", "r") as f:
    # reading in map
    l = []
    while True:
        line = f.readline()
        if line[0] == "\n":
            break # we've reached the end of the grid
        l.append(list(line.strip()))
    warehouse = np.array(l)
    warehouse_input = warehouse.copy()

    # reading in instructions
    instructions = []
    for line in f.readlines():
        instructions.extend(list(line.strip()))

bot = np.argwhere(warehouse == "@")[0]

step_map = {
    "^": np.array((-1,0)),
    ">": np.array((0,1)),
    "v": np.array((1,0)),
    "<": np.array((0,-1))
}

def step_bot(warehouse, inst: str, bot: np.array) -> np.array:
    # process a single instruction on the warehouse, inplace. Returns new bot position
    dir = step_map[inst]

    ck_pos = bot+dir
    spaces_to_move = [bot]
    while True:
        # check that direction for things to move
        match warehouse[*ck_pos]:
            case "#":
                return bot # we've hit a wall, nothing can move
            case ".":
                break # we've found an empty space, proceed to moving elements
            case "O"|"]"|"[":
                # we've found a box we need to move
                spaces_to_move.append(ck_pos.copy())
        ck_pos += dir

    # now move the things we found
    for spc in reversed(spaces_to_move):
        warehouse[*spc+dir] = warehouse[*spc]
    warehouse[*bot] = "."
    return bot+dir

def print_warehouse(warehouse):
    print("—"*len(warehouse[0]))
    for row in warehouse:
        print("".join(row))


# Run the robot's instructions!
for inst in instructions:
    bot = step_bot(warehouse, inst, bot)
    
print_warehouse(warehouse)

# Compute the CPS score
score = 0
for box in np.argwhere(warehouse=="O"):
    score += np.sum(box*[100, 1])
print(f"Final warehouse box score: {score}")


## Part 2 - Boxes got wider! Now we have to consider a bunch of possible collision points in our movement.

# form expanded warehouse from original imput
warehouse = np.empty((warehouse_input.shape[0], 2*warehouse_input.shape[1]), dtype=str)
replacements = {
    "#": ["#", "#"],
    "O": ["[", "]"],
    ".": [".", "."],
    "@": ["@", "."]
}
for (x,y), tile in np.ndenumerate(warehouse_input):
    warehouse[x,2*y:2*y+2] = replacements[tile]
bot = np.argwhere(warehouse == "@")[0]

box_map = {
    "[": np.array((0,1)),
    "]": np.array((0,-1))
}
def step_wide_bot(warehouse, inst: str, bot: np.array) -> np.array:
    # similar to step_bot, except for wide boxes that can be stopped by multiple collision points
    dir = step_map[inst]

    if inst in (">", "<"):
        # no fancy logic, apply prior step algorithm
        return step_bot(warehouse, inst, bot)

    spaces_to_move = [bot]
    spaces_to_check = [bot+dir]
    while len(spaces_to_check)>0:
        last_spaces_to_check = spaces_to_check.copy()
        spaces_to_check.clear()
        for ck_pos in last_spaces_to_check:
            match (c:=warehouse[*ck_pos]):
                case "#":
                    return bot # we've hit a wall, nothing can move
                case ".":
                    continue # we've found an empty space
                case "["|"]":
                    # we've found a box we need to move
                    spaces_to_move.extend((ck_pos.copy(), ck_pos+box_map[c]))
                    # add their branched dependencies to the check list
                    spaces_to_check.extend((ck_pos+dir, ck_pos+box_map[c]+dir))

    # now move the things we found
    spaces_moved_to = set()
    for spc in reversed(spaces_to_move):
        warehouse[*spc+dir] = warehouse[*spc] # move each space
        spaces_moved_to.add(tuple(spc+dir))
    spaces_to_move = {tuple(e) for e in spaces_to_move}
    for spc in spaces_to_move-spaces_moved_to: # now for any space left empty
        warehouse[*spc] = "."
    return bot+dir

# Run the robot's instructions!
for inst in instructions:
    bot = step_wide_bot(warehouse, inst, bot)
    
print_warehouse(warehouse)

# Compute the CPS score
score = 0
for box in np.argwhere(warehouse=="["):
    score += np.sum(box*[100, 1])
print(f"Final wide warehouse box score: {score}")