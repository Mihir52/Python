# Write a Python program to count the number of characters (character frequency) in a string.

def count_ch(str):

  dict = {}
  for i in str:                   #mihir
    if i in dict:                 #i=1
      dict[i] += 1
    else:                         #m=1, i=1+1=2, h=1, r=1
      dict[i] = 1

  return dict                     #m=1, i=2, h=1, r=1

input_str = input("Enter string : ") 
print(f"Character frequency:\n{count_ch(input_str)}")