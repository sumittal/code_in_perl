"""
Find the starting index of largest increasing subarray of integer array
"""
def solution(A):
    start = 0
    final_start = 0
    end = 0
    ln = len(A)
    max_length = 0
    i = 0

    while i < ln-1:
        if A[i+1] > A[i]:
            end = i+1
            pass
        else:
            start = i+1
            
        if max_length < end - start:
            max_length = end - start
            final_start = start
        i+=1
        
    return final_start

A = [10,9,8,7,3]
print(solution(A))

