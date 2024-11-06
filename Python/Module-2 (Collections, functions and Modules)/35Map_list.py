# Write a Python program to map two lists into a dictionary 

keys = ['a','b','c','d']
value = [1,2,3,4]

# map lists to a dictionary using the zip() function
map_dict = dict(zip(keys,value))

# print the dictionary
print(f"Mapped list : {map_dict}")