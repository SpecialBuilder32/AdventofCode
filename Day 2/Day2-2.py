# Adent of Code 2020
# Day 2, Puzzle 2

# determines if a particular passowrd meets requirements for letter position 
import re # regex library


valid_passwords = 0

# get input file and loop through data
with open('Day 2/Input_2.txt', 'r') as input_file:
    for line in input_file:

        # regex to separate line into required format and password data
        pattern = re.compile(r'(\w+)-(\w+).(.):.(.+)')
        grouped_line = pattern.match(line)
        
        # pull specifics from grouped line
        pos1 = int(grouped_line.group(1))
        pos2 = int(grouped_line.group(2))
        character = grouped_line.group(3)
        password = grouped_line.group(4)

        # see if password meets requirements
        char1_match = password[pos1-1]==character # boolean for if the index matches characterr
        char2_match = password[pos2-1]==character

        if char1_match != char2_match: # XOR for exactly 1 match to be valid
            valid_passwords += 1 # increment counter

# print final correct count
print("Number of valid Passwords: ", valid_passwords)