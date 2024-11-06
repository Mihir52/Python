# Write a Python function to check whether a number is perfect or not. 

num = int(input("Enter number : "))

# initialize sum with 1
divisor_sum = 1

# check number is 2 or greatest
if num >= 2:
    for i in range(2,(num // 2) + 1):
        if num % i == 0:
          divisor_sum += i

#check divisor and number is equal to 
if divisor_sum == num:
  print(f"{num} is perfect number.")
else:
  print(f"{num} is not perfect number!")
