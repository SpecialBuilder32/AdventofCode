# Advent of Code 2024

# Start Time: 10:20 AM

# Pt 1 End Time: 11:02 AM
# Pt 2 End Time: 11:21 AM

# Total Time: 61 min
import math

# Part 1 - Doubling Stones Simulation
# initial = [125, 17]
initial = [112, 1110, 163902, 0, 7656027, 83039, 9, 74]
num_blinks = 25
num_stones = len(initial)
space = [None]*(num_stones*10)

def rules(val: int) -> int|tuple[int]:
    if val == 0:
        return 1, False
    elif (num_digits:=math.floor(math.log10(val)+1))%2==0: # even num digits
        a = int(val // 10**(num_digits/2))
        b = int(val - a*10**(num_digits/2))
        return (a,b), True
    else:
        return val*2024, False

space[0:num_stones] = initial
for _ in range(num_blinks):
    j = 0
    new_stones = [None]*num_stones

    for i, stone in enumerate(space): # apply rules on each stone
        if stone is None:
            break # end of stones
        new_val, split = rules(stone)
        if split:
            space[i] = new_val[0]
            new_stones[j] = new_val[1]
            j += 1
            num_stones += 1
        else:
            space[i] = new_val

    # allocate more memory to the list if needed - should be only list expansion I need!
    if len(space) < num_stones*2:
        space.extend([None]*num_stones)

    # add new stones to the list
    for jj in range(j):
        space[i] = new_stones[jj]
        i += 1


# print(space[0:num_stones])
print(f"after {num_blinks} blinks there will be {num_stones} stones")

# Part 2 - well my fear was valid, part 2 is doing it 75 times. Thats a potential 37,778,931,862,957,161,709,568 needed elements. 
    # aka 37 sextillion.... and there's no way I have the memory space for that

    # theres also no way I have every integer between 0 and 2^75, so maybe there's enough repetition that doing the calculation
    # for each integer only once and skipping any repititions will be sufficient

num_blinks = 75
num_stones = len(initial)
space = dict()
for stone in initial:
    space[stone] = space.setdefault(stone, 0) + 1

for _ in range(num_blinks):
    new_space = dict()

    for stone, count in space.items(): # apply rules on each stone
        new_val, split = rules(stone)
        if split:
            new_space[new_val[0]] = new_space.setdefault(new_val[0], 0) + count
            new_space[new_val[1]] = new_space.setdefault(new_val[1], 0) + count
            num_stones += count
        else:
            new_space[new_val] = new_space.setdefault(new_val, 0) + count

    space = new_space

print(f"after {num_blinks} blinks there will be {num_stones} stones")

# hell yea the mapping (is this caching?) was the answer