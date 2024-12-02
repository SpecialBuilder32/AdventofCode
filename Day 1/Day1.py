# Advent of Code 2024

# Start Time: 8:26 PM
# Pt 1 End Time: 8:36 PM
# Pt 2 End Time: 8:46 PM

# Total Time: 20 mins 🎉

# Part 1 - find differences between two lists, summing total integer differences after sorting.
import numpy as np
import collections

with open("Day 1/Day1_Input.txt", "r") as f:
    in_arr = np.loadtxt(f, int)   
    arr = np.sort(in_arr, axis=0)
    arr = np.diff(arr, axis=1)
    res = np.sum(np.abs(arr))
    print(f"Total differences: {res}")

# Part 2 - "similarity score"
    counter = collections.Counter(in_arr[:,1])
    similarity_score = lambda n: n * counter[n]
    arr = np.vectorize(similarity_score)(in_arr[:,0])
    res = np.sum(np.abs(arr))
    print(f"Total similarity score : {res}")
    