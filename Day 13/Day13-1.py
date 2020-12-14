# Advent of Code 2020
# Day 13 Puzzle 1

# Finds the earliest possible bus that could be taken after the specified time

# input data
with open('Day 13/Input_13.txt', 'r') as input_file:
    lines = input_file.readlines()
    arrival_time = int(lines[0])
    # read in time ID, and calculate modulus with arrival time
    buses = [ [int(x), int(x)-arrival_time%int(x)] for x in lines[1].replace('x,', '').split(',')]

# find minimum wait time
min_wait = 1e10
min_ID = -1
for bus in buses:
    if bus[1] < min_wait:
        min_wait = bus[1]
        min_ID = bus[0]

# print result
print("First Bus * Wait Time :", min_wait * min_ID)
