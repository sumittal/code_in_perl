import re
import sys
from codecs import decode

string = str(sys.argv[1])

def is_palindrome(s):
    s = re.sub(r'\W+', '', s)
    s = s.lower()

    return s == s[::-1]

if is_palindrome(string):
    print('Palindrome!')
else:
    print('Not a Palindrome!')
