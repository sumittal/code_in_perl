"""
* works only on sorted arrays
* the optimal size of block to be jumped is O(root n). This makes the time complexity of Jump search O(root n).
* The time complexity of Jump Search is between Linear Search and Binary Search
* Binary Search is better than Jump Search, but Jump search has an advantage that we traverse back only once jumps.  So where jumping back is costly, we use Jump search
"""
import math

def jumpSearch(arr, x):

    # Finding block size to be jumped
    n = len(arr)
    step = int(math.sqrt(n))

    prev = 0

    # Finding the block where element is present (if it is present)
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Doing a linear search for x in block beginning with prev.
    while arr[prev] < x:
        prev += 1

        # If we reached next block or end of array, element is not present.
        if prev == min(step,n):
            return -1

    if arr[prev] == x:
        return prev

    return -1

if __name__ == "__main__":

    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ]
    x = 55
   
    result = jumpSearch(arr,x)
    if result != -1:
        print("Element is present at index %d" % (result))
    else:
        print("Element is not present in array")
