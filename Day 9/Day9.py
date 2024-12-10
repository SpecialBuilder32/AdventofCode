# Advent of Code 2024

# Start Time: 12:22 PM
            
# Pt 1 End Time: 1:01 PM

# Pt 2 Start Time: 7:57 PM - 8:57 (w show)
# Pt 2 End Time: 10:30 PM

# Total Time: ~1hr 40min

# Part 1 - file defrag! 
#   Trying this from a speed perspective instead of replicating the list structure given

with open("Day 9/Day9_Input.txt", "r") as f:
    line = f.readline()
    a = 0 # index within input
    b = len(line)-1
    max_blocks = (len(line)+1)//2 -1

    bkid = 0 # current block id
    bkix = 0 # current block index
    eid = max_blocks # current index of the last blocks we're moving backward
    es = int(line[b]) # size of end block

    cksum = 0 # running checksum
    dbg = ""
    while a <= b-1: # until we meet in the middle
        fchar = line[a]
        for _ in range(int(fchar)): # for each memory cell describing a file
            # dbg += str(bkid)
            cksum += bkid*bkix
            bkix += 1
        a += 1
        echar = line[a]
        for _ in range(int(echar)): # for each memory cell describing an empty space
            # dbg += str(eid)
            es -= 1
            cksum += eid*bkix
            bkix += 1

            if es <= 0: # move to next block at the end
                b -= 2 # ignoring blank space from this end
                es = int(line[b])
                eid -= 1

                if b <= a: # we've met in the middle
                    break
        a += 1
        bkid += 1
        if bkid == eid: # we've met in the middle
            # process the remaining blocks of the end
            for _ in range(es):
                # dbg += str(eid)
                cksum += eid*bkix
                bkix += 1
            break
    # print(dbg)
    print(f"final checksum = {cksum}")

# Part 2 - I don't think we can do this efficiently like before. So this time we use the full list movig stuff
    # this is consequently much much slower than the near instant approach of part 1
with open("Day 9/Day9_Input.txt", "r") as f:
    line = f.readline()

    # setup block representation
    s = 0
    for char in line:
        s += int(char)
    mem = [None]*s
    
    i = 0
    bid = 0
    f = True
    for char in line:
        if f:
            for _ in range(int(char)):
                mem[i] = bid
                i += 1
            bid += 1
        else:
            for _ in range(int(char)):
                mem[i] = "."
                i += 1

        f = not f
    
    # do the compression stuff
    eid = s
    b = len(mem)-1
    for _ in range(bid):
        while (bid:=mem[b]) == ".": # advance past empty space
            b -= 1
        i = b-1
        blen = 1
        while mem[i] == bid:
            i -= 1
            blen += 1

        # find available space
        j = 0
        elen = 0
        cont = False
        while True:
            if mem[j] == ".":
                elen += 1
                if elen == blen:
                    break
            else:
                elen = 0
            j += 1
            if j >= len(mem) or j > b:
                cont = True
                break
        if cont:
            b -= blen
            continue # no space to move this block set

        # move the blocks
        j -= (elen-1)
        for o in range(blen):
            mem[j+o] = bid
            mem[i+1+o] = "."

        b -= blen

    # compute checksum
    cksum = 0
    for i, v in enumerate(mem):
        if isinstance(v, int):
            cksum += v*i
    print(f"final checksum = {cksum}")

        
        