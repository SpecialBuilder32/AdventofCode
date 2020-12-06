# Advent of Code 2020
# Puzzle 2

# Counts customs declaration items of people of various sized groups

import string

# input data
with open('Day 6/Input_6.txt', 'r') as input_file:
    # parse input data into lists of each persons entries
    groups = [g.split('\n') for g in input_file.read().split('\n\n')]

counts = [] # empty list of group counts

# calculate logical intersection of each groups members lists
for group in groups:
    s = set(string.ascii_lowercase) # master set to accumulate intersections
    for member in group:
        s &= set(member) # intersection of member with previous members
    counts.append(len(s))

# print results
print("Sum of all group counts: ", sum(counts))