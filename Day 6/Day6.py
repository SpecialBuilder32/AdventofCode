# Advent of Code 2025
# Day 6 - Cephalapod Mathematics!

# Pt 1 Start Time: 10:16 PM
# Pt 1 End Time: 11:07 PM
# Pt 2 Start Time: 5:43 PM
# Pt 2 End Time: 5:59 PM (16 min)

import re
from dataclasses import dataclass
from typing import Literal
from math import prod

with open("Day 6/Day6_Input.txt", 'rt') as f:
    intext = f.readlines()

@dataclass
class Problem():
    values: list[int]
    op: Literal["*","+",None] = None

    def op_func(self):
        if self.op == "*":
            return prod
        elif self.op == "+":
            return sum

# parse input
repattern = r" *?(\d+?) *?[ \n]"
first_line_matches = re.findall(repattern, intext[0])
problems = [Problem([int(match)], None) for match in first_line_matches]
            
for line in intext[1:-1]: # for remaining lines
    for new_val, problem in zip(re.finditer(repattern, line), problems):
        problem.values.append(int(new_val.group(0)))

for op, problem in zip(re.finditer(r"[\*\+]", intext[-1]), problems):
    problem.op = op.group(0).strip()

# process problems
total_sol = 0
for problem in problems:
    total_sol += problem.op_func()(problem.values)

print(f"Pt1: Total problems sum {total_sol}")

# part 2 requires re-parsing entirely
columns = zip(*intext[0:-1])
ops = iter(intext[-1].split())

pt2_problems = []
curr_prob = Problem([])
for column in columns:
    if all(e in (" ","\n") for e in column):
        # end of current problem
        curr_prob.op = next(ops)
        pt2_problems.append(curr_prob)
        curr_prob = Problem([])
        continue

    # otherwise its a value
    curr_prob.values.append(int("".join(column)))

# print(pt2_problems)
# process problems
total_sol_pt2 = 0
for problem in pt2_problems:
    total_sol_pt2 += problem.op_func()(problem.values)

print(f"Pt2: Total problems sum {total_sol_pt2}")
