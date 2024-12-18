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
initA = 0
while True:
    # print(f"trying regA = {initA}")
    regA = initA
    inst = 0
    stout.clear()
    
    while True:
        try:
            OpCode[prog[inst]](prog[inst+1])
            inst += 2
        except IndexError:
            # valid end of program
            break

        # can we quit early (incase of infinite loops?)
        if stout:
            i = len(stout)-1
            if stout[i] != prog[i]:
                break


    if stout==prog:
        # we've found the static pair!
        print(f"initial register A value for input->output: {initA}")
        break

    initA += 1 # try the next value

    ## Well damn its such a big number that even with the early quits checking every number is taking more than 30 mins.
        # we need a different approach