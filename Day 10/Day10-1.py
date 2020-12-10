# Advent of Code 2020
# Day 10 Puzzle 1

# When connecting chargers togehter in order from smallest to largest, finds the list of differences between them

adapters = [0]

# Data input
with open('Day 10/Input_10.txt', 'r') as input_file:
    for l in input_file:
        adapters.append(int(l))

adapters.sort()
adapters.append(max(adapters)+3) # add the joltage of the device

differences = [None for x in range(len(adapters)-1)] # list of same length as adapters

# calculate differences
for i in range(0, len(adapters)-1):
    differences[i] = adapters[i+1]-adapters[i]

threes = differences.count(3)
ones = differences.count(1)

print("1-Jolt differences times 3-Jolt differences : ", threes*ones)