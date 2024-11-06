# Write a Python program to get unique values from a list 

# Simple method
list_1 = [5,6,8,9,1,2,3,1,3,2]
print(list_1)  
unique_list = set(list_1) # using set method to remove duplicates
print(list(unique_list))   #print unique values in list


# using parameterized function
def get_unique(l):    
  return list(set(l))  #return list form to unique values

l = [1,2,3,4,1,2,3.7]   
unique_val = get_unique(l)  # function to store a variable
print(f"Unique values are : {unique_val}")  #print unique value list


# Without using inbuilt method
list_2 = ['a','b','c','d','e','a','c','e']  
unique_vals = []           #empty list to store unique val
for ele in list_2:  
  if ele not in unique_vals:    
    unique_vals.append(ele)   #append method to add unique elements in unique_vals[] variable
print(unique_vals)     #print unique values list

  
  