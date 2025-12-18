# Advent of Code 2025
# Day 9 - Floor tile analysis

# Pt 1 Start TIme: 8:30 AM
# Pt 1 End Time: 8:38 AM (8 min)        ... I'm suspicious of how easy that was and how terrible pt 2 might be

from itertools import product

with open("Day 9\Day9_Input.txt", "rt") as f:
    redtiles = (tuple(map(int, line.split(","))) for line in f.readlines()) # read input into tuple[int] (form of generator)


largest_area = 0
for (aX, aY), (bX, bY) in product(redtiles, repeat=2):
    rect_area = (abs(aX-bX)+1) * (abs(aY-bY)+1)
    if rect_area > largest_area:
        largest_area = rect_area
        largest_corners = ((aX, aY), (bX, bY))

print(f"Pt 1: Largest tile area is {largest_area} large, from {largest_corners}")
