# Advent of Code 2022

# Start Time: 1:38a (16th)
# Pt 1 End Time: 2:45a
# Pt 2 End Time: 3:05a
# Total Time: 1hr 27min

# today is parsing and recursion hell
    # correction - it wasn't that bad. Thanks Python!
from functools import cmp_to_key

# Parse input
    # we're going to to the unsafe-option and use eval, since the input is in a python-friendly syntax
# pylint: disable=eval-used
# pylint: disable=redefined-outer-name

pairs = []
packets = []
with open('Day 13/Day13_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

    for pair1, pair2 in zip(lines[::3], lines[1::3]):
        combined_pair = (
            eval(pair1.strip()),#.replace('[','(').replace(']',')')), # hush its fine
            eval(pair2.strip())#.replace('[','(').replace(']',')'))
            )           # turns out python interprets '(())' as a single empty tuple, lists properly stack
        pairs.append(combined_pair)

    for line in lines:
        if (l:=line.strip()) != '':
            packets.append(eval(l))

# helper function for iterating through pair lists of different lengths
def long_zip(a, b):
    # a version of zip that padds the shorter list with 'None' rather than stop at the length of the shorter list
    la = len(a)
    lb = len(b)
    N = max( (la, lb) )
    i = 0
    while i < N:
        if i < la:
            ra = a[i]
        else:
            ra = None
        if i < lb:
            rb = b[i]
        else:
            rb = None
        
        yield(ra, rb) # i get to use fun generator functionality
        i+=1


# define recursive order checkers
def is_pair_in_order(left, right):
    # if both values are integers
    if type(left) is int and type(right) is int:
        if left < right:
            # this pair is in the right order!
            return True
        elif right < left:
            # this pair is in the wrong order!
            return False
        # otherwise they are the same integer, correctness undetermined
        return None
    
    # if one is list, convert int to list and compare as lists
    if type(right) is list and type(left) is int:
        left = (left,) # convert to single-element-tuple
    if type(left) is list and type(right) is int:
        right = (right,)

    # if both are lists
    for l, r in long_zip(left, right):
        if l is None: # left list ran out of items
            return True # pair is in the right order!
        elif r is None: # right list ran out of items
            return False # pair is in the wrong order!
        # compare items if both exist
        if (ret:=is_pair_in_order(l,r)) is not None: # a concrete answer was found
            return ret
        # otherwise still undetermined, proceed to next items in pair
    # if all items return undetermined, then we ..well are undetermined
    return None
    

# PT 1 - Check each pair for correctness
pt1 = 0
for i, (left, right) in enumerate(pairs, start=1):
    if is_pair_in_order(left, right):
        pt1 += i
print(f'Sum of correctly-ordered pairs is {pt1}')
            

# PT 2 - Now we have to sort the inputs so that they are ALL in the correct order
    # I'm going to try and use python's sorting features rather than manually implement a sorting
    # algorithm myself. There are too many and I don't think thats my strong suit.

# append 'divider packets'
packets.append([[2]])
packets.append([[6]])

@cmp_to_key
def keyed_pair_comparator(a, b):
    # transforms output of is_pair_in_order to -=+ format
        # if pair is in order, report a is less than (-): order is fine
            # True -> -1
        # if pair is not in order, report a is greater than (+) and in need of swapping
            # False -> +1
    return int(not is_pair_in_order(a,b))*2 -1

# sort the packets using very hot python inbuilt sorting 
sorted_packets = sorted(packets, key=keyed_pair_comparator)

# locate indices of the divider packets
i1 = sorted_packets.index([[2]])+1
i2 = sorted_packets.index([[6]])+1
pt2 = i1*i2
print(f'The decoder key is {pt2}')
