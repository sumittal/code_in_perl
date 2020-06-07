'''
For NxM array , Write a function such that if user input is (x,y) It should return a sum of all values from (0,0) to (x,y). where x<N & y<M
'''
def getSum(A, n, m, x, y):

    res = 0

    for row in range(x + 1):
        last_col = m - 1 if row < x else y
        for col in range(last_col + 1):
            res += A[row][col]

    return res

'''
you should try to iterate only over the values that you need, which in this case is possible and not hard. With the rows you
just need to go from row indices 0 to x, so you would use for row in range(x + 1). For the columns, you would have to iterate 
through all of them (up to m - 1) for rows 0 to x - 1 and only up to y for row index x. You can just compute that as 
last_col = m - 1 if row < x else y and then iterate like for col in range(last_col + 1). Then you simply sum all the values 
that you iterate, since you do not need to "filter" any of them:

Note: The n and m parameters are not really necessary in the function, I have kept them to maintain the same function prototype
that you proposed, but if it is up to you to decide what parameters you need you would leave them out. Even if you needed them
you could get them from A using len.

Note 2: I am only considering the problem of computing the result for a valid set of inputs. Remember that many times in this
kind of tests the interviewer wants to check how you deal with bad inputs (negative numbers, invalid sizes, None, etc) and 
corner cases.

'''

'''
using dynamic programmin
'''


def sumMatrix(A):
    S = [[0 for i in range(len(A[j]))] for j in range(len(A))]
    S[0][0] = A[0][0]

    for i in range(1, len(A)):
        S[i][0] = S[i - 1][0] + A[i][0]

    for j in range(1, len(A[0])):
        S[0][j] = S[0][j - 1] + A[0][j]

    for i in range(1, len(A)):
        for j in range(1, len(A[0])):
            S[i][j] = S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1] + A[i][j]

    return S

'''
The solution relies on a simple recurrence relation (S[x][y] denotes the sum of elements of A from (0, 0) to (x, y)):

S[0, 0] = A[0, 0]
S[0, y] = S[0, y - 1] + A[0, y] when y > 0
S[x, 0] = S[x - 1, 0] + A[x, 0] when x > 0
S[x, y] = S[x, y - 1] + S[x - 1, y] - S[x - 1, y - 1] + A[x, y] when x, y > 0
The key point is, both of the sums of the sub-matrices from (0, 0) to (x, y - 1) and from (0, 0) to (x - 1, y) contain the 
sum of the sub-matrix from (0, 0) to (x - 1, y -1), so we are adding it twice. That's why we need to subtract it once.
'''
