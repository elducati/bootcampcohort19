def words(phrase):
  count_dict = {}   #store the word count in  a dicionary
  for word in phrase.split():
      try:
        int(word)
        word = int(word)
      except Exception as e:
        pass
    
      if count_dict.get(word):
      
        count_dict[word] += 1
      else:
        count_dict[word] = 1

  
  return count_dict