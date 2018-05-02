def pairOfSum(a, num):
    a.sort()

    l = 0
    r = len(a) - 1

    while l < r:
        if a[l] + a[r] < num:
            l += 1
        elif a[l] + a[r] > num:
            r -= 1
        else:
            return 1

    return 0

# Driver program to test the functions
a = [1,4,45,6,10,-8]
n = 16

if pairOfSum(a,n):
    print("pair exist with given sum")
else:
    print("pair do not exist with given sum")

def quickSort(a, start, end):
    pi = partition(a, start, end)
    quickSort(a, start, pi - 1)
    quickSort(a, pi + 1, end)

# Utility function for partitioning the array
def partition(a, s, e):

    # choose last element as pivot element
    x = a[e]
    i = s - 1

    for j in range(s,e):
        if a[j] < x:
            i += 1
            a[i], a[j] = a[j], a[i]

        a[i+1],a[e] = a[e],a[i+1]

    return i + 1 



