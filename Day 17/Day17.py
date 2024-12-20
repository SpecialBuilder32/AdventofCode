# Advent of Code 2024

# Start Time: 8:59 AM

# Pt 1 End Time: 9:59 AM (embarrased that I mixed up OR and XOR for that long)
# Pt 2 End Time:

# Total Time: 


## Part 1 - 3-bit computer simulation. Opcodes lets gooooo
    # I wonder if anyone tried solving this via hardware. Could be interesting

regA: int = 0
regB: int = 0
regC: int = 0
prog: list[int] = []
inst: int = 0 # instruction pointer
stout: list[int] = []

# load input
import re
with open("Day 17/Day17_Input.txt", 'r') as f:
    regA = int(re.match(r"Register A: (\d+)", f.readline()).group(1))
    regB = int(re.match(r"Register B: (\d+)", f.readline()).group(1))
    regC = int(re.match(r"Register C: (\d+)", f.readline()).group(1))
    f.readline()
    prog = list(map(int, re.match(r"Program: (.+)", f.readline()).group(1).split(",")))

# define operand variants
def literal_opd(val: int):
    return val

def combo_opd(val: int):
    if 0 <= val <= 3:
        return val
    elif val == 4:
        return regA
    elif val == 5:
        return regB
    elif val == 6:
        return regC
    elif val == 7:
        raise ValueError()

# define opcodes
def _dv(opd: int):
    return regA//(2**combo_opd(opd))
def adv(opd):
    global regA
    regA = _dv(opd)
def bdv(opd):
    global regB
    regB = _dv(opd)
def cdv(opd):
    global regC
    regC = _dv(opd)
def bxl(opd):
    global regB
    regB = regB ^ literal_opd(opd)
def bst(opd):
    global regB
    regB = combo_opd(opd) % 8
def jnz(opd):
    global inst
    if regA != 0:
        inst = literal_opd(opd) - 2
def bxc(_):
    global regB, regC
    regB = regB ^ regC
def out(opd):
    stout.append(combo_opd(opd)%8)

OpCode = {
    0: adv,
    1: bxl,
    2: bst,
    3: jnz,
    4: bxc,
    5: out,
    6: bdv,
    7: cdv
}

# run the program
while True:
    try:
        OpCode[prog[inst]](prog[inst+1])
        inst += 2
    except IndexError:
        # valid end of program
        break

# print results
prog_output = ",".join(map(str, stout))
print(f"Program outputs: \n {prog_output}")


## Part 2 - now we run this machine a until we find a static input-output program pair!
# initA = 0
# while True:
#     # print(f"trying regA = {initA}")
#     regA = initA
#     inst = 0
#     stout.clear()
    
#     while True:
#         try:
#             OpCode[prog[inst]](prog[inst+1])
#             inst += 2
#         except IndexError:
#             # valid end of program
#             break

#         # can we quit early (incase of infinite loops?)
#         if stout:
#             i = len(stout)-1
#             if stout[i] != prog[i]:
#                 break


#     if stout==prog:
#         # we've found the static pair!
#         print(f"initial register A value for input->output: {initA}")
#         break

#     initA += 1 # try the next value

    ## Well damn its such a big number that even with the early quits checking every number is taking more than 30 mins.
        # we need a different approach


# Alright so instead I did a manual translation of the program input we're running, and it is essentially taking X bits from the initial regA value to produce each output. 
# so with some reverse engineering, we can figure the bits of the initial regA required to make the desired output. This WILL NOT be generic! and only work on my specific
# program, so unless everyone's program follows mostly the same structure, my solution will not solve theirs.

# program: bst(A), bxl(5), cdv(B), bxl(6), adv(3), bxc, out(B), jnz(0)

# This solution heavily references by-hand notes in my remarkable. 

# form digit -> possible input table
d_table = {}
for B1 in range(8):
    C2 = list(range(8))
    B2 = list((B1^C2 for C2 in C2)) # index C -> B2
    B3 = list((B2^6 for B2 in B2)) # index C -> B3
    B4 = list((B3^5 for B3 in B3)) # index C -> B4

    d_table[B1] = []
    for i in range(8):
        if B3[i] < 3: # we need to check if a valid "overlap" exists
            x = C2[i] & B3[i] # least n bits of C
            y = B4[i]>>B3[i] # most n bits of B
            if x==y: # overlap is the same - a valid number exists here
                d_table[B1].append( (C2[i]<<B3[i]) | B4[i] )
        else: # normal shifting is fine
            for k in range(2**(B3[i]-3)):
                d_table[B1].append( (C2[i]<<B3[i]) + (k<<3) + (B4[i]) )

        # NOTE after running, turns out the overlap case here never happens! All 3 cases with smaller shifts are invalid values. 
        # ... but I'll leave the code here because i'll need it for the next part
        # ... except I found a better method to check by using bitwise operators

# find a combination of values that is valid for the fixed bitshift of each
from itertools import product
from math import log2, floor
solutions: list[list[int]] = [[]]
for i, outd in enumerate(prog[:3]):
    last_solutions = solutions.copy()
    solutions.clear()

    # branch solutions for each new number
    for Ai, sol in product(d_table[outd], last_solutions):
        solutions.append([Ai] + sol)
    # print(solutions)

    # filter solutions to remove invalids
    for sol in solutions.copy():
        # we only need to check the latest digit against each other, the prior couplings will be checked on prior loops
        x = sol[0]
        # print(f"for sol {sol}")
        for i, y in enumerate(sol[1:]):
            # print(f"checking {y=}")
            if not x % 2**(floor(log2(y))-(3*(i+1))) == y >> (3*(i+1)):
                # invalid! we can drop this solution
                # print(f"{bin(x)} invalid with {bin(y)} upon << {(i+1)*3}")
                solutions.remove(sol)
                break
            else:
                print(f"{bin(x)} VALID with {bin(y)} upon << {(i+1)*3}")

    # print(solutions)
