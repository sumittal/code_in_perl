"""
Count pairs in an array which have at least one digit common
Given an array of N numbers. Find out the number of pairs i and j such that i < j and Ai and Aj have atleast one digit common (For e.g. (11, 19) have 1 digit common but (36, 48) have no digit common)
"""

def hasCommonDigit(n1,n2):
    #converting integers to strings
    s1 = str(n1)
    s2 = str(n2)

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                return True
    return False

def findPair(a):
    n = len(a)

    numOfPairs = 0

    for i in range(n):
        for j in range(i+1, n):
            if hasCommonDigit(a[i],a[j]):
                numOfPairs += 1

    return numOfPairs

a = [10, 12, 24, 21]
print(findPair(a))
