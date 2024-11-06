# Write a Python function that takes two lists and returns true if they have at least one common member. 
"""
def common(list1,list2):
  return bool(set(list1) & set(list2))   #Convert lists to sets and check values

list1 = [1,2,3] 
list2 = [3,4,5]

if common(list1,list2):      #if list1 and list2 inner find at least one common member
  print("Find common member in list")
else:                          #either execute else statement
  print("Not find common member in list")
"""


# Second method
def common(list1,list2):
  for item in list1:    #iterate each elements in list1 
    if item in list2:   #this line check item exits in list2
      return True       #item from list1 is found in list2,execure this line
  return False          #loop complete without finding any common member,this line execute

list_a = [1,2,3]
list_b = [3,4,5]

if common(list_a,list_b):
  print("Lists have common member")
else:
  print("Not find common member in list")
  

