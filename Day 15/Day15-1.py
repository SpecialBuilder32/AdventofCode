# Advent of Code 2020
# Day 15 puzzle 1

# Processes a list of numbers in a game

# "Hardcode input" since its so small
numbers = [17,1,3,16,19,0]
indexes = {} # dictionary to keep track of the last time a number was spoken

# init indexes
for i in range(len(numbers)-1):
    indexes[numbers[i]] = i

# start processing list
for i in range(len(numbers)-1, 2020): # iterate until the 2020'th number

    if numbers[i] in indexes: # if the number was already spoken
        n = i - indexes[numbers[i]]
        numbers.append(n)
    
    else: # otherwise the number is new
        numbers.append(0)

    # update index of previous number
    indexes[numbers[i]] = i

# print final number
print(numbers[2019])
