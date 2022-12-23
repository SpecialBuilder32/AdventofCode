# Advent of Code 2022

# Start Time: 4:30p (22nd)
    # pause 5:33p - 7:52p
# Pt 1 End: 8:24p
# Pt 2 End: 
# Total Time:

# Sortof anti-triangulation

from functools import cached_property
import re
from dataclasses import dataclass
from typing import ClassVar

@dataclass
class SensorData():
    my_x: int
    my_y: int
    beacon_x: int
    beacon_y: int
    max_x: ClassVar[int] = -1e9
    min_x: ClassVar[int] = 1e9

    def __post_init__(self): # record bounds on x values as data comes in
        SensorData.max_x = max(self.my_x + self.coverage_distance, self.max_x)
        SensorData.min_x = min(self.my_x - self.coverage_distance, self.min_x)

    @cached_property
    def coverage_distance(self) -> int:
        return self.distance_to(self.beacon_x, self.beacon_y)

    def distance_to(self, other_x, other_y):
        return abs(self.my_x-other_x) + abs(self.my_y-other_y)

# read in beacon information
sensor_data = []
with open('Day 15/Day15_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

    for line in lines:
        m = map(int, re.match(r'Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)', line.strip()).groups())
        sensor_data.append( SensorData(*m) )

# Pt 1 - compute coverage of desired row
# pylint: disable=redefined-outer-name
def scan_row(row_y, hole_search=False, search_area=(SensorData.min_x, SensorData.max_x)):
    # scans a single row for number of covered spaces
    occupied_spaces = 0
    hole_x = None
    col_x = search_area[0]
    while col_x <= search_area[1]:
        for sensor in sensor_data:
            if sensor.coverage_distance >= sensor.distance_to(col_x, row_y):
                # compute horizontal distance this sensor covers of interest row
                slice_radius = sensor.coverage_distance - abs(row_y-sensor.my_y)
                # how much of this width do we have left to cover
                remaining_slice = slice_radius - (col_x - sensor.my_x) + 1
                
                # check if this sensor's beacon is in this row
                if sensor.beacon_y == row_y \
                    and sensor.beacon_x > col_x: # and we haven't counted it already
                    occupied_spaces -= 1 # we know a beacon is already here. 

                col_x += remaining_slice
                occupied_spaces += remaining_slice

                break
        else: # no sensor covered the space
            if hole_search:
                hole_x = col_x
            col_x += 1
    return occupied_spaces, hole_x

# INTEREST_ROW = 10
INTEREST_ROW = 2000000
pt1_sol, _ = scan_row(INTEREST_ROW)
print(f'Number of spaces in row {INTEREST_ROW} where a beacon cannot be is {pt1_sol}')

# Pt 2 - Now we search the entire grid for the only possible place the missing beacon could be.
    # ie the only space our sensors don't cover

# search_area = (0,20)
search_area = (0,4000000)
for row_y in range(*search_area):
    # on the big grid this takes ages. 4milx4mil is a huge space to search, even if
        # each row individually is quite fast. 
    print(f'\tsearching row {row_y}...')
    _, found_hole_x = scan_row(row_y, hole_search=True, search_area=search_area)
    if found_hole_x is not None:
        # we've found the hole!
        found_hole = (found_hole_x, row_y)
        break

# solution value (tuning frequency)
pt2_sol = found_hole[0]*4000000 + found_hole[1]
print(f'The only hole in the search grid is at {found_hole} with tuning frequency of {pt2_sol}')
    # after long compute the solution found was : 
        # The only hole in the search grid is at (2673432, 3308112) with tuning frequency of 10693731308112

    # For fun I'm going to try and make a new geometry-intersection method to 
    # solve this problem within a reasonable amount of time (while the brute force method runs)