# Write a Python function that checks whether a passed string is palindrome or not

# input string
str = input("Enter a string : ")

# slicing method use to reverse a string
check_palindrome = str[::-1]

# if string is palindrom to execute this condition
if str == check_palindrome:
  print("Palindrome string")
else:  #else:string is not palindrome
  print("Not palindrome!")
