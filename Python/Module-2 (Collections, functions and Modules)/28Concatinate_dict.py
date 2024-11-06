# Write a Python script to concatenate following dictionaries to create a new one. 

dict1={
  'a':1,
  'b':2,
  'c':3,
}
dict2={
  'd':4,
  'e':5,
  'f':6,
}

# concatenate dict using unpacking operator
dict3 = {**dict1, **dict2}
# print the concatinate dictionary
print(f"Concatenate dictionary : {dict3}")


# using for loop
new_dict = {} #empty dict
for i in (dict1,dict2):  #each dictionary and update the new_dict
  new_dict.update(i)

print(f"Concatenate using loop : {new_dict}")


