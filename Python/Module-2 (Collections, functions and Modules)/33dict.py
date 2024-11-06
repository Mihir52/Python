# Write a Python program to check multiple keys exists in a dictionary 

my_dict = {
  'a' : 97,
  'b' : 98,
  'c' : 99,
  'd' : 100,
}

# List of keys to check
keys_to_check = ['a', 'b']

# Check if all keys exist using 'all()'
if all(key in my_dict for key in keys_to_check):
  print(f"All keys {keys_to_check} exist in the dictionary.")
else:
  print(f"keys does not exits")


