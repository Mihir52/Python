# How Do You Traverse Through A Dictionary Object In Python?

dictionary = {
  'a' : 97,
  'b' : 98,
  'c' : 99,
  'd' : 100,
}

# Loop through keys:
for k in dictionary:
  print(f"key : {k}")

# Loop through values:
for val in dictionary.values():
  print(f"value : {val}")

# Loop through key-value pairs
for key,value in dictionary.items():
  print(f"key : {key} , value : {value}")

# Loop through keys and access values
print("----------")
for key in dictionary:
  print(f"Key : {key}, value : {dictionary[key]}")