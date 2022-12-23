# Advent of Code 2022

# a new approach to day 15 pt 2

# Start Time: 9:15p (22nd)
    # pause 10:56p, 1:39a
# End Time: 3:11a (23rd)

# attempts to locate the hole in the search grid not by checking
# every space, but by checking a reduced set of potential locations
# determined by intersections

from itertools import combinations, product
from Day15 import sensor_data

# calculate the intersection of every pair of sensors
    # equation of manhattan distance circles |(x-xc)| + |(y-yc)| = r
    # there is no closed form solution for the intersections of this shape! We'll
        # need some conditional computing

intersections = set()
for sensor1, sensor2 in combinations(sensor_data, 2):
    for a1,b1 in product([+1,-1],repeat=2): # for each edge of sensor_1
        for a2,b2 in product([+1,-1],repeat=2): # for each edge orthogonal edge of sensor_2
            if a1*b2!=a2*b1: # orthogonal pair
                # intersection of lines
                y = (-sensor1.coverage_distance/a1 + sensor2.coverage_distance/a2 \
                    -b1/a1*sensor1.my_y + b2/a2*sensor2.my_y \
                    -sensor1.my_x + sensor2.my_x) \
                    / (b2/a2 - b1/a1)
                x = (sensor1.coverage_distance - b1*(y-sensor1.my_y))/a1 + sensor1.my_x
                
                # is this a valid intersection
                if sensor1.distance_to(x,y) == sensor1.coverage_distance \
                    and sensor2.distance_to(x,y) == sensor2.coverage_distance:
                    intersections.update({(x,y)})

print(f'{len(intersections)} were located as the search region')

# because there is no way to perfectly tile diamonds in a way that leaves a singular gap without overlaps
    # searching around the intersections will find the hole without needing to check all positions
        
# discard any intersections outside the search area
# search_area = (0,20)
search_area = (0,4000000)
dropped = 0
for intersect in intersections.copy():
    if not (search_area[0] <= intersect[0] <= search_area[1]) or \
        not (search_area[0] <= intersect[0] <= search_area[1]):
        intersections.discard(intersect)
        dropped += 1
print(f'Discarded {dropped} intersections outside search area')

# search 3x3 around remaining intersections (4x4 if odd-even center misaligns)
hole = None
for x,y in intersections:
    s = 3
    if x%0.5 == 0: # not grid-aligned intersection
        s = 4
        x = int(x) # floor to integer
        y = int(y)
    for cx, cy in product(range(max(x-1, search_area[0]), min(x+s, search_area[1])), \
            range(max(y-1, search_area[0]), min(y+s, search_area[1]))):
        for sensor in sensor_data:
            if sensor.distance_to(cx, cy) <= sensor.coverage_distance:
                # the space is covered by a sensor
                break
        else:
            # no sensor covers this space, this is the solution!
            hole = (cx, cy)
            break
    if hole is not None:
        break # stop checking more intersections

print(f'The located hole is at {hole}')

# yep it found the hole.. and super fast too!