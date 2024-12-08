# Advent of Code 2024

# Start Time: 10:24 AM
            
# Pt 1 End Time: 10:54 AM   
# Pt 2 End Time: 11:07 AM

# Total Time: 43 Min

# Part 1 - tower antinode location
import numpy as np
import itertools
import math

m = []
with open("Day 8/Day8_Input.txt", "r") as f:
    for line in f.readlines():
        m.append(list(line.strip()))
    m = np.array(m)

    def within(c: tuple[int]):
        a, b = c
        return a >= 0 and b >= 0 and a < m.shape[0] and b < m.shape[1]

    freqs = set(np.unique(m)) - {'.'}
    antinode_locs = set()
    for f in freqs:
        coords = zip(*np.where(m==f))
        for a, b in itertools.combinations(coords, 2):
            v = (b[0]-a[0], b[1]-a[1])
            n1 = (b[0]+v[0], b[1]+v[1])
            n2 = (a[0]-v[0], a[1]-v[1])
            if within(n1):
                antinode_locs.add(n1)
            if within(n2):
                antinode_locs.add(n2)
    
    # for n in antinode_locs:
    #     m[n] = "#"
    print(f"number of antinodes: {len(antinode_locs)}")

# Part 2 - more vector additions! horray
    antinode_locs2 = set()
    for f in freqs:
        coords = zip(*np.where(m==f))
        for a, b in itertools.combinations(coords, 2):
            a = np.array(a)
            b = np.array(b)
            v = a-b
            reduce_f = math.gcd(*v)
            v //= reduce_f

            i = 0
            while within(n:=(i*v + a)):
                antinode_locs2.add(tuple(n))
                i += 1
            i = 0
            while within(n:=(-i*v + b)):
                antinode_locs2.add(tuple(n))
                i += 1
    
    # for n in antinode_locs2:
    #     m[n] = "#"
    # print(m)
    print(f"number of resonant antinodes: {len(antinode_locs2)}")