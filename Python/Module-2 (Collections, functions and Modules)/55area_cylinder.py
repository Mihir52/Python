# Write a Python program to calculate surface volume and area of a cylinder 

# Volume = π * r2 * h 
# Surface area = 2*3.14*r(r+h)

# r - adius of the cylinder's base
# h - cylinder height 

radius = float(input("Enter radius of a cylinder : "))
height = float(input("Enter height of a cylinder : "))

# Calculate the volume
volume = 3.14 * radius** 2 * height

# Calculate the surface area
surface_area = 2 * 3.14 * radius * (radius + height)

print(f"volume of the cylinder is: {volume}")
print(f"surface area of the cylinder is: {surface_area}")

