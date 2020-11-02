#!/usr/local/bin/python
answer = "no"
print(answer)
while answer == "no":
     answer = input("Are you there:? ")
     print(answer)
print("We're there")

# Working on for loop

list1 = ["anand", "Kutties", "Ezhil"]

for items in list1:
    print("NUmber of names in the given list: "  '{}' .format(items))
