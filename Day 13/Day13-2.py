# Advent of Code 2020
# Day 13 Puzzle 2

# Finds the earliest possible time that has buses depart in the specified consecutive minutes

## Solves by an attempted usage of the Chinese Remainder Theorem (Based on 2 hours of modular arithmetic learning)
#       Uses the existance construction

# input data
with open('Day 13/Input_13.txt', 'r') as input_file:
    lines = input_file.readlines()
    buses = lines[1].split(',')

# calculate each step of the remainder theorem
    # x=x1(mod n1) and x=x2(mod n2)
x1=len(buses)-1
n1=int(buses[0])
for i in range(1, len(buses)):
    if not buses[i] == 'x': # ignore if its an x
        x2=len(buses)-1-i # get next bus
        n2=int(buses[i])

        print('-'*25)
        print('x1 ≡ {0} (mod {1})'.format(x1, n1))
        print('x2 ≡ {0} (mod {1})'.format(x2, n2))

        # calculate Bezout Coefficients
        # α*n1 + β*n2 = gcd(n1, n2) = 1      n1 and n2 are coprime, ∴ gcd=1
        # thus, α*n1 ≡ 1 (mod n2)     β*n2 ≡ 1 (mod n1)
        α = pow(n1, -1, n2) # modular inverse of n1
        β = pow(n2, -1, n1) # modular inverse of n2

        print("Bezout: α=", α, " β=", β, sep='')
        print("α*n1 + β*n2 = {0} ≡ {1} (mod {2})".format(α*n1 + β*n2, (α*n1+β*n2) % (n1*n2), n1*n2))

        # calculate x, with a mod of n1*n2
        x1 = x1*β*n2 + x2*α*n1
        n1 = n1*n2

        print('Existence Constuction: x = {0} ≡ {1} (mod {2})'.format(x1, x1%n1, n1))

# print x
print('-'*25)
print("x ≡", x1)
print("x ≡", x1%n1)

# print earliest time
print("Earliest Time for Bus Departure Ordering: ", x1%n1-(len(buses)-1))
