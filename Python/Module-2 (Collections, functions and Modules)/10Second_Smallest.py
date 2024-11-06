# Write a Python program to find the second smallest number in a list. 

num_list = [10,20,45,78,10]
unique_numbers = list(set(num_list))  #set method use to remove duplicates
unique_numbers.sort()   #sort method is convert list in ascending order

print(unique_numbers)               

if len(unique_numbers) < 2:        # If the list has less than 2 elements, return None
  print("There is no second smallest number.")
else:            
  second_smallest = unique_numbers[1]  # return the second smallest number
  print("Second smallest number is : ",second_smallest) #print second smallest number

