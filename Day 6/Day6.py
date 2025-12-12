# Advent of Code 2025
# Day 6 - Cephalapod Mathematics!

# Pt 1 Start Time: 10:16 PM
# Pt 1 End Time: 11:07 PM

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