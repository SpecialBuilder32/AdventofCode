# Advent of Code 2024

# Start Time: 11:51 PM

# Pt 1 End Time: 12:13 PM
    # to 2:27 AM
# Pt 2 End Time: 

# Total Time: 

# Part 1 - Love me some more easy linear and modulos
import re
from dataclasses import dataclass
from math import prod

@dataclass
class Robot:
    pos: tuple[int]
    vel: tuple[int]

robots = []
# load robots
with open("Day 14/Day14_Input.txt", "r") as f:
    for line in f.readlines():
        m = re.match(r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)", line)
        px, py, vx, vy = map(int, m.groups())
        robots.append(Robot((px, py), (vx, vy)))

# simulate X steps
lobby_size = (101,103) # (11,7)
steps = 100
quads = [0,0,0,0]
mid = ((lobby_size[0]-1)/2, (lobby_size[1]-1)/2)

for r in robots:
    # find final pos
    end_pos = ((r.pos[0] + r.vel[0]*steps)%lobby_size[0], (r.pos[1] + r.vel[1]*steps)%lobby_size[1])

    # determine quadrant
    if end_pos[0] < mid[0] and end_pos[1] < mid[1]: # q2
        quads[0] += 1
    elif end_pos[0] > mid[0] and end_pos[1] < mid[1]: # q1
        quads[1] += 1
    elif end_pos[0] > mid[0] and end_pos[1] > mid[1]: # q4
        quads[2] += 1
    elif end_pos[0] < mid[0] and end_pos[1] > mid[1]: # q1
        quads[3] += 1

print(f"quadrants safety score = {prod(quads)}")

# Part 2 - Finding when the bots form the image of a christmas tree!
    # ... this seems extremely open ended and difficult programatically

# approach 1; maybe the tree happens in the first 100 seconds we've already simulated. 
#   Lets just run through 100 steps, display each and see if my eyeballs see a tree in there somewhere
import time

def display_lobby(robots: list[Robot]):
    out_arr = [list("."*lobby_size[0]) for _ in range(lobby_size[1])]

    for r in robots:
        out_arr[r.pos[1]][r.pos[0]] = "#"

    for line in out_arr:
        print("".join(line))

def step_robots(robots: list[Robot]):
    for r in robots:
        r.pos = ((r.pos[0] + r.vel[0])%lobby_size[0], (r.pos[1] + r.vel[1])%lobby_size[1])

# for s in range(100):
#     display_lobby(robots)
#     print(f"current time = {s} seconds")
#     step_robots(robots)
#     time.sleep(0.3)


# approach 2; okay so its after the first 100 seconds at some unknown point. Image recognition is hard but lets try a simple neural net thingy
#   Train it on some hand-drawn tree images and let it run until it finds something we can hand verify

# we'll do the training in a juypter notebook for clarity


# and if needed, approach 3; just look for a time where most robots are next to one another, thats probably an image!
