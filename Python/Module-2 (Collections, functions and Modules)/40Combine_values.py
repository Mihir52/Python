"""Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, 
{'item': 'item2', 'amount': 300},
{'item': 'item1', 'amount': 750}]
Expected Output:
Counter ({'item1': 1150, 'item2': 300})
"""

data = [  
  {'item' : 'item1','amount' : 400},
  {'item' : 'item2','amount' : 300},
  {'item' : 'item1','amount' : 750}
]

result = {}

for i in data:
  item = i['item']
  amount = i['amount']
  # if item is already in the result,add the amount
  if item in result:
    result[item] += amount
  # otherwise same it is
  else:
    result[item] = amount

# print the expected output
print(f"Combined values : {result}")



