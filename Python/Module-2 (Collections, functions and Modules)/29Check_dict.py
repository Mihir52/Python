# Write a Python script to check if a given key already exists in a dictionary

dictionary = {
  4:'four',
  9:'nine',
  0:'zero'
}

check_key = 10

# if condition check the key exits in the dictionary
if check_key in dictionary:
  print(f"{check_key} is already exists in dictionary")
# either else condition execute
else:
  print(f"{check_key} does not exits in dictionary!")
