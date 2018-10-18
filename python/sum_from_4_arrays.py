'''
Suppose there are 4 unsorted arrays as given below:

A = [0, 100, -100, 50, 200]
B = [30, 100, 20, 0]
C = [0, 20, -1, 80]
D = [50, 0, -200, 1]
Suppose X is 0, so the few of the possible O/P should be (pick 1 element from each array which satisfy condition):

0,0,0,0
-100, 100, 0, 0
-100, 30, 20,50 
I was able to devise the algorithm which can do this in O(n^3LogN), is there any better way to achieve the same?
'''

from collections import defaultdict

A = [0, 100, -100, 50, 200]
B = [30, 100, 20, 0]
C = [0, 20, -1, 80]
D = [50, 0, -200, 1]

def initialize_sums(lst):
    return {item: [[item]] for item in lst}

def update_sums(sums, lst):
    new_sums = defaultdict(list)
    for sm, ways in sums.items():
        for item in lst:
            new_sum = sm + item
            for way in ways:
                new_sums[new_sum].append(way + [item])
    return new_sums

def find_sum(sums, last_lst, X):
    last_lst = sorted(last_lst)
    ret = []
    for sm, ways in sorted(sums.items()):
        for item in last_lst:
            x = sm + item
            if x > X:
                break
            if x == X:
                for way in ways:
                    ret.append(way + [item])
                break
    return ret


sums = initialize_sums(lst=A)
sums = update_sums(sums, lst=B)
sums = update_sums(sums, lst=C)

ret = find_sum(sums, last_lst=D, X=0)
print(ret)
