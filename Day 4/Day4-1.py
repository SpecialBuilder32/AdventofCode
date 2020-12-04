# Advent of Code 2020
# Day 4, Puzzle 1

# Counts the number of "valid" passports a set of data describes

# credentials class
class Credential():
    def __init__(self):
        self.data = {
            'byr' : None, # Birth Year
            'iyr' : None, # Issue Year
            'eyr' : None, # Expiration Year
            'hgt' : None, # Height
            'hcl' : None, # Hair Color
            'ecl' : None, # Eye Color
            'pid' : None, # Passport ID
            'cid' : None # Country ID
       }

    def register_pair(self, pair):
        # adds the data provided by pair into the attributes of the object
        key, value = pair.split(':')
        self.data[key] = value

    def check_validity(self):
        # checks validity of overall credential
        return not (self.data['byr']==None or self.data['iyr']==None or self.data['eyr']==None or self.data['hgt']==None or self.data['hcl']==None or self.data['ecl']==None or self.data['pid']==None) 
            # using DeMorgans law to return false if any entries are None
            # ignores CID because the hero dosen't have a passport and is being sneaky

    def __str__(self):
        string = ""
        for key in self.data:
            string += key+':'+str(self.data[key])+'\n'
        return string.rstrip('\n')

creds = [] # empty list of credentials
current_cred = Credential() # create object to add incoming data to


# read in input and parse data
with open('Day 4/Input_4.txt', 'r') as input_file:
    for line in input_file:
        
        if line == "\n": # newline separates credential entries
            creds.append(current_cred) # push credential to list
            current_cred = Credential() # create new credential object
        
        else:
            for pair in line.rstrip('\n').split(' '): # split into key-value pairs
                current_cred.register_pair(pair)
    
    creds.append(current_cred) # push last credential, as last entry is not followed by newline

# count valid passports
valid_creds = 0
for cred in creds:
    # print('-'*25)
    # print(cred)
    # print('VALIDITY:', cred.check_validity())
    if cred.check_validity():
        valid_creds += 1

print("Valid Passports:  ", valid_creds)