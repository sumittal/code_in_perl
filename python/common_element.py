def common_element(a,b):
    a_set = set(a)
    b_set = set(b)
    if len(a_set.intersection(b_set)) > 0:
        return True
    return False
    
a = [1, 2, 3, 4, 5]
b = [5, 6, 7, 8, 9]
print(common_element(a, b))

a =[1, 2, 3, 4, 5]
b =[6, 7, 8, 9]
print(common_element(a, b))

