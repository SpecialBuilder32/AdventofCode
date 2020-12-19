#Advent of Code 2020
# Day 18 Puzzle 1

# Evaulates math expressions where the operations are handled in left-to-right order and not by PEMDAS
import re
evaluations = []

def matching_parenthesis(expression):
    # finds and returns the indicies of a pair of parenthesis
    open_parentheses = 0
    closed_parentheses = 0
    for i in range(len(expression)):

        if expression[i] == '(': #
            if open_parentheses == 0:
                a = i # record the first one
            open_parentheses += 1

        if expression[i] == ')': # figure out if closed parenthesis is the outermost or not
            closed_parentheses += 1

            if closed_parentheses == open_parentheses: # matching set
                return a, i

    return 0, 0 # incase something went wrong

def new_math_evaluate(expression):
    # evaluates the given expression using the new math order of operations

    # find and evaluate parenthesis
    while expression.count('(') > 0: # while there are still parenthesis in the expression
        a, b = matching_parenthesis(expression)

        # split into parts for replacement
        prefix = expression[:a]
        par = expression[a+1:b]
        suffix = expression[b+1:]

        new_par = new_math_evaluate(par) # evaluate the parentheses
        
        # reassemble
        expression = prefix + new_par + suffix

    # evaluate left-to-right expressions
    split_exp = expression.split(' ') # split on the spaces
    while split_exp.count('*') > 0 or split_exp.count('+') > 0: # while there are still operations to do
        x = int(split_exp[0])
        y = int(split_exp[2])

        if split_exp[1] == '+': # evaluate and store result into list
            split_exp[0] = x + y
        elif split_exp[1] == '*':
            split_exp[0] = x * y

        split_exp.pop(2) # remove operator and second number
        split_exp.pop(1)

    return str(split_exp[0])

# input lines and process
with open('Day 18/Input_18.txt', 'r') as input_file:
    for line in input_file:
        print("Evaluating:", line.rstrip('\n'), end=' ')
        evaluations.append( int(new_math_evaluate(line)) )
        print('=', evaluations[-1])

print("Sum of each expression: ", sum(evaluations))