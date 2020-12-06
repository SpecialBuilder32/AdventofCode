# Advent of Code 2020
# Puzzle 1

# Counts customs declaration items of people of various sized groups

# input data
with open('Day 6/Input_6.txt', 'r') as input_file:
    # split the input file on empty lines, remove newlne characters, cast to set, find length
    counts = [len(set(l.replace('\n', ''))) for l in input_file.read().split('\n\n')]

# print sum of counts
print("Sum of all group counts: ", sum(counts))