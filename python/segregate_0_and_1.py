def segregate(a):
    n = len(arr)
    count = 0
    for i in range(n):
        if a[i] == 0:
            count += 1

    for i in range(count):
        a[i] = 0

    for i in range(count,n):
        a[i] = 1

def segregate_1(a):
    n = len(a)
    left = 0
    right = n-1

    while left < right:
        while a[left] == 0 and left < right:
            left += 1

        while a[right] == 1 and left < right:
            right -= 1

        if left < right:
            a[left], a[right] = a[right], a[left]
            left += 1
            right -= 1

    return a


arr = [0, 1, 0, 1, 1, 1]
print("Array after segregation")
segregate(arr)
print(arr)

arr = [0, 1, 0, 1, 1, 1, 0, 1, 0]
res = segregate_1(arr)
print(res)

