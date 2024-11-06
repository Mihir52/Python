"""Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
Sample data: {'1': ['a','b'], '2': ['c','d']}
Expected Output:
ac ad bc bd """

data = {
  '1' : ['a','b'],
  '2' : ['c','d']
}

# lists of letters from the dictionary
list1 = data['1']
list2 = data['2']

# nested loop 
for letter1 in list1:
  for letter2 in list2:
    print(letter1 + letter2) #print combination of letters