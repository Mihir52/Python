"""Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged. """

str = input("Enter a string : ")    #input string 

if len(str) < 3:    #if string length is less than 3 to print same string
  print(str)
elif str[-3:] == 'ing':     #end of string,last three char is 'ing' to replace 'ly'
  print(str.replace('ing','ly'))
elif str[-2:] == 'ly':      #end of string,last two char is 'ly' to replace 'ing'
  print(str.replace('ly','ing'))
else:                       #length of string is greater than 3 to add 'ing'
  print(str + 'ing')