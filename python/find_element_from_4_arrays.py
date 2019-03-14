'''
From 4 given arrays(not sorted), find the elements from each array whose sum is equal to some number X
Suppose there are 4 unsorted arrays as given below:

A = [0, 100, -100, 50, 200]
B = [30, 100, 20, 0]
C = [0, 20, -1, 80]
D = [50, 0, -200, 1]
Suppose X is 0, so the few of the possible O/P should be (pick 1 element from each array which satisfy condition):

0,0,0,0
-100, 100, 0, 0
-100, 30, 20,50 .. etc.
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
# [[-100, 30, 20, 50], [0, 0, -1, 1], [-100, 100, -1, 1], ...]

'''
initialize sums (a dict of the form {possible_sum0: [way_to_get_sum0, ...]}) with the first list A. this results in

sums = {0: [[0]], 100: [[100]], -100: [[-100]], 50: [[50]], 200: [[200]]}
the update that dictionary with the lists B and C. sums will now contain entries like

sums = {..., 
        30: [[0, 30, 0]], 
        50: [[0, 30, 20], [50, 0, 0]], 
        29: [[0, 30, -1]], ...}
then in find_sum i sort the last list D and the sums for some speedup and break if a give sum X is no longer accessible.
'''
