def rotate_matrix( X ):
    c = len(X[0])
    r = len(X)

    # calculate the transpose of matrix i.e. exchange row with columns
    T = [[X[j][i] for j in range(r)] for i in range(c)]

    # reverse the columns of transpose to get left rotation
    # NOTE: if we reverse the rows of transposed matrix thrn 
    # we eill get the matrix rotated by right direction 
    for i in range(c): 
        j = 0
        k = c-1
        while j < k: 
            T[j][i] , T[k][i] = T[k][i], T[j][i]
            j += 1
            k -= 1

    return T

m = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate_matrix(m))

