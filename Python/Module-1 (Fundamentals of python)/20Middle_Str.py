# Write a Python function to insert a string in the middle of a string. 


def inset_middle_str(str,insert_str):         

  mid_index = len(str) // 2           #find mid part of string 

  new_string = str[:mid_index] + insert_str + str[mid_index:]  #concatination the string

  return new_string               #return final inserted string

str = input("Enter a string : ")   #input string
insert_str = input("Enter insert string in the middle: ")  #input insert string in the middle
print(f"inserted string is : {inset_middle_str(str,insert_str)}")
  