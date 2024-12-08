# Advent of Code 2024

# Start Time: 7:55 PM

# Pt 1 End Time: 8:12 PM
# Pt 2 End Time: 8:18 PM

# Total Time: 23 min

# Part 1 - brute forcing equation operators
import re
from itertools import product
from operator import mul, add
import math

with open("Day 7/Day7_Input.txt", "r") as f:
    valid_tols = 0
    calib_tol = 0
    for line in f.readlines():
        g = re.match(r"(\d+):(.+)", line)
        tol = int(g.group(1))
        comp = list(map(int, g.group(2).strip().split(" ")))

        #try every combination of * and + and check which meet the total
        op_iter = product([mul, add], repeat=len(comp)-1)
        for op_seq in op_iter:
            test_tol = comp[0]
            # evaluate the value
            for op, a in zip(op_seq, comp[1:]):
                test_tol = op(test_tol, a)
            if test_tol == tol:
                valid_tols += 1
                calib_tol += tol
                break
    
    print(f"sum of correct equations = {calib_tol}")

# Part 2 - a secret third option!
def cat(a: int, b: int) -> int:
    #12 || 345 = 12345
    p = math.floor(math.log10(b))+1 # number of place values to shift a by
    a *= 10**p
    return a+b

with open("Day 7/Day7_Input.txt", "r") as f:
    valid_tols = 0
    calib_tol = 0
    for line in f.readlines():
        g = re.match(r"(\d+):(.+)", line)
        tol = int(g.group(1))
        comp = list(map(int, g.group(2).strip().split(" ")))

        #try every combination of * and + and check which meet the total
        op_iter = product([mul, add, cat], repeat=len(comp)-1)
        for op_seq in op_iter:
            test_tol = comp[0]
            # evaluate the value
            for op, a in zip(op_seq, comp[1:]):
                test_tol = op(test_tol, a)
            if test_tol == tol:
                valid_tols += 1
                calib_tol += tol
                break
    
    print(f"sum of correct equations, but with cat = {calib_tol}")
        