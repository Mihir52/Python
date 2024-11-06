"""Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string."""

# The lyrics is not that poor!
# The lyrics are poor that good!
str = input("Enter a string : ")  #input string 

not_str = str.find('not')          #not_str store find(not) method
poor_str = str.find('poor')         #poor_str store find(poor) method

if not_str < poor_str:            # if first find not and then poor
  result = str[:not_str] + 'good' + str[poor_str+4:]      
else:
  result = str

print(result)       #print string
