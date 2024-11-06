# Write a Python script to print a dictionary where the keys are numbers between 1 and 15.

dictionary = {}

# for loop to add keys and values to the dictionary
for key in range(1,16):
  #Assigning the square of the key as the value
  dictionary[key] = key ** 2  

print(dictionary)
