# Advent of Code 2025
# Day 7 - Tachyon beam splitting

# Pt 1 Start Time: 1:37 PM
# Pt 2 End Time: 2:06 PM

import numpy as np

with open("Day 7/Day7_Input.txt", "rt") as f:
    manifold_map = f.readlines()

# locate splitters and start beam
start_beam = manifold_map[0].index("S")

    # use numpy because .where is nice for locating all splitters at once
np_manifold_map = np.array([list(e.strip()) for e in manifold_map[1:]], dtype="U")
splitters = np.argwhere(np_manifold_map=="^") # already sorted by y-index increasing


# flow down map, tracking where beams wind up
no_splits = 0
beams = {start_beam}
for _,x in splitters: # we don't actually need the y coord, since splitters is already sorted by that index
    x = int(x)
    if x in beams: # a beam will hit this splitter
        beams -= {x}
        beams |= {x-1,x+1}
        no_splits += 1
        # print(f"splitting beam {x} into {x+1},{x-1}")

print(f"Pt 1: The beam was split {no_splits} times")
