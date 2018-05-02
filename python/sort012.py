# Python program to sort an array with 0,1 and 2 in a single pass
 
# Function to sort array
def sort012(a):

    lo = 0
    mid = 0
    hi = len(arr) - 1

    while mid <= hi:

        if a[mid] == 0:
            a[lo], a[mid] = a[mid], a[lo]
            lo += 1
            mid += 1
        elif a[mid] == 1:
            mid += 1
        else:
            a[mid], a[hi] = a[hi], a[mid]
            hi -= 1

    return arr

# Function to print array
def printArray(a):
    for k in a:
        print k,
    print

if __name__ == '__main__':
    arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
    arr = sort012(arr)
    print "Array aftter segregation :",
    printArray(arr)
 
