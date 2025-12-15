# Advent of Code 2025
# Day 7 - Tachyon beam splitting

# Pt 1 Start Time: 1:37 PM
# Pt 2 End Time: 2:06 PM (29 min)
# Pt 2 Start Time: 2:13 PM
# Pt 2 End Time: 2:44 PM (31 min)

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
no_timelines = 1 # initial beam
beams = {start_beam}
pt2_beams = {start_beam: 1} # pt2 tracks how many "timelines" each beam could take, ie multiple beams occupy the same space {idx: count}
for y,x in splitters: # we don't actually need the y coord, since splitters is already sorted by that index
    # print(f"processing splitter {(y,x)}, {len(pt2_beams)=}")
    x = int(x)
    if x in beams: # a beam will hit this splitter
        beams -= {x}
        beams |= {x-1,x+1}
        no_splits += 1
        # print(f"splitting beam {x} into {x+1},{x-1}")

        # pt2 beams in the same space
        curr_beams = pt2_beams.get(x, 0)
        no_timelines += curr_beams # each beam hitting this splitter is a new future
        existing_beams = pt2_beams.setdefault(x+1, 0)
        pt2_beams[x+1] = existing_beams + curr_beams
        existing_beams = pt2_beams.setdefault(x-1, 0)
        pt2_beams[x-1] = existing_beams + curr_beams
        del pt2_beams[x]

print(f"Pt 1: The beam was split {no_splits} times")
print(f"Pt 2: The beam took {no_timelines} possible paths/timelines")




# Pt 2: alternate timelines. Each splitter splits the timeline and the particle continues on each side alone.
    # we could BFS this, but I think we can be smarter with the results from pt 1 and scanning upward

# no_timelines = len(beams) # each end-beam is at least one timeline-path

# prev_row_beams = beams.copy()
# num_splitter_rows = len(manifold_map)//2 - 1
# for row in range(2*num_splitter_rows-1, 0, -2):
#     for beam in beams:
#         if (row,beam+1) in used_splitters and (row,beam-1) in used_splitters: # two beams split into the same position
#             no_timelines += 1

#         if (row,beam+1) in used_splitters:



#     beams = prev_row_beams.copy()

## Actually, this won't account for beams incoming from a higher level. Instead I'll just modify pt 1 to count how many coexisting beams there
# are at each location, since each of those is a possible future.