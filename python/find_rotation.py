"""
Minimum rotations required to get the same string

Step 1 : Initialize result = 0 (Here result is count of rotations)
Step 2 : Take a temporary string equals to original string concatenated with itself.
Step 3 : Now take the substring of temporary string of size same as original string starting from second character (or index 1).
Step 4 : Increase the count.
Step 5 : Check whether the substring becomes equal to original string. If yes, then break the loop. Else go to step 2 and repeat it from the next index.
"""

def getRotations(s):
    tmp = s + s
    n = len(s)

    for i in range(1,n+1):
        ts = tmp[i:n+1]

        if ts == s:
            return i

    return n

s = "abccba"

print("Rotation required :", getRotations(s))
