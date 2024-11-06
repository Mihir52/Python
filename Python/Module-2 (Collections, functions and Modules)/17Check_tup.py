# Write a Python program to check whether an element exists within a tuple.

my_tuple = (10,20,30,40,50)

ele = 70

if ele in my_tuple:           #check whether an element exists within a tuple
  print(f"Element : {ele} exits in tuple")
else:                         #not exists in tuple to execute this condition
  print(f"Element : {ele} does not exits in tuple.")
