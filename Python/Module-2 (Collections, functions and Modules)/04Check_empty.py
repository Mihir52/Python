# Write a Python program to check a list is empty or not. 

"""
empty_list = []
list1 = [12,45,"kem cho",13] 

if empty_list == list1:   #if emptylist equal to list1 to print "Empty list"
  print("Empty list")
else:                      #either print "Not empty list"
  print("Not empty list")
"""

# using parameterized function

def is_empty(input_list):
  return len(input_list) == 0   #list length isequl to 0

myList = [1,2,3,4,5,6,7,8]   
if is_empty(myList):          #if check the list is empty or not
  print("List is empty!!")
else:
  print("List is not empty")   #if list is not empty to execute this print statement