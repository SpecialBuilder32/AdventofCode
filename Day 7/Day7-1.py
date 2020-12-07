# Advent of Code 2020
# Day 7, Puzzle 1

# Analyzes a huge list of rules concerning the contents of various colored bags to find how many can hold a gold bag.

import re

gold_holding_bags = set() # set containing the bags that can contain either a gold bag, or any bag further down
bags = [] # list of all bags

class bag():
    def __init__(self, color, contents):
        self.color = color
        self.contents = contents

    def contains(self, list_to_check):
        # return true if any of the specified bags is contained within
        for b in list_to_check:
            if b in self.contents:
                return True

        return False # otherwise

# import rules
with open('Day 7/Input_7.txt', 'r') as input_file:
    for rule in input_file:
        grouped_rule = re.match(r'(.+) bags contain (.+)', rule) # parse out bag color from contents
        
        color = grouped_rule.group(1)
        raw_contents = grouped_rule.group(2).rstrip('.').split(', ')
        contents = []

        if 'no other bag' not in raw_contents[0]: # unless the bag is an innermost bag
            for inner_bag in raw_contents: # get list of potential contents
                grouped_bag = re.match(r'\d+ (.+) bags?', inner_bag) # parse inner bag color from contents
                contents.append(grouped_bag.group(1))

        bags.append(bag(color, contents)) # create bag object and add to the list

# find bags that can contain the gold
bags_to_check = {'shiny gold'}
new_bags = set()
while len(bags_to_check) > 0: # while there are still bags to check
    for b in bags:
        if b.contains(bags_to_check):
            new_bags.add(b.color) # add possible parent bags to a list

    bags_to_check = new_bags # update list of colors to find parents of
    gold_holding_bags.update(new_bags) # add found bags to master list
    new_bags = set() # empty new_bags

# print results
print("Total different bag colors that can hold gold: ", len(gold_holding_bags))
