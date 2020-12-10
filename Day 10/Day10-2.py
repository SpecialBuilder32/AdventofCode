# Advent of Code 2020
# Day 10 Puzzle 2

# Counts the number of possible ways the large number of chargers could be connected together to power the device properly

#       This problem is simplified by the input, which seems designed to avoid complex special cases. There are no differences of 2 to consider, nor strings of 
#        incremental chargers (diff 1) longer than 5. 
#
#       Every charger that is 3 jolts from either neighbor is required in the chain of chargers, as there are no repeats. 
#       Any charger only 1 jolt from both neighbors is optional, unless it is a chain of 3 consecuitive optional chargers
#        You can't take all 3 consecuitive optional chargers out, otherwise the chain breaks, so you may only take any 2. (3 2) = 6 permutations, plus taking none. 7
#       
#       Every optional charger can be thought of as a bernoulii trial, doubling the paths (n)
#       Every 4-chain (3 consecutive optional chargers) instead increases the paths 7fold (m)
#           2^n * 7^m

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

# run through difference list and count optional chargers and 4-chains
n = 0
m = 0
i = 0
while i < len(differences):
    # check for 4 chain
    if differences[i:i+4] == [1,1,1,1]: # four chain, has a different impact on permutaations
        m += 1
        i += 4
    elif differences[i:i+2] == [1,1]: # regular optional value
        n += 1
        i +=1
    else:  
        i += 1

# possible chains
chains = 2**n * 7**m
print("Total possible valid charger chains: ", chains)
