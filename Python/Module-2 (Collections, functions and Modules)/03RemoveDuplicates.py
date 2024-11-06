# Write a Python program to remove duplicates from a list.
"""
list1 = [1,2,3,100,1,"Hello","mihir","mihir",100]

unique_list = list(set(list1))     #using set method to remove duplicate values

print(f"Original List : {list1}")        #print original list

print(f"Remove duplicates from a list : {unique_list}")   #print-duplicate values remove list
"""


# Second way
list1 = [1,2,3,4,5,1,2,3]        
unique_list = []          #empty list 
for items in list1:             #for loop using iterate each items
  if items not in unique_list:   #if condition to check and append the value is not duplicates
    unique_list.append(items)
  
print(f"Original list : {list1}")      #print original list
print(f"Removing duplicates : {unique_list}")   #print list removing duplicate values

