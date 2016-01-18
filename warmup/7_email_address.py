# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
line=input()
data=''

r=[]
for _ in range(line):
    d=raw_input()
    regex=r'\b[\w\-][\w\-\.]+@[\w\-][\w\-\.]+[a-zA-Z]{1,4}\b'
    all=re.findall(regex,d)
    r=r+all
print ';'.join(sorted(set(r)))
