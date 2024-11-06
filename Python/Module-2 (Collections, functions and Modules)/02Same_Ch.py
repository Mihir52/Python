"""Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings."""

str_list = ["abcda","121","hello","coc","new"]

count = 0         #count variable initialize with 0 value

for i in str_list:       # for loop use to each elements in list 
  if len(str_list) >= 2 and i[0] == i[-1]:    #To find first char and last char are same
    count += 1                          #count = 0 is increment to based on condition

print("count str : ",count)   #print result