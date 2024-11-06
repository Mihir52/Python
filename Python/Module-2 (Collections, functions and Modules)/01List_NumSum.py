# Write a Python function to get the largest number, smallest num and sum of all from a list.

# Using inbuild method
"""
def largest_smallest_sum(number):              
  if not number:   #Check if the list is empty
    return None,None,0  #Return largest and smallest None, and sum is 0
  
  largest = max(number)      #max is a inbuild method to find max number
  smallest = min(number)     #min is a inbuild method to find mininum number
  total_sum = sum(number)    

  return largest,smallest,total_sum

list = [3,8,10,56,89,2]       #static List
largest,smallest,total_sum = largest_smallest_sum(list)   #Functino call
print(f"Largest : {largest}\nSmallest : {smallest}\nSum : {total_sum}")  #print the result
"""


# without using inbuild method
def sumofNumbers(numbers):
  if not numbers:         #if list is empty then 
    return None,None,0    #return largest = None,smallest = None and sum = 0
  
  largest = numbers[0]       #Largest varibale to store largest number
  smallest = numbers[0]      #smallest variable to store smallest number
  total_sum = 0               #total sum of whole list numbers

  for numbers in numbers:           #for loop iterate each number in the list
    if numbers > largest:
      largest = numbers               #if number is largest
    elif numbers < smallest:            
      smallest = numbers              #if numbers is smallest
    total_sum += numbers           

  return largest, smallest, total_sum

list = [10,20,50,100,80]        #static list
largest, smallest, total_sum = sumofNumbers(list)    
print(f"Largest : {largest}\nSmallest : {smallest}\nSum : {total_sum}") #print the last result
  


