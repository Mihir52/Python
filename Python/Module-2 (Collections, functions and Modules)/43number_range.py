# Write a Python function to check whether a number is in a given range

# user inputs
num = int(input("Enter a number : "))
start_range = int(input("Enter a start range : "))
end_range = int(input("Enter a end range : "))

# chekc number in the range or not
if start_range<=num<=end_range:
  print(f"{num} is in the range {start_range} to {end_range}")
else:
  print(f"{num} is not in the range {start_range} to {end_range}")