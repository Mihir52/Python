# Write a Python program to find the length of a tuple. 

# Using in-built method
tuple1 = (1,2,3,4,5)

# len() function to provide a length of tuple
length1 = len(tuple1)

print("length of the tuple is:", length1)


# Without in-built method
tuple2 = (1,2,3,4,5,6,7,8,9,10)

length2 = 0 #length variable,initialize a zero

for i in tuple2:
  length2 += 1   #count the elements in tuple and add length variable

print(f"length of the tuple is : {length2}")




