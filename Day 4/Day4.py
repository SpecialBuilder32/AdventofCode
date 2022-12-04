# Advent of Code 2022

# Start Time: 12:48 AM
# Pt 1 End Time: 1:40 AM    *while also watching DS9
# Pt 2 End Time: 1:53 AM
# Total Time: 1hr 5min

# Part 1 - How may pairs are fully contained in another

with open('Day 4/Day4_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()
    pairs1 = 0
    pairs2 = 0

    for line in lines:
        r = list(map(lambda a: a.split('-'), line.strip().split(',')))
        (l1, u1), (l2, u2) = ((int(r[0][0]), int(r[0][1])),(int(r[1][0]),int(r[1][1]))) # pretty python methods failed me so I gave up
        # test a in b
        if l1<=l2<=u1 and l1<=u2<=u1:
            pairs1 += 1 # yes, fully enclosed pair
        elif l2<=l1<=u2 and l2<=u1<=u2:
            pairs1 += 1 # yes, fully enclosed pair

        # Part 2 - How many pairs overlapa at all
        if l1<=l2<=u1 or l1<=u2<=u1:
            pairs2 += 1 # yes, some overlap
        elif l2<=l1<=u2 or l2<=u1<=u2:
            pairs2 += 1 # yes, some overlap


    print(f'The number of redundant pairs is {pairs1}')
    print(f'The number of overlapping pairs is {pairs2}')
        