# Advent of Code 2025
# Day 8 - Junction box christmas light spiderwebs

# Pt 1 Start Time: 3:28 PM - 4:00 PM
    # 9:53 AM - 11:22 AM; still debugging
    # 2:10 PM - 2:19 PM; I only updated x or y's membership list, not the whole set that is getting merged
    # Total time: 2hr 10min
# Pt 2 Start Time: 2:19 PM
# Pt 2 End Time: 2:35 PM (16min)

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
networks = {x:{x} for x in range(len(juncboxes))} # {network_id: set(junc_idx)}
network_membership = {x:x for x in range(len(juncboxes))} # {junc_idx: network_id}
new_network_id = len(juncboxes)+1000
for x,y in zip(*indx_incr_distance):
    x = int(x)
    y = int(y)

    if distances_matrix[x,y] == np.inf: # no more boxes to process
        break

    if max_connections == 0: # we've finished for part 1
        netwk_sizes = sorted(map(len, networks.values()), reverse=True)
        pt1_answer = prod(netwk_sizes[0:3])
        print(f"Pt1: Product of 3 largest circuits is {pt1_answer}")

    # print(f"box {juncboxes[x]}({x}) is closest to {juncboxes[y]}({y}); dist={distances_matrix[x,y]:0.2f}")


    # if x not in network_membership and y not in network_membership:
    #     # new standalone segment
    #     networks[new_network_id] = {x,y}
    #     network_membership[x] = new_network_id
    #     network_membership[y] = new_network_id
    #     new_network_id += 1
    ## Pt 2 makes all operations a merge

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
        netxid = network_membership[x]
        netx = networks[netxid]

        netyid = network_membership[y]
        nety = networks[netyid]

        merge_into_id = netxid # always merge onto the x segment
        del_id = netyid
        networks[merge_into_id] = netx|nety
        network_membership[x] = network_membership[y] = merge_into_id
        for connected_id in networks.get(del_id,{}):
            network_membership[connected_id] = merge_into_id
        networks.pop(del_id, None)
        
    if len(networks) == 1: # only one network! pt2 done
        print(f"Last two boxes to connect are {juncboxes[x]}, {juncboxes[y]}")
        pt2_answer = juncboxes[x][0] * juncboxes[y][0]
        print(f"Pt2: product of x coords is {pt2_answer}")
        break
    
    # print(networks)
    max_connections -= 1



# check solution
    # each number should show up in exactly one set
# counts = {}
# for netwk in networks.values():
#     for junc in netwk:
#         counts.setdefault(junc, 0)
#         counts[junc] += 1

# print(sorted(counts.items(),key=lambda e:e[1], reverse=True)[0:5])    #found : [(948, 2), (1, 2), (825, 2), (788, 2), (642, 2)]