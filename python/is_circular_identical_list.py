# Check whether two lists are circularly identical

# function to check circularly identical or not
def circularly_identical(list1, list2):
    
   return(' ' .join(map(str, list2)) in ' ' . join(map(str, list1 * 2)))
   

# driver code
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]
 
 
# check for list 1 and list 2 
if(circularly_identical(list1, list2)):
    print("Yes")
else:
    print("No")
 
# check for list 2 and list 3 
if(circularly_identical(list2, list3)):
    print("Yes")
else:
    print("No")

