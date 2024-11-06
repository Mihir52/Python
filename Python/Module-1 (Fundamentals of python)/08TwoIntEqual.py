# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.
# First method
"""
num1 = int(input("Enter number1 : "))   #user input
num2 = int(input("Enter number2 : "))


if (num1 == num2) or (num1+num2==5) or (abs(num1-num2) == 5) :   #check conditions: equl and diffrence 5
  print("Result is : True")
else:                                       #if condition is false then print else statement
  print(f"Result is : {num1+num2}")
"""

# abs(absolute value) - build in functionality returns the absolute value of the specific number


# Second method using parameterized function:
def check_equal_val(a,b):
  return a == b or a+b==5 or abs(a-b) == 5

n1 = int(input("Enter a : "))
n2 = int(input("Enter b : "))
print(check_equal_val(n1,n2))


"""
print(abs(5))    # Output: 5
print(abs(-5))   # Output: 5
print(abs(0))    # Output: 0
"""