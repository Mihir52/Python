# Write python program that swap two number with temp variable and without temp variable

# Using temp variable
print("------Using temmp variable------")
a = 10
b = 50
print(f"Before swap value:\na : {a}, b : {b} ")
temp = a
a = b
b = temp
print(f"After swap value:\na : {a}, b : {b}")

# Without using temp variable
print("-----Without using temp variable------ ")
c = 60
d = 40

print(f"Before swap value:\nc : {c}, d : {d} ")

c,d = d,c
print(f"After swap value:\nc : {c}, d : {d}")


# Using another method
print("------Using addition and subtraction------")
e = 50
f = 78
print(f"Before swap value:\ne : {e}, f : {f} ")
e = e + f
f = e - f
e = e - f
print(f"After swap value:\ne : {e}, f : {f} ")



