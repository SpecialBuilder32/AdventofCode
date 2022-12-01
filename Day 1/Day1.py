# Advent of Code 2022

# Start Time: 12:07 PM
# Pt 1 End Time: 12:37 PM
# Pt 2 End Time: 12:46 PM
# Total Time:  39min 24sec
    # I had completely forgotten how to handle Regex :(

# Part 1 - find highest Calorie carrying elf
import re

with open('Day 1/Day1_Input.txt', 'rt') as f:
    elf_calorie_lists = re.findall(r'((?:\w+\n?)+)', f.read()) # regex capture each portion of list
    total_elf_calories = []
    for elf in elf_calorie_lists:
        elf_list = [int(val) for val in elf.strip().split('\n')]
        total_elf_calories.append( sum(elf_list) )
    
    # find elf with most snacks
    most_calories = max(total_elf_calories)
    print(f'The most Caloric-dense Elf is carrying {most_calories} Calories')
    
    # Part 2 - find the top 3 elves calorie count
    total_elf_calories.sort()
    top_three = total_elf_calories[-3:]
    top_three_calories = sum(top_three)
    print(f'The total Calories carries by the top three Elves is {top_three_calories} Calories')
