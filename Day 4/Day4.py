# Advent of Code 2024

# Start Time: 8:06 PM - 8:55PM
            # 9:12 PM
# Pt 1 End Time: 9:18 PM
# Pt 2 End Time: 9:26 PM

# Total Time: 68Min

# Part 1 - word-search central

import numpy as np

with open("Day 4/Day4_Input.txt", "r") as f:
    puzz = np.loadtxt(f, str, delimiter=None)
    puzz = np.array([list(row) for row in puzz]) # loadtxt made each string one element due to no spaces :(
    h,w = puzz.shape

    xmas = ['X','M','A','S']
    found = 0
    for i, j in np.ndindex(puzz.shape):
        if puzz[i,j] != 'X':
            continue
        
        if j>=3:
            if np.all(np.flip(puzz[i,j-3:j+1]) == xmas): #-x
                found += 1

            if i>=3:
                if np.all(puzz[[i,i-1,i-2,i-3],[j,j-1,j-2,j-3]] == xmas): #-x,+y
                    found += 1

        if i>=3:
            if np.all(np.flip(puzz[i-3:i+1,j]) == xmas): #+y
                found += 1

            if j<w-3:
                if np.all(puzz[[i,i-1,i-2,i-3],[j,j+1,j+2,j+3]] == xmas): #+x,+y
                    found += 1

        if j<w-3:
            if np.all(puzz[i,j:j+4] == xmas): #+x
                found += 1

            if i<h-3:
                if np.all(puzz[[i,i+1,i+2,i+3],[j,j+1,j+2,j+3]] == xmas): #+x,-y
                    found += 1

        if i<h-3:
            if np.all(puzz[i:i+4,j] == xmas): # -y
                found += 1
            
            if j>=3:
                if np.all(puzz[[i,i+1,i+2,i+3],[j,j-1,j-2,j-3]] == xmas): #-x,-y
                    found += 1


    print(f"total found xmass = {found}")

    # Part 2 - oops a new pattern
    cross_found = 0
    mas = ["M","A","S"]
    for i, j in np.ndindex(puzz.shape):
        if i==0 or i==h-1 or j==0 or j==w-1:
            continue # no center of the X can be here

        if puzz[i,j] != 'A':
            continue

        d1 = puzz[[i-1,i,i+1],[j-1,j,j+1]]
        d2 = puzz[[i-1,i,i+1],[j+1,j,j-1]]

        if (np.all(d1==mas) or np.all(np.flip(d1)==mas)) and (np.all(d2==mas) or np.all(np.flip(d2)==mas)):
            cross_found += 1

    print(f"total found crossed X-Mas = {cross_found}")
