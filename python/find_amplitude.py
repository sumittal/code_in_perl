def solution(A, B):

    if A < 3 and B < 3:
        return 'a' * A + 'b' * B

    x = 'a'
    y = 'b'
    res = ''
    if A == B:
        while A > 0:
            res += x
            res += y
            A -= 1
        return res

    if B > A:
        A, B = B, A
        x, y = y, x

    if 2 * B + 2 < A:
        return ''

    step = 2

    res = ''
    while A > 0 or B > 0:
        if A < step:
            step = A
        res += x * step
        if B > 0:
            res += y
        A -= step
        B -= 1
    return res

print(solution(0,0))
print(solution(3,3))
print(solution(1,4))
print(solution(3,1))
print(solution(1,10))
