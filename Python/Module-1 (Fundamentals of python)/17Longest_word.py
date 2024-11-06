# Write a Python function that takes a list of words and returns the length of the longest one. 


def find_longestWord(mylist):
  # count = 0   
  longest_word = ""                      #emply string to store a longest word

  for word in mylist:                    #for loop using check whole list
    if len(word) > len(longest_word):    #if word is greater than longest word to store longest_word variable
      # count = len(word)
      longest_word = word                    
  return longest_word , len(longest_word) 

list = ["helo","long","complete","word"]     #list
longest_word,length = find_longestWord(list)     
print(f"Longest word:'{longest_word}' and its length :{length}") #print longest word and its length
