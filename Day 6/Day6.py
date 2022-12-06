# Advent of Code 2022

# Start Time: 9:09 AM
# Pt 1 End Time: 9:22 AM
# Pt 2 End Time: 9:24 AM
# Total Time: 15min 08sec

#s 9:09a

# Uhoh... a signal processing problem :/

with open('Day 6/Day6_Input.txt', 'rt', encoding='UTF-8') as f: # read in large puzzle input
    datastream = f.read()

# additional trial cases
# datastream = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb' # solution=7
# datastream = 'bvwbjplbgvbhsrlpgdmjqwftvncz' # solution=5
# datastream = 'nppdvjthqldpwncqszvftbrmjlhg' # solution=6
# datastream = 'nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg' # solution=10
# datastream = 'zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw' # solution=11


# Part 1 - finding start-of-packet marker of exclusive 4 char sets
packet_found = False
i = 0
while not packet_found: # for every grouping of four in the datastream
    # crawl through datastream 4 char at a time
    segment = datastream[i:i+4]
    if len(set(segment)) == 4: # 4 unique characters
        packet_found = True
    else:
        i+=1

    if i+4 > len(datastream): # we've reached the end of the string
        packet_found = True
        print('ERROR : NO START-OF-PACKET MARKER FOUND')
    

print(f'The marker {segment} was located {i+4} characters into the datastream')
    # Part 1 Completion Time - 9:22 AM

# Part 2 - finding start-of-message markers of exclusive 14 char sets
packet_found = False
i = 0
while not packet_found: # for every grouping of four in the datastream
    # crawl through datastream 4 char at a time
    segment = datastream[i:i+14]
    if len(set(segment)) == 14: # 4 unique characters
        packet_found = True
    else:
        i+=1

    if i+14 > len(datastream): # we've reached the end of the string
        packet_found = True
        print('ERROR : NO START-OF-MESSAGE MARKER FOUND')
    

print(f'The message marker {segment} was located {i+14} characters into the datastream')