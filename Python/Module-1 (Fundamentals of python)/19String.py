"""Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string."""

str = input("Enter a string : ")   #user input


if len(str) < 2:        # check length of string < 2
  empty = ""
  print(empty)
else:                   
  result = str[:2] + str[-2:]   #first 2 and the last 2 characters
  print(result)
