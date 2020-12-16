# Advent of Code 2020
# Day 16 Puzzle 2

# Reads in ticket data, removes invalid tickets, and figures out the labels for stuff
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

    # read in my tickets
    my_ticket = ticket(grouped_input.group(2))

    # read in tickets
    for line in grouped_input.group(3).split('\n'):
        tickets.append(ticket(line))

# process tickets, removing invalid tickets
for t in tickets.copy(): # copy to allow for loop to complete properly
    for v in t.values:
        validity = 0
        for r in rules: # check each value against each rule
            validity += r.within_range(v) # if value is within the rule, add to accumulator
        
        if validity == 0: # did not fit any range
            tickets.remove(t) # discard this ticket
            break # from the v for loop

field_names = [r.field for r in rules] 
possible_fields = []
# list keeping track of all possible fields for each position
for i in range(len(my_ticket.values)):
    possible_fields.append(field_names.copy())

# deduce field position on ticket
for i in range(len(my_ticket.values)): # for each value in the same position of each ticket
    for t in tickets:
        # check this tickets i'th value against all the rules
        for r in rules:
            if not r.within_range( t.values[i] ): # if the value is not in the range, this rule can't be in this position
                try: # incase the field has already been removed
                    possible_fields[i].remove(r.field) # remove the field name from the list
                except:
                    pass # nothing to catch

# go through the list and look (hope) for positions with only one possible field
correct_fields = [None]*len(field_names)
while True:
    for i in range(len(possible_fields)):
        if len(possible_fields[i]) == 1: # only one item is in this position!
            correct_fields[i] = possible_fields[i][0]
            # remove this field from the other positions. 
            for l in possible_fields:
                try: # incase the field wasn't there to begin with
                    l.remove(correct_fields[i])
                except:
                    pass # nothing to catch

    if not None in correct_fields: # we've deduced all the way!
        break # from the while loop

# print results
print("Field Ordering: ", correct_fields)

# find the puzzle answer
product = 1
for i in range(len(correct_fields)):
    if correct_fields[i].split(' ')[0] == 'departure':
        product *= my_ticket.values[i]

print("Puzzle Output: ", product)

