"""
Maximum path sum in a triangle.
We have given numbers in form of triangle, by starting at the top of the triangle and moving to adjacent numbers on the row below, find the maximum total from top to bottom.

Examples:

Input : 
   3
  7 4
 2 4 6
8 5 9 3
Output : 23
Explanation : 3 + 7 + 4 + 9 = 23 

Input :
   8
 -4 4
 2 2 6
1 1 1 1
Output : 19
Explanation : 8 + 4 + 6 + 1 = 19 

Applying, DP in bottom-up manner we should solve our problem as:
Example:

         3
        7 4
       2 4 6
      8 5 9 3

      Step 1 :
      3 0 0 0
      7 4 0 0
      2 4 6 0
      8 5 9 3

      Step 2 :
      3  0  0  0
      7  4  0  0
      10 13 15 0

      Step 3 :
      3  0  0  0
      20 19 0  0

      Step 4:
      23 0 0 0

      output : 23

https://www.geeksforgeeks.org/maximum-path-sum-triangle/
"""

def maxPathSum(tri, m, n):
    # loop for bottom-up calculation
    for i in range(m-1, -1, -1):
        for j in range(i+1):

            # for each element, check both
            # elements just below the number
            # and below right to the number
            # add the maximum of them to it
            if(tri[i+1][j] > tri[i+1][j+1]):
                tri[i][j] += tri[i+1][j]
            else:
                tri[i][j] += tri[i+1][j+1]

    # return the top element
    # which stores the maximum sum
    return tri[0][0]

# Driver program to test above function
 
tri = [[1, 0, 0],[4, 8, 0],[1, 5, 3]]
print(maxPathSum(tri, 2, 2))
