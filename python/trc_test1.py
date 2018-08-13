# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input : 13:46:26.512321 ORDER not:(hahahah) ost:(hahahah) ref:(hhhdh,gfgf) mkt:(12345,123) pac:1 mid:84 src:1 cxr:(0,0), sec:JYOTHLAB sid:202727 way:SELL qty:30 prc:368 typ:LIMIT
import sys

# if reverse of string is same as original, then string is palindrome
def is_palindrome(s):
    input_str = str(s)
    return input_str == input_str[::-1]
    
def reverse(s):
    return s[::-1]

def pow(x,y):
    x = int(x)
    y = int(y)
    if y == 0:
        return 1
    elif (int(y%2) == 0):
        return(pow(x, int(y/2)) * pow(x, int(y/2)))
    else:
        return(x*pow(x, int(y/2)) * pow(x, int(y/2)))

line_no = 1
while(line_no <= 7):
    raw_line = sys.stdin.readline()
    words = raw_line.strip().split(' ')
    
    lis = []
    timestamp = words[0]
    mid_field = ""

    for word in words[1:]:
        if 'sid:' in word:
            lis.append(word.split(':')[1])
        if 'way:' in word:
            lis.append(word.split(':')[1])
        if 'qty:' in word:
            lis.append(word.split(':')[1])
            quantity = word.split(':')[1]
        if 'prc:' in word:
            lis.append(word.split(':')[1])
        
        if 'mid:' in word:
            mid_field = word.split(':')[1]
    
    reversed_list = lis[::-1]
    elements = ','.join(reversed_list)
    print(timestamp, '-', elements)
    
    warning = 'mid ' + mid_field + ' is not palindrome' 
    if mid_field is not "":
        if not is_palindrome(mid_field):
            print('WARN :', timestamp,'-', warning)
        
    power = pow(quantity,line_no)
    log_element = str(quantity) + '^' + str(line_no)
    print(timestamp, '-', log_element, '=', power)
    line_no += 1
    

