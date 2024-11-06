# Write a Python program to test whether a passed letter is a vowel or not.


letter_input = input("Enter a letter to find vowel or not: ").lower()
vowel = "aeiou"

if len(letter_input) > 1:                #letter > 1 to print this statement
  print("**Please enter a only one letter!!")
elif letter_input in vowel:              #check vowel or not
  print(f"{letter_input} is vowel")
else:
  print(f"{letter_input} is consonent")
