# Advent of Code 2024

# Start Time: 8:33 AM - 10:10 AM
                # 1:30 - 1:44 PM (after getting advice from Misode/MCC and redesigning)
# Pt 1 End Time: 
# Pt 2 End Time:

# Total Time: 

from functools import cache

with open("Day 19/Day19_Input.txt", "r") as f:
    towels = set(f.readline().strip().split(", "))
    f.readline()
    patterns = []
    for line in f.readlines():
        patterns.append(line.strip())

# pre-sort towels by length
towels_len = [len(t) for t in towels]

MAX_TOWEL_LEN = len(sorted(towels, key=len)[-1])

@cache
def check_possible(pattern: str) -> bool:
    # recursively check if a pattern is valid, utilizing the recursion for DFS and cacheing
    if pattern == "":
        return True
    for n in range(1, MAX_TOWEL_LEN+1):
        if pattern[:n] in towels:
            sub_call = check_possible(pattern[n:])
            if sub_call:
                return True
            # else continue
    return False

count = 0
for pattern in patterns:
    count += 1 if check_possible(pattern) else 0

print(f"There are {count} possible patterns!")

