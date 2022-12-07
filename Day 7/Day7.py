# Advent of Code 2022

# Start Time: 3:09 PM (yes during Space Robotics class :P)
    # paused 3:36,
    # resume 4:24
    # pause 6:01p (2hr05min)
    # resume 6:28p
# Pt 1 End Time: 6:41p (2hr17min)
# Pt 2 End Time: 6:57p
# Total Time: 2hr45min

# This is gonna be a fun time - File system crawling
from __future__ import annotations # to allow type hints of self class
import re
from dataclasses import dataclass, field
from typing import ClassVar

# objects for the tree
@dataclass
class fileo(): # filesystem object
    name: str
    size: int = 0
    parent: fileo = field(default=None, repr=False)

@dataclass # with all the special stuff I'm doing, this shouldn't be a dataclass - however want to learn more about its features
class direc(fileo):
    children: dict = field(default_factory=dict) # syntax generates new list
    direcs: ClassVar[list] = []
    
    def __post_init__(self,*args): # runs after generated @dataclass init
        direc.direcs.append(self) # add to global list of all direcs
            # this has really become an exercise in pointers for me.

    def append_child(self, child: fileo) -> fileo:
        self.children.update({child.name: child})
        self.update_size(child.size) # update size of direc and all parents
        child.parent = self # add reference to parent to the child
        return child

    def update_size(self, added_size: int) -> None:
        self.size += added_size
        if self.parent: # if not None (aka root dir)
            #pylint: disable-next=no-member
            self.parent.update_size(added_size)

with open('Day 7/Day7_Input.txt', 'rt', encoding='UTF-8') as f:
    lines = f.readlines()

cl = 1 # current line index, starting from second line
cd = root = direc('/')

# run through log and reconstruct directory tree
while cl<len(lines):
    if lines[cl][2:3+1] == 'cd': # change dir
        name = re.match(r'\$ cd ([\w\.]+)', lines[cl]).group(1)
        if name == '..': # go up a dir
            cd = cd.parent
        else:
            cd = cd.children[ name ] # substring portion after command
        cl += 1
    elif lines[cl][2:3+1] == 'ls': # list subdirs
        cl += 1
        while cl<len(lines) and lines[cl][0] != '$': # until hitting another command
            m = re.match(r'(\w+) ([\w\.]+)', lines[cl])
            if m.group(1) == 'dir':
                cd.append_child( direc(m.group(2)) ) # create new direc() and add to parent
            else: # individual file
                cd.append_child( fileo(m.group(2), int(m.group(1))) )
            cl += 1

print(f'Reconstructed {len(direc.direcs)} directories')
# 1hr 57min to here - 5:54 PM
    # additional corrections to above done after this time

# Part 1 find smallest directories (over 100000 size)
s = 0
for d in direc.direcs:
    if d.size <= 100000:
        s += d.size
print(f'The sum of the bloated directories is {s}')

# Part 2 find smallest directory to free up enough space
total_space = 70000000
needed_space = 30000000

free_space = total_space - root.size
required_delete_size = needed_space - free_space

print(f'The required deletion space is {required_delete_size}')
big_enough = list(filter(lambda e: e.size>required_delete_size, direc.direcs))
big_enough.sort(key=lambda e: e.size)
print(f'The smallest directory to delete is {big_enough[0].name} with a size of {big_enough[0].size}')
