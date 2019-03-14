'''
program that finds most frequent word in a .txt file, Must print word and its count
'''
import sys
import collections

def find_most_common_words(textfile, top=10):    
    ''' Returns the most common words in the textfile.'''
    words = collections.Counter()
    with open(textfile) as textfile:
         for line in textfile:
              #how often each word appears
              words.update(line.lower().split())

    return dict(words.most_common(top))

filename = sys.argv[1]
top_five_words = find_most_common_words(filename, 5)

print(top_five_words)
