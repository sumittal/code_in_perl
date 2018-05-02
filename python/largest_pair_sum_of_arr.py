
"""
Find the largest pair sum in an unsorted array
Given an unsorted of distinct integers, find the largest pair sum in it. For example, the largest pair sum in {12, 34, 10,6, 40} is 74.

Algo:
1) Initialize both first and second largest
   first = max(arr[0], arr[1])
   second = min(arr[0], arr[1])
2) Loop through remaining elements (from 3rd to end)
   a) If the current element is greater than first, then update first 
       and second. 
   b) Else if the current element is greater than second then update 
    second
3) Return (first + second)
"""
def findLargestSumPair(arr,n):
    
    # initialize the first and second lasrgest elements
    if arr[0] > arr[1]:
        first = arr[0]
        second = arr[1]
        
    else:
        first = arr[1]
        second = arr[0]

    # Traverse remaining array and 
    # find first and second largest
    # elements in overall array
    for i in range(2,n):
        if arr[i] > first:
            second = first
            first = arr[i]
            
        # If arr[i] is in between first 
        # and second then update second
        elif arr[i] > second and arr[i] != first:
            second = arr[i]
            
    return (first + second)
    
# Driver program to test above function */
arr = [12, 34, 10, 6, 40]
n = len(arr)
print("Max Pair Sum is", 
      findLargestSumPair(arr, n))

