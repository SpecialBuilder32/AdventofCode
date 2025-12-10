# Advent of Code 2025
# Day 3 - Battery Joltage!!

# Pt 1 Start Time: 10:52 PM
# Pt 2 End Time: 10:58 PM (6min 🎉)

with open("Day 3/Day3_Input.txt", "rt") as f:
    readin = f.readlines()

total_joltage = 0
for bank in readin:
    batteries = tuple(map(int, bank.strip()))
    digit1 = max(batteries[:len(batteries)-1])
    bat1_idx = batteries.index(digit1)
    remaining_batteries = batteries[bat1_idx+1:]
    digit2 = max(remaining_batteries)

    joltage = 10*digit1 + digit2
    total_joltage += joltage

print(f"Pt1: Total joltage is {total_joltage}")