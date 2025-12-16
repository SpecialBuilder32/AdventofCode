# Advent of Code 2025
# Day 8 - Junction box christmas light spiderwebs

# Pt 1 Start Time: 3:28 PM - 4:00 PM
    # 9:53 AM - 11:22 AM; still debugging

import numpy as np
from math import prod

juncboxes = []
with open("Day 8/Day8_Input.txt", "rt") as f:
    for line in f.readlines():
        juncboxes.append(np.array(list(map(int, line.strip().split(",")))))

# compute distances as a matrix
l = len(juncboxes)
# distances_matrix = np.subtract.outer(juncboxes, juncboxes) # theres some way to do this efficiently with this, but I couldnt figure it out
distances_matrix = np.zeros((l,l))
for (x,y), _ in np.ndenumerate(distances_matrix):
    distances_matrix[x,y] = np.linalg.norm(juncboxes[x]-juncboxes[y])
print("..distances precomputed")

# remove redundancy
distances_matrix = np.triu(distances_matrix)

# replace zeros with inf so they are sorted last
distances_matrix[distances_matrix==0] = np.inf

# get indices that sort matrix ascending value
indx_incr_distance = np.unravel_index(np.argsort(distances_matrix, axis=None), distances_matrix.shape)
print("..junction boxes sorted")

# go through list in distance order and connect junction boxes into the network/web
max_connections = 1000
networks = {} # {network_id: set(junc_idx)}
network_membership = {} # {junc_idx: network_id}
new_network_id = 1000
for x,y in zip(*indx_incr_distance):
    x = int(x)
    y = int(y)
    if distances_matrix[x,y] == np.inf or max_connections <= 0:
        break # we've processed all the boxes, quit

    # print(f"box {juncboxes[x]}({x}) is closest to {juncboxes[y]}({y}); dist={distances_matrix[x,y]:0.2f}")


    if x not in network_membership and y not in network_membership:
        # new standalone segment
        networks[new_network_id] = {x,y}
        network_membership[x] = new_network_id
        network_membership[y] = new_network_id
        new_network_id += 1

    # elif network_membership.get(x) == network_membership.get(y):
    #     # these boxes are already connected via other connections, skip!
    #     print("these boxes are already connected, skipping")
    #     continue
    ## The puzzle is worded confusingly!! If two boxes are already connected in the same circuit network, we *still* connect them with a new string of lights
    ## "nothing happens" refers to what happens to the network and number of total circuits!
    ## Seems silly to me these boxes already have power to them!

    elif network_membership.get(x) == network_membership.get(y):
        pass # connect the boxes, which does not change the network

    else:
        # we merge existing segments
        netxid = network_membership.get(x, -1) # if x is not connected, treat it as a network of one element (-1 will not be a valid id)
        netx = networks.get(netxid, {x})

        netyid = network_membership.get(y, -1)
        nety = networks.get(netyid, {y})

        merge_into_id = netxid if netxid > -1 else netyid
        del_id = netyid if netxid > -1 else netxid
        networks[merge_into_id] = netx|nety
        network_membership[x] = network_membership[y] = merge_into_id
        networks.pop(del_id, None)
        
    # print(networks)
    max_connections -= 1

print(networks)
netwk_sizes = sorted(map(len, networks.values()), reverse=True)
pt1_answer = prod(netwk_sizes[0:3])
print(f"Pt1: Product of 3 largest circuits is {pt1_answer}")