# Write a Python program to find the highest 3 values in a dictionary 

dictionary = {
  'a' : 100,
  'b' : 500,
  'c' : 1000,
  'd' : 900,
  'e' : 400,
}

# find highest 3 value
highest_val = sorted(dictionary.values(),reverse=True)[:3]

print(f"highest 3 values : {highest_val}")


# Using loop through
# empty list to store highest 3 values
highest_three_val = []

for val in dictionary.values():
  highest_three_val.append(val) #add value in list
  # sort the list in descending order and only 3 values
  highest_three_val = sorted(highest_three_val,reverse=True)[:3]
print(f"highest 3 value using loop : {highest_three_val}")