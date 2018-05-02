"""Given a sorted array and a number x, find the pair in array whose sum is closest to x

Examples:

Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
Output: 22 and 30

Input: arr[] = {1, 3, 4, 7, 10}, x = 15
Output: 4 and 10


1) Initialize a variable diff as infinite (Diff is used to store the 
   difference between pair and x).  We need to find the minimum diff.
2) Initialize two index variables l and r in the given sorted array.
       (a) Initialize first to the leftmost index:  l = 0
       (b) Initialize second  the rightmost index:  r = n-1
3) Loop while l < r.
       (a) If  abs(arr[l] + arr[r] - sum) < diff  then 
           update diff and result 
       (b) Else if(arr[l] + arr[r] <  sum ) > then l++
       (c) Else r-- 
"""

# Prints the pair with sum closest to x
def printClosest(arr, x):
    
    res_l , res_r = 0, 0  # To store indexes of result pair

    l = 0 
    r = len(arr) - 1
    max_diff = 999999

    while r > l:
        
        if abs(arr[l] + arr[r] - x) <  max_diff:
            res_l = l
            res_r = r
            max_diff = abs(arr[l] + arr[r] - x)

        if arr[l] + arr[r] > x:
            r -= 1
        else:
            l += 1

    print "closest pair is - ", res_l, res_r

if __name__ == '__main__':
    arr = [10, 22, 28, 29, 30, 40]
    x = 54
    printClosest(arr,x)

    arr = [1, 3, 4, 7, 10]
    x = 15
    printClosest(arr,x)
