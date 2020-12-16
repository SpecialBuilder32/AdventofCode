# Advent of Code 2020
# Day 16 Puzzle 1

# Reads in ticket data and finds invalid ticket data
import re

class rule():
    def __init__(self, line):
        grouped_line = re.match(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', line)
        self.field = grouped_line.group(1)
        self.range = [ [int(grouped_line.group(2)), int(grouped_line.group(3))], [int(grouped_line.group(4)), int(grouped_line.group(5))] ]

    def within_range(self, num):
        return (num >= self.range[0][0] and num <= self.range[0][1]) or (num >= self.range[1][0] and num <= self.range[1][1])

class ticket():
    def __init__(self, line):
        self.values = [int(x) for x in line.split(',')]

rules = [] # list for rules
tickets = [] # list for tickets

# input file
with open('Day 16/Input_16.txt', 'r') as input_file:
    lines = input_file.read()
    grouped_input = re.match(r'((?:.+\n)+?)\nyour ticket:\n(.+)\n\nnearby tickets:\n((?:.+(?:\n|$))+)', lines)
    
    # read in rules
    for line in grouped_input.group(1).rstrip('\n').split('\n'):
        rules.append(rule(line)) # parse in rules

    # read in tickets
    for line in grouped_input.group(3).split('\n'):
        tickets.append(ticket(line))

# process tickets, looking for invalid numbers
invalid_values = []

for t in tickets:
    for v in t.values:
        validity = 0
        for r in rules: # check each value against each rule
            validity += r.within_range(v) # if value is within the rule, add to accumulator
        
        if validity == 0: # did not fit any range
            invalid_values.append(v)

# print error rate
print("Ticket Scanning Error Rate: ", sum(invalid_values))
            