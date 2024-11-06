# Write a Python program to check if a number is positive, negative or zero.
# User input
n = int(input("Enter a number : "))

if n==0:    # zero number to execute if condition
  print(f"{n} is zero")
elif n<0:   #negative number to execute this condition
  print(f"{n} is negative number.")
else:       #positive number to execute this condition
  print(f"{n} is positive number")