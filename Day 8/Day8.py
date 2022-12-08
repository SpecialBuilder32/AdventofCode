# Advent of Code 2022

# Start Time: 11:34a
# Pt 1 End Time: 12:27p
# Pt 2 End Time: 1:09p
# Total Time: 1hr31min

# Determining visibility / heightmap of a forest of trees
import numpy as np # for nice 2d arrays
import matplotlib.pyplot as plt

# Read forest height data in
with open('Day 8/Day8_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()
    width = len(lines[0].strip())
    forest = np.ndarray((0,width))
    
    for line in lines:
        forest = np.append( forest, [tuple(map(int, tuple(line.strip())))], axis=0)
# height = forest.shape[0] # forest is a square

# Part 1 - step through forest and find visibility
    # since the input is so large, we care about efficiency. Only look as far into the forest as necessary.
visibility = np.zeros((width, width)) # 0 indicates visible from edge of grid
visibility[1:-1,1:-1] = 1 # inner segment is unknown, so set to invisible by default

for _ in range(4):
    forest = np.rot90(forest) # rotate 90° to do from all 4 sides
    visibility = np.rot90(visibility) # rotate 90° to do from all 4 sides
    # from current left side
    for i in range(width):
        H = forest[i,0] # highest encountered tree
        j = 1
        while H<9 and j<width: # run until the tallest possible tree is reached
            if forest[i,j]>H: # current tree is taller
                H = forest[i,j]
                visibility[i,j] *= 0 # set tree to visible
            j+=1

num_visible = width**2 - np.sum(visibility, axis=(0,1))
# plt.imshow(forest)
# plt.colorbar()
# plt.show()
# plt.imshow(visibility)
# plt.show()
print(f'The total number of visible trees in the forest is {num_visible}')

# Pt 2 - step through and calculate scenic scores
scenic_score = np.ones((width,)*2)

for _ in range(4): # once for each cardinal direction
    forest = np.rot90(forest)
    scenic_score = np.rot90(scenic_score)

    for i,j in np.ndindex((width,)*2): #each row
        H = forest[i,j]
        k = 0 # number of trees away
        while forest[i,j+k] <= H and j+k < width-1:
            k += 1
            if forest[i,j+k] == H: # if equal height, can see but no further
                break
        scenic_score[i,j] *= k

plt.imshow(scenic_score)
plt.colorbar()
plt.show()
print(f'The max scenic scoring tree is {np.max(scenic_score)}')
