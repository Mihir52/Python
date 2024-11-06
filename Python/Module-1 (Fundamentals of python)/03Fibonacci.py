# Write a Python program to get the Fibonacci series of given range. 
n = int(input("Enter a number : "))  #user input

a = -1
b = 1
 
if(n == 0 or n<0): #if condition to user enter valid number
  print("Please enter a valid number") 

for i in range(0,n):  
  c = a + b                #-1 + 1 = 0
  print(c,end=",")         #print fibonacci series
  a = b                    #swap value a = b
  b = c                    #swap value b = c
  
  