# Advent of Code 2022

# Start Time: 12:24 AM
# Pt 1 End Time: 12:54 AM   *also while watching Heartstoppers :P
# Pt 2 End Time: 1:31 AM
# Total Time: 1hr 7min (again, while distracted with Heartstoppers)

from string import ascii_letters
letter_values = {letter:val+1 for val,letter in enumerate(ascii_letters)}

# Pt 1
with open('Day 3/Day3_Input.txt', 'rt', encoding='UTF-8') as f:
    item_sum = 0
    for line in [l.strip() for l in f.readlines()]:
        # yooooo python sets support the & operator. Das hot
        half_idx = int(len(line)/2)
        comp1 = set(line[0:half_idx])
        comp2 = set(line[half_idx:])
        common_item = (comp1 & comp2).pop() # hot pythonic set intersecion for .intersection() method
        item_sum += letter_values[common_item]

    print(f'The total sum of the out-of-place items is {item_sum}')

    # Pt 2
    f.seek(0)
    lines = [l.strip() for l in f.readlines()]
        # we're using some overly complex iter stuff to try and learn them :)
    lines_iter = iter(lines) # returns next element in lines when accessed
    grouped_lines = zip(*(iter(lines),)*3) # put three lines from the iter into a tuple, then unpack into a zip
        # all could be put into a one-liner but I separated for comments to future me :)
    
    badge_sum = 0
    for group in grouped_lines:
        badge_item = set(group[0]) & set(group[1]) & set(group[2]) # intersection of the three sets
        badge_sum += letter_values[badge_item.pop()]

    print(f'The total sum of the badge items is {badge_sum}')