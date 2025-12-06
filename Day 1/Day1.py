# Advent of Code 2025

# Start Time: 11:09 PM (while sick and watching Star Trek)
# Pt 1 End Time: 11:21 PM
# Pt 2 End Time: 5:05 PM (took a while cause double counting nonsense)

debug_print = False

with open("Day 1/Day1_Input.txt", "rt") as f:
    instructions = f.readlines()

    dial = 50
    password = 0
    password2 = 0

    for instruct in instructions:
        direc = instruct[0]
        scal = -1 if direc=="L" else +1
        val = scal*int(instruct[1:])
        
        zero_crosses = 0
        dist_to_zero = dial if direc == "L" else (100-dial)%100
        dist_past_zero = abs(val)-dist_to_zero

        if debug_print: print(f"{instruct.strip()}, {dial}->{(dial+val)%100}", end="")

        start_at_zero = dial==0
        dial += val
        dial %= 100
        end_at_zero = dial==0

        if dist_past_zero > 0:
            zero_crosses = dist_past_zero//100 + 1 - start_at_zero - end_at_zero
            password2 += zero_crosses

        if debug_print: print(f", {zero_crosses=}", end="")

        if end_at_zero:
            password += 1
            password2 += 1

        # if start_at_zero and end_at_zero:
        #     password2 -= 1 # we've double counted this 0 already

        if debug_print: print(f", {password2}", end="\n")

print(f"Part 1 Solution: {password}")
print(f"Part 2 Solution: {password2}")
     