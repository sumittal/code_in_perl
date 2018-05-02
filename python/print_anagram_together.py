# A Python program to print all anagarms together

#structure for each word of duplicate array
class Word():
    def __init__(self, string, index):
        self.string = string
        self.index = index
        

# create a duplicate array object that contains an array of Words
def create_dup_array(string, size):
    dup_array = []
    
    for i in range(size):
        dup_array.append(Word(string[i], i))
        
    return dup_array
    

# Given a list of words in wordArr[]
def print_anagrams_together(wordArr, size):
    # Step 1: Create a copy of all words present in
    # given wordArr.
    # The copy will also have orignal indexes of words
    dupArray = create_dup_array(wordArr, size)
    
    # Step 2: Iterate through all words in dupArray and sort
    # individual words.
    for i in range(size):
        dupArray[i].string = ''.join(sorted(dupArray[i].string))

    # Step 3: Now sort the array of words in dupArray
    dupArray = sorted(dupArray, key=lambda k: k.string)
    
    # Step 4: Now all words in dupArray are together, but
    # these words are changed. Use the index member of word
    # struct to get the corresponding original word
    
    for word in dupArray:
        print(wordArr[word.index])
        
# Driver program
wordArr = ["cat", "dog", "tac", "god", "act"]
size = len(wordArr)
print_anagrams_together(wordArr, size)

