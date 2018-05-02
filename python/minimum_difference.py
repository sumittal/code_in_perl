"""
Link : https://www.geeksforgeeks.org/find-minimum-difference-pair/

Given an unsorted array, find the minimum difference between any pair in given array.

Examples :

    Input  : {1, 5, 3, 19, 18, 25};
    Output : 1
    Minimum difference is between 18 and 19

"""

def Diff(arr):

    n = len(arr)
    
    # Initialize difference as infinite
    diff = 10 ** 20

    # Sort array in non-decreasing order
    arr = sorted(arr)

    # Find the min diff by comparing adjacent
    # pairs in sorted array
    for i in range(n - 1):

        if (arr[i + 1] - arr[i] < diff):
            diff = arr[i+1] - arr[i]

    return diff

# Driver code
arr = [1, 5, 3, 19, 18, 25]
print("Minimum difference is " + str(Diff(arr)))
