# Advent of Code 2024

# Start Time: 10:47 AM

# Pt 1 End Time: 11:34 AM
# Pt 2 End Time:

# Total Time:


# Part 1 - Box pushing grid
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
            case "O":
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
