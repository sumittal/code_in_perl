def Count1(arr, l, h):

    m = l + (h - l)/2

    while h > l:
        # check if the element at middle index is last 1
        if ((m == h) or (arr[m + 1] == 0) and arr[m] == 1):
            return m + 1

        # If element is not last 1, recur for right side
        if arr[m] == 1:
            return Count1(arr, m+1,h)

        # else recur for left side
        return Count1(arr, l , m - 1)

if __name__ == '__main__':

    arr=[1, 1, 1, 1, 0, 0, 0]
    print "Count of 1's in given array is",Count1(arr, 0 , len(arr)-1)

