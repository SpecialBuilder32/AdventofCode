# Advent of Code 2020
# Day 15 puzzle 2

# Processes a list of numbers in a game, predicting a number far into the future
# This time, we don't need to keep all the list of numbers around, just the last couple

# "Hardcode input" since its so small
numbers = [17,1,3,16,19,0]
indexes = {} # dictionary to keep track of the last time a number was spoken
stop = 30000000

number = numbers[-1]
previous_number = numbers[-2]

# init indexes
for i in range(len(numbers)-1):
    indexes[numbers[i]] = i

# start processing list
for i in range(len(numbers)-1, stop-1): # iterate until the 2020'th number
    print(i, previous_number, number)

    if number in indexes: # if the number was already spoken
        n = i - indexes[number]
        previous_number = number
        number = n
    
    else: # otherwise the number is new
        previous_number = number
        number = 0

    # update index of previous number
    indexes[previous_number] = i

# print final number
print("Final Number: ", number)
