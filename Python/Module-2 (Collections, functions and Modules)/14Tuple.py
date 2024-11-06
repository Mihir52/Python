# Write a Python program to create a tuple with different data types. 

my_tuple = (25,"hello",3.54,True,[45,5,1],{'key':'value'})  #create a tuple

print(f"Different data types tuple : {my_tuple}")  #print this tuple

# each element with its type print
for ele in my_tuple:
  print(f"Element : {ele},Type : {type(ele)}")