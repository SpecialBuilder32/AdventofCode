# used in the debug of day 11 logic

# compares the results from monkey1 and monkey2 and identifies the differences. 
    # I need to use this because i have a single error in the first 20 rounds and cannot
    # manually sort through that and find the error

from Day11 import monkeys, monkeys2

# D = 1
# Ds = []
# for mon in monkeys2:
#     D *= mon.test
#     Ds.append(mon.test)
D = 2*3*5*7*11*13*17*19*23
Ds = [2, 3, 5, 7, 11, 13, 17, 19, 23]

def tested_factors(val): # check divisibility of the important primes
    res = []
    for d in Ds:
        if val%d == 0:
            res.append(d)
    return tuple(res)

def list_tested_factors(val_list):
    res = []
    for val in val_list:
        res.append(tested_factors(val))
    return(res)

rounds = 25
for r in range(1, rounds+1):
    # each round the monkeys pass around the items
    print(f'\n== Begin Round {r} ==')
    for mon1, mon2 in zip(monkeys, monkeys2):
        print(f'\tTurn of monkey {mon1.id}')
        mon1.throw_all_items(monkeys, relief=False)
        mon2.throw_all_items(monkeys2, D)

        # see if important factors match
        for fmon1, fmon2 in zip(monkeys, monkeys2):
            if (fd1:=list_tested_factors(fmon1.holding)) != (fd2:=list_tested_factors(fmon2.holding)):
                print(f'{fmon1.id}, factors of 1:{fmon1.holding}, 2:{fmon2.holding}\n\t\t are 1:{fd1}, 2:{fd2}')

        # see if throws match
        intended_catch = invalid_catch = -1
        for cmon1, cmon2 in zip(monkeys, monkeys2):
            if len(cmon1.holding) > len(cmon2.holding):
                intended_catch = cmon1.id
            if len(cmon2.holding) > len(cmon1.holding):
                invalid_catch = cmon2.id
        if intended_catch > -1 and invalid_catch > -1:
            print(f'\t\tThrow Discrepancy Detected! Monkey {mon1.id} threw to {invalid_catch} instead of {intended_catch}')

            print(f'\nMonkey {mon1.id} test val: {mon1.test}')
            print(f'Wrapping val {D=}')
            print(f'Correct throw: value of {monkeys[intended_catch].holding[-1]}')
            print(f'Invalid throw: value of {monkeys2[invalid_catch].holding[-1]}')

# Finally! 3 hours later. The problem was with my conclusion on the power rule. 