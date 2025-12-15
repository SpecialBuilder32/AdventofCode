# Advent of Code 2025
# Day 8 - Junction box christmas light spiderwebs

# Pt 1 Start Time: 3:28 PM - 4:00 PM

import numpy as np
from itertools import product

juncboxes = []
with open("Day 8/Day8_Input.txt", "rt") as f:
    for line in f.readlines():
        juncboxes.append(np.array(list(map(int, line.strip().split(",")))))

# compute distances as a matrix
l = len(juncboxes)
# distances_matrix = np.subtract.outer(juncboxes, juncboxes) # theres some way to do this efficiently with this, but I couldnt figure it out
distances_matrix = np.zeros((l,l))
for x,y in product(juncboxes, repeat=2)