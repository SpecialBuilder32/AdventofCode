# Advent of Code 2020
# Day 11 Puzzle 2

# Models how seats are filled and abandoned based on a more complex set of rules.

import copy
seats = []

# Read in seat arrangement
with open('Day 11/Input_11.txt', 'r') as input_file:
    for line in input_file:
        seats.append(list(line.rstrip('\n')))

# function to check if the index is within the seating arrangement
def within_bounds(seats, x, y):
    return x>=0 and y>=0 and y<len(seats) and x<len(seats[y])

# function to check if an occupied seat is visible in a given direction
def check_direction_occupied(seats, x, y, dx, dy):
    x += dx
    y += dy
    while within_bounds(seats, x, y): # loop till the end of the seats
        if seats[y][x] == "#":
            return True # found occupied seat
        elif seats[y][x] == "L":
            return False # found a vacant seat, and can't see nay further
        x += dx
        y += dy
    return False # if no occupied seat is found


# function to count occupied seats nearby to specified seat
def count_visible_occupied(seats, x, y):
    occupied = 0
    occupied += check_direction_occupied(seats, x, y, 0, -1) #up
    occupied += check_direction_occupied(seats, x, y, 0, +1) #down
    occupied += check_direction_occupied(seats, x, y, -1, 0) #left
    occupied += check_direction_occupied(seats, x, y, +1, 0) #right
    
    occupied += check_direction_occupied(seats, x, y, +1, -1) #upright
    occupied += check_direction_occupied(seats, x, y, +1, +1) #downright
    occupied += check_direction_occupied(seats, x, y, -1, +1) #downleft
    occupied += check_direction_occupied(seats, x, y, -1, -1) #upleft

    return occupied

# function that calculates and updates the seats after one time interval
def apply_rules(seats):
    new_seats = copy.deepcopy(seats) # make an complete copy to store the new arrangement of seats into.
    changes = 0

    for y in range(len(seats)): # for each row
        for x in range(len(seats[y])): # for each column in that row
            if seats[y][x] in ("L", "#"): # if a seat
                # if there are no occupied neighbors, fill
                if seats[y][x] == "L" and count_visible_occupied(seats, x, y) == 0:
                    new_seats[y][x] = "#"
                    changes += 1
                # if 4 or more occupied neighbors, vacate
                if seats[y][x] == "#" and count_visible_occupied(seats, x, y) >= 5:
                    new_seats[y][x] = "L"
                    changes += 1

    # print("-"*25)
    # for row in new_seats:
    #     print("".join(row))

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
