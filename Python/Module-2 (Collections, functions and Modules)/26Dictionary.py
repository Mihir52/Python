# How will you create a dictionary using tuples in python? 

tup = (('name','mihir'),('age','21'),('career','IT'))

# using dict() function to convert in dictionary
dictionary = dict(tup)

# Print the dictionary
print(dictionary)



# without using dict() function
tup1 = ((1,'one'),(2,'two'),(3,'three'))

dictionary1 = {}  

for key,value in tup1:
  dictionary1[key] = value

print(dictionary1)

