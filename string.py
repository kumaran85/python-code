#!/usr/bin/env python
hai = 'welcome'
print(hai)

# To avoid single quotes within vars. use \
var = "Ezhil Kuttie's"
print(len(var))

# To print in Upper case
upp = hai.upper()
print(hai.upper())
print(upp)

# To print strings in Lower case
print("Priniting in Lower character")
print(upp.lower())

# Slicing Strings
print(upp[1])
print(upp[2:4])

# Print string from 2nd index onwards
print(upp[2:])

print("printing from last character")
print(upp[-1])
print(upp[:-1])

################################

vars = "Welcome To Red Hat"
print(vars.count('Welcome'))

print(vars.find('Red Hat'))

vars1 = vars.replace('Welcome To Red Hat', 'Linux')
print(vars1)

##############################
# Strring Formatting

strig = '{}  &  {}'.format(vars, vars1)
print(strig)

# Below can be written in python above 3.6

# strig1 = f'{vars} & {vars1} in the World'
