#Print all sublists of a list

"""
Examples:

Input  : list = [1, 2, 3] 
Output : [[], [1], [1, 2], [1, 2, 3], [2], 
         [2, 3], [3]]

Input : [1, 2, 3, 4] 
Output : [[], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4], 
         [2], [2, 3], [2, 3, 4], [3], [3, 4], [4]]
"""

# Python program to print all 
# sublist from a given list 
 
# function to generate all the sub lists
def sub_lists(lst):
    
    sublist = [[]]
    
    for i in range(len(lst)):
        
        for j in range(i+1, len(lst)):
            sub = lst[i:j]
            sublist.append(sub)
    
    return sublist[1:]

# driver code
l1 = [1, 2, 3, 4]
print(sub_lists(l1))

