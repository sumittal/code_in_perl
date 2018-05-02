# Maximum and minimum element’s position in a list

def get_pos(a):
    
    min_pos = a.index(min(a))
    
    max_pos = a.index(max(a))
    
    # printing the position 
    print("The maximum is at position", max_pos + 1) 
    print("The minimum is at position", min_pos + 1)
     
     
# driver code
a = [3, 4, 1, 3, 4, 5] 
get_pos(a)

