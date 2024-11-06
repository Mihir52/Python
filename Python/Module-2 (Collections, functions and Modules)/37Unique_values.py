# Write a Python program to print all unique values in a dictionary. 

dictionary = {'a' : 10,'b' : 20,'c' : 30,'d' : 10,'e' : 20}

# using set method to get unique values
unique_val = set(dictionary.values())

print(unique_val)


# Without using set method
dictionary1 = {'a' : 10,'b' : 20,'c' : 30,'d' : 10,'e' : 20}

unique_val1 = []  #empty list

for val in dictionary1.values():  
  if val not in unique_val1:
    unique_val1.append(val)

print(unique_val1)


