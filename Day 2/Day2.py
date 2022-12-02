# Advent of Code 2022

# Start Time: 12:00 AM
# Pt 1 End Time: 12:24 AM
# Pt 2 End Time: 12:38 AM
# Total Time: 38min 16sec

# Part 1 - Compute score of scripted Rock-Paper-Scissors Game
    # A/X = Rock, 1pt
    # B/Y = Paper, 2pt
    # C/Z = Scissors, 3pt

points = 0
shape_worth = ['X', 'Y', 'Z'] # [1,2,3] pts

win_map = dict([(val, key) for key, val in enumerate('ABC')])
win_map.update(dict([(val, key) for key, val in enumerate('XYZ')]))

with open('Day 2/Day2_Input.txt', 'rt', encoding='UTF-8') as f:
    for line in f.readlines():
        oppon, me = line.strip().split(' ')
        points += shape_worth.index(me)+1 # add points for your shape's worth
        
        # determine match outcome
        outcome = (win_map[me]-win_map[oppon]+1)%3 -1 # modular math for winner. 1=win,-1=lose
        points += (outcome+1)*3 # points for match
    print(f'My points for following the strategy guide is {points} points')

    # Part 2 - Compute score when given game result instead of my move
        # X = lose, Y = tie, Z = win
    f.seek(0) # reset file reader to start of file.
    points2 = 0
    for line in f.readlines():
        oppon, outcome = line.strip().split(' ')
        points2 += win_map[outcome]*3 # add points for match outcome

        # determine required move to meet outcome
        me = (win_map[oppon]+win_map[outcome]-1)%3
        points2 += me+1
    print(f'My points for throwing matches according to guide is {points2} points')


