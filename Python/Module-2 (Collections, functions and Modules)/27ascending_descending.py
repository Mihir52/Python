# Write a Python script to sort (ascending and descending) a dictionary by value.

dictionary = {
  'num1' : 10,
  'num2' : 50,
  'num3' : 9,
  'num4' : 30,
  'num5' : 100,
}

# Use sorted() to sort the items of the dictionary.
asc = dict(sorted(dictionary.items(), key=lambda item: item[1]))
# The reverse=True argument tells sorted() to sort the values in descending order.
desc = dict(sorted(dictionary.items(), key=lambda item: item[1],reverse=True))

print(asc)
print(desc)
