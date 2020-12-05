# Advent of Code 2020
# Day 5, Puzzle 2

# Calculates seat numbers from a strange numbering mechanism, and finds the missing one

seat_IDs = [] # list for seat IDs

# input file
with open('Day 5/Input_5.txt', 'r') as input_file:
    for seat in input_file:
        row = int(seat[0:7].replace('F', '0').replace('B', '1'), 2) # convert letters to binary and translate
        col = int(seat[7:10].replace('L', '0').replace('R', '1'), 2)
        seat_ID = 8 * row + col
        seat_IDs.append(seat_ID)

# loop through list and find the missing seat
for i in range(min(seat_IDs), max(seat_IDs)+1): # we know the end seats are filled
    if i not in seat_IDs:
        print("Unfilled Seat :", i)