# Advent of Code 2022

# Start Time: 11:36p (11th)
# Pt 1 End Time: 12:15a
# Pt 2 End Time: 1:00a
# Total Time: 1hr 24min

import re
import numpy as np
import math
with open('Day 10/Day10_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()
    # the heck the input is super short...

# Part 1 - Reading cpu instructions
    # the simplest and fastest way I can think of doing pt 1 is just by looping through the instructions and processing it
    # one at a time. Any tricks are just going to be slower since they'd need to add everything anyway. 

# loop through instructions, adding to register
X = 1 # register value
cycle_count = 1 # cpu cycles counter
signal_strg_sum = 0 # running sum for times of interest

def check_and_apply_signal_log(forcast = 1):
    global signal_strg_sum # yes yes I know global bad. Only needed for assignment
    for i in range(0, forcast):
        if (cycle_count+i)%40-20 == 0:
            # print(f'During Cycle {cycle_count+i}, X={X}, and signal strength is {X*(cycle_count+i)}')
            signal_strg_sum += X*(cycle_count+i)

# Part 2 - Ah here's the complexity.. we're doina a racing-the-beam CRT image simulation now
    # deliverable: the text drawn by the program on a screen

screen_dim = (6,40)
pixels = np.ndarray(screen_dim, dtype=object)
pixels = np.reshape(pixels, math.prod(screen_dim))
pixel_chars = {False: '.', True: '#'}

def draw_pixels(n): # draw n pixels, one per clock cycle
    global pixels
    for i in range(0, n):
        pixels[cycle_count+i-1] = pixel_chars[ X-1 <= (cycle_count+i-1)%40 <= X+1 ]
            # if 3-pixel-wide "enable drawing sprite" is at beam drawing location


# process instructions for pt1 and pt2
for line in lines:
    inst, V = re.match(r'(noop|addx) ?(-?\d+)?', line).groups()

    if inst == 'noop':
        check_and_apply_signal_log(1)
        draw_pixels(1)
        cycle_count += 1
    elif inst == 'addx':
        check_and_apply_signal_log(2)
        draw_pixels(2)
        X += int(V)
        cycle_count += 2

# Pt 1 solution
print(f'Final signal strength summation is {signal_strg_sum}\n')

# Pt 2 solution
pixels = np.reshape(pixels, screen_dim)
screen = '\n'.join( [''.join(row) for row in pixels] )
print(screen)

