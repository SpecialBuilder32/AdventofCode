# Advent of Code 2025
# Day 4

# Pt 1 Start Time: 11:36 PM
# Pt 2 Start Time: 11:56 PM (20min)

import numpy as np
from scipy.signal import convolve2d

# Forklift searching? This is just convolution! 

# read map and make np array
with open("Day 4/Day4_Input.txt", "rt") as f:
    warehouse = []
    for line in f.readlines():
        warehouse.append(list(map(int, line.replace(".", "0").replace("@", "1").strip())))
    warehouse = np.array(warehouse)
    print("input parsed...")

pt1_done = False
cleared_cells = 0
while True:
    # convolve to count neighbors
    neighbor_mask = np.array([[1,1,1], [1,0,1], [1,1,1]])
    neighbor_map = convolve2d(warehouse, neighbor_mask, mode='same')

    # count occupied cells with <4 neighbors
    accessible_map = (neighbor_map<4).astype(int) * warehouse
    accessible_cells = np.count_nonzero(accessible_map)
    # print(accessible_map)

    if not pt1_done:
        print(f"Pt 1: There are {accessible_cells} rolls a forklift can access")
        pt1_done = True

    # PT 2: Now remove the accessible cellsand  try again!
    warehouse -= accessible_map
    cleared_cells += accessible_cells

    if accessible_cells == 0:
        break

print(f"Pt 2: There are {cleared_cells} rolls a forklift can access and remove later")