"""
Get Level of a node in a Binary Tree
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def getLevel(root, data):
    return getLevelUtil(root,data,1)
    
def getLevelUtil(root, data, level):
    if root is None:
        return 0
        
    if root.data == data:
        return level
        
    downlevel = getLevelUtil(root.left, data, level + 1)
    
    if downlevel != 0:
        return downlevel
        
    downlevel = getLevelUtil(root.right, data, level + 1)
    return downlevel
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

for i in range(1,6):
    level = getLevel(root, i);
    if level:
        print("Level of %d is %d\n"%(i, level))
    else:
        print("%d is not present in tree \n" % i)
