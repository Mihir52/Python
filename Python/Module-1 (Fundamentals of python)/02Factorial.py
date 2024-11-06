# Write a Python program to get the Factorial number of given number

# user input
n = int(input("Enter a number to get the factorial : "))
fact = 1     # initialize fact 1
for i in range(1,n+1): # using for loop ,1 to n 
  fact = fact * i  # return factorial

# print statement
print(f"Factorial is : {fact}")
