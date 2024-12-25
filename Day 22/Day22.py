# Advent of Code 2024

# Start Time: 12:14 AM

# Pt 1 End Time: 12:24 AM
# Pt 2 End Time: 8:40 PM, the next day

# Total Time: ~ 2 hr

import numpy as np
# Part 1 - psudorandom sequence generating
    # ..do I suspect that there is some clever math trick to make this fater than manually iterating?
    # probably. If there is I dont doubt it'll come in in part 2 though :P

seeds = []
with open("Day 22/Day22_Input.txt", "r") as f:
    for line in f.readlines():
        seeds.append(int(line))

def evolve(num: int) -> int:
    # evolves a number into its psudorandom successor
    num = mix(num, num*64)
    num = prune(num)

    num = mix(num, num//32)
    num = prune(num)

    num = mix(num, num*2048)
    num = prune(num)

    return num

def mix(into: int, num: int) -> int:
    return into^num

def prune(num: int) -> int:
    return num%16777216

# P2 - initialize storage of prices
prices = np.empty((len(seeds), 2000), dtype=int)

# find the 2000'th number generated by each starting seed
secret_sum = 0
for i, seed in enumerate(seeds):
    num = seed
    for j in range(2000):
        num = evolve(num)
        prices[i,j] = num%10 # ones digit of number
    secret_sum += num

print(f"sum of 2000th secret numbers is {secret_sum}")
#... this was suspiciously straightforward, even though it took 10 seconds to run


## Part 2 - Finding the best set of 4 deltas to buy the most bananas!
    # first we need to store all the prices calculated from the secret numbers - done inline with above
    # doesn't increase runtime significanly yet

# next calculate differences in price-over-time
diffs = np.diff(prices, axis=1)

# for each seller, precompute the number of bananas each sequence will get and store in a map for lookup
seller_map: list[dict[tuple, int]] = []
for i, seller in enumerate(diffs):
    seller_map.insert(i, {})
    for j in range(len(seller)-4, 0, -1):
        seller_map[i][tuple(seller[j:j+4])] = prices[i,j+4]
print("...completed sequence map")

# run through sequences until we find the best one
checked_seqs = set()
best_price = 0
for seller in seller_map:
    for seq, price in seller.items():
        if seq in checked_seqs:
            continue
        checked_seqs.add(seq)
        # check for sequence in the rest of the sellers
        for other_seller in seller_map:
            if other_seller is seller:
                continue
            price += other_seller.get(seq, 0)
        if price > best_price:
            best_price = price
            best_seq = seq


print(f"The best sequence for the monkey to act on is {best_seq}, yielding {best_price} bananas")