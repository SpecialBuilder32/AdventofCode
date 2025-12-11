# Advent of Code 2025
# Day 5 - Membership in ranges for hello not fresh

# Pt 1 Start Time: 9:00 PM
# Pt 2 End Time: 9:08 PM (seemed suspiciously easy... pt 2 may be a nightmare)


with open("Day 5/Day5_Input.txt", 'rt') as f:
    # parse input
    ranges = []
    while True:
        line = f.readline()
        if line == "\n":
            break
        ranges.append(tuple(map(int, line.strip().split("-"))))

    ingredients = []
    for line in f.readlines():
        ingredients.append(int(line.strip()))

fresh_count = 0
for ingred in ingredients:
    for lb, ub in ranges:
        if lb <= ingred <= ub:
            fresh_count += 1
            # print(f"found fresh ingred {ingred}")
            break # on to next ingred

print(f"Pt1: There are {fresh_count} fresh ingredients")