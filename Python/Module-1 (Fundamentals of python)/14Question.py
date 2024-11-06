"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string."""

str1 = "hello"
str2 = "world"
print(str1,str2)

swap_str1 = str2[:2] + str1[2:]       #hello world = str2[:2] + str1[2:]
# print(swap_str1)                    #                 wo    + __llo  = wollo
swap_str2 = str1[:2] + str2[2:]       #hello world = str[:2]  + str2[2:]
# print(swap_str2)                    #                 he    + __rld  = herld

result = swap_str1 + " " + swap_str2  
print(f"result is : {result}")        #print result
