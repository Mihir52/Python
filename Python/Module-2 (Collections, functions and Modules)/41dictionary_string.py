"""Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
Sample string: 'w3resource'
Expected output:
{'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 
"""

sample_str = "w3resource"

# empty dictionary
char_count = {}

# loop use to each character
for ch in sample_str:
  if ch in char_count:
    # character is already in a dict,increment the count
    char_count[ch] += 1
    # not same character repeat to count 1
  else:
    char_count[ch] = 1

print(f"Characters : {char_count}")


