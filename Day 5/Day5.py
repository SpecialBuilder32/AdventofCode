# Advent of Code 2025
# Day 5 - Membership in ranges for hello not fresh

# Pt 1 Start Time: 9:00 PM
# Pt 1 End Time: 9:08 PM (seemed suspiciously easy... pt 2 may be a nightmare)
# - 9:24-9:40 break for dinner
# Pt 2 End Time: 10:32 PM (embarrasing e[0] index typo ;-;)


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

# Pt 2 - range reduction, how many values meet any of the ranges. 
reduced_ranges = ranges.copy()
reduced_ranges.sort(key=lambda e: e[0]) # sort ascending by first key

    # attempt to merge ranges where they overlap
while True:
    loop_made_no_changes = True
    new_reduced_ranges = []
    merges = 0
    # print(f"start of loop, {len(reduced_ranges)} ranges")
    i = 0
    while i<len(reduced_ranges)-1:
        aa,ab = reduced_ranges[i]
        ba,bb = reduced_ranges[i+1]
        # print(f"checking {(aa,ab), (ba,bb)}")
        if ab>=ba: # we can merge
            new_reduced_ranges.append(v:=(aa, max((ab, bb))))
            merges += 1
            # print(f"merging {(aa,ab)} and {(ba,bb)} into {v}")
            loop_made_no_changes = False
            i+=2
        else:
            new_reduced_ranges.append((aa,ab))
            i+=1
            
        #if at end, keep last range that we couldnt just merge
        if i==len(reduced_ranges)-1:
            new_reduced_ranges.append(reduced_ranges[-1])

    reduced_ranges = new_reduced_ranges
    # print(f"end of loop, {len(reduced_ranges)} ranges, {merges} merges")

    if loop_made_no_changes:
        break


# compute number of values in exclusive ranges
sum_ranges = 0
for a, b in reduced_ranges:
    sum_ranges += b-a+1
print(f"Pt2: There are {sum_ranges} possible fresh ingredients")