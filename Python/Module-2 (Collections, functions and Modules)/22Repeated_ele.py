# Write a Python program to find the repeated items of a tuple. 

tup = (45,56,45,10,85,10,85)

repeat_items = set()

# each elements in tuple to count and add repeaat.items variable to store repeted items
for i in tup:    
  if tup.count(i) > 1:
    repeat_items.add(i)

# print result 
print(f"repeted items of a tuple : {repeat_items}")

