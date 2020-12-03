# Advent of Code 2020
# Day 3, Puzzle 1

# Counts how many trees are encountered at a particular angle in an infinitely repeating forest

forest = [] # empty list to contain map
encountered_trees = 0
x = 0 # starting index coordinate

slope = 3 # 3 right, 1 down

# read "forest map" in from file
with open('Day 3/Input_3.txt', 'r') as input_file:
    for l in input_file:
        forest.append(l.rstrip('\n')) # add forest row to list

    width = len(forest[0]) # width of repeating segment

for row in forest:
    if row[x] == '#':
        encountered_trees += 1 # incrent counter

    # adjust by slope
    x += slope
    if x > width-1: # if off the given segment, wrap around to the other side
        x -= width

print("Trees Encountered: ", encountered_trees)