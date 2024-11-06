# Write a Python program to count occurrences of a substring in a string. 

"""
string = "hello python world hello you are learning python hello welcome"
sub_str = "hello"
count = string.count(sub_str)
print(f"number of occurrences : {sub_str} = {count}")
"""

str_inp = input("Enter a string : ").split()      #user input string
sub_str = input("Enter a substring : ")          #substring input

count =  str_inp.count(sub_str)           #count input word or letter

print("Occurences of substring : ",count)        #print last result to count in string