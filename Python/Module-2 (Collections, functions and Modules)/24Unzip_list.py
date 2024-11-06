# Write a Python program to unzip a list of tuples into individual lists. 

tup_list = [(45,56),(8,9),(5,0),(4,9)]

# Use zip() to unzip the list of tuples 
list1, list2 = zip(*tup_list)

# zip returns tuples
list1 = list(list1)
list2 = list(list2)

# print the result
print(f"List 1 : {list1}")
print(f"List 2 : {list2}")



