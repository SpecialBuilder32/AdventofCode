# Advent of Code 2022

# Start Time: 9:18am (12th)
# Pt 1 End Time: 10:04a
    # pause for breakfast and shower
    # working-it-out resume: 10:42a
    # working-it-out done: 11:42a
    # lots of on-and-off cause this one was hard. Used a timer to track
# Pt 2 End Time: 7:05p
# Total Time: 3hr50min

import math
import re

class monkey(): # pt 1 monkeys - worry decreases
    def __init__(self, m_id: int, starting_items: tuple, op: str, op_val: int, test: int, throw_true: int, throw_false: int):
        self.id = m_id
        self.holding = list(starting_items)
        self.additive_op = op=='+'
        self.multiply_op = op=='*'
        self.pow_op = op=='**'
        self.op_val = op_val
        self.test = test
        self.throw_tree = {True: throw_true, False: throw_false}

        self.inspect_counter = 0

    def throw_all_items(self, monkeys, relief=True):
        for _ in range(len(self.holding)):
            self.inspect_and_throw(monkeys, relief)

    def inspect_and_throw(self, monkeys, relief=True):
        ## inspects first item in queue and passes to respective target

        # increase worry based on item
        item = self.holding.pop(0)
        self.inspect_counter += 1
        if self.additive_op:
            item += self.op_val
        elif self.multiply_op:
            item *= self.op_val
        elif self.pow_op:
            item **= self.op_val

        # monkey gets bored and worry drops
        if relief:
            item //= 3

        # throw to respective target
        monkeys[self.throw_tree[item%self.test == 0]].recieve_item(item)
    
    def recieve_item(self, item):
        self.holding.append(item)


    def __repr__(self): # simple priint out of elements
        return str(self.__dict__)

class monkey2(monkey): # pt 2 monkeys, worry never decreases
    def __init__(self, *args):
        super().__init__(*args)

    def throw_all_items(self, monkeys, D):
        for _ in range(len(self.holding)):
            self.inspect_and_throw(monkeys, D)

    def inspect_and_throw(self, monkeys, D):
        item = self.holding.pop(0)
        self.inspect_counter += 1

        if self.additive_op:
            item = (item+self.op_val)%D
        elif self.multiply_op:
            item = (item*self.op_val)%D
        elif self.pow_op:
            item **= 2

        # throw to respective target
        monkeys[self.throw_tree[item%self.test == 0]].recieve_item(item)



with open('Day 11/Day11_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

    # parse data into monkeys
    i = 0
    monkeys = []
    monkeys2 = []
    while i < len(lines):
        # monkey i
        monkey_id = int(re.match(r'Monkey (\d+):', lines[i]).group(1))
        starting_items = tuple(map(int, re.match(r'  Starting items: ([\d, ]+)', lines[i+1]).group(1).split(', ')))
        m = re.match(r'  Operation: new = old ([\*\+]) ([\d+]+|old)', lines[i+2])
        if m.group(2) == 'old':
            op = '**' # a squaring operation
            op_val = 2
        else:
            op = m.group(1)
            op_val = int(m.group(2))
        test_val = int(re.match(r'  Test: divisible by (\d+)', lines[i+3]).group(1))
        throw_true = int(re.match(r'    If true: throw to monkey (\d+)', lines[i+4]).group(1))
        throw_false = int(re.match(r'    If false: throw to monkey (\d+)', lines[i+5]).group(1))

        m = monkey(monkey_id, starting_items, op, op_val, test_val, throw_true, throw_false)
        monkeys.append(m)
        m2 = monkey2(monkey_id, starting_items, op, op_val, test_val, throw_true, throw_false)
        monkeys2.append(m2)

        i += 7

if __name__ == "__main__":
    # PT 1 - Monkey Buisness Inspection - this looks like it might get numbers way too big
    rounds = 20
    for r in range(1, rounds+1):
        # each round the monkeys pass around the items
        for mon in monkeys:
            mon.throw_all_items(monkeys)
        
        # print round results
        # print(f'After round {r}, the monkeys are holding items with these worry levels')
        # for mon in monkeys:
        #     print(f'Monkey {mon.id}, {mon.holding}')
        # print('\n')

    # find top two active monkeys
    monkeys.sort(key=lambda m: m.inspect_counter)
    monkey_buisness = monkeys[-1].inspect_counter * monkeys[-2].inspect_counter
    print(f'Total PT1 monkey buisness is {monkey_buisness}')

    # PT 2 - Monkey Buisness, but without the worry decrease... and for 10000 rounds.. oof
        # I did some working-it-out math to find the caps on the various worry levels. I shouldve put the pdf in this directory
    rounds = 10000
    printing_rounds = (1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000)

    # find product of all the monkey's test values
    D = 1
    for mon in monkeys2:
        D *= mon.test

    for r in range(1, rounds+1):
        # each round the monkeys pass around the items
        for mon in monkeys2:
            mon.throw_all_items(monkeys2, D)
        
        # print round results
        # if r in printing_rounds:
        #     print(f'== After round {r} ==')
        #     for mon in monkeys2:
        #         print(f'Monkey {mon.id} inspected items {mon.inspect_counter} times.')
        #     print('\n')

    # find top two active monkeys, pt 2
    monkeys2.sort(key=lambda m: m.inspect_counter)
    monkey_buisness2 = monkeys2[-1].inspect_counter * monkeys2[-2].inspect_counter
    print(f'Total PT1 monkey buisness is {monkey_buisness2}')
