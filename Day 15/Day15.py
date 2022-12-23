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
INTEREST_ROW = y = 2000000

occupied_spaces = 0
col_x = SensorData.min_x
while col_x <= SensorData.max_x:
    for sensor in sensor_data:
        if sensor.coverage_distance >= sensor.distance_to(col_x, y):
            # compute horizontal distance this sensor covers of interest row
            slice_radius = sensor.coverage_distance - abs(y-sensor.my_y)
            # how much of this width do we have left to cover
            remaining_slice = slice_radius - (col_x - sensor.my_x) + 1
            
            # check if this sensor's beacon is in this row
            if sensor.beacon_y == y \
                and sensor.beacon_x > col_x: # and we haven't counted it already
                occupied_spaces -= 1 # we know a beacon is already here. 

            col_x += remaining_slice
            occupied_spaces += remaining_slice

            break
    else: # no sensor covered the space
        col_x += 1
    

print(f'Number of spaces in row {INTEREST_ROW} where a beacon cannot be is {occupied_spaces}')