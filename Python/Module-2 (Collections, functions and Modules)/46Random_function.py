# How can you pick a random item from a list or tuple? 

import random

list1 = [10,20,30,40,50]
tuple1 = ('a','b','c','d','e') 

# random item from list
random_list = random.choice(list1)
print(f"Random item from list : {random_list}")

# random item from tuple
random_tuple = random.choice(tuple1)
print(f"Random item from tuple : {random_tuple}")
