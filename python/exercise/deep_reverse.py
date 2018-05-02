def deep_rev(lis):
    return [deep_rev(x) if isinstance(x,list) else x for x in lis[::-1]]

p = [[1, 2], [3, [4, 5]], 6]
print("Input: ", p)
print("O/P: ",deep_rev(p))
