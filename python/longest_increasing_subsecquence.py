"""
Let us discuss Longest Increasing Subsequence (LIS) problem as an example problem that can be solved using Dynamic Programming.
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given sequence such that
all elements of the subsequence are sorted in increasing order. 
For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
"""

# lis returns length of the longest increasing subsequence
# in arr of size n
def lis(arr):
	n = len(arr)

	# Declare the list (array) for LIS and initialize LIS
	# values for all indexes
	lis = [1]*n

	# Compute optimized LIS values in bottom up manner
	for i in range (1 , n):
	    for j in range(0 , i):
		if arr[i] > arr[j] and lis[i] < lis[j] + 1 :
		    lis[i] = lis[j]+1

	# Initialize maximum to 0 to get the maximum of all LIS
	maximum = 0

	# Pick maximum of all LIS values
	for i in range(n):
		maximum = max(maximum , lis[i])

	return maximum

# Driver program to test above function
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is", lis(arr))

