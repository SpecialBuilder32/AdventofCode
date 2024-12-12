# Advent of Code 2024

# Start Time: 10:35 AM

# Pt 1 End Time: 11:23 AM (switch from recursion to BFS took time)
                    # 11:54 Think time
# Pt 2 End Time:

# Total Time: 

import itertools


# Part 1 - Area and perimeter calculations
garden = []
with open("Day 12/Day12_Input.txt", "r") as f:
    for line in f.readlines():
        garden.append(list(line.strip()))

def b_get(i,j,grid):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return None
    return grid[i][j]

# search the grid for regions
searched = set()   
tol_price = 0
eff_price = 0
for row_i in range(len(garden)):
    for col_j in range(len(garden[0])):
        if (row_i, col_j) in searched:
            continue # already part of a computed region

        plant = garden[row_i][col_j]
        horiz = [(row_i,col_j)]
        area = 0
        perim = 0
        region = set()
        boundary = set()

        while len(horiz) > 0:
            new_horiz = []
            for i,j in horiz:
                if (i,j) in region: # already searched, skip
                    continue
                if b_get(i,j,garden)==plant:
                    area += 1
                    region.add((i,j))
                
                    # add neighbors of horizon element
                    for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                        new_horiz.append((i+di,j+dj))
                
                else: # different plant or outside the grid
                    perim += 1
                    boundary.add((i,j))
            horiz = new_horiz
        
        # Part 2 - loop through identified region and count corners
        corners = 0
        for ei, ej in region:
            for (ai,aj),(bi,bj) in itertools.pairwise([(1,0),(0,1),(-1,0),(0,-1),(1,0)]):
                if b_get(ei+ai,ej+aj,garden) != plant and b_get(ei+bi,ej+bj,garden) != plant:
                    # exterior corner
                    corners += 1
        for ei,ej in boundary:
            for (ai,aj),(bi,bj) in itertools.pairwise([(1,0),(0,1),(-1,0),(0,-1),(1,0)]):
                if b_get(ei+ai,ej+aj,garden) == plant and b_get(ei+bi,ej+bj,garden) == plant:
                    # interior corner
                    corners += 1
        # print(f"plot {plant} has {corners} corners")

        searched.update(region)
        
        price = perim * area
        tol_price += price

        price = corners * area
        eff_price += price

print(f"final fence pricing: ${tol_price}")
print(f"final bulk pricing: ${eff_price}")

# Part 2 - neighbor aware straightn-ess counting
    # we're instead counting the number of corners, which == edges in a closed shape

    # added inline to existing field traverser

# TODO deal with the warned condition of two intertior regions touching!!!