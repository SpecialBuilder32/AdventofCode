# Advent of Code 2025

# Start Time: 6:31 PM
# Pt 1 End Time: 7:12 PM (41 min)

# Pt 2 Start Time: 10:17 PM
# Pt 2 End Time: 10:47 PM (30 min)

import itertools
from functools import cache

@cache
def factors(n:int): # quick utility for getting factors of a number
    ret = {1,n}
    for i in range(1,n//2+1):
        if n%i==0:
            ret |= {i,n//i}
    return ret

with open("Day 2/Day2_Input.txt", "rt") as f:
    input_txt = f.readline()
    input_ranges_1 = input_txt.split(",")
    input_ranges_2 = (v.split("-") for v in input_ranges_1)
    input_ranges = list(((int(a), int(b)) for a,b in input_ranges_2))

    # count total cases to check to see if we can exhaustively search or need to be clever
    total_to_check = 0
    for a,b in input_ranges:
        total_to_check += b-a
    print(f"total IDs to check is {total_to_check}") # real input: 2245793. Feasible for exhaustive!

    # find and sum up all invalid ids
    pt1_invalids = 0
    pt2_invalids = 0
    for a,b in input_ranges:
        for ID in range(a,b+1):
            next_id = False

            # PT 1 solver
            sID = str(ID)
            bA = sID[0:len(sID)//2] # bisect on midpoint
            bB = sID[len(sID)//2:]

            # if len(sID)%2 ==1: # odd number of digits, not possible for perfect repetition! NOT true under pt 2 rules
            #     continue

            if bA == bB:
                pt1_invalids += ID
                # print(f"found invalid ID {ID}")

            # PT 2 solver - looking for chunks repeated more than twice!
            digits = tuple(map(int, str(ID)))

            for chunk_len in sorted(factors(len(digits))-{len(digits)}):
                chunks = tuple(itertools.batched(digits, chunk_len))
                reduced_chunks = set(chunks) # set will remove all repeated elements
                if len(reduced_chunks)==1:
                    print(f"{ID} is invalid!, found {''.join(map(str, reduced_chunks.pop()))}")
                    pt2_invalids += ID

                    break # no need to keep checking this ID


    print(f"sum of invalid IDs (pt 1 solution): {pt1_invalids}")
    print(f"sum of invalid IDs (pt 2 solution): {pt2_invalids}")
