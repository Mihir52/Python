# Write a Python function that takes a list and returns a new list with unique elements of the first list. 
 
def list():  #function defination
  user_list = []     #empty list
  print("Enter elements for the list. Type 'done' to finish the list.")  

  while True:   
      list_input = input("Enter an element (or 'done' to finish): ") #user input list
      if list_input.lower() == 'done':      #if user write 'done' to end of list
          break
      user_list.append(list_input)   #add items in user_list[]

  print("Original List is:", user_list)     #print original list


  unique_list = set(user_list)     #find unique elements
  print(f"Unique list : {unique_list}")   #print unique elements in the list

list()  #function calling