# Advent of Code 2025
# Day 3 - Battery Joltage!!

# Pt 1 Start Time: 10:52 PM
# Pt 1 End Time: 10:58 PM (6min 🎉)
# Pt 2 End Time: 11:26 PM (28min)

with open("Day 3/Day3_Input.txt", "rt") as f:
    readin = f.readlines()

# PT 1
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

# PT 2
total_joltage = 0
for bank in readin:
    batteries = tuple(map(int, bank.strip()))
    digits = [None]*12

    start_idx = -1
    for i in range(12): # for each of the 1 batteries
        end_idx = len(batteries)-(12-i) # don't check the last 12-ith elements, we to still have 12 batteries total
        searchable_digits = batteries[start_idx+1:end_idx+1]
        digits[i] = max(searchable_digits)
        start_idx = searchable_digits.index(digits[i])+start_idx+1
    
    joltage = 0
    for pow, dig in enumerate(reversed(digits)): # convert to value
        joltage += dig*10**pow

    total_joltage += joltage
print(f"Pt2: Total joltage is {total_joltage}")
