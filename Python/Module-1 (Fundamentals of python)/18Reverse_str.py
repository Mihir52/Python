# Write a Python function to reverses a string if its length is a multiple of 4.

def reverse_str(str):                
  if len(str) % 4 == 0:           #if string is multiple of 4 to execute this condition
    print(f"Reverse string : {str[::-1]}")
  else:                           #if string is not multiple of 4 to output else conditin
    print(f"same string : {str}")
    print("because of string is not multiple of 4 ")


input_str = input("Enter a string : ")   #input string
print(reverse_str(input_str))            #function calling