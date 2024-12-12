# Advent of Code 2024

# Start Time: 10:35 AM

# Pt 1 End Time: 11:23 AM (switch from recursion to BFS took time)
                    # 11:54 Think time
# Pt 2 End Time:

# Total Time: 


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
tol_price =0
for row_i in range(len(garden)):
    for col_j in range(len(garden[0])):
        if (row_i, col_j) in searched:
            continue # already part of a computed region

        plant = garden[row_i][col_j]
        horiz = [(row_i,col_j)]
        area = 0
        perim = 0
        region = set()

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
            horiz = new_horiz
        # print(region)
        # print(f"{area=}, {perim=}")
        
        searched.update(region)
        price = perim * area
        tol_price += price

print(f"final fence pricing: ${tol_price}")

# Part 2 - neighbor aware straightn-ess counting