"""
Equilibrium index of an array
Equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. For example, in an arrya A:

A[0] = -7, A[1] = 1, A[2] = 5, A[3] = 2, A[4] = -4, A[5] = 3, A[6]=0

3 is an equilibrium index, because:
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

6 is also an equilibrium index, because sum of zero elements is zero, i.e., A[0] + A[1] + A[2] + A[3] + A[4] + A[5]=0

7 is not an equilibrium index, because it is not a valid index of array A.

1) Initialize leftsum  as 0
2) Get the total sum of the array as sum
3) Iterate through the array and for each index i, do following.
    a)  Update sum to get the right sum.  
           sum = sum - arr[i] 
       // sum is now right sum
    b) If leftsum is equal to sum, then return current index. 
    c) leftsum = leftsum + arr[i] // update leftsum for next iteration.
4) return -1 // If we come out of loop without returning then
             // there is no equilibrium index
"""

def equilibrium(arr):
    
    # finding the sum of whole array
    total_sum = sum(arr)
    left_sum = 0
    
    for i, num in enumerate(arr):
        # total_sum is now right sum
        # for index i
        total_sum -= num
        
        if left_sum == total_sum:
            return i
            
        left_sum += num
        
    # If no equilibrium index found, 
    # then return -1
    return -1
    
# driver code
arr = [-7, 1, 5, 2, -4, 3, 0]
print ('First equilibrium index is ',
       equilibrium(arr))
