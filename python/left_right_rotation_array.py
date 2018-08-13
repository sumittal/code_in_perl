# Write a function rotate(arr[], d, n) that rotates arr[] to left/right of size n by d elements.

"""
Input:  arr[] = [1, 2, 3, 4, 5, 6, 7]
            d = 2
Output: arr[] = [3, 4, 5, 6, 7, 1, 2] 
"""

def reverseArray(arr, start, end):
    while(start < end):
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def leftRotate(arr, d):
    n = len(arr)
    print("original array : ", arr)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)
    reverseArray(arr, 0, n-1)
 
    print("Left rotated array :" ,arr, end = '')

def rightRotate(arr, d):
    n = len(arr)
    
    print("original array :",arr)
    reverseArray(arr, 0, n-1)
    reverseArray(arr, 0, d-1)
    reverseArray(arr, d, n-1)

    print("Right rotated array :" , arr, end = '')
    print("\n\n")
        
# Driver function to test above functions
arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2) # Left Rotate array by 2
print("\n\n")
arr = [1, 2, 3, 4, 5, 6, 7]
rightRotate(arr, 2) # Right Rotate array by 2

    
