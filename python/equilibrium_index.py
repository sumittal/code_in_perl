"""
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
def equilibrium(a):
    totalsum = sum(a)
    leftsum = 0

    for i, num in enumerate(a):

        totalsum -= num

        if leftsum == totalsum:
            return i
        leftsum += num

    return -1

arr = [-7, 1, 5, 2, -4, 3, 0]
print ('First equilibrium index is ', equilibrium(arr))
