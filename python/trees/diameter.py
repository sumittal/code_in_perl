"""
    Diameter of a Binary Tree
    The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two end nodes.
"""

class Node:
    
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
def height(root):
    
    if root is None:
        return 0
        
    return 1 + max(height(root.left), height(root.right))
    
def diameter(root):
    
    if root is None:
        return 0
    
    # Get the height of left and right sub-trees
    lh = height(root.left)
    rh = height(root.right)
    
    # Get the diameter of left and irgh sub-trees
    ld = diameter(root.left)
    rd = diameter(root.right)
    
    return max(1 + lh + rh, max(ld, rd))
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Diameter of given binary tree is %d" %(diameter(root)))
