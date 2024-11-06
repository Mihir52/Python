# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 

try:
  num1 = int(input("Enter number 1 : "))  #user input
  num2 = int(input("Enter number 2 : "))  #user input
  num3 = int(input("Enter number 3 : "))  #user input

  if num1 == num2 or num2 == num3 or num1 == num3:  #two values are equal sum will be zero.
    print("The result is  : 0")
  else:
    print(f"The result is  : {num1+num2+num3}")     #print sum of 3 numbers

except:
  print("Enter a valid input!!")