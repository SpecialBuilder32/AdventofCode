# Advent of Code 2024

# Start Time: 10:32 PM
# Pt 1 End Time: 10:47 PM
# Pt 2 End Time: 11:27 PM

# Total Time: 55 min

# Part 1 - radioactive reindeer radiation reports
import numpy as np
from collections import Counter

with open("Day 2/Day2_Input.txt", "r") as f:
    input_text = f.readlines()
    
    safe_reports = 0
    dampened_safe_reports = 0

    def is_safe(reports: np.array):
        deltas = np.diff(reports)
        strictly_incr_or_decr = np.all(deltas<0) or np.all(deltas>0)
        gradual_adjacency = set(np.abs(deltas)).issubset({1,2,3}) # values differ by >1, <3

        return strictly_incr_or_decr and gradual_adjacency

    for line in input_text:
        reports = np.fromstring(line, dtype=int, sep=" ")

        if is_safe(reports):
            safe_reports += 1
            dampened_safe_reports += 1

        else: # not safe, lets see if removing one element will fix it
            # I tried to do this with intelligent case checks, but edge cases were many and recursion wound up faster, if only in writing time
            for i in range(len(reports)):
                if is_safe(np.concatenate((reports[0:i],reports[i+1:]))):
                    # is possible!
                    dampened_safe_reports += 1
                    break

    print(f"Number of safe reports = {safe_reports}")
    print(f"Number of safe reports, using the ignore-one dampener = {dampened_safe_reports}")

# Part 2 - adding a problem dampener which lets us ignore a single element per report
 # done inline with prior solution
