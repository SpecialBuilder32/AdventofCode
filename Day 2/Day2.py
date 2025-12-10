# Advent of Code 2025

# Start Time: 6:31 PM
# Pt 1 End Time: 7:12 PM (41 min)

import itertools

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
    invalids = 0
    for a,b in input_ranges:
        for ID in range(a,b+1):
            next_id = False
            sID = str(ID)
            bA = sID[0:len(sID)//2] # bisect on midpoint
            bB = sID[len(sID)//2:]

            if len(sID)%2 ==1: # odd number of digits, not possible for perfect repetition!
                continue

            if bA == bB:
                invalids += ID
                print(f"found invalid ID {ID}")

            ## whoops went too complex, looking for any repeated pieces, not just repeats by bisection
            # i'll keep incase pt 2 is this :P
            # digits = tuple(map(int, str(ID)))
            # max_chunk_length = len(digits)//2

            # for chunk_len in range(2,max_chunk_length+1):
            #     chunks = tuple(itertools.batched(digits, chunk_len))

            #     for ca, cb in zip(chunks, chunks[1:]):
            #         if ca==cb:
            #             print(f"{ID} is invalid!, found {''.join(map(str, ca))}")
            #             invalids += ID
            #             next_id = True
            #             break

            #     if next_id:
            #         break

    print(f"sum of invalid IDs (pt 1 solution): {invalids}")
