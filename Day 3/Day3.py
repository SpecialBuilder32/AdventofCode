# Advent of Code 2024

# Start Time: 10:43 PM
# Pt 1 End Time: 10:55 PM
# Pt 2 End Time: 11:11 PM

# Total Time: 28 Min

# Part 1 - regex searching for "uncorrupted" syntax
import re

with open("Day 3/Day3_Input.txt", "r") as f:
    prog = f.read()
    tol = 0
    for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", prog):
        tol += int(a) * int(b)
    
    print(f"corrected program output = {tol}")

# Part 2 - regex pro mode, conditionals!
    # okay I can't figure out the regex golf conditions that check for both the most recent do() or don't() and see which is closer,
    # look-aheads are weird and I do not understand them

    tol = 0
    do = True
    for seg in re.split(r"(do\(\)|don't\(\))", prog):
        if seg == "do()":
            do = True
        elif seg == "don't()":
            do = False
        else:
            if do:
            # use same pattern as before
                for a, b in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", seg):
                    tol += int(a) * int(b)

    print(f"accounting for conditionals. output = {tol}")                
