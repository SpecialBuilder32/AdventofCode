# Advent of Code 2020
# Day 7, Puzzle 2

# Calculates the total number of bags held within the shiny gold bag, analyizing a huge list of rules describing such

import re

bags = {} # dict of all bags

class bag():
    def __init__(self, color, contents):
        self.color = color
        self.contents = contents

# import rules
with open('Day 7/Input_7.txt', 'r') as input_file:
    for rule in input_file:
        grouped_rule = re.match(r'(.+) bags contain (.+)', rule) # parse out bag color from contents
        
        color = grouped_rule.group(1)
        raw_contents = grouped_rule.group(2).rstrip('.').split(', ')
        contents = {}

        if 'no other bag' not in raw_contents[0]: # unless the bag is an innermost bag
            for inner_bag in raw_contents: # get list of potential contents
                grouped_bag = re.match(r'(\d+) (.+) bags?', inner_bag) # parse inner bag color from contents
                
                contents.update({grouped_bag.group(2) : int(grouped_bag.group(1))}) # add dict entry of contents

        bags.update({color: bag(color, contents)}) # create bag object and add to the list

# recursive function to traverse down the rabbit hole of bags
def count_contents(bag_dict):
    total_contents = 0
    for color in bag_dict:
        total_contents += bag_dict[color] + bag_dict[color] * count_contents(bags[color].contents) # send inner bag contents back into recursive function
    return total_contents

# print results
print("Bags contained within the Shiny Gold bag: ", count_contents({'shiny gold': 1}) -1 ) # don't include the gold bag itself