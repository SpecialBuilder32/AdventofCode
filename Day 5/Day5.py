# Advent of Code 2024

# Start Time: 6:18 PM
            
# Pt 1 End Time: 7:02 PM
# Pt 2 End Time: 7:11 PM

# Total Time: 53 Min


# Part 1 - Printer manual printing support
import re
import json

with open("Day 5/Day5_Input.txt", "r") as f:
    lines = f.readlines()
    rules: dict[int, set[int]] = dict()
    updates: list[list[int]] = list()
    rules_seg = True
    for line in lines:
        if line == "\n":
            rules_seg = False
            continue

        if rules_seg:
            a, b = map(int, re.match(r"(\d+)\|(\d+)", line).groups())
            r = rules.setdefault(a, set())
            r |= {b}
        else:
            updates.append(json.loads(f"[{line.strip()}]"))
    
    # checking each pages list
    score = 0
    score2 = 0
    for update in updates:
        good_update = True
        for i, page in enumerate(update): # except for last page
            preceeding_pages = set(update[:i])
            if len(rules.get(page, set())&preceeding_pages) > 0:
                # a rule has been broken!
                good_update = False
                break
        if good_update:
            mid_page = update[len(update)//2]
            score += mid_page

        # Part 2 - fixing the wrong ordered updates!
        if not good_update:
            supdate = set(update)
            order = [] # build in reverse, finding elements with no pages that must come after
            while len(supdate) > 0:
                for p in supdate:
                    if rules.get(p,set()).isdisjoint(supdate-{p}):
                        # this page has no required pages after it
                        break
                order.append(p)
                supdate.remove(p)
            fixed_update = order[::-1]
            mid_page = fixed_update[len(fixed_update)//2]
            score2 += mid_page



    print(f"summed middle page numbers = {score}")
    print(f"summed middle page numbers, or the fixed updates = {score2}")
