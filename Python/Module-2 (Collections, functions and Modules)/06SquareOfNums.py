# Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30.

square = []      #empty list to store squares

for i in range(1,31):  #for loop generate squres from 1 to 30
  square.append(i**2)

first_five = square[:5]     #first five elements
last_five = square[-5:]     #last five elements

#print result
print(f"First five squares : {first_five}")  
print(f"Last five squares  : {last_five}")