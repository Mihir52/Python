# Write a python program to sum of the first n positive integers. 

n = int(input("Enter number1 : "))

if n<0:
  print("Please enter a positive number!")
else:
  sum = 0                   #sum intialize with zero
  for i in range(1,n+1):    #for loop to start 1 and end of n
    sum = sum + i           #sum formula
  print(f"Sum of {n} is the : {sum}")     #print result