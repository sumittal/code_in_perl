# Enter your code here. Read input from STDIN. Print output to STDOUT

import os


def maxSubArraySum(a):
    size = len(a)
    max_last = 0
    max_new = 0
    for i in range(0, size):
        max_new = max_new + a[i]
        if max_new < 0:
            max_new = 0
        elif (max_last < max_new):
            max_last = max_new
    return max_last


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    result = 0
    p = [x.strip() for x in input().split(',')]
    print(p)
    a = []
    invalidInput = False
    for i in range(len(p)):
        try:
            a.append(int(p[i]))
        except:
            print(p[i])
            result = 0
            invalidInput = True

    if not invalidInput:
        result = maxSubArraySum(a)
        if result < 0:
            result = 0

    fptr.write(' '.join(map(str, str(result))))
    fptr.write('\n')

    fptr.close()
