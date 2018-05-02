# Returns the position of first
# occurence of x in array
def exponentialSearch(arr, x):
    n = len(arr)

    # IF x is present at first location itself
    if arr[0] == x:
        return 0

    # Find range for binary seaarch by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Call binary search for the found range
    return binarySearch(arr, i/2, min(i,n), x)


def binarySearch(arr, l, r, x):

    if r >= l:

        mid = l + (r - l)/2

        # If the element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid, then it
        # can only be present in the left subarray
        if arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)

        else:
            return binarySearch(arr, mid + 1, r, x)

    # We reach here if the element is not present
    return -1

if __name__ == '__main__':

    arr = [2, 3, 4, 10, 40]
    x = 10

    result = exponentialSearch(arr, x)

    if result == -1:
        print "Element not found in thye array"
    else:
        print "Element is present at index %d" %(result)
