# Advent of Code 2020
# Day 3, Puzzle 2

# Counts how many trees are encountered at a range of angles in an infinitely repeating forest

forest = [] # empty list to contain map

class slope(): # class to keep track of slope data neatly
    def __init__(self, dy, dx):
        self.dy = dy
        self.dx = dx
        self.encountered_trees = 0

# list of slopes to check
slopes = [slope(1,1), slope(1,3), slope(1,5), slope(1,7), slope(2,1)] # [down, right]
product = 1

# read "forest map" in from file
with open('Day 3/Input_3.txt', 'r') as input_file:
    for l in input_file:
        forest.append(l.rstrip('\n')) # add forest row to list

    width = len(forest[0]) # width of repeating segment
    length = len(forest) # length of forest (num of rows)

# traverse at various angles and count trees
for s in slopes:
    # at each particlar slope
    x = 0
    for y in range(0, length, s.dy): # step through forest rows
        # check for tree
        if forest[y][x] == '#':
            s.encountered_trees += 1 # increment counter

        # increment x according to slope value
        x += s.dx
        if x >= width: # if past index edge, wrap back around
            x -= width

    print(s.encountered_trees)
    product *= s.encountered_trees

# print results
print("Product of Trees Encountered at all Angles: ", product)


