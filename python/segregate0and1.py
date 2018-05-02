def Seg1and0(arr):

    n = len(arr)

    count = 0
    for i in range(n):
        if arr[i] == 0:
            count += 1

    res = []
    # loop fills the arr with 0 until count
    for i in range(count):
        res.append(0)

    # loop fills remaining arr space with 1
    for i in range(n - count):
        res.append(1)
    
    print res

if __name__ == '__main__':
    arr = [0, 1, 0, 0, 0, 1 ]

    Seg1and0(arr)
