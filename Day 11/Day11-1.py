# Advent of Code 2020
# Day 11 Puzzle 1

# Models how seats are filled and abandoned based on a simple set of rules.

import copy
seats = []

# Read in seat arrangement
with open('Day 11/Input_11.txt', 'r') as input_file:
    for line in input_file:
        seats.append(list(line.rstrip('\n')))

# function to allow for accessing of un-indexed coordinates without throwing exceptions
def check_seat(seats, x, y):
    try:
        if x < 0: # negative index would index from the end of the array, but we need it to error
            x = None
        if y < 0:
            y = None
        return seats[y][x]
    except:
        # the index dosen't exist, so we return a dummy value
        return None

# function to count occupied seats nearby to specified seat
def count_occupied(seats, x, y):
    occupied = 0
    occupied += check_seat(seats, x-1, y-1) == "#"
    occupied += check_seat(seats, x,   y-1) == "#"
    occupied += check_seat(seats, x+1, y-1) == "#"

    occupied += check_seat(seats, x-1, y) == "#"
    occupied += check_seat(seats, x+1, y) == "#"
    
    occupied += check_seat(seats, x-1, y+1) == "#"
    occupied += check_seat(seats, x  , y+1) == "#"
    occupied += check_seat(seats, x+1, y+1) == "#"

    return occupied

# function that calculates and updates the seats after one time interval
def apply_rules(seats):
    new_seats = copy.deepcopy(seats) # make an complete copy to store the new arrangement of seats into.
    changes = 0

    for y in range(len(seats)): # for each row
        for x in range(len(seats[y])): # for each column in that row
            if seats[y][x] in ("L", "#"): # if a seat
                # if there are no occupied neighbors, fill
                if seats[y][x] == "L" and count_occupied(seats, x, y) == 0:
                    new_seats[y][x] = "#"
                    changes += 1
                # if 4 or more occupied neighbors, vacate
                if seats[y][x] == "#" and count_occupied(seats, x, y) >= 4:
                    new_seats[y][x] = "L"
                    changes += 1

    return new_seats, changes

# loop through rules until steady-state is reached
c = 1 # dummy init value
while c > 0:
    seats, c = apply_rules(seats)

# count filled seats and print
filled_seats = 0
for row in seats:
    filled_seats += row.count("#")

print("Total Number of Filled Seats in Steady-State :", filled_seats)
