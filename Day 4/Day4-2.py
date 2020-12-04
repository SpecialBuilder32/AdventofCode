# Advent of Code 2020
# Day 4, Puzzle 2

# Counts the number of "valid" passports a set of data within valid parameters

import re

# credentials class
class Credential():
    def __init__(self):
        self.data = {
            'byr' : '-1', # Birth Year
            'iyr' : '-1', # Issue Year
            'eyr' : '-1', # Expiration Year
            'hgt' : '-1', # Height
            'hcl' : 'None', # Hair Color
            'ecl' : 'None', # Eye Color
            'pid' : 'None', # Passport ID
            'cid' : 'None' # Country ID
       }

    def register_pair(self, pair):
        # adds the data provided by pair into the attributes of the object
        key, value = pair.split(':')
        self.data[key] = value

    def check_validity(self):
        # applies data validation and checks overall validity of overall credential
        valid_fields = 0
        
        # verify each data field is within expected ranges
        if int(self.data['byr']) >= 1920 and int(self.data['byr']) <= 2002:
            valid_fields += 1

        if int(self.data['iyr']) >= 2010 and int(self.data['iyr']) <= 2020:
            valid_fields += 1

        if int(self.data['eyr']) >= 2020 and int(self.data['eyr']) <= 2030:
            valid_fields += 1

        #hgt
        grouped_hgt = re.match(r'(\d+)(.+)', self.data['hgt'])
        if grouped_hgt:
            if grouped_hgt.group(2) == 'in' and int(grouped_hgt.group(1)) >= 59 and int(grouped_hgt.group(1)) <= 76:
                valid_fields += 1
            if grouped_hgt.group(2) == 'cm' and int(grouped_hgt.group(1)) >= 150 and int(grouped_hgt.group(1)) <= 193:
                valid_fields += 1

        # hcl
        if re.match(r'#([a-f]|[0-9]){6}', self.data['hcl']):
            valid_fields += 1

        # ecl
        if re.match(r'(amb|blu|brn|gry|grn|hzl|oth)$', self.data['ecl']):
            valid_fields += 1

        # pid
        if re.match(r'\d{9}$', self.data['pid']):
            valid_fields += 1

        return valid_fields == 7


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
    if cred.check_validity():
        # print('-'*25)
        # print(cred)
        # print('VALIDITY:', cred.check_validity())
        valid_creds += 1

print("Valid Passports:  ", valid_creds)