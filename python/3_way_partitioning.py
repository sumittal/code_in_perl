#Three way partitioning of an array

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
