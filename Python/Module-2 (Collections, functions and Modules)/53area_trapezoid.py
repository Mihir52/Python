# Write a Python program to calculate the area of a trapezoid 

# Area = 1/2 * (b1 + b2) * h
# b1 is the length of the first base,
# b2 is the length of the second base,
# h is the height of the trapezoid

# user input
b1 = float(input("length of the first base : "))
b2 = float(input("length of the second base : "))
h = float(input("Enter height : "))

# find area of a trapezoid
area = 0.5 * (b1 + b2) * h

# print area of a trapezoid
print(f"area of a trapezoid : {area}")

