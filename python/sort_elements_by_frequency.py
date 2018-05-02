"""
Sort elements by frequency:
Given an array of integers, sort the array according to frequency of elements. For example, if the input array is {2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12}, then modify the array to {3, 3, 3, 3, 2, 2, 2, 12, 12, 4, 5}.
"""

def sort_by_freq(arr):
    word_freq = {}
        
    for word in arr:
        word_freq[word] = word_freq.get(word, 0) + 1
        
    lis = sorted(word_freq.items(), key = lambda x:x[1], reverse = True)
    
    result = []
    for word,freq in lis:
        #print ("%-10s %d" % (word, freq))
        result.extend([word for i in range(freq)])
    
    return result
    
if __name__ == '__main__':
    arr = [2, 3, 2, 4, 5, 12, 2, 3, 3, 3, 12]
    
    print(sort_by_freq(arr))
