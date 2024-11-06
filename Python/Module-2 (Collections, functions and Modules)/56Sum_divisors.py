# Write a Python program to returns sum of all divisors of a number 
# Ex:(12)=(1+2+2^2)(1+3)
#        =(1+2+4)(1+3)
#        = 7×4=28

# user input number
num = int(input("Enter a number : "))

# initialize with 0
sum_divisors = 0

# using loop to find divisors
for i in range(1,num+1):
  if num % i == 0:
    sum_divisors += i

print(f"sum of all divisors is : {sum_divisors}")