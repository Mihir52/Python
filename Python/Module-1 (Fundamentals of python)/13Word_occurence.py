#Write a Python program to count the occurrences of each word in a given sentence 

def word_occurence(str):
  dict = {}              
  word = str.split()
  
  for i in word:       
    if i in dict:
      dict[i] += 1 
    else:
      dict[i] = 1

  return dict

input_str = input("Enter string : ")  #input string
print(f"Occurence of string : {word_occurence(input_str)}")  #print last result


  