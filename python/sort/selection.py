import sys

def selectionSort(arr):
    
    for i in range(len(arr)):

        # Find the minimum element in remaining 
        # unsorted array
        min_id = i
        for j in range(i+1, len(arr)):
            if arr[min_id] > arr[j]:
                min_id = j

        # Swap the found minimum element with 
        # the first element
        arr[i], arr[min_id] = arr[min_id], arr[i]


if __name__ == '__main__':
    arr = [64, 25, 12, 22, 11]

    print ("Sorted array")
    res = selectionSort(arr)

    for i in range(len(arr)):
        print("%d" % arr[i]),
