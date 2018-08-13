"""
#Three way partitioning of an array

Given an array and a range [lowVal, highVal], partition the array around the range such that array is divided in three parts.
1) All elements smaller than lowVal come first.
2) All elements in range lowVal to highVVal come next.
3) All elements greater than highVVal appear in the end.
The individual elements of three sets can appear in any order.

Examples:

Input: arr[] = {1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32}  
        lowVal = 14, highVal = 20
        Output: arr[] = {1, 5, 4, 2, 1, 3, 14, 20, 20, 98, 87, 32, 54}
"""

def sort_list_3way(input_list, low, high):

    sorted_list = [[] for _ in range(3)]

    for elem in input_list:
        if elem < low:
           sorted_list[0].append(elem)
        elif elem > high:
           sorted_list[2].append(elem)
        else:
           sorted_list[1].append(elem)
    print([item for sublist in sorted_list for item in sublist])

sort_list_3way([1, 14, 5, 20, 4, 2, 54, 20, 87, 98, 3, 1, 32], 10, 20)
