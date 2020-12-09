# Advent of Code 2020
# Day 9 Puzzle 1

# Finds which number in a list is not the sum of any of the prior 25

PREAMBLE_LENGTH = 25
numbers = []
sums = []

# Input numbers and process
with open('Day 9/Input_9.txt', 'r') as input_file:
    for n in input_file:
        numbers.append(int(n))

# calculate list of sum for faster searching than brute force solution
for i in range(len(numbers)):
    #points prior
    start = 0
    if i > PREAMBLE_LENGTH: # after the end of the preamble, stop looking further back than needed
        start = i - PREAMBLE_LENGTH
    
    s = set()
    # for each point prior
    for j in range(start, i):
        s.add(numbers[i]+numbers[j])
    
    sums.append(s)

def join_sets(list):
    total_set = set()
    for s in list:
        total_set.update(s)
    return total_set

# starting at the PREAMBLE_LENGTH-th index, find the first number that doesn't appear in sums
for i in range(PREAMBLE_LENGTH, len(numbers)):        
    if numbers[i] in join_sets(sums[i-PREAMBLE_LENGTH:i]):
        continue # to next for loop iteration
    
    else: # number was not in set!
        print("The first incorrect number is : ", numbers[i])
        break # from the for loop

