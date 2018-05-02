def test_main():
    #      0 1 2 3 4  5 6  7 8
    arr = [4,5,1,3,10,4,1,1,1,1,11,2,2,2,2,2,2]
    length = len(arr)
    null_p = 0

    for i in range(1,length):
        if arr[i] in arr[:i-1]:
            for j in range(i+1,length):
                if not arr[j] in arr[:j-1]:
                    arr[i],arr[j] = arr[j],arr[i]
                    null_p = i
                    break
    arr = arr[:null_p+1]
    print arr
 
if __name__ == "__main__":
    test_main()
