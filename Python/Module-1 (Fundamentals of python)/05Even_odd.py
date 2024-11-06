# Write a Python program to find whether a given number is even or odd,print out an appropriate message to the user. 

n = int(input("Enter a number : "))

if n == 0:                       #user enter 0 to execute this statement
  print("Zero number")
elif n % 2 == 0:                 #check even number and execute
  print("Even number")
else:                            #Not zero and not even then print odd number
  print("Odd number")