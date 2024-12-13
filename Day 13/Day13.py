# Advent of Code 2024

# Start Time: 10:37 AM

# Pt 1 End Time: 11:37 AM (only due to bizzare math ..bug?)
# Pt 2 End Time: 11:45 AM

# Total Time: 1hr 8min

# Part 1 - Our first optimization problem of the year
    # sike no optimization yet - this be pure linear algebra.

import re
import numpy as np

with open("Day 13/Day13_Input.txt", "r") as f:
    text = f.read()

cost = 0
cost2 = 0
button_costs = np.array([3,1])
for g in re.findall(r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", text):
    ax, ay, bx, by, px, py = map(int, g)
    M = np.matrix([[ax, bx],[ay, by]]) # transform matrix solves for required presses of each button
    presses = np.linalg.inv(M)@np.matrix([[px],[py]])

    # for some unknown reason, numpy is returning 1 for some integers n%1, which really shouldn't be the case
        # but i guess I'll just check for that?
    dec = np.mod(presses, 1)

    if np.all(np.logical_or(dec < 1e-12, dec > 0.999)) and np.all(presses > 0): # positive whole number of presses - a solution exists
        cost += np.sum(button_costs*presses)


    # pt 2
    presses2 = np.linalg.inv(M)@np.matrix([[px+10_000_000_000_000],[py+10_000_000_000_000]])
    dec2 = np.mod(presses2, 1)
    # due to precision drift, we've got to loosen tolerances on the "is a whole number" test
    if np.all(np.logical_or(dec2 < 1e-4, dec2 > 0.99)) and np.all(presses2 > 0): # positive whole number of presses - a solution exists
        cost2 += np.sum(button_costs*presses2)

print(f"Cost to win the most prizes: {cost:.0F} tokens")
print(f"Cost to win the most prizes, with big boi offset: {cost2:.0F} tokens")

# Part 2 - whoops theres a giant offset in the target! Good thing I didn't brute force this, but hopefully I'll have enough precision still
    # done inline with the for loop above
