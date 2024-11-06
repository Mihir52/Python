# How Do You Check The Presence Of A Key In A Dictionary? 

dictionary = {
  'a' : 97,
  'b' : 98,
  'c' : 99,
  'd' : 100,
}

check_key = 'a'

# if condition check the key exits in the dictionary
if check_key in dictionary:
  print(f"{check_key} exits in the dictionary ")
# either else condition execute
else:
  print(f"{check_key} is not exits in the dictionary!")
