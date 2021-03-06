#Advent of Code 2020
# Day 1, puzzle 2

# Finds the product of the 3 numbers in a list which add to 2020

data = [] # empty list

# get input
with open('Day 1/Input_1.txt', 'r') as input_file:
    for l in input_file:
        data.append(int(l))

# loop through to find rows with product
def data_process(): # function so code can quit after answer is found
    for i in range(len(data)):
        for j in range(i+1, len(data)): # only scan data after row i to prevent doubling
            for k in range(j+1, len(data)): # only scan data after row j to prevent doubling
                if data[i] + data[j] + data[k] == 2020:
                    return data[i] * data[j] * data[k]
                

product = data_process()

print(product)