# Write a Python function to calculate the factorial of a number (a nonnegative integer) 

n = int(input("Enter a number : "))   #user input

# factorial intialize with 0
fact = 1

for i in range(1,n+1):
  fact = fact * i

# if number is less than 0 to print this condition
if n < 0:
  print("please enter positive number!")
else:
  print(f"factorial is : {fact}")

