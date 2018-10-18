"""
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to 
reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to 
reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse down, right
and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be
traversed. You may assume that all costs are positive integers.

https://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/
"""

import sys

def minCost(arr, m, n):
    if( m < 0 or n < 0):
        return sys.maxsize
    elif (m == 0 and n == 0):
        return arr[m][n]
    else:
        return arr[m][n] + min(minCost(arr, m-1, n-1), minCost(arr, m-1,n), minCost(arr, m, n-1))
        

def min(x,y,z):
    if (x<y):
        return x if(x<z) else z
    else:
        return y if(y<z) else z

# Driver program to test above functions 
arr= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
print(minCost(arr, 2, 2))
