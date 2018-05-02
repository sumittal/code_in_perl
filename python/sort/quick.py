# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition(arr, low, high):
    i = low - 1
    p = arr[high]

    for j in range(low, high):
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= p:
            # increment index of smaller element
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if low < high:

        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quickSort(arr,0,n-1)

    print ("Sorted array is:")
    for i in range(n):
        print ("%d" % arr[i]),

