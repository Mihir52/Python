# Write a Python program to replace last value of tuples in a list. 

tup_list = [(45,89,52),(41,63,7),(1, 2, 3),(7, 8, 9)]

add_val = 10   

#Replace the last value in each tuple using a list comprehension
replace_val = [t[:-1] + (add_val,) for t in tup_list]  

print(f"Original tuple of list : {tup_list}")
print(f"Replace last value of tuples in a list : {replace_val}")

