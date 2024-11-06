# Write a Python program to calculate the length of a string.


str = input("Enter a string : ")  #input a string

"""
# in-build method - len(str)
print(f"length of string is : {len(str)}") #find length of string and print length
"""


# Without using in build mehthod
length = 0
for char in str:
  length += 1

print(f"Length of string is : {length}")


