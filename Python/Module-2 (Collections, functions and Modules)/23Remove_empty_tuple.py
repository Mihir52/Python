# Write a Python program to remove an empty tuple(s) from a list of tuples. 

tuple_list = [(1,2,3),(),(4,5),(),(6,7,8),()]

#empty list to store empty tuples
filtered_list = []

for t in tuple_list:
    if t:  # Check if the tuple is non-empty
        filtered_list.append(t)

# Print the result
print("removing empty tuples:", filtered_list)
