# Advent of Code 2020
# Day 9 Puzzle 2

# Finds the continous set of numbers which add up to the solution for part 1

PREAMBLE_LENGTH = 25
numbers = []
sums = []

# Input numbers and process
with open('Day 9/Input_9.txt', 'r') as input_file:
    for n in input_file:
        numbers.append(int(n))

# calculate list of sums for faster searching than brute force solution
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
        invalid_number = numbers[i]
        break # from the for loop


# now start looking for the continious set
for i in range(len(numbers)):
    j = 0
    current_sum = numbers[i]
    while current_sum < invalid_number: # if the sum exceeds the number the continous set can't be right
        j += 1
        current_sum += numbers[i+j]

        if current_sum == invalid_number: # we found the range!
            cont_range = numbers[i:i+j+1]
            print("Continious Range: ", cont_range)
            print("Largest in Range: ", max(cont_range), "   Smallest in Range: ", min(cont_range))
            print("Encryption Weakness: ", max(cont_range)+min(cont_range))

