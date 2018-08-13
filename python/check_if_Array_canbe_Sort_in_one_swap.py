def solution(A):
    # write your code in Python 3.6
    ln = len(A)
       
    B = sorted(A)
    count = 0

    for i in range(len(A)):
        if A[i] != B[i]:
            count += 1

    print(count)
    if count > 2:
        return False
    return True

#A = [1,5,3,4,2]
#A= [2,1,3,4,5]
A = [1,2,4,3,5]
print(solution(A))
