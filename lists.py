#!/usr/local/bin/python
list1 = ["apple", "banana", "jack"]
print("printing all the items in the list: " '{}'.format (list1))
print("printing the number of items in the list: "'{}' .format (len(list1)))
print("printing the last item:  "'{}' .format (list1[-1]))
list1.insert(2, "tiger")
list1.extend(["rose", "lotus", "peacock"])
list1.append("panther")
print(list1)
print("removing an item from the list: " '{}' .format (list1.remove("tiger")))
print("after removing an item: " '{}' .format (list1))

# Iterate the items in the for loop

val = 1
for items in list1:
    print("printing the item " '{}' " "   '{}' .format  (val,items))
    val +=1
exit    

# Adding list of list
list_new = ["one", 1 , "two", 2 , 
        ["animal",
           ["me", "you", "she"]]]
print(list_new[2])
print(type(list_new))
