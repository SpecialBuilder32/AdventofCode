# Adent of Code 2020
# Day 2, Puzzle 1

# determines if a particular passowrd meets requirements for letter count 
import re # regex library


valid_passwords = 0

# get input file and loop through data
with open('Day 2/Input_2.txt', 'r') as input_file:
    for line in input_file:

        # regex to separate line into required format and password data
        pattern = re.compile(r'(\w+)-(\w+).(.):.(.+)')
        grouped_line = pattern.match(line)
        
        # pull specifics from grouped line
        min_count = int(grouped_line.group(1))
        max_count = int(grouped_line.group(2))
        character = grouped_line.group(3)
        password = grouped_line.group(4)

        # see if password meets requirements
        char_count = password.count(character)

        if min_count <= char_count and max_count >= char_count:
            valid_passwords += 1 # increment counter

# print final correct count
print("Number of valid Passwords: ", valid_passwords)