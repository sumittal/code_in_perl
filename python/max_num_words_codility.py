import re

def solution(S):
    # write your code in Python 3.6

    # create the sentence by spliting the text on special charecters
    sentences = re.split('\\.|\\!|\\?',S)

    # create the list containing length of each sentence
    max_len_per_sentence = [len(re.split("\s+",sentence.strip())) for sentence in sentences]

    # return the length of longest sentence
    return (max(max_len_per_sentence))
