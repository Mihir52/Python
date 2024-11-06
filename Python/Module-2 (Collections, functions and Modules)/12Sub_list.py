# Write a Python program to check whether a list contains a sub list 
def check_list(main_list,sub_list):
  sub_len = len(sub_list)           # length to sub list
  for i in range(len(main_list) - sub_len + 1):  #for loop used length of list and minus sublist length 
    if main_list[i:i+sub_len] == sub_list:   #slicing list values 
        return True                          #if match the value return to be true
  return False 

main_list = [1,2,4,0,4] 
sub_list = [5,6]
if check_list(main_list,sub_list): #call the function and passed list using argument,if sublist is found to execute this condition
  print("Sublist found")  
else:     #not found sublist to execute this condition
  print("Sublist not found.")
