"""Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'a': 300, 'b': 200,'d':400}
Sample output: Counter ({'a': 400, 'b': 400,'d': 400, 'c': 300})."""

# using counter
from collections import Counter

d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'a': 300, 'b': 200,'d':400}

# Counter to add values of common keys
combined_dict = Counter(d1) + Counter(d2)

print(f"Combined dictionary : {combined_dict}")


# without using counter
d1 = {'a': 100, 'b': 200, 'c':300}  
d2 = {'a': 300, 'b': 200,'d':400}

com_dict = d1.copy()  #copy d1

for key,value in d2.items():
  if key in com_dict:
    com_dict[key] += value  #add value for common key
  else:
    com_dict[key] = value  #add new key from d2
print(f"Combined dictionary : {com_dict}")




