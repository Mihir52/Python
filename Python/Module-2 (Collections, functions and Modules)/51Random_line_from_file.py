# Write a Python program to read a random line from a file. 

import random

filename = 'text.txt'
# open file
file_open = open(filename,'r')

# file open and read line
line_read = file_open.readlines()

# pick a random line
random_line = random.choice(line_read).strip()

# print a random line
print(f"Random line from a file : {random_line}")