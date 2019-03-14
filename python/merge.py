def mergeArrays(arr1, arr2, n1, n2):
    arr3 = [None] * (n1 + n2)
    print(arr3)
    i = 0
    j = 0
    k = 0
    while i < n1 and j < n2:
        print(arr1[i])
        print(arr2[j].split(':')[0])
        if int(arr1[i].split(':')[0]) < int(arr2[j].split(':')[0]):
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
        print(arr3)
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1

    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    print("Array after merging")
    print(arr3)
    return arr3
arr1 = ['3:F', '11:S']
arr2 = ['5:E', '7:J', '9:K', '10:G']
c = [3,0]
arr3 = mergeArrays(arr1, arr2, 2, 4);

s = ''
for i in c:
    s += arr3[i] + ','
else:
    s = s[:-1]
print(s)