# Write a Python script to merge two Python dictionaries

dict1 = {'a':1,'b':2}
dict2 = {'x':3,'y':4}

# 1.merge dictionary using unpacking  
merge_dict = {**dict1,**dict2}

# 2.Using update method
merge_dict1 = dict1.copy()
merge_dict1.update(dict2)

print(f"Merge dictionary : {merge_dict}")
print(f"Merge dictionary using update method : {merge_dict1}")
