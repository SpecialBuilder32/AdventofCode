# Advent of Code 2020
# Day 19 Puzzle 2

# Checks if text follows a series of that can loop (sadly)
import re

rules = {} # dict containing rules
class rule():
    def __init__(self, input_line):
        groups = re.match(r'(\d+): (?:"(\w)"|((?:(?:\d|\|)+.?)+))$', input_line)
        
        self.id = int(groups.group(1)) # set rule ID
        self.char = groups.group(2) # set rule's character, if it exists. Otherwise None
        
        if groups.group(3): # if list of rules
            subrules_text = groups.group(3)
            if subrules_text.count('|') > 0: # if there is a pipe
                split_text = subrules_text.split('|')
                self.subrules = [None, None]
                self.subrules[0] = tuple(map(int, split_text[0].rstrip(' ').split(' ')))
                self.subrules[1] = tuple(map(int, split_text[1].lstrip(' ').split(' ')))
            else: # no pipe
                self.subrules = [tuple(map(int, subrules_text.split(' ')))]
        else: #no rules
            self.subrules = None

        self.length = None

    def get_length(self):
        # returns the length of characters the rule applies to, and figures it out if needed
        if not self.length: # if it hasn't been determined, find it
            if self.char: # if this is a character rule
                self.length = len(self.char)

            else: # start running through rules
                l = 0
                for r in self.subrules[0]:
                    l += rules[r].get_length()
                self.length = l
        
        return self.length

    def check_message(self, message):
        # checks if the given message or message portion follows this rule
        if not len(message) == self.get_length(): # if the lengths don't match
            return False

        else: # start checking sub rules
            if self.subrules: # if there are subrules
                compliance = False
                for option in self.subrules: # for any of the optional orderings
                    option_compliance = True
                    c = 0 # iterator for current character
                    for rule in option:
                        try:
                            alotted_characters = rules[rule].get_length()
                            option_compliance *= rules[rule].check_message(message[c:c+alotted_characters])
                            c += alotted_characters
                        except IndexError: # if we've looped past the end of the string
                            option_compliance *= False # rule has failed
                            print("End of loop")

                    compliance += option_compliance # or of the overall
                
                return bool(compliance)

            else: # check character
                return message == self.char


# read in rules and messages
with open('Day 19/Input_19.txt', 'r') as input_file:
    rules_text, messages_text = input_file.read().split('\n\n')

    # parse rules text
    for line in rules_text.split("\n"):
        this_rule = rule(line)
        rules[this_rule.id] = this_rule

    messages = messages_text.split("\n")

# fix the two broken rules
rules[8] = rule('8: 42 | 42 8')
rules[11] = rule('11: 42 31 | 42 11 31')


# count messages that meet rules
valid_messages = 0
for message in messages:
    valid_messages += rules[0].check_message(message)

# print results
print("Valid Messages: ", valid_messages)

